# 🌐 AWS Networking — Detailed Notes

## Chapter 32 — DevOps Networking Handbook

AWS Networking is one of the most important areas for a DevOps Engineer because almost every AWS workload depends on networking.

A DevOps Engineer should understand how traffic moves between:

```text
User
  ↓
Internet
  ↓
Load Balancer
  ↓
Application
  ↓
Database
```

and how AWS controls that traffic using:

```text
VPC
Subnets
Route Tables
Internet Gateway
NAT Gateway
Security Groups
NACLs
DNS
VPC Endpoints
Load Balancers
```

---

# 1. AWS Region

An AWS Region is a geographical area containing multiple Availability Zones.

Examples:

```text
Mumbai
ap-south-1

Singapore
ap-southeast-1

Frankfurt
eu-central-1

Virginia
us-east-1
```

A Region is made up of multiple Availability Zones.

```text
AWS Region
│
├── Availability Zone A
├── Availability Zone B
└── Availability Zone C
```

## Why use multiple Availability Zones?

Because if one Availability Zone becomes unavailable, workloads in another AZ can continue operating.

This improves:

* High availability
* Fault tolerance
* Reliability

---

# 2. Availability Zone

An Availability Zone is a separate location within an AWS Region.

Example:

```text
ap-south-1
│
├── ap-south-1a
├── ap-south-1b
└── ap-south-1c
```

A production application should normally avoid depending on a single AZ when high availability is required.

Example:

```text
              Load Balancer
                /       \
               /         \
             AZ-A       AZ-B
              |           |
            EC2         EC2
```

---

# 3. Amazon VPC

VPC stands for:

**Virtual Private Cloud**

A VPC is a logically isolated virtual network in AWS.

You define things such as:

* IPv4/IPv6 CIDR ranges
* Subnets
* Route tables
* Network connectivity
* Security controls
* DNS settings

Example:

```text
VPC
10.0.0.0/16
│
├── Public Subnet
│   10.0.1.0/24
│
├── Private App Subnet
│   10.0.2.0/24
│
└── Private DB Subnet
    10.0.3.0/24
```

---

# 4. VPC CIDR

CIDR defines the IP address range available inside the VPC.

Example:

```text
10.0.0.0/16
```

This provides a large private IPv4 address range.

You can divide it into smaller subnet ranges.

Example:

```text
VPC
10.0.0.0/16

├── 10.0.1.0/24
├── 10.0.2.0/24
├── 10.0.3.0/24
└── 10.0.4.0/24
```

## Important rule

Subnet CIDRs must be contained within the VPC CIDR and must not overlap with other subnets in the same VPC.

---

# 5. Subnet

A subnet is an IP address range inside a VPC.

Example:

```text
VPC
10.0.0.0/16
      |
      +---- Subnet
            10.0.1.0/24
```

A subnet belongs to a single Availability Zone.

Example:

```text
VPC
│
├── AZ-A
│   └── Subnet-A
│
└── AZ-B
    └── Subnet-B
```

---

# 6. Public Subnet

A public subnet is a subnet whose route table contains a route that can reach an Internet Gateway.

Example:

```text
Public Subnet
      |
Route Table
      |
0.0.0.0/0
      |
Internet Gateway
      |
Internet
```

Common resources:

* Application Load Balancer
* Network Load Balancer
* Bastion host
* Public-facing resources
* NAT Gateway

---

# 7. Private Subnet

A private subnet does not have a direct route to an Internet Gateway.

Example:

```text
Private Subnet
      |
Route Table
      |
NAT Gateway
      |
Internet Gateway
      |
Internet
```

Common resources:

* Application servers
* Backend services
* Databases
* Internal services

---

# 8. Public vs Private Subnet

| Feature            | Public Subnet                                        | Private Subnet                                       |
| ------------------ | ---------------------------------------------------- | ---------------------------------------------------- |
| Direct IGW route   | Yes                                                  | No                                                   |
| Internet inbound   | Possible with appropriate public addressing/security | Not directly                                         |
| Typical resources  | Load Balancer                                        | Application                                          |
| Database placement | Usually no                                           | Yes                                                  |
| Internet outbound  | IGW                                                  | NAT Gateway or VPC Endpoint depending on destination |

Remember:

> A subnet is not "public" simply because it has a public IP somewhere inside it. Its routing determines whether it is public.

---

# 9. Route Table

A route table determines where packets should be sent.

Example:

```text
Destination       Target

10.0.0.0/16       local
0.0.0.0/0         igw-123456
```

Meaning:

```text
10.0.0.0/16
    ↓
Keep traffic inside VPC

0.0.0.0/0
    ↓
Send traffic toward Internet Gateway
```

---

# 10. Local Route

Every VPC route table has a local route for the VPC's CIDR.

Example:

```text
Destination
10.0.0.0/16

Target
local
```

This allows communication between resources in the VPC according to the applicable security controls.

---

# 11. Default Route

A default route is commonly:

```text
0.0.0.0/0
```

It means:

> Traffic destined for addresses that do not match a more specific route should use this route.

Example:

```text
0.0.0.0/0 → Internet Gateway
```

---

# 12. Internet Gateway

An Internet Gateway connects a VPC to the Internet.

Architecture:

```text
Internet
    |
    v
Internet Gateway
    |
    v
VPC
```

However, simply attaching an Internet Gateway to a VPC does not automatically make resources Internet-accessible.

You also need:

* Appropriate route
* Public IPv4 address where applicable
* Security Group rules
* NACL rules
* Correct resource configuration

---

# 13. NAT Gateway

NAT Gateway provides outbound Internet connectivity for resources in private subnets.

Example:

```text
Private EC2
     |
     v
Private Route Table
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

Typical use:

```text
Private EC2
     |
     +---- apt update
     |
     +---- Download package
     |
     +---- Call external API
```

The private resource does not need to become directly Internet-addressable.

---

# 14. NAT Gateway vs Internet Gateway

| Feature                            | Internet Gateway            | NAT Gateway                             |
| ---------------------------------- | --------------------------- | --------------------------------------- |
| Purpose                            | VPC ↔ Internet connectivity | Private subnet outbound Internet access |
| Common placement                   | Attached to VPC             | Public subnet                           |
| Used by                            | Public resources            | Private resources                       |
| Provides NAT                       | No                          | Yes                                     |
| Direct inbound to private resource | No                          | No                                      |

---

# 15. Elastic IP

An Elastic IP is a static public IPv4 address that can be associated with supported AWS resources.

Example:

```text
Internet
   |
Elastic IP
   |
Resource
```

It is useful when a stable public IPv4 address is required.

Avoid allocating unnecessary public IPv4 addresses because AWS charges can apply to public IPv4 usage.

---

# 16. Security Group

A Security Group is a stateful virtual firewall associated with resources through network interfaces.

Example:

```text
Internet
   |
   | HTTPS :443
   ↓
Load Balancer
   |
   | TCP :8080
   ↓
Application
```

Security Group rules determine which traffic is allowed.

Example:

```text
Inbound:

Protocol: TCP
Port: 443
Source: 0.0.0.0/0
```

---

# 17. Stateful Security Groups

Security Groups are stateful.

If an allowed inbound connection is established, the corresponding return traffic is automatically allowed.

Example:

```text
Client
  |
  | Request
  ↓
EC2
  |
  | Response
  ↓
Client
```

You do not normally need a separate inbound rule for the response traffic.

---

# 18. Network ACL

A Network ACL is a subnet-level network filter.

NACLs support:

* Allow rules
* Deny rules
* Inbound rules
* Outbound rules

Example:

```text
VPC
 |
Subnet
 |
NACL
 |
Resources
```

---

# 19. Stateless NACL

NACLs are stateless.

That means inbound and outbound traffic are evaluated independently.

Example:

```text
Inbound:
Allow TCP 443

Outbound:
Allow required return traffic
```

You must consider both directions.

---

# 20. Security Group vs NACL

| Feature         | Security Group             | NACL                   |
| --------------- | -------------------------- | ---------------------- |
| Scope           | Resource/network interface | Subnet                 |
| Stateful        | Yes                        | No                     |
| Allow rules     | Yes                        | Yes                    |
| Deny rules      | No explicit deny rules     | Yes                    |
| Rule evaluation | All applicable rules       | Ordered rules          |
| Common purpose  | Resource protection        | Subnet-level filtering |

---

# 21. VPC DNS

AWS VPC supports DNS resolution and DNS hostnames through VPC DNS settings.

DNS converts names into IP addresses.

Example:

```text
database.internal
       |
       v
10.0.3.20
```

DNS is extremely important in:

* Microservices
* Kubernetes
* EC2
* Load Balancers
* Service discovery

---

# 22. Route 53

Amazon Route 53 is AWS's DNS service.

It can provide:

* Public DNS
* Private hosted zones
* Domain registration
* Health checks
* Routing policies

Example:

```text
app.example.com
       |
       v
Load Balancer
       |
       v
Application
```

---

# 23. VPC Peering

VPC Peering connects two VPCs privately.

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

Both sides need appropriate routes.

Example:

```text
VPC-A route table:

10.1.0.0/16 → peering connection
```

And:

```text
VPC-B route table:

10.0.0.0/16 → peering connection
```

---

# 24. VPC Peering Limitations

VPC Peering is not transitive.

Example:

```text
VPC-A
  |
  | Peering
  |
VPC-B
  |
  | Peering
  |
VPC-C
```

VPC-A cannot automatically communicate with VPC-C through VPC-B.

For larger architectures, AWS Transit Gateway can be more suitable.

---

# 25. Transit Gateway

Transit Gateway acts as a central network hub.

Example:

```text
             VPC-A
                |
                |
VPC-B ---- Transit Gateway ---- VPC-C
                |
                |
             VPC-D
```

This is useful for:

* Multiple VPCs
* Hybrid networking
* Centralized routing
* Large organizations

---

# 26. VPC Endpoints

VPC Endpoints allow private connectivity to supported AWS services.

Example:

```text
Private EC2
    |
    v
VPC Endpoint
    |
    v
AWS Service
```

This can avoid sending traffic through:

```text
NAT Gateway
     |
Internet Gateway
     |
Internet
```

when an appropriate endpoint is available.

---

# 27. Gateway Endpoint

Gateway endpoints are commonly used for:

* Amazon S3
* Amazon DynamoDB

Example:

```text
Private Subnet
      |
      v
Gateway Endpoint
      |
      v
S3
```

---

# 28. Interface Endpoint

Interface endpoints use AWS PrivateLink and create elastic network interfaces in your subnets.

Example:

```text
Private EC2
    |
    v
Interface Endpoint
    |
    v
AWS Service
```

They are useful for accessing many AWS services and supported endpoint services privately.

---

# 29. Load Balancing

Elastic Load Balancing distributes traffic across healthy targets.

Example:

```text
Clients
   |
   v
Load Balancer
   |
   +---- EC2
   |
   +---- EC2
   |
   +---- EC2
```

Benefits:

* High availability
* Traffic distribution
* Health checks
* Scalability

---

# 30. Application Load Balancer

ALB operates at Layer 7.

It understands application protocols such as:

```text
HTTP
HTTPS
```

Example:

```text
User
 |
HTTPS
 |
ALB
 |
+---- /api ----> Backend
|
+---- /web ----> Frontend
```

ALB supports routing based on things such as:

* Host
* Path
* Headers
* Query parameters

---

# 31. Network Load Balancer

NLB operates primarily at Layer 4.

It is designed for high-performance network traffic such as:

```text
TCP
UDP
TLS
```

Example:

```text
Client
  |
  v
NLB
  |
  +---- Target
  |
  +---- Target
```

---

# 32. ALB vs NLB

| Feature               | ALB              | NLB                               |
| --------------------- | ---------------- | --------------------------------- |
| Layer                 | 7                | 4                                 |
| Main protocols        | HTTP/HTTPS       | TCP/UDP/TLS                       |
| Content-aware routing | Yes              | No application-layer path routing |
| Typical use           | Web applications | High-performance network traffic  |

---

# 33. EC2 Networking

An EC2 instance receives networking through an Elastic Network Interface (ENI).

A simplified model:

```text
EC2
 |
ENI
 |
Private IP
 |
Subnet
 |
VPC
```

An ENI can have networking attributes such as:

* Private IP
* Security Groups
* MAC address
* Subnet association

---

# 34. Private IP

Resources inside a VPC commonly communicate using private IP addresses.

Example:

```text
EC2-A
10.0.1.10

       ↓

EC2-B
10.0.2.10
```

Communication stays within the AWS network when routing and security rules allow it.

---

# 35. Public IP

A public IPv4 address allows a supported resource to communicate with the Internet through an Internet Gateway when the routing and security configuration permits it.

Example:

```text
Internet
   |
Public IPv4
   |
EC2
```

Public exposure should be minimized.

---

# 36. Bastion Host

A bastion host is a controlled entry point used to access resources in private networks.

Example:

```text
Developer
    |
    | SSH
    v
Bastion Host
    |
    | SSH
    v
Private EC2
```

Modern AWS architectures may instead use AWS Systems Manager Session Manager to avoid exposing SSH publicly.

---

# 37. Three-Tier Architecture

A common AWS architecture is:

```text
                Internet
                    |
                    v
             Public Subnet
                    |
             Load Balancer
                    |
                    v
          Private App Subnet
                    |
             Application
                    |
                    v
           Private DB Subnet
                    |
                Database
```

The three layers are:

1. Presentation
2. Application
3. Database

---

# 38. Production VPC Architecture

A production design may look like:

```text
                         Internet
                            |
                            v
                     Internet Gateway
                            |
             +--------------+--------------+
             |                             |
          AZ-A                           AZ-B
             |                             |
      +------+-------+              +------+-------+
      |              |              |              |
   Public         Private        Public         Private
   Subnet         App Subnet     Subnet         App Subnet
      |              |              |              |
     ALB            EC2            ALB            EC2
                     \              /
                      \            /
                       +----------+
                            |
                      Private DB
                         Subnets
```

This provides:

* High availability
* Network isolation
* Scalability
* Security

---

# 39. AWS Networking Traffic Flow

Understanding traffic flow is more important than memorizing services.

## Public EC2 → Internet

```text
EC2
 ↓
Subnet Route Table
 ↓
Internet Gateway
 ↓
Internet
```

The instance generally needs appropriate public IPv4 addressing and security rules.

---

## Private EC2 → Internet

```text
Private EC2
 ↓
Private Route Table
 ↓
NAT Gateway
 ↓
Internet Gateway
 ↓
Internet
```

---

## Private EC2 → S3

Depending on architecture:

```text
Private EC2
 ↓
VPC Endpoint
 ↓
S3
```

This can provide private connectivity without requiring Internet/NAT traversal.

---

# 40. Security Architecture

A secure application should minimize public exposure.

Bad design:

```text
Internet
   |
   +---- EC2
   |
   +---- Database
```

Better:

```text
Internet
   |
   v
Load Balancer
   |
   v
Private Application
   |
   v
Private Database
```

The database should generally not be directly exposed to the public Internet.

---

# 41. Security Group Chaining

Instead of allowing the database to accept traffic from the entire Internet, allow traffic from the application tier.

Example:

```text
Internet
   |
   v
ALB-SG
   |
   v
APP-SG
   |
   v
DB-SG
```

Rules:

```text
ALB-SG:
Allow HTTPS from Internet
```

```text
APP-SG:
Allow application port from ALB-SG
```

```text
DB-SG:
Allow database port from APP-SG
```

This is much better than:

```text
DB:
Allow 3306 from 0.0.0.0/0
```

---

# 42. Least Privilege Networking

Allow only what is required.

Example:

Bad:

```text
0.0.0.0/0
All ports
```

Better:

```text
Source:
Application Security Group

Port:
3306

Protocol:
TCP
```

For SSH:

Bad:

```text
22 from 0.0.0.0/0
```

Better:

```text
22 from a trusted source
```

or use Session Manager where appropriate.

---

# 43. AWS Networking and DevOps

DevOps engineers use AWS networking when deploying:

* EC2
* ECS
* EKS
* RDS
* Load Balancers
* CI/CD systems
* Microservices
* Databases
* Monitoring systems

Terraform can automate the entire network.

Example:

```text
Terraform
   |
   +-- VPC
   |
   +-- Subnets
   |
   +-- Route Tables
   |
   +-- Internet Gateway
   |
   +-- NAT Gateway
   |
   +-- Security Groups
   |
   +-- Load Balancer
   |
   +-- EC2
```

---

# 44. AWS Networking and Terraform

A simplified Terraform architecture:

```text
main.tf
│
├── VPC
├── Subnets
├── Route Tables
├── Internet Gateway
├── NAT Gateway
├── Security Groups
└── EC2
```

Terraform makes infrastructure:

* Repeatable
* Version-controlled
* Reviewable
* Automated

---

# 45. AWS Networking Troubleshooting Method

When an application cannot connect, follow this order.

## 1. Identify source

```text
Who is sending traffic?
```

## 2. Identify destination

```text
Where is traffic going?
```

## 3. Check IP

```text
Is the destination IP correct?
```

## 4. Check subnet

```text
Which subnet contains the resource?
```

## 5. Check route table

```text
Does a route exist?
```

## 6. Check Internet Gateway/NAT

```text
Does traffic need Internet connectivity?
```

## 7. Check Security Group

```text
Is the port allowed?
```

## 8. Check NACL

```text
Could subnet-level filtering block it?
```

## 9. Check application

```text
Is the service listening?
```

## 10. Check DNS

```text
Does the hostname resolve?
```

---

# 46. Example Troubleshooting

Suppose:

```text
EC2-A
10.0.1.10

EC2-B
10.0.2.10
```

EC2-A cannot connect to EC2-B on port 8080.

Check:

```text
1. EC2-B running?
2. EC2-B private IP correct?
3. Route table?
4. Security Group?
5. NACL?
6. Application listening on 8080?
7. OS firewall?
```

On the server:

```bash
ss -lntp
```

Test:

```bash
nc -vz 10.0.2.10 8080
```

---

# 47. Common Networking Ports

| Service        | Port |
| -------------- | ---: |
| SSH            |   22 |
| HTTP           |   80 |
| HTTPS          |  443 |
| DNS            |   53 |
| MySQL          | 3306 |
| PostgreSQL     | 5432 |
| Redis          | 6379 |
| Kubernetes API | 6443 |

Always expose only the ports actually required.

---

# 48. Important AWS Networking Terms

## VPC

Virtual network in AWS.

## Subnet

IP range inside a VPC.

## Route Table

Determines where traffic goes.

## Internet Gateway

Provides Internet connectivity for appropriately configured public resources.

## NAT Gateway

Provides outbound Internet connectivity for private resources.

## Security Group

Stateful resource-level firewall.

## NACL

Stateless subnet-level network filter.

## VPC Peering

Private connection between two VPCs.

## Transit Gateway

Centralized network hub.

## VPC Endpoint

Private connectivity to supported AWS services/endpoints.

## Load Balancer

Distributes traffic across targets.

---

# 49. Interview Mental Model

When an interviewer asks:

> "How does a user access an application running on a private EC2 instance?"

A strong answer is:

```text
User
 ↓
Internet
 ↓
Internet Gateway
 ↓
Public Load Balancer
 ↓
Private Application EC2
 ↓
Database
```

Then explain:

* Load Balancer is publicly reachable as configured.
* Application servers remain private.
* Security Groups control allowed traffic.
* Route tables control traffic paths.
* Database remains in private subnets.
* NAT can provide outbound Internet access to private application instances if required.

---

# 50. Final AWS Networking Mental Model

Remember:

```text
                         AWS REGION
                             |
                            VPC
                             |
            +----------------+----------------+
            |                                 |
       PUBLIC SUBNET                    PRIVATE SUBNET
            |                                 |
       Load Balancer                    Application
            |                                 |
      Internet Gateway                      |
                                             |
                                       Database
```

Traffic decisions:

```text
IP
 ↓
Subnet
 ↓
Route Table
 ↓
Gateway/Endpoint
 ↓
Security Group
 ↓
NACL
 ↓
Application
```

This mental model is extremely useful for AWS networking troubleshooting.

---

# ✅ Chapter 32 Study Checklist

## Fundamentals

* [ ] Region
* [ ] Availability Zone
* [ ] VPC
* [ ] CIDR
* [ ] Subnet

## Routing

* [ ] Route Table
* [ ] Local Route
* [ ] Default Route
* [ ] Internet Gateway
* [ ] NAT Gateway

## Security

* [ ] Security Group
* [ ] Stateful traffic
* [ ] NACL
* [ ] Stateless traffic
* [ ] Least privilege
* [ ] Security Group chaining

## Connectivity

* [ ] VPC Peering
* [ ] Transit Gateway
* [ ] VPC Endpoints
* [ ] Route 53
* [ ] DNS

## Load Balancing

* [ ] ALB
* [ ] NLB
* [ ] Health checks
* [ ] Target groups

## DevOps

* [ ] EC2 networking
* [ ] Container networking
* [ ] EKS networking
* [ ] Terraform networking
* [ ] Production architecture
* [ ] Troubleshooting

---

# 🎯 Key DevOps Principle

> **Understand the traffic path, not just the AWS service names.**

Whenever something cannot communicate, ask:

```text
SOURCE
  ↓
DESTINATION
  ↓
IP
  ↓
SUBNET
  ↓
ROUTE
  ↓
GATEWAY / ENDPOINT
  ↓
SECURITY GROUP
  ↓
NACL
  ↓
APPLICATION
```

If you can trace this path confidently, you have a strong foundation in AWS Networking.
