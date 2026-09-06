# 🌐 AWS Networking — Commands Reference

## Chapter 32 — AWS Networking

This file contains practical AWS CLI and Linux networking commands useful for DevOps Engineers working with AWS networking.

> **Important:** Run AWS CLI commands only after configuring valid AWS credentials and a region.

---

# 📚 Table of Contents

1. AWS CLI Basics
2. AWS Identity
3. AWS Region
4. VPC Commands
5. Subnet Commands
6. Route Table Commands
7. Internet Gateway Commands
8. NAT Gateway Commands
9. Security Group Commands
10. Network ACL Commands
11. Network Interface Commands
12. Elastic IP Commands
13. VPC Peering Commands
14. VPC Endpoint Commands
15. EC2 Networking Commands
16. Load Balancer Commands
17. DNS Commands
18. Linux Networking Commands
19. Connectivity Testing
20. JSON Filtering
21. Useful Troubleshooting Commands
22. Command Cheat Sheet

---

# 1. AWS CLI Basics

Check AWS CLI version:

```bash
aws --version
```

Check current configuration:

```bash
aws configure list
```

Configure AWS CLI:

```bash
aws configure
```

Set a default region:

```bash
aws configure set region ap-south-1
```

Check current region:

```bash
aws configure get region
```

---

# 2. AWS Identity

Check which AWS account/user/role is being used:

```bash
aws sts get-caller-identity
```

Example:

```bash
aws sts get-caller-identity
```

This is one of the first commands to run when troubleshooting AWS CLI authentication.

If credentials are invalid, fix authentication before running resource-management commands.

---

# 3. AWS Region

List AWS regions:

```bash
aws ec2 describe-regions
```

List region names only:

```bash
aws ec2 describe-regions \
  --query "Regions[].RegionName" \
  --output text
```

Set Mumbai region:

```bash
aws configure set region ap-south-1
```

Verify:

```bash
aws configure get region
```

---

# 4. VPC Commands

## List VPCs

```bash
aws ec2 describe-vpcs
```

List VPC IDs:

```bash
aws ec2 describe-vpcs \
  --query "Vpcs[].VpcId" \
  --output text
```

List VPC CIDRs:

```bash
aws ec2 describe-vpcs \
  --query "Vpcs[].{VPC:VpcId,CIDR:CidrBlock}" \
  --output table
```

---

## Find a Specific VPC

```bash
aws ec2 describe-vpcs \
  --vpc-ids vpc-xxxxxxxx
```

---

## Filter by Tag

```bash
aws ec2 describe-vpcs \
  --filters "Name=tag:Name,Values=MyVPC"
```

---

# 5. Subnet Commands

## List all subnets

```bash
aws ec2 describe-subnets
```

## List subnet IDs

```bash
aws ec2 describe-subnets \
  --query "Subnets[].SubnetId" \
  --output text
```

## Show subnet details

```bash
aws ec2 describe-subnets \
  --query "Subnets[].{Subnet:SubnetId,VPC:VpcId,CIDR:CidrBlock,AZ:AvailabilityZone}" \
  --output table
```

## Show public IPv4 setting

```bash
aws ec2 describe-subnets \
  --query "Subnets[].{Subnet:SubnetId,CIDR:CidrBlock,AZ:AvailabilityZone,MapPublicIP:MapPublicIpOnLaunch}" \
  --output table
```

---

# 6. Route Table Commands

## List route tables

```bash
aws ec2 describe-route-tables
```

## Show route tables in table format

```bash
aws ec2 describe-route-tables \
  --query "RouteTables[].{RouteTable:RouteTableId,VPC:VpcId}" \
  --output table
```

## Show routes

```bash
aws ec2 describe-route-tables \
  --query "RouteTables[].Routes[]" \
  --output table
```

## Find routes for a VPC

```bash
aws ec2 describe-route-tables \
  --filters "Name=vpc-id,Values=vpc-xxxxxxxx"
```

---

# 7. Internet Gateway Commands

## List Internet Gateways

```bash
aws ec2 describe-internet-gateways
```

## Show Internet Gateway IDs

```bash
aws ec2 describe-internet-gateways \
  --query "InternetGateways[].InternetGatewayId" \
  --output text
```

## Find Internet Gateway for a VPC

```bash
aws ec2 describe-internet-gateways \
  --filters "Name=attachment.vpc-id,Values=vpc-xxxxxxxx"
```

---

# 8. NAT Gateway Commands

## List NAT Gateways

```bash
aws ec2 describe-nat-gateways
```

## Show NAT Gateway state

```bash
aws ec2 describe-nat-gateways \
  --query "NatGateways[].{ID:NatGatewayId,State:State,Subnet:SubnetId,VPC:VpcId}" \
  --output table
```

## Filter by VPC

```bash
aws ec2 describe-nat-gateways \
  --filter "Name=vpc-id,Values=vpc-xxxxxxxx"
```

## Filter available NAT Gateways

```bash
aws ec2 describe-nat-gateways \
  --filter "Name=state,Values=available"
```

Possible NAT Gateway states include:

```text
pending
available
deleting
deleted
failed
```

---

# 9. Security Group Commands

## List Security Groups

```bash
aws ec2 describe-security-groups
```

## Show Security Group IDs

```bash
aws ec2 describe-security-groups \
  --query "SecurityGroups[].GroupId" \
  --output text
```

## Show names and IDs

```bash
aws ec2 describe-security-groups \
  --query "SecurityGroups[].{Name:GroupName,ID:GroupId,VPC:VpcId}" \
  --output table
```

## Show one Security Group

```bash
aws ec2 describe-security-groups \
  --group-ids sg-xxxxxxxx
```

---

## Show inbound rules

```bash
aws ec2 describe-security-groups \
  --group-ids sg-xxxxxxxx \
  --query "SecurityGroups[].IpPermissions"
```

## Show outbound rules

```bash
aws ec2 describe-security-groups \
  --group-ids sg-xxxxxxxx \
  --query "SecurityGroups[].IpPermissionsEgress"
```

---

# 10. Network ACL Commands

## List NACLs

```bash
aws ec2 describe-network-acls
```

## Find NACLs for a VPC

```bash
aws ec2 describe-network-acls \
  --filters "Name=vpc-id,Values=vpc-xxxxxxxx"
```

## Show NACL entries

```bash
aws ec2 describe-network-acls \
  --query "NetworkAcls[].Entries" \
  --output table
```

## Show NACL and subnet association

```bash
aws ec2 describe-network-acls \
  --query "NetworkAcls[].{NACL:NetworkAclId,VPC:VpcId,Associations:Associations}" \
  --output json
```

---

# 11. Network Interface Commands

An ENI is an Elastic Network Interface.

## List ENIs

```bash
aws ec2 describe-network-interfaces
```

## Show ENI information

```bash
aws ec2 describe-network-interfaces \
  --query "NetworkInterfaces[].{ENI:NetworkInterfaceId,PrivateIP:PrivateIpAddress,Subnet:SubnetId,VPC:VpcId}" \
  --output table
```

## Find ENI by private IP

```bash
aws ec2 describe-network-interfaces \
  --filters "Name=addresses.private-ip-address,Values=10.0.1.10"
```

## Find ENIs in a subnet

```bash
aws ec2 describe-network-interfaces \
  --filters "Name=subnet-id,Values=subnet-xxxxxxxx"
```

---

# 12. Elastic IP Commands

## List Elastic IP addresses

```bash
aws ec2 describe-addresses
```

## Show allocation IDs

```bash
aws ec2 describe-addresses \
  --query "Addresses[].{PublicIP:PublicIp,Allocation:AllocationId,Association:AssociationId}" \
  --output table
```

---

# 13. VPC Peering Commands

## List peering connections

```bash
aws ec2 describe-vpc-peering-connections
```

## Show peering status

```bash
aws ec2 describe-vpc-peering-connections \
  --query "VpcPeeringConnections[].{ID:VpcPeeringConnectionId,Status:Status.Code,Requester:RequesterVpcInfo.VpcId,Accepter:AccepterVpcInfo.VpcId}" \
  --output table
```

---

# 14. VPC Endpoint Commands

## List VPC endpoints

```bash
aws ec2 describe-vpc-endpoints
```

## Show endpoint information

```bash
aws ec2 describe-vpc-endpoints \
  --query "VpcEndpoints[].{ID:VpcEndpointId,Service:ServiceName,Type:VpcEndpointType,VPC:VpcId,State:State}" \
  --output table
```

## Find endpoints for a VPC

```bash
aws ec2 describe-vpc-endpoints \
  --filters "Name=vpc-id,Values=vpc-xxxxxxxx"
```

---

# 15. EC2 Networking Commands

## List EC2 instances

```bash
aws ec2 describe-instances
```

## Show instance networking

```bash
aws ec2 describe-instances \
  --query "Reservations[].Instances[].{Instance:InstanceId,PrivateIP:PrivateIpAddress,PublicIP:PublicIpAddress,Subnet:SubnetId,VPC:VpcId}" \
  --output table
```

## Show instance state

```bash
aws ec2 describe-instances \
  --query "Reservations[].Instances[].{ID:InstanceId,State:State.Name}" \
  --output table
```

## Find instances in a subnet

```bash
aws ec2 describe-instances \
  --filters "Name=subnet-id,Values=subnet-xxxxxxxx"
```

## Find instances in a VPC

```bash
aws ec2 describe-instances \
  --filters "Name=vpc-id,Values=vpc-xxxxxxxx"
```

---

# 16. Load Balancer Commands

AWS CLI networking work often involves Elastic Load Balancing.

## List ALB/NLB resources

```bash
aws elbv2 describe-load-balancers
```

## Show load balancer names

```bash
aws elbv2 describe-load-balancers \
  --query "LoadBalancers[].{Name:LoadBalancerName,Type:Type,State:State.Code,VPC:VpcId}" \
  --output table
```

## List target groups

```bash
aws elbv2 describe-target-groups
```

## Show target groups

```bash
aws elbv2 describe-target-groups \
  --query "TargetGroups[].{Name:TargetGroupName,Port:Port,Protocol:Protocol,VPC:VpcId}" \
  --output table
```

## Check target health

```bash
aws elbv2 describe-target-health \
  --target-group-arn <target-group-arn>
```

---

# 17. DNS Commands

## Check local DNS configuration

```bash
cat /etc/resolv.conf
```

## Resolve a hostname

```bash
nslookup example.com
```

or:

```bash
dig example.com
```

or:

```bash
getent hosts example.com
```

## Check Route 53 hosted zones

```bash
aws route53 list-hosted-zones
```

## List Route 53 records

```bash
aws route53 list-resource-record-sets \
  --hosted-zone-id <hosted-zone-id>
```

---

# 18. Linux Networking Commands

AWS troubleshooting often requires Linux networking commands inside EC2 instances.

## Show IP addresses

```bash
ip addr
```

Short form:

```bash
ip a
```

## Show routes

```bash
ip route
```

## Show network interfaces

```bash
ip link
```

## Show ARP/neighbour table

```bash
ip neigh
```

## Show listening ports

```bash
ss -lntp
```

## Show all TCP connections

```bash
ss -ant
```

## Show UDP sockets

```bash
ss -lunp
```

---

# 19. Connectivity Testing

## Ping

```bash
ping <IP>
```

Example:

```bash
ping 10.0.2.10
```

Remember:

> ICMP may be blocked by Security Groups/NACLs, so ping failure does not always mean that TCP connectivity is unavailable.

---

## Test HTTP

```bash
curl http://<IP>
```

Example:

```bash
curl http://10.0.2.10
```

Test HTTPS:

```bash
curl -I https://example.com
```

---

## Test TCP Port

```bash
nc -vz <IP> <PORT>
```

Example:

```bash
nc -vz 10.0.2.10 8080
```

Another option:

```bash
timeout 5 bash -c '</dev/tcp/10.0.2.10/8080' && echo "OPEN" || echo "CLOSED"
```

---

# 20. Trace Network Path

Use:

```bash
traceroute example.com
```

If unavailable:

```bash
tracepath example.com
```

For TCP:

```bash
traceroute -T -p 443 example.com
```

---

# 21. DNS Troubleshooting

Check DNS:

```bash
dig example.com
```

Detailed answer:

```bash
dig example.com +short
```

Check DNS server:

```bash
resolvectl status
```

Resolve:

```bash
getent hosts example.com
```

If DNS fails, investigate:

```text
DNS configuration
      ↓
VPC DNS settings
      ↓
Route 53
      ↓
Security rules
      ↓
Application
```

---

# 22. Packet Capture

`tcpdump` can capture network traffic.

Install if required:

```bash
sudo apt update
sudo apt install tcpdump
```

Capture traffic:

```bash
sudo tcpdump -i any
```

Capture traffic on port 80:

```bash
sudo tcpdump -i any port 80
```

Capture TCP traffic:

```bash
sudo tcpdump -i any tcp
```

Capture traffic from an IP:

```bash
sudo tcpdump -i any host 10.0.2.10
```

---

# 23. Curl Debugging

Basic:

```bash
curl http://example.com
```

Verbose:

```bash
curl -v http://example.com
```

Headers only:

```bash
curl -I https://example.com
```

Follow redirects:

```bash
curl -L https://example.com
```

Check HTTPS certificate/handshake details:

```bash
curl -v https://example.com
```

---

# 24. Check Local Firewall

For Ubuntu systems using UFW:

```bash
sudo ufw status
```

Detailed:

```bash
sudo ufw status verbose
```

Check iptables:

```bash
sudo iptables -L -n -v
```

If nftables is being used:

```bash
sudo nft list ruleset
```

---

# 25. Check Service

Check a service:

```bash
systemctl status nginx
```

Check whether it is listening:

```bash
ss -lntp
```

Check logs:

```bash
journalctl -u nginx
```

Follow logs:

```bash
journalctl -u nginx -f
```

---

# 26. AWS CLI Output Formats

AWS CLI supports multiple output formats.

JSON:

```bash
aws ec2 describe-vpcs --output json
```

Table:

```bash
aws ec2 describe-vpcs --output table
```

Text:

```bash
aws ec2 describe-vpcs --output text
```

---

# 27. AWS CLI Query

AWS CLI uses JMESPath queries.

Example:

```bash
aws ec2 describe-vpcs \
  --query "Vpcs[].VpcId"
```

Show VPC ID and CIDR:

```bash
aws ec2 describe-vpcs \
  --query "Vpcs[].{ID:VpcId,CIDR:CidrBlock}" \
  --output table
```

---

# 28. Useful Filtering

Find running instances:

```bash
aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=running"
```

Find stopped instances:

```bash
aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=stopped"
```

Find instances by tag:

```bash
aws ec2 describe-instances \
  --filters "Name=tag:Name,Values=web-server"
```

---

# 29. Find an EC2 Instance's IP

```bash
aws ec2 describe-instances \
  --instance-ids i-xxxxxxxx \
  --query "Reservations[].Instances[].PrivateIpAddress" \
  --output text
```

Public IP:

```bash
aws ec2 describe-instances \
  --instance-ids i-xxxxxxxx \
  --query "Reservations[].Instances[].PublicIpAddress" \
  --output text
```

---

# 30. Find an Instance's Security Groups

```bash
aws ec2 describe-instances \
  --instance-ids i-xxxxxxxx \
  --query "Reservations[].Instances[].SecurityGroups" \
  --output table
```

---

# 31. Find Instance Subnet and VPC

```bash
aws ec2 describe-instances \
  --instance-ids i-xxxxxxxx \
  --query "Reservations[].Instances[].{Subnet:SubnetId,VPC:VpcId}" \
  --output table
```

---

# 32. Network Troubleshooting Flow

Use this sequence:

```text
SOURCE
  ↓
DESTINATION
  ↓
IP ADDRESS
  ↓
SUBNET
  ↓
ROUTE TABLE
  ↓
IGW / NAT / ENDPOINT
  ↓
SECURITY GROUP
  ↓
NACL
  ↓
OS FIREWALL
  ↓
APPLICATION
  ↓
PORT
```

---

# 33. Example Troubleshooting

Suppose:

```text
EC2-A
10.0.1.10

EC2-B
10.0.2.10

Application:
Port 8080
```

Test:

```bash
nc -vz 10.0.2.10 8080
```

If it fails, check:

### 1. Route

```bash
ip route
```

### 2. Security Group

```bash
aws ec2 describe-security-groups \
  --group-ids sg-xxxxxxxx
```

### 3. NACL

```bash
aws ec2 describe-network-acls
```

### 4. Application

```bash
ss -lntp
```

### 5. Local firewall

```bash
sudo ufw status
```

### 6. Packet capture

```bash
sudo tcpdump -i any port 8080
```

---

# 34. Check Current AWS Resources

A quick VPC inspection:

```bash
aws ec2 describe-vpcs
```

```bash
aws ec2 describe-subnets
```

```bash
aws ec2 describe-route-tables
```

```bash
aws ec2 describe-internet-gateways
```

```bash
aws ec2 describe-nat-gateways
```

```bash
aws ec2 describe-security-groups
```

```bash
aws ec2 describe-network-acls
```

```bash
aws ec2 describe-network-interfaces
```

---

# 35. Useful Command Cheat Sheet

| Task                | Command                                    |
| ------------------- | ------------------------------------------ |
| AWS version         | `aws --version`                            |
| Current identity    | `aws sts get-caller-identity`              |
| Current region      | `aws configure get region`                 |
| List VPCs           | `aws ec2 describe-vpcs`                    |
| List subnets        | `aws ec2 describe-subnets`                 |
| List route tables   | `aws ec2 describe-route-tables`            |
| List IGWs           | `aws ec2 describe-internet-gateways`       |
| List NAT gateways   | `aws ec2 describe-nat-gateways`            |
| List SGs            | `aws ec2 describe-security-groups`         |
| List NACLs          | `aws ec2 describe-network-acls`            |
| List ENIs           | `aws ec2 describe-network-interfaces`      |
| List EIPs           | `aws ec2 describe-addresses`               |
| List VPC peering    | `aws ec2 describe-vpc-peering-connections` |
| List endpoints      | `aws ec2 describe-vpc-endpoints`           |
| List EC2            | `aws ec2 describe-instances`               |
| List Load Balancers | `aws elbv2 describe-load-balancers`        |
| List target groups  | `aws elbv2 describe-target-groups`         |
| DNS lookup          | `dig example.com`                          |
| Show IP             | `ip addr`                                  |
| Show routes         | `ip route`                                 |
| Show neighbours     | `ip neigh`                                 |
| Listening ports     | `ss -lntp`                                 |
| TCP test            | `nc -vz IP PORT`                           |
| HTTP test           | `curl -v URL`                              |
| Packet capture      | `sudo tcpdump -i any`                      |
| Firewall            | `sudo ufw status`                          |

---

# 🎯 DevOps Engineer Command Mindset

Do not memorize every AWS CLI command.

Instead remember the resource hierarchy:

```text
AWS
 |
Region
 |
VPC
 |
+--- Subnets
|      |
|      +--- EC2
|      +--- Load Balancer
|      +--- NAT Gateway
|
+--- Route Tables
|
+--- Internet Gateway
|
+--- Security Groups
|
+--- NACLs
|
+--- VPC Endpoints
```

When troubleshooting, identify:

```text
1. Resource
2. IP
3. Subnet
4. Route
5. Gateway
6. Security Group
7. NACL
8. OS firewall
9. Application
10. Port
```

That workflow is more valuable than memorizing hundreds of commands.
