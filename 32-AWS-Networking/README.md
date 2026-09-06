# 🌐 AWS Networking

AWS Networking is the foundation for designing secure, scalable, and highly available applications in Amazon Web Services.

As a DevOps Engineer, you need to understand how AWS resources communicate with:

* The Internet
* Other AWS services
* Other VPCs
* On-premises networks
* Public and private subnets
* Application Load Balancers
* EC2 instances
* Databases
* Containers
* Kubernetes clusters

---

# 📚 Table of Contents

1. What is AWS Networking?
2. Amazon VPC
3. VPC Architecture
4. CIDR
5. Public and Private Subnets
6. Availability Zones
7. Route Tables
8. Internet Gateway
9. NAT Gateway
10. Security Groups
11. Network ACLs
12. VPC DNS
13. Elastic IP
14. VPC Peering
15. Transit Gateway
16. VPC Endpoints
17. Load Balancers
18. AWS Networking and EC2
19. AWS Networking and Containers
20. AWS Networking and Kubernetes
21. Real-World Architecture
22. Common AWS Networking Commands
23. Troubleshooting
24. DevOps Use Cases
25. Interview Preparation
26. Final Checklist

---

# 1. What is AWS Networking?

AWS Networking is the collection of AWS services and networking components used to connect, isolate, secure, and route traffic between AWS resources and external networks.

A typical AWS application may contain:

```text
Internet
   |
   v
Internet Gateway
   |
   v
Public Subnet
   |
   v
Load Balancer
   |
   v
Private Subnet
   |
   v
Application Servers
   |
   v
Database
```

The goal is to control:

* Who can communicate?
* From where?
* Through which route?
* On which port?
* Using which protocol?
* Is the resource publicly accessible?
* Is the traffic encrypted?
* Is the architecture highly available?

---

# 2. Amazon VPC

## What is VPC?

**VPC = Virtual Private Cloud**

Amazon VPC allows you to create a logically isolated network inside AWS.

You can control:

* IP address ranges
* Subnets
* Routing
* Internet access
* Network security
* DNS
* Connectivity between networks

Example:

```text
AWS
└── VPC
    ├── Public Subnet
    ├── Private Subnet
    ├── Route Tables
    ├── Internet Gateway
    ├── NAT Gateway
    ├── Security Groups
    └── Network ACL
```

---

# 3. VPC Architecture

A VPC can be designed across multiple Availability Zones.

Example:

```text
                    AWS Region
                        |
          +-------------+-------------+
          |                           |
      AZ-1                         AZ-2
          |                           |
   +------+-------+            +------+-------+
   |              |            |              |
Public         Private       Public         Private
Subnet         Subnet        Subnet         Subnet
   |              |            |              |
  ALB            EC2          ALB            EC2
```

This architecture improves:

* Availability
* Fault tolerance
* Scalability
* Disaster recovery

---

# 4. CIDR

CIDR stands for:

**Classless Inter-Domain Routing**

CIDR defines an IP address range.

Example:

```text
10.0.0.0/16
```

This can be used as a VPC CIDR.

A VPC:

```text
10.0.0.0/16
```

can contain subnets such as:

```text
10.0.1.0/24
10.0.2.0/24
10.0.3.0/24
10.0.4.0/24
```

Example architecture:

```text
VPC
10.0.0.0/16

├── Public Subnet
│   └── 10.0.1.0/24
│
├── Private App Subnet
│   └── 10.0.2.0/24
│
└── Private DB Subnet
    └── 10.0.3.0/24
```

## Important

The subnet CIDR must be inside the VPC CIDR and must not overlap with another subnet in the same VPC.

---

# 5. Public and Private Subnets

## Public Subnet

A subnet is considered public when its route table has a route to an Internet Gateway.

Example:

```text
0.0.0.0/0
      |
      v
Internet Gateway
```

Typical resources:

* Load Balancers
* Bastion hosts
* Public-facing EC2 instances
* NAT Gateway

---

## Private Subnet

A private subnet does not have a direct route to an Internet Gateway.

Example:

```text
Private EC2
     |
     v
NAT Gateway
     |
     v
Internet Gateway
     |
     v
Internet
```

Typical resources:

* Application servers
* Backend services
* Databases
* Internal services

---

# 6. Availability Zones

An Availability Zone is an isolated location within an AWS Region.

Example:

```text
Region: ap-south-1

├── ap-south-1a
├── ap-south-1b
└── ap-south-1c
```

For production systems, resources are commonly distributed across multiple Availability Zones.

Example:

```text
          Application
              |
       Load Balancer
          /       \
         /         \
       AZ-1       AZ-2
        |           |
      EC2         EC2
```

If one Availability Zone experiences a failure, the application can continue serving traffic from another AZ.

---

# 7. Route Tables

A route table determines where network traffic should go.

Example:

```text
Destination       Target

10.0.0.0/16       local
0.0.0.0/0         igw-xxxxx
```

Meaning:

```text
10.0.0.0/16
     |
     +----> Stay inside VPC

0.0.0.0/0
     |
     +----> Internet Gateway
```

Another example:

```text
Destination       Target

10.0.0.0/16       local
0.0.0.0/0         nat-xxxxx
```

This is commonly used for a private subnet that needs outbound Internet access.

---

# 8. Internet Gateway

An Internet Gateway allows communication between a VPC and the Internet.

Architecture:

```text
Internet
    |
    v
Internet Gateway
    |
    v
Public Subnet
    |
    v
EC2
```

An Internet Gateway is attached to a VPC.

A route table must also contain an appropriate route, such as:

```text
0.0.0.0/0 → Internet Gateway
```

---

# 9. NAT Gateway

NAT stands for:

**Network Address Translation**

A NAT Gateway allows resources in a private subnet to initiate outbound connections to the Internet without allowing unsolicited inbound Internet connections to those private resources.

Example:

```text
Private EC2
    |
    v
NAT Gateway
    |
    v
Internet Gateway
    |
    v
Internet
```

Example use case:

An application server in a private subnet needs to:

```text
apt update
download packages
call an external API
download dependencies
```

The private server can use a NAT Gateway for outbound access.

---

# 10. Security Groups

A Security Group acts as a virtual firewall for AWS resources such as EC2 instances.

Security Groups control traffic at the resource level.

Example:

```text
Internet
   |
   | TCP 443
   v
Load Balancer
   |
   | TCP 8080
   v
Application Server
```

Example rules:

```text
Inbound

HTTPS
TCP
443
Source: 0.0.0.0/0
```

Another example:

```text
Inbound

SSH
TCP
22
Source: Trusted IP
```

## Important characteristics

Security Groups are:

* Stateful
* Associated with network interfaces/resources
* Primarily used for instance-level traffic control
* Allow-rule based

---

# 11. Network ACLs

NACL stands for:

**Network Access Control List**

A Network ACL controls traffic at the subnet level.

Example:

```text
VPC
 |
 +-- Subnet
      |
      +-- NACL
           |
           +-- EC2
           +-- EC2
```

NACLs support:

* Allow rules
* Deny rules
* Inbound rules
* Outbound rules

## Security Group vs NACL

| Feature        | Security Group                         | NACL                          |
| -------------- | -------------------------------------- | ----------------------------- |
| Level          | Resource/ENI                           | Subnet                        |
| Stateful       | Yes                                    | No                            |
| Rules          | Allow                                  | Allow + Deny                  |
| Return traffic | Automatically allowed when appropriate | Must be explicitly considered |
| Common use     | Resource security                      | Subnet-level filtering        |

---

# 12. VPC DNS

AWS VPC provides DNS functionality for resources inside the VPC.

DNS is used to convert names into IP addresses.

Example:

```text
database.internal
        |
        v
10.0.3.20
```

AWS commonly uses Amazon Route 53 for DNS services.

DNS is important for:

* EC2
* Load Balancers
* Applications
* Service discovery
* Private resources

---

# 13. Elastic IP

An Elastic IP is a static public IPv4 address associated with an AWS resource.

Example:

```text
Internet
    |
    v
Elastic IP
    |
    v
EC2
```

Elastic IPs should be used carefully because unnecessary allocation can create costs.

---

# 14. VPC Peering

VPC Peering allows two VPCs to communicate privately.

Example:

```text
VPC-A
10.0.0.0/16
     |
     |
 VPC Peering
     |
     |
VPC-B
10.1.0.0/16
```

Important:

The CIDR ranges should not overlap.

Routes must be configured so that traffic can travel between the VPCs.

---

# 15. Transit Gateway

AWS Transit Gateway provides a centralized way to connect multiple VPCs and networks.

Without Transit Gateway:

```text
VPC-A ---- VPC-B
  \         /
   \       /
     VPC-C
```

As the number of VPCs increases, this can become difficult to manage.

With Transit Gateway:

```text
       VPC-A
          |
       VPC-B
          |
          v
   Transit Gateway
      /       \
     /         \
  VPC-C       VPC-D
```

This is useful for large AWS environments.

---

# 16. VPC Endpoints

VPC Endpoints allow private communication from a VPC to supported AWS services without requiring public Internet access.

Example:

```text
Private EC2
    |
    v
VPC Endpoint
    |
    v
Amazon S3
```

This can reduce the need for:

```text
Private EC2
    |
    v
NAT Gateway
    |
    v
Internet
    |
    v
AWS Service
```

Common endpoint types include:

* Gateway endpoints
* Interface endpoints

A common example is accessing S3 privately from a VPC.

---

# 17. Load Balancers

AWS provides Elastic Load Balancing.

Common types include:

## Application Load Balancer

ALB works at Layer 7.

It understands protocols such as:

* HTTP
* HTTPS

Example:

```text
Users
  |
  v
ALB
  |
  +----> EC2
  |
  +----> EC2
  |
  +----> EC2
```

---

## Network Load Balancer

NLB operates at Layer 4 and is designed for high-performance TCP/UDP/TLS traffic.

Example:

```text
Client
  |
  v
NLB
  |
  +----> Server
  |
  +----> Server
```

---

# 18. AWS Networking and EC2

A typical EC2 networking architecture:

```text
Internet
   |
   v
Internet Gateway
   |
   v
Public Subnet
   |
   v
EC2
```

For a private EC2 instance:

```text
Internet
   |
   v
Internet Gateway
   |
   v
NAT Gateway
   |
   v
Private Subnet
   |
   v
EC2
```

---

# 19. AWS Networking and Containers

Containers can run in AWS using services such as:

* Amazon ECS
* Amazon EKS

A simplified architecture:

```text
Internet
   |
   v
Load Balancer
   |
   v
ECS/EKS
   |
   +---- Container
   |
   +---- Container
   |
   +---- Container
```

Networking becomes especially important when containers communicate with:

* Databases
* APIs
* Load Balancers
* AWS services
* Other containers

---

# 20. AWS Networking and Kubernetes

Amazon EKS runs Kubernetes on AWS.

A simplified architecture:

```text
                 AWS VPC
                    |
        +-----------+-----------+
        |                       |
   Public Subnets          Private Subnets
        |                       |
     Load Balancer          EKS Nodes
                                |
                         +------+------+
                         |             |
                       Pod           Pod
                         |
                      Service
```

Important EKS networking concepts include:

* VPC
* Subnets
* Security Groups
* Route Tables
* AWS VPC CNI
* Load Balancers
* Pod networking
* Private/public subnets

---

# 21. Real-World AWS Architecture

A common production architecture:

```text
                         Internet
                            |
                            v
                    Internet Gateway
                            |
                            v
                 +---------------------+
                 |   Public Subnets    |
                 |                     |
                 |  Application LB     |
                 |       /   \         |
                 +------/-----\--------+
                       /       \
                      v         v
              +-----------------------+
              |    Private Subnets    |
              |                       |
              |   App Server   App    |
              |      |          |     |
              +------+----------+-----+
                     |
                     v
              +----------------+
              | Database Subnet|
              |                |
              |    Database    |
              +----------------+
```

Production architecture commonly separates:

```text
Public
Private Application
Private Database
```

This reduces unnecessary public exposure.

---

# 22. Common AWS Networking Commands

## Check AWS identity

```bash
aws sts get-caller-identity
```

## List VPCs

```bash
aws ec2 describe-vpcs
```

## List subnets

```bash
aws ec2 describe-subnets
```

## List route tables

```bash
aws ec2 describe-route-tables
```

## List Internet Gateways

```bash
aws ec2 describe-internet-gateways
```

## List security groups

```bash
aws ec2 describe-security-groups
```

## List network interfaces

```bash
aws ec2 describe-network-interfaces
```

## List NAT Gateways

```bash
aws ec2 describe-nat-gateways
```

---

# 23. Troubleshooting AWS Networking

When an application cannot communicate, troubleshoot layer by layer.

## Step 1 — Check the resource

```text
Is EC2 running?
```

## Step 2 — Check subnet

```text
Which subnet is the resource in?
```

## Step 3 — Check route table

```text
Does the subnet have the required route?
```

## Step 4 — Check Internet Gateway/NAT

```text
Does the resource need Internet access?
```

## Step 5 — Check Security Group

```text
Is the required port allowed?
```

## Step 6 — Check NACL

```text
Is traffic blocked at subnet level?
```

## Step 7 — Check application

```text
Is the application actually listening?
```

Example:

```bash
ss -lntp
```

## Step 8 — Test connectivity

```bash
ping <IP>
```

```bash
curl http://<IP>:<PORT>
```

For TCP testing:

```bash
nc -vz <IP> <PORT>
```

---

# 24. DevOps Use Cases

AWS networking is used in almost every DevOps environment.

## CI/CD

```text
GitHub
   |
   v
CI/CD
   |
   v
AWS
   |
   v
Private Application
```

## Microservices

```text
Load Balancer
      |
      v
Service A
      |
      v
Service B
      |
      v
Database
```

## Kubernetes

```text
Internet
   |
   v
AWS Load Balancer
   |
   v
EKS
   |
   v
Pods
```

## Terraform

AWS networking can be completely automated using Terraform.

Example:

```text
Terraform
    |
    +---- VPC
    +---- Subnets
    +---- Route Tables
    +---- IGW
    +---- NAT
    +---- Security Groups
    +---- EC2
```

---

# 25. Interview Preparation

You should be able to explain:

### Basic

* What is AWS VPC?
* What is a subnet?
* What is CIDR?
* What is an Availability Zone?
* What is a Route Table?
* What is an Internet Gateway?
* What is a NAT Gateway?

### Security

* What is a Security Group?
* What is a Network ACL?
* Security Group vs NACL?
* Why should databases be private?
* How do you restrict SSH access?

### Connectivity

* What is VPC Peering?
* What is Transit Gateway?
* What is a VPC Endpoint?
* How does a private subnet access the Internet?
* How does a public subnet access the Internet?

### Load Balancing

* What is ALB?
* What is NLB?
* ALB vs NLB?
* How does a Load Balancer communicate with EC2?

### DevOps

* How would you design a production VPC?
* How would you secure an application?
* How would you troubleshoot an unreachable EC2 instance?
* How does EKS networking work?
* How would Terraform create AWS networking infrastructure?

---

# 26. Final Mental Model

Remember AWS networking using this flow:

```text
                    AWS REGION
                        |
                       VPC
                        |
             +----------+----------+
             |                     |
        Public Subnet        Private Subnet
             |                     |
       Load Balancer          Application
             |                     |
       Internet Gateway            |
                                   |
                              Database
```

For Internet access:

```text
Public:
Resource
   |
Route Table
   |
Internet Gateway
   |
Internet
```

Private outbound:

```text
Private Resource
      |
Route Table
      |
 NAT Gateway
      |
Internet Gateway
      |
Internet
```

Security:

```text
Security Group
      +
    NACL
      +
 Route Tables
      +
   IAM
```

---

# ✅ AWS Networking Checklist

Before considering this chapter complete, understand:

* [ ] AWS VPC
* [ ] CIDR
* [ ] Subnets
* [ ] Public subnet
* [ ] Private subnet
* [ ] Availability Zones
* [ ] Route Tables
* [ ] Internet Gateway
* [ ] NAT Gateway
* [ ] Security Groups
* [ ] Network ACL
* [ ] VPC DNS
* [ ] Elastic IP
* [ ] VPC Peering
* [ ] Transit Gateway
* [ ] VPC Endpoints
* [ ] ALB
* [ ] NLB
* [ ] EC2 networking
* [ ] Container networking
* [ ] EKS networking
* [ ] AWS CLI networking commands
* [ ] AWS networking troubleshooting
* [ ] Production VPC architecture
* [ ] Terraform networking concepts

---

# 🎯 DevOps Engineer Goal

Do not only memorize AWS networking services.

You should be able to look at an architecture and answer:

> **Where is the resource?**

> **What IP range does it use?**

> **Which subnet is it in?**

> **Where does the traffic go?**

> **Which security rule allows or blocks it?**

> **Does it need Internet access?**

> **Should it be public or private?**

> **How can I troubleshoot the connection?**

That is the mindset required for real-world AWS networking.
