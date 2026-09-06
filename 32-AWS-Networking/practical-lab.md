# 🧪 AWS Networking — Practical Lab

## Chapter 32 — AWS Networking

This practical lab builds an AWS VPC networking environment step by step.

We will practice:

* AWS CLI authentication
* VPC
* CIDR
* Subnets
* Availability Zones
* Route Tables
* Internet Gateway
* Security Groups
* EC2 networking
* Private IP
* Public IP
* Connectivity testing
* DNS
* Network troubleshooting
* AWS CLI inspection
* Resource cleanup

> ⚠️ **Cost Warning:** NAT Gateways and EC2 instances can incur AWS charges. Create only the resources you need and destroy paid resources when finished.

---

# 1. Lab Architecture

We will build:

```text
                         Internet
                            |
                            |
                    Internet Gateway
                            |
                     Public Route Table
                            |
                    Public Subnet
                    10.0.1.0/24
                            |
                           EC2
```

The VPC:

```text
VPC
10.0.0.0/16
```

The subnet:

```text
Public Subnet
10.0.1.0/24
```

---

# 2. Prerequisites

You need:

```text
AWS Account
AWS CLI
Linux terminal
Basic AWS knowledge
```

Check AWS CLI:

```bash
aws --version
```

Check identity:

```bash
aws sts get-caller-identity
```

If this command fails with an authentication error, fix your AWS credentials before continuing.

Check region:

```bash
aws configure get region
```

For this lab we will use:

```text
ap-south-1
```

Set it if required:

```bash
aws configure set region ap-south-1
```

Verify:

```bash
aws configure get region
```

---

# 3. Set Lab Variables

Using variables makes the commands easier to reuse.

```bash
export AWS_REGION=ap-south-1
export VPC_CIDR=10.0.0.0/16
export PUBLIC_SUBNET_CIDR=10.0.1.0/24
```

Verify:

```bash
echo $AWS_REGION
echo $VPC_CIDR
echo $PUBLIC_SUBNET_CIDR
```

---

# 4. Check Availability Zones

List Availability Zones:

```bash
aws ec2 describe-availability-zones \
  --region $AWS_REGION \
  --filters Name=state,Values=available \
  --query "AvailabilityZones[].ZoneName" \
  --output table
```

Choose one available AZ.

For example:

```text
ap-south-1a
```

Set:

```bash
export AZ=ap-south-1a
```

> Use an Availability Zone actually returned by your account.

---

# 5. Create the VPC

Create:

```text
10.0.0.0/16
```

Command:

```bash
export VPC_ID=$(aws ec2 create-vpc \
  --cidr-block $VPC_CIDR \
  --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=devops-networking-vpc}]' \
  --query "Vpc.VpcId" \
  --output text)
```

Check:

```bash
echo $VPC_ID
```

Example:

```text
vpc-0123456789abcdef0
```

---

# 6. Verify the VPC

```bash
aws ec2 describe-vpcs \
  --vpc-ids $VPC_ID \
  --query "Vpcs[].{ID:VpcId,CIDR:CidrBlock,State:State}" \
  --output table
```

Expected concept:

```text
VPC ID                 CIDR           State
---------------------  -------------  -------
vpc-xxxxxxxx           10.0.0.0/16    available
```

---

# 7. Enable DNS Support

Check DNS support:

```bash
aws ec2 describe-vpc-attribute \
  --vpc-id $VPC_ID \
  --attribute enableDnsSupport
```

Enable it:

```bash
aws ec2 modify-vpc-attribute \
  --vpc-id $VPC_ID \
  --enable-dns-support
```

---

# 8. Enable DNS Hostnames

Enable:

```bash
aws ec2 modify-vpc-attribute \
  --vpc-id $VPC_ID \
  --enable-dns-hostnames
```

Check:

```bash
aws ec2 describe-vpc-attribute \
  --vpc-id $VPC_ID \
  --attribute enableDnsHostnames
```

DNS is important for AWS service discovery and hostname resolution.

---

# 9. Create Public Subnet

Create:

```text
10.0.1.0/24
```

Command:

```bash
export SUBNET_ID=$(aws ec2 create-subnet \
  --vpc-id $VPC_ID \
  --cidr-block $PUBLIC_SUBNET_CIDR \
  --availability-zone $AZ \
  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=devops-public-subnet}]' \
  --query "Subnet.SubnetId" \
  --output text)
```

Check:

```bash
echo $SUBNET_ID
```

---

# 10. Verify Subnet

```bash
aws ec2 describe-subnets \
  --subnet-ids $SUBNET_ID \
  --query "Subnets[].{ID:SubnetId,CIDR:CidrBlock,AZ:AvailabilityZone,VPC:VpcId}" \
  --output table
```

Expected:

```text
Subnet
10.0.1.0/24
```

---

# 11. Enable Public IPv4 Assignment

For this lab, enable automatic public IPv4 assignment:

```bash
aws ec2 modify-subnet-attribute \
  --subnet-id $SUBNET_ID \
  --map-public-ip-on-launch
```

Verify:

```bash
aws ec2 describe-subnets \
  --subnet-ids $SUBNET_ID \
  --query "Subnets[].{Subnet:SubnetId,MapPublicIP:MapPublicIpOnLaunch}" \
  --output table
```

---

# 12. Create Internet Gateway

Create:

```bash
export IGW_ID=$(aws ec2 create-internet-gateway \
  --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=devops-igw}]' \
  --query "InternetGateway.InternetGatewayId" \
  --output text)
```

Check:

```bash
echo $IGW_ID
```

---

# 13. Attach Internet Gateway to VPC

```bash
aws ec2 attach-internet-gateway \
  --internet-gateway-id $IGW_ID \
  --vpc-id $VPC_ID
```

Verify:

```bash
aws ec2 describe-internet-gateways \
  --internet-gateway-ids $IGW_ID
```

You should see the VPC attachment.

---

# 14. Create Route Table

Create:

```bash
export RT_ID=$(aws ec2 create-route-table \
  --vpc-id $VPC_ID \
  --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=devops-public-rt}]' \
  --query "RouteTable.RouteTableId" \
  --output text)
```

Check:

```bash
echo $RT_ID
```

---

# 15. Add Internet Route

Create the default route:

```text
0.0.0.0/0 → Internet Gateway
```

Command:

```bash
aws ec2 create-route \
  --route-table-id $RT_ID \
  --destination-cidr-block 0.0.0.0/0 \
  --gateway-id $IGW_ID
```

Verify:

```bash
aws ec2 describe-route-tables \
  --route-table-ids $RT_ID \
  --query "RouteTables[].Routes" \
  --output table
```

You should see:

```text
10.0.0.0/16 → local
0.0.0.0/0   → Internet Gateway
```

---

# 16. Associate Route Table With Subnet

```bash
export RT_ASSOC_ID=$(aws ec2 associate-route-table \
  --route-table-id $RT_ID \
  --subnet-id $SUBNET_ID \
  --query "AssociationId" \
  --output text)
```

Check:

```bash
echo $RT_ASSOC_ID
```

---

# 17. Verify Public Subnet Routing

```bash
aws ec2 describe-route-tables \
  --route-table-ids $RT_ID \
  --query "RouteTables[].{Routes:Routes,Associations:Associations}" \
  --output json
```

Architecture now:

```text
VPC
10.0.0.0/16
      |
      v
Public Subnet
10.0.1.0/24
      |
      v
Route Table
      |
      | 0.0.0.0/0
      v
Internet Gateway
      |
      v
Internet
```

---

# 18. Create Security Group

Create a Security Group:

```bash
export SG_ID=$(aws ec2 create-security-group \
  --group-name devops-web-sg \
  --description "Security group for AWS networking lab" \
  --vpc-id $VPC_ID \
  --query "GroupId" \
  --output text)
```

Check:

```bash
echo $SG_ID
```

---

# 19. Add HTTP Rule

Allow HTTP:

```bash
aws ec2 authorize-security-group-ingress \
  --group-id $SG_ID \
  --protocol tcp \
  --port 80 \
  --cidr 0.0.0.0/0
```

Verify:

```bash
aws ec2 describe-security-groups \
  --group-ids $SG_ID \
  --query "SecurityGroups[].IpPermissions" \
  --output table
```

---

# 20. SSH Rule — Use Carefully

SSH should not normally be opened to the whole Internet.

Avoid:

```text
0.0.0.0/0 → TCP 22
```

Instead, if you need SSH, restrict it to your trusted public IP:

```bash
MY_IP=$(curl -s https://checkip.amazonaws.com)
echo $MY_IP
```

Then:

```bash
aws ec2 authorize-security-group-ingress \
  --group-id $SG_ID \
  --protocol tcp \
  --port 22 \
  --cidr ${MY_IP}/32
```

Verify:

```bash
aws ec2 describe-security-groups \
  --group-ids $SG_ID \
  --query "SecurityGroups[].IpPermissions"
```

> If you do not need SSH, skip this step.

---

# 21. Create EC2 Instance

For a real EC2 launch you need:

* AMI ID
* Instance type
* Subnet
* Security Group
* Key pair if using SSH

Find Ubuntu AMIs in your selected region using the AWS Console or an appropriate AWS CLI query.

Example structure:

```bash
aws ec2 describe-images \
  --owners 099720109477 \
  --filters \
    "Name=name,Values=ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*" \
    "Name=state,Values=available" \
  --query "Images | sort_by(@, &CreationDate)[-1].{ID:ImageId,Name:Name,Date:CreationDate}" \
  --output table
```

Set the returned AMI:

```bash
export AMI_ID=ami-xxxxxxxx
```

Choose an instance type appropriate for your account and current pricing/free-tier eligibility.

Example:

```bash
export INSTANCE_TYPE=t3.micro
```

Launch:

```bash
export INSTANCE_ID=$(aws ec2 run-instances \
  --image-id $AMI_ID \
  --instance-type $INSTANCE_TYPE \
  --subnet-id $SUBNET_ID \
  --security-group-ids $SG_ID \
  --associate-public-ip-address \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=devops-networking-server}]' \
  --query "Instances[0].InstanceId" \
  --output text)
```

Check:

```bash
echo $INSTANCE_ID
```

---

# 22. Check EC2 State

```bash
aws ec2 describe-instances \
  --instance-ids $INSTANCE_ID \
  --query "Reservations[].Instances[].{ID:InstanceId,State:State.Name}" \
  --output table
```

Wait until:

```text
running
```

---

# 23. Get EC2 Networking Information

```bash
aws ec2 describe-instances \
  --instance-ids $INSTANCE_ID \
  --query "Reservations[].Instances[].{Instance:InstanceId,PrivateIP:PrivateIpAddress,PublicIP:PublicIpAddress,Subnet:SubnetId,VPC:VpcId,AZ:Placement.AvailabilityZone}" \
  --output table
```

Record:

```text
Private IP
Public IP
Subnet
VPC
Availability Zone
```

---

# 24. Understand the EC2 Traffic Path

Your EC2 now has a path like:

```text
Internet
   |
   v
Public IPv4
   |
   v
EC2 ENI
   |
   v
Public Subnet
   |
   v
Route Table
   |
0.0.0.0/0
   |
   v
Internet Gateway
```

---

# 25. Install a Web Server

If you connect to the EC2 instance:

```bash
ssh -i <key-file>.pem ubuntu@<public-ip>
```

Update packages:

```bash
sudo apt update
```

Install NGINX:

```bash
sudo apt install nginx -y
```

Check:

```bash
sudo systemctl status nginx
```

---

# 26. Check Listening Port

On the EC2 instance:

```bash
sudo ss -lntp
```

You should see NGINX listening on:

```text
80
```

Example:

```text
LISTEN
0.0.0.0:80
```

---

# 27. Test HTTP

From your local machine:

```bash
curl http://<EC2-PUBLIC-IP>
```

You should receive the NGINX response.

You can also open:

```text
http://<EC2-PUBLIC-IP>
```

in a browser.

---

# 28. Troubleshoot HTTP

If HTTP does not work, check:

## Security Group

```bash
aws ec2 describe-security-groups \
  --group-ids $SG_ID
```

Make sure TCP port 80 is allowed.

---

## Route Table

```bash
aws ec2 describe-route-tables \
  --route-table-ids $RT_ID
```

Check:

```text
0.0.0.0/0 → Internet Gateway
```

---

## Public IP

```bash
aws ec2 describe-instances \
  --instance-ids $INSTANCE_ID \
  --query "Reservations[].Instances[].PublicIpAddress" \
  --output text
```

---

## NGINX

```bash
sudo systemctl status nginx
```

---

## Port

```bash
sudo ss -lntp | grep ':80'
```

---

## Ubuntu Firewall

```bash
sudo ufw status
```

---

# 29. Test DNS

From the EC2 instance:

```bash
getent hosts google.com
```

Or:

```bash
dig google.com
```

If `dig` is unavailable:

```bash
sudo apt install dnsutils -y
```

Then:

```bash
dig google.com
```

---

# 30. Test Internet Connectivity

```bash
curl -I https://example.com
```

You can also test:

```bash
ping -c 4 8.8.8.8
```

Remember:

> Ping can fail even when Internet connectivity works because ICMP may be blocked.

HTTP/HTTPS tests are often more useful for application troubleshooting.

---

# 31. Inspect Network Interface

Inside EC2:

```bash
ip addr
```

You should see the instance's private IP.

Check routes:

```bash
ip route
```

You should see a route similar to:

```text
default via <gateway>
```

Check neighbours:

```bash
ip neigh
```

---

# 32. Inspect AWS ENI

From your local machine:

```bash
aws ec2 describe-network-interfaces \
  --filters "Name=attachment.instance-id,Values=$INSTANCE_ID" \
  --query "NetworkInterfaces[].{ENI:NetworkInterfaceId,PrivateIP:PrivateIpAddress,Subnet:SubnetId,VPC:VpcId,SecurityGroups:Groups}" \
  --output table
```

This connects the AWS networking model with the Linux networking model.

---

# 33. Inspect Complete VPC

```bash
aws ec2 describe-vpcs \
  --vpc-ids $VPC_ID
```

---

# 34. Inspect Subnet

```bash
aws ec2 describe-subnets \
  --subnet-ids $SUBNET_ID
```

---

# 35. Inspect Route Table

```bash
aws ec2 describe-route-tables \
  --route-table-ids $RT_ID
```

---

# 36. Inspect Internet Gateway

```bash
aws ec2 describe-internet-gateways \
  --internet-gateway-ids $IGW_ID
```

---

# 37. Inspect Security Group

```bash
aws ec2 describe-security-groups \
  --group-ids $SG_ID
```

---

# 38. Networking Architecture After EC2

```text
                    Internet
                       |
                       |
                Internet Gateway
                       |
                       |
                Public Route Table
                       |
                       |
                Public Subnet
                 10.0.1.0/24
                       |
                       |
                     ENI
                       |
                       |
                      EC2
                       |
                +------+------+
                |             |
             Private IP    Public IP
```

---

# 39. Create a Second Subnet

Now practice subnet segmentation.

Create:

```text
10.0.2.0/24
```

Command:

```bash
export PRIVATE_SUBNET_CIDR=10.0.2.0/24
```

```bash
export PRIVATE_SUBNET_ID=$(aws ec2 create-subnet \
  --vpc-id $VPC_ID \
  --cidr-block $PRIVATE_SUBNET_CIDR \
  --availability-zone $AZ \
  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=devops-private-subnet}]' \
  --query "Subnet.SubnetId" \
  --output text)
```

Check:

```bash
echo $PRIVATE_SUBNET_ID
```

---

# 40. Understand Private Subnet Routing

The private subnet should not use:

```text
0.0.0.0/0 → Internet Gateway
```

for direct Internet access.

Instead, a production private subnet may use:

```text
0.0.0.0/0 → NAT Gateway
```

for outbound Internet access.

Architecture:

```text
Private EC2
     |
Private Route Table
     |
NAT Gateway
     |
Internet Gateway
     |
Internet
```

---

# 41. NAT Gateway Cost Warning

NAT Gateway is a managed AWS service that can incur charges.

Therefore:

> Do not create a NAT Gateway just for practice unless you understand the cost and intend to clean it up immediately.

For this chapter, understand the architecture first.

---

# 42. Security Group Chaining Exercise

Imagine this architecture:

```text
Internet
   |
   v
ALB
   |
   v
Application EC2
   |
   v
Database
```

Create conceptual Security Groups:

```text
ALB-SG
APP-SG
DB-SG
```

Rules:

```text
ALB-SG
443 ← Internet
```

```text
APP-SG
8080 ← ALB-SG
```

```text
DB-SG
3306 ← APP-SG
```

This is called Security Group chaining.

The important principle is:

> Allow traffic from the security group that represents the calling tier rather than exposing internal services to the entire Internet.

---

# 43. Test TCP Connectivity

From a Linux machine:

```bash
nc -vz <IP> <PORT>
```

Example:

```bash
nc -vz <EC2-IP> 80
```

Possible output:

```text
Connection to <IP> 80 port [tcp/http] succeeded!
```

---

# 44. Test HTTP With Curl

```bash
curl -v http://<EC2-IP>
```

Look for:

```text
Connected
HTTP/1.1
200 OK
```

If you get:

```text
Connection timed out
```

investigate:

```text
Route Table
Security Group
NACL
Public IP
Internet Gateway
Application
```

---

# 45. Test DNS

```bash
nslookup google.com
```

or:

```bash
dig google.com
```

or:

```bash
getent hosts google.com
```

---

# 46. Packet Capture

On EC2:

```bash
sudo tcpdump -i any port 80
```

Then from your local system:

```bash
curl http://<EC2-PUBLIC-IP>
```

Watch the packets arrive.

Stop capture:

```text
Ctrl + C
```

---

# 47. Troubleshooting Exercise

## Problem

You installed NGINX, but:

```bash
curl http://<PUBLIC-IP>
```

fails.

Follow this checklist:

### Step 1

Check EC2:

```bash
aws ec2 describe-instances \
  --instance-ids $INSTANCE_ID \
  --query "Reservations[].Instances[].State.Name"
```

### Step 2

Check public IP:

```bash
aws ec2 describe-instances \
  --instance-ids $INSTANCE_ID \
  --query "Reservations[].Instances[].PublicIpAddress" \
  --output text
```

### Step 3

Check subnet:

```bash
aws ec2 describe-instances \
  --instance-ids $INSTANCE_ID \
  --query "Reservations[].Instances[].SubnetId" \
  --output text
```

### Step 4

Check route:

```bash
aws ec2 describe-route-tables \
  --route-table-ids $RT_ID
```

### Step 5

Check Security Group:

```bash
aws ec2 describe-security-groups \
  --group-ids $SG_ID
```

### Step 6

Check NGINX:

```bash
sudo systemctl status nginx
```

### Step 7

Check listening port:

```bash
sudo ss -lntp | grep ':80'
```

### Step 8

Check firewall:

```bash
sudo ufw status
```

---

# 48. Final Troubleshooting Flow

Memorize:

```text
Client
  |
  v
Public IP / DNS
  |
  v
Internet Gateway
  |
  v
Route Table
  |
  v
Subnet
  |
  v
Security Group
  |
  v
NACL
  |
  v
ENI
  |
  v
EC2
  |
  v
OS Firewall
  |
  v
Application
  |
  v
Port
```

---

# 49. Inspect Everything With AWS CLI

Run:

```bash
aws ec2 describe-vpcs \
  --vpc-ids $VPC_ID
```

```bash
aws ec2 describe-subnets \
  --filters "Name=vpc-id,Values=$VPC_ID"
```

```bash
aws ec2 describe-route-tables \
  --filters "Name=vpc-id,Values=$VPC_ID"
```

```bash
aws ec2 describe-internet-gateways \
  --filters "Name=attachment.vpc-id,Values=$VPC_ID"
```

```bash
aws ec2 describe-security-groups \
  --filters "Name=vpc-id,Values=$VPC_ID"
```

```bash
aws ec2 describe-network-acls \
  --filters "Name=vpc-id,Values=$VPC_ID"
```

```bash
aws ec2 describe-network-interfaces \
  --filters "Name=vpc-id,Values=$VPC_ID"
```

---

# 50. Resource Cleanup

⚠️ **Always clean up resources when the lab is finished.**

First terminate EC2:

```bash
aws ec2 terminate-instances \
  --instance-ids $INSTANCE_ID
```

Check:

```bash
aws ec2 describe-instances \
  --instance-ids $INSTANCE_ID \
  --query "Reservations[].Instances[].State.Name"
```

Wait until the instance reaches:

```text
terminated
```

---

# 51. Delete Private Subnet

If you created it:

```bash
aws ec2 delete-subnet \
  --subnet-id $PRIVATE_SUBNET_ID
```

---

# 52. Delete Public Subnet

```bash
aws ec2 delete-subnet \
  --subnet-id $SUBNET_ID
```

---

# 53. Delete Route Table Association

If necessary, disassociate:

```bash
aws ec2 disassociate-route-table \
  --association-id $RT_ASSOC_ID
```

---

# 54. Delete Route Table

```bash
aws ec2 delete-route-table \
  --route-table-id $RT_ID
```

---

# 55. Delete Security Group

```bash
aws ec2 delete-security-group \
  --group-id $SG_ID
```

If AWS says the Security Group is still in use, check the EC2/ENI resources and wait for termination to complete.

---

# 56. Detach Internet Gateway

```bash
aws ec2 detach-internet-gateway \
  --internet-gateway-id $IGW_ID \
  --vpc-id $VPC_ID
```

---

# 57. Delete Internet Gateway

```bash
aws ec2 delete-internet-gateway \
  --internet-gateway-id $IGW_ID
```

---

# 58. Delete VPC

Finally:

```bash
aws ec2 delete-vpc \
  --vpc-id $VPC_ID
```

Verify:

```bash
aws ec2 describe-vpcs \
  --vpc-ids $VPC_ID
```

If it no longer exists, the VPC has been removed.

---

# 59. Final Cleanup Verification

Check running instances:

```bash
aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=running" \
  --query "Reservations[].Instances[].{ID:InstanceId,Name:Tags[?Key=='Name']|[0].Value}" \
  --output table
```

Check NAT Gateways:

```bash
aws ec2 describe-nat-gateways \
  --filter "Name=state,Values=available,pending"
```

Check Elastic IPs:

```bash
aws ec2 describe-addresses
```

Check VPCs:

```bash
aws ec2 describe-vpcs
```

---

# 🧠 What You Practiced

After completing this lab, you should understand:

```text
AWS Region
    ↓
Availability Zone
    ↓
VPC
    ↓
Subnet
    ↓
Route Table
    ↓
Internet Gateway
    ↓
Security Group
    ↓
ENI
    ↓
EC2
```

You also practiced:

* CIDR
* Public subnet
* Private subnet concept
* Public IP
* Private IP
* Routing
* Security Groups
* DNS
* Connectivity testing
* Linux networking
* AWS CLI
* Troubleshooting
* Resource cleanup

---

# 🎯 Practical Interview Question

### Question

**An EC2 instance is running but you cannot access its web server from the Internet. How would you troubleshoot it?**

### Answer

I would troubleshoot from the network path:

```text
Internet
   ↓
Public IP
   ↓
Internet Gateway
   ↓
Route Table
   ↓
Subnet
   ↓
Security Group
   ↓
NACL
   ↓
ENI
   ↓
EC2
   ↓
OS Firewall
   ↓
Web Server
   ↓
Port 80/443
```

I would verify:

1. EC2 is running.
2. EC2 has the expected public IPv4 address.
3. The subnet is associated with the correct route table.
4. The route table has `0.0.0.0/0` pointing to an Internet Gateway.
5. The Security Group allows the required port.
6. NACL rules are not blocking traffic.
7. The OS firewall allows the port.
8. The web server is running.
9. The application is listening on the expected interface and port.
10. DNS resolves to the correct address if a hostname is being used.

This demonstrates a systematic DevOps troubleshooting approach.

---

# ✅ Lab Completion Checklist

* [ ] AWS CLI working
* [ ] AWS identity verified
* [ ] Region configured
* [ ] Availability Zone identified
* [ ] VPC created
* [ ] VPC CIDR understood
* [ ] Public subnet created
* [ ] Private subnet concept understood
* [ ] Internet Gateway created
* [ ] Internet Gateway attached
* [ ] Route Table created
* [ ] Default route configured
* [ ] Route Table associated with subnet
* [ ] Security Group created
* [ ] HTTP rule configured
* [ ] EC2 networking inspected
* [ ] Private IP identified
* [ ] Public IP identified
* [ ] DNS tested
* [ ] HTTP tested
* [ ] TCP connectivity tested
* [ ] Linux networking inspected
* [ ] Packet capture practiced
* [ ] AWS CLI troubleshooting practiced
* [ ] Resources cleaned up

---

# 🏆 Final Goal

Do not just say:

> "I know AWS VPC."

You should be able to explain:

> "I can design a VPC, divide it into public and private subnets, configure routing through Internet/NAT gateways where required, secure resources with Security Groups and NACLs, inspect ENIs and IP addresses, test connectivity, troubleshoot traffic flow, and automate the infrastructure with Terraform."

That is the practical AWS Networking mindset required for a DevOps Engineer.
