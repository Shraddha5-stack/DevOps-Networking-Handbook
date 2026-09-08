# 🔄 CI/CD Networking — Commands

## Chapter 33 — CI/CD Networking

This file contains practical commands used to troubleshoot and understand networking in CI/CD environments.

---

# 📚 Table of Contents

1. Git Commands
2. DNS Commands
3. IP and Interface Commands
4. Routing Commands
5. Port and Socket Commands
6. Connectivity Testing
7. HTTP/HTTPS Testing
8. SSH Commands
9. Docker Networking
10. Kubernetes Networking
11. AWS Networking
12. Network Troubleshooting
13. Packet Capture
14. Proxy Commands
15. Useful CI/CD Checks
16. Troubleshooting Workflow

---

# 1. Git Commands

## Check Git Version

```bash
git --version
```

---

## Check Remote Repository

```bash
git remote -v
```

---

## Test Git Repository Connectivity

```bash
git ls-remote https://github.com/user/repository.git
```

This checks whether Git can communicate with the remote repository.

---

## Clone Repository

```bash
git clone https://github.com/user/repository.git
```

---

## Clone Using SSH

```bash
git clone git@github.com:user/repository.git
```

---

## Test SSH Connection

```bash
ssh -T git@github.com
```

---

# 2. DNS Commands

DNS problems are common causes of CI/CD failures.

---

## Check DNS Resolution

```bash
dig example.com
```

---

## Short DNS Output

```bash
dig +short example.com
```

---

## Query a Specific DNS Server

```bash
dig @8.8.8.8 example.com
```

---

## Using nslookup

```bash
nslookup example.com
```

---

## Check Host Resolution

```bash
getent hosts example.com
```

---

## Check Resolver Configuration

```bash
cat /etc/resolv.conf
```

---

## Test Internal DNS

```bash
dig internal.example.com
```

---

# 3. IP and Network Interface Commands

## Show IP Addresses

```bash
ip addr
```

Short version:

```bash
ip a
```

---

## Show Interfaces

```bash
ip link
```

---

## Show One Interface

```bash
ip addr show eth0
```

---

## Show MAC Address

```bash
ip link show eth0
```

---

## Show Interface Statistics

```bash
ip -s link
```

Useful for identifying:

* Dropped packets
* Errors
* RX problems
* TX problems

---

# 4. Routing Commands

## Show Routing Table

```bash
ip route
```

---

## Find Route to Destination

```bash
ip route get 8.8.8.8
```

This helps identify which interface and gateway Linux would use.

---

## Show Default Gateway

```bash
ip route | grep default
```

Example:

```text
default via 192.168.1.1 dev eth0
```

---

# 5. Port and Socket Commands

## Show Listening TCP Ports

```bash
ss -lnt
```

---

## Show Listening TCP Ports With Processes

```bash
sudo ss -lntp
```

---

## Show Listening UDP Ports

```bash
ss -lnu
```

---

## Show All TCP Connections

```bash
ss -ant
```

---

## Check a Specific Port

```bash
sudo ss -lntp | grep ':8080'
```

---

## Check HTTPS

```bash
sudo ss -lntp | grep ':443'
```

---

# 6. Connectivity Testing

## Ping

```bash
ping -c 4 8.8.8.8
```

Ping tests ICMP connectivity.

Remember:

> Ping failure does not automatically mean TCP/HTTPS connectivity is unavailable.

---

## Test Host

```bash
ping -c 4 example.com
```

---

## Test TCP Port with Netcat

```bash
nc -vz example.com 443
```

Example:

```bash
nc -vz 10.0.1.10 8080
```

---

## Test Multiple Ports

```bash
nc -vz example.com 80
nc -vz example.com 443
```

---

# 7. HTTP/HTTPS Testing

## Basic HTTP Request

```bash
curl http://example.com
```

---

## HTTPS Request

```bash
curl https://example.com
```

---

## Show HTTP Headers

```bash
curl -I https://example.com
```

---

## Verbose HTTP Debugging

```bash
curl -v https://example.com
```

This is extremely useful for CI/CD troubleshooting.

---

## Follow Redirects

```bash
curl -L https://example.com
```

---

## Show Response Headers

```bash
curl -i https://example.com
```

---

## Test Specific Port

```bash
curl -v http://10.0.1.10:8080
```

---

## Test HTTPS Certificate

```bash
curl -Iv https://example.com
```

---

# 8. SSH Commands

## Connect to Server

```bash
ssh user@server
```

---

## Specify Port

```bash
ssh -p 2222 user@server
```

---

## Use Specific Key

```bash
ssh -i ~/.ssh/id_ed25519 user@server
```

---

## Verbose SSH Debugging

```bash
ssh -v user@server
```

For more debugging:

```bash
ssh -vvv user@server
```

---

## Test SSH Port

```bash
nc -vz server.example.com 22
```

---

# 9. Docker Networking

## List Docker Networks

```bash
docker network ls
```

---

## Inspect Network

```bash
docker network inspect bridge
```

---

## Create Network

```bash
docker network create ci-network
```

---

## Run Container on Network

```bash
docker run -d \
  --name app \
  --network ci-network \
  nginx
```

---

## Run Another Container

```bash
docker run -d \
  --name client \
  --network ci-network \
  alpine \
  sleep 3600
```

---

## Inspect Container

```bash
docker inspect app
```

---

## Check Container IP

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' app
```

---

## Test Container Connectivity

Enter the client:

```bash
docker exec -it client sh
```

Then:

```bash
ping app
```

If the image does not contain `ping`, install the required diagnostic tools or use a diagnostic image.

---

## Check Published Ports

```bash
docker ps
```

Example:

```text
0.0.0.0:8080->80/tcp
```

This means:

```text
Host Port 8080
       |
       v
Container Port 80
```

---

# 10. Kubernetes Networking

## Check Pods

```bash
kubectl get pods
```

---

## Show Pod IP

```bash
kubectl get pods -o wide
```

---

## Describe Pod

```bash
kubectl describe pod <pod-name>
```

---

## Check Services

```bash
kubectl get svc
```

---

## Describe Service

```bash
kubectl describe svc <service-name>
```

---

## Check Endpoints

```bash
kubectl get endpoints
```

---

## Check EndpointSlices

```bash
kubectl get endpointslices
```

---

## Check Nodes

```bash
kubectl get nodes -o wide
```

---

## Test Kubernetes DNS

Start a temporary diagnostic Pod:

```bash
kubectl run dns-test \
  --image=busybox:1.36 \
  --restart=Never \
  --rm -it \
  -- nslookup kubernetes.default
```

---

## Run a Temporary Network Debug Pod

```bash
kubectl run network-debug \
  --image=nicolaka/netshoot \
  --rm -it \
  -- bash
```

Inside it:

```bash
ip addr
ip route
ss -lnt
dig kubernetes.default
curl https://kubernetes.default.svc
```

---

## Test Service

```bash
kubectl run curl-test \
  --image=curlimages/curl \
  --rm -it \
  -- sh
```

Then:

```bash
curl http://<service-name>:<port>
```

---

## Check Network Policies

```bash
kubectl get networkpolicy
```

---

## Describe NetworkPolicy

```bash
kubectl describe networkpolicy <policy-name>
```

---

## Check Kubernetes API Server

```bash
kubectl cluster-info
```

---

## View Kubernetes Context

```bash
kubectl config current-context
```

---

## View Cluster Configuration

```bash
kubectl config view
```

---

# 11. AWS Networking Commands

## Check AWS CLI

```bash
aws --version
```

---

## Check AWS Configuration

```bash
aws configure list
```

---

## Check AWS Identity

```bash
aws sts get-caller-identity
```

This is one of the first commands to run when debugging AWS CLI authentication.

---

# VPC

## List VPCs

```bash
aws ec2 describe-vpcs
```

---

## List VPC IDs

```bash
aws ec2 describe-vpcs \
  --query 'Vpcs[].VpcId' \
  --output text
```

---

# Subnets

## List Subnets

```bash
aws ec2 describe-subnets
```

---

## List Subnet CIDRs

```bash
aws ec2 describe-subnets \
  --query 'Subnets[].{ID:SubnetId,CIDR:CidrBlock,AZ:AvailabilityZone}' \
  --output table
```

---

# Route Tables

## List Route Tables

```bash
aws ec2 describe-route-tables
```

---

## Show Routes

```bash
aws ec2 describe-route-tables \
  --query 'RouteTables[].Routes[]'
```

---

# Internet Gateways

## List Internet Gateways

```bash
aws ec2 describe-internet-gateways
```

---

# NAT Gateways

## List NAT Gateways

```bash
aws ec2 describe-nat-gateways
```

---

# Security Groups

## List Security Groups

```bash
aws ec2 describe-security-groups
```

---

## Show Security Group Rules

```bash
aws ec2 describe-security-group-rules
```

---

# Network ACLs

## List NACLs

```bash
aws ec2 describe-network-acls
```

---

# Network Interfaces

## List ENIs

```bash
aws ec2 describe-network-interfaces
```

---

# EC2 Networking

## Describe Instance

```bash
aws ec2 describe-instances \
  --instance-ids <instance-id>
```

---

## Find Private IP

```bash
aws ec2 describe-instances \
  --instance-ids <instance-id> \
  --query 'Reservations[].Instances[].PrivateIpAddress' \
  --output text
```

---

## Find Public IP

```bash
aws ec2 describe-instances \
  --instance-ids <instance-id> \
  --query 'Reservations[].Instances[].PublicIpAddress' \
  --output text
```

---

## Find Security Groups

```bash
aws ec2 describe-instances \
  --instance-ids <instance-id> \
  --query 'Reservations[].Instances[].SecurityGroups'
```

---

# Load Balancers

## List Load Balancers

```bash
aws elbv2 describe-load-balancers
```

---

## List Target Groups

```bash
aws elbv2 describe-target-groups
```

---

## Check Target Health

```bash
aws elbv2 describe-target-health \
  --target-group-arn <target-group-arn>
```

---

# Route 53

## List Hosted Zones

```bash
aws route53 list-hosted-zones
```

---

## List Records

```bash
aws route53 list-resource-record-sets \
  --hosted-zone-id <hosted-zone-id>
```

---

# VPC Endpoints

```bash
aws ec2 describe-vpc-endpoints
```

---

# VPC Flow Logs

```bash
aws ec2 describe-flow-logs
```

---

# 12. Network Troubleshooting

## Check DNS

```bash
dig example.com
```

↓

## Check IP

```bash
ip addr
```

↓

## Check Route

```bash
ip route
```

↓

## Check Port

```bash
nc -vz <host> <port>
```

↓

## Check Application

```bash
curl -v http://<host>:<port>
```

---

# 13. Packet Capture

## Capture All Traffic

```bash
sudo tcpdump -i any
```

---

## Capture HTTPS Traffic

```bash
sudo tcpdump -i any port 443
```

---

## Capture HTTP Traffic

```bash
sudo tcpdump -i any port 80
```

---

## Capture Traffic From Specific Host

```bash
sudo tcpdump -i any host 10.0.1.10
```

---

## Capture Specific Port

```bash
sudo tcpdump -i any port 8080
```

---

## Read a Capture File

```bash
tcpdump -r capture.pcap
```

---

# 14. Proxy Commands

## Check HTTP Proxy

```bash
echo $HTTP_PROXY
```

---

## Check HTTPS Proxy

```bash
echo $HTTPS_PROXY
```

---

## Check NO_PROXY

```bash
echo $NO_PROXY
```

---

## Test Without Proxy

For a one-off test:

```bash
env -u HTTP_PROXY -u HTTPS_PROXY curl -v https://example.com
```

Also consider lowercase variables because some tools use them:

```bash
echo $http_proxy
echo $https_proxy
echo $no_proxy
```

---

# 15. Useful CI/CD Checks

## Check Current User

```bash
whoami
```

---

## Check Hostname

```bash
hostname
```

---

## Check OS

```bash
cat /etc/os-release
```

---

## Check Environment

```bash
env
```

Be careful when displaying environment variables because CI environments may contain sensitive values.

---

## Check PATH

```bash
echo $PATH
```

---

## Check DNS

```bash
getent hosts github.com
```

---

## Check Internet Connectivity

```bash
curl -I https://github.com
```

---

## Check Registry Connectivity

```bash
curl -I https://registry-1.docker.io
```

---

## Check Kubernetes API

```bash
kubectl cluster-info
```

---

## Check AWS Authentication

```bash
aws sts get-caller-identity
```

---

# 16. GitHub Actions Example Checks

Inside a workflow, you can use commands such as:

```yaml
- name: Network Diagnostics
  run: |
    hostname
    ip addr
    ip route
    getent hosts github.com
    curl -I https://github.com
```

For a controlled debugging workflow, you can also check:

```yaml
- name: Check Tools
  run: |
    git --version
    docker --version
    kubectl version --client
    aws --version
```

Do not print secrets.

---

# 17. Docker CI/CD Diagnostics

Check Docker:

```bash
docker version
```

Check Docker daemon:

```bash
docker info
```

Check networks:

```bash
docker network ls
```

Check containers:

```bash
docker ps
```

Check container networking:

```bash
docker inspect <container>
```

---

# 18. Kubernetes CI/CD Diagnostics

Check context:

```bash
kubectl config current-context
```

Check cluster:

```bash
kubectl cluster-info
```

Check nodes:

```bash
kubectl get nodes -o wide
```

Check Pods:

```bash
kubectl get pods -A -o wide
```

Check Services:

```bash
kubectl get svc -A
```

Check events:

```bash
kubectl get events -A --sort-by=.lastTimestamp
```

---

# 19. AWS CI/CD Diagnostics

Check identity:

```bash
aws sts get-caller-identity
```

Check region:

```bash
aws configure get region
```

Check EC2:

```bash
aws ec2 describe-instances
```

Check VPC:

```bash
aws ec2 describe-vpcs
```

Check subnets:

```bash
aws ec2 describe-subnets
```

Check routes:

```bash
aws ec2 describe-route-tables
```

Check Security Groups:

```bash
aws ec2 describe-security-groups
```

---

# 20. CI/CD Network Troubleshooting Flow

Use this sequence:

```text
                CI/CD FAILURE
                     |
                     v
                Identify Source
                     |
                     v
              Identify Destination
                     |
                     v
                  DNS?
                     |
                     v
                   IP?
                     |
                     v
                  Route?
                     |
                     v
                  Gateway?
                     |
                     v
                   Port?
                     |
                     v
             Firewall / SG / NACL?
                     |
                     v
                   Proxy?
                     |
                     v
              Authentication?
                     |
                     v
                Application?
```

---

# 21. Example: Git Clone Failure

Run:

```bash
getent hosts github.com
```

Then:

```bash
curl -I https://github.com
```

Then:

```bash
git ls-remote https://github.com/user/repository.git
```

If using SSH:

```bash
nc -vz github.com 22
```

Then:

```bash
ssh -vT git@github.com
```

---

# 22. Example: Container Registry Failure

Check DNS:

```bash
dig registry.example.com
```

Check HTTPS:

```bash
curl -v https://registry.example.com
```

Check Docker:

```bash
docker info
```

Check login:

```bash
docker login registry.example.com
```

Then test:

```bash
docker push registry.example.com/myapp:1.0
```

---

# 23. Example: Kubernetes Deployment Failure

Check:

```bash
kubectl config current-context
```

Then:

```bash
kubectl cluster-info
```

Then:

```bash
kubectl get nodes
```

Then:

```bash
kubectl get pods -A
```

Then:

```bash
kubectl get svc -A
```

If application traffic fails:

```bash
kubectl get networkpolicy -A
```

---

# 24. Example: Private Runner Cannot Reach Internet

Check:

```bash
ip route
```

Check DNS:

```bash
getent hosts example.com
```

Check HTTPS:

```bash
curl -v https://example.com
```

In AWS, verify:

```text
Private Subnet
      ↓
Route Table
      ↓
NAT Gateway
      ↓
Internet Gateway
      ↓
Internet
```

---

# 25. Example: Application Port Not Reachable

First check the server:

```bash
ss -lntp
```

Then locally:

```bash
curl http://localhost:8080
```

Then from another host:

```bash
nc -vz <server-ip> 8080
```

Then check:

```text
Security Group
NACL
Firewall
Route
Application
```

---

# 26. Quick Command Cheat Sheet

| Purpose                | Command                            |
| ---------------------- | ---------------------------------- |
| IP address             | `ip addr`                          |
| Interfaces             | `ip link`                          |
| Routes                 | `ip route`                         |
| Route lookup           | `ip route get <IP>`                |
| DNS                    | `dig <domain>`                     |
| DNS short              | `dig +short <domain>`              |
| Resolver               | `cat /etc/resolv.conf`             |
| Listening ports        | `ss -lntp`                         |
| TCP test               | `nc -vz <host> <port>`             |
| HTTP test              | `curl -v <URL>`                    |
| SSH debug              | `ssh -vvv user@host`               |
| Trace route            | `traceroute <host>`                |
| Packet capture         | `sudo tcpdump -i any`              |
| Docker networks        | `docker network ls`                |
| Docker network details | `docker network inspect <network>` |
| Kubernetes Pods        | `kubectl get pods -o wide`         |
| Kubernetes Services    | `kubectl get svc`                  |
| Kubernetes DNS         | `nslookup <service>`               |
| AWS identity           | `aws sts get-caller-identity`      |
| AWS VPCs               | `aws ec2 describe-vpcs`            |
| AWS subnets            | `aws ec2 describe-subnets`         |
| AWS routes             | `aws ec2 describe-route-tables`    |
| AWS SGs                | `aws ec2 describe-security-groups` |

---

# 🧠 Golden Rule

When debugging CI/CD networking, remember:

```text
SOURCE
  ↓
DNS
  ↓
IP
  ↓
ROUTE
  ↓
GATEWAY
  ↓
PORT
  ↓
FIREWALL
  ↓
SECURITY GROUP
  ↓
NACL
  ↓
PROXY
  ↓
AUTHENTICATION
  ↓
APPLICATION
```

Don't randomly run commands.

First identify **what is communicating with what**.

Then test each layer.

---

# 🎯 Interview Tip

If an interviewer asks:

**"How do you troubleshoot a CI/CD network issue?"**

Answer:

> "First I identify the source and destination of the connection. Then I check DNS resolution, IP addressing, routing, gateway connectivity, required port, firewall and cloud security controls such as Security Groups and NACLs. If a proxy or private network is involved, I verify that as well. Finally, I check authentication and the application itself. I use commands such as `dig`, `ip route`, `ss`, `nc`, `curl`, `tcpdump`, AWS CLI, Docker CLI, and kubectl depending on the environment."

---

# 🚀 Chapter 33 Commands Complete

You should now be comfortable using networking commands across:

```text
Linux
  ↓
Git
  ↓
CI/CD
  ↓
Docker
  ↓
Kubernetes
  ↓
AWS
```

The next file is:

```text
practical-lab.md
```

This will be a **hands-on CI/CD Networking lab** that you can actually perform from your VS Code terminal.
