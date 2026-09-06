# ☁️ AWS Networking — Interview Questions

## Chapter 32 — AWS Networking

This document contains AWS Networking interview questions from **beginner → intermediate → advanced → scenario-based DevOps questions**.

---

# 📚 Table of Contents

1. AWS Networking Fundamentals
2. VPC
3. CIDR and Subnets
4. Route Tables
5. Internet Gateway
6. NAT Gateway
7. Security Groups
8. Network ACL
9. ENI and IP Addressing
10. DNS and Route 53
11. Load Balancing
12. VPC Peering
13. VPC Endpoints
14. Private and Public Subnets
15. Troubleshooting
16. DevOps Scenario Questions
17. Advanced Questions
18. Quick Revision
19. Interview-Ready Answers

---

# 1. AWS Networking Fundamentals

## Q1. What is AWS Networking?

AWS Networking is the collection of AWS services and networking components used to connect, isolate, secure, route, and monitor resources in AWS.

Important components include:

* VPC
* Subnets
* Route Tables
* Internet Gateway
* NAT Gateway
* Security Groups
* Network ACLs
* Elastic Network Interfaces
* Elastic IPs
* Load Balancers
* Route 53
* VPC Peering
* VPC Endpoints
* Transit Gateway

---

# 2. What is Amazon VPC?

VPC stands for **Virtual Private Cloud**.

It is a logically isolated virtual network in AWS where you can launch resources such as:

* EC2
* RDS
* Load Balancers
* ECS
* EKS
* Other AWS resources

Example:

```text
VPC
10.0.0.0/16
```

---

# 3. What is a CIDR block?

CIDR stands for:

**Classless Inter-Domain Routing**

Example:

```text
10.0.0.0/16
```

The `/16` indicates how many bits belong to the network portion.

A VPC commonly uses a CIDR such as:

```text
10.0.0.0/16
```

which provides:

```text
65,536 IPv4 addresses
```

before AWS-specific subnet/address reservations are considered.

---

# 4. What is a subnet?

A subnet is a logical subdivision of a VPC IP address range.

Example:

```text
VPC
10.0.0.0/16

        |
        +--- Public Subnet
        |    10.0.1.0/24
        |
        +--- Private Subnet
             10.0.2.0/24
```

---

# 5. What is the difference between a VPC and a subnet?

| VPC                    | Subnet                              |
| ---------------------- | ----------------------------------- |
| Larger virtual network | Smaller network inside VPC          |
| Regional               | Exists inside one Availability Zone |
| Contains subnets       | Belongs to a VPC                    |
| Defines overall CIDR   | Uses a portion of VPC CIDR          |

---

# 6. What is an Availability Zone?

An Availability Zone, or AZ, is an isolated location within an AWS Region.

Example:

```text
Region: ap-south-1

├── ap-south-1a
├── ap-south-1b
└── ap-south-1c
```

A subnet belongs to exactly one Availability Zone.

---

# 7. What is a public subnet?

A subnet is considered public when its routing provides a path to an Internet Gateway.

Typical route:

```text
0.0.0.0/0 → Internet Gateway
```

A resource also needs appropriate addressing and security configuration to actually be reachable from the Internet.

---

# 8. What is a private subnet?

A private subnet does not have a direct route to an Internet Gateway for Internet access.

For outbound Internet access, a private subnet commonly uses:

```text
Private Subnet
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

---

# 9. Can a private subnet access the Internet?

Yes, if it has an appropriate route to a NAT Gateway or another supported egress mechanism.

Example:

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

The Internet cannot directly initiate a connection to the private EC2 through the NAT Gateway.

---

# 10. What is a Route Table?

A Route Table contains rules that determine where network traffic should go.

Example:

```text
Destination       Target

10.0.0.0/16       local
0.0.0.0/0         igw-xxxxxxxx
```

Meaning:

* Traffic inside the VPC → local
* Other IPv4 traffic → Internet Gateway

---

# 11. What is the `local` route?

When a VPC is created, AWS automatically provides a route for the VPC's CIDR.

Example:

```text
10.0.0.0/16 → local
```

This enables routing between resources using addresses within the VPC, subject to security controls.

---

# 12. What is an Internet Gateway?

An Internet Gateway, or IGW, is a horizontally scaled, redundant AWS component that enables communication between a VPC and the Internet when routing and addressing are configured appropriately.

Example:

```text
VPC
 |
Route Table
 |
Internet Gateway
 |
Internet
```

---

# 13. Does attaching an Internet Gateway automatically make a subnet public?

No.

You also need a route such as:

```text
0.0.0.0/0 → Internet Gateway
```

in a route table associated with the subnet.

For an Internet-reachable IPv4 resource, appropriate public IPv4 addressing and Security Group/NACL rules are also required.

---

# 14. What is a NAT Gateway?

NAT stands for:

**Network Address Translation**

A NAT Gateway allows resources in a private subnet to initiate connections to external networks, commonly the Internet, without making those private resources directly Internet-reachable.

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

# 15. Internet Gateway vs NAT Gateway

| Internet Gateway                  | NAT Gateway                                             |
| --------------------------------- | ------------------------------------------------------- |
| Enables VPC Internet connectivity | Provides outbound Internet access for private resources |
| Used by public subnet routing     | Usually placed in a public subnet                       |
| Supports Internet communication   | Private resources use it for outbound connections       |
| No hourly NAT processing charge   | NAT Gateway has usage/cost considerations               |

---

# 16. What is a Security Group?

A Security Group is a **stateful virtual firewall** associated with resources such as EC2 network interfaces.

Example:

```text
Inbound:
TCP 80
TCP 443

Outbound:
Allowed according to configured rules
```

---

# 17. What does stateful mean?

If an inbound connection is allowed by a Security Group, the response traffic is automatically allowed as part of the established connection.

You do not normally need to create a separate inbound rule for the response traffic.

---

# 18. What is a Network ACL?

Network ACL, or NACL, is a subnet-level network traffic filter.

It controls:

* Inbound traffic
* Outbound traffic

NACLs are **stateless**.

Therefore, both directions must be considered.

---

# 19. Security Group vs NACL

| Security Group                       | NACL                                      |
| ------------------------------------ | ----------------------------------------- |
| Resource/ENI level                   | Subnet level                              |
| Stateful                             | Stateless                                 |
| Allow rules                          | Allow and deny rules                      |
| Return traffic automatically handled | Return traffic must be explicitly allowed |
| Commonly used for workload security  | Additional subnet-level control           |

---

# 20. What is an ENI?

ENI stands for:

**Elastic Network Interface**

It is a virtual network interface in AWS.

It can have:

* Private IPv4 addresses
* Public IPv4 association
* Security Groups
* MAC address
* Subnet association

An EC2 instance communicates through its network interface.

---

# 21. Public IP vs Private IP

### Private IP

Used for communication inside private networks such as a VPC.

Example:

```text
10.0.1.10
```

### Public IP

Used for Internet-facing connectivity.

Example:

```text
203.x.x.x
```

---

# 22. What is an Elastic IP?

An Elastic IP is a static public IPv4 address allocated to your AWS account.

It can be associated with supported AWS resources.

Use Elastic IPs carefully because unused public IPv4 addresses can incur charges.

---

# 23. What is Route 53?

Amazon Route 53 is AWS's scalable DNS service.

It can provide:

* Domain registration
* DNS resolution
* Health checks
* Routing policies

Example:

```text
app.example.com
       |
       v
Route 53
       |
       v
Load Balancer
```

---

# 24. What is DNS?

DNS stands for:

**Domain Name System**

It translates names into IP addresses or other DNS records.

Example:

```text
example.com
     |
     v
IP address
```

---

# 25. What is Load Balancing?

A Load Balancer distributes incoming traffic across multiple targets.

Example:

```text
              Users
                |
                v
         Load Balancer
          /     |     \
         /      |      \
       EC2     EC2     EC2
```

Benefits:

* High availability
* Scalability
* Traffic distribution
* Health checks

---

# 26. ALB vs NLB

### ALB — Application Load Balancer

Works primarily at Layer 7.

Supports features such as:

* HTTP
* HTTPS
* Host-based routing
* Path-based routing

### NLB — Network Load Balancer

Works primarily at Layer 4.

Designed for:

* TCP
* TLS
* UDP

and high-performance network traffic.

---

# 27. What is VPC Peering?

VPC Peering creates private network connectivity between two VPCs.

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

Routes must be configured on both sides as appropriate.

---

# 28. What is a VPC Endpoint?

A VPC Endpoint allows supported AWS services to be accessed privately without requiring Internet Gateway or NAT-based Internet access.

Example:

```text
Private EC2
     |
     v
VPC Endpoint
     |
     v
S3
```

Types include:

* Gateway endpoints
* Interface endpoints

---

# 29. Gateway Endpoint vs Interface Endpoint

| Gateway Endpoint                  | Interface Endpoint                  |
| --------------------------------- | ----------------------------------- |
| Commonly used for S3 and DynamoDB | Uses AWS PrivateLink                |
| Route-table based                 | Uses ENIs                           |
| No endpoint ENI required          | Creates endpoint network interfaces |
| Supports specific services        | Supports many AWS services          |

---

# 30. What is AWS PrivateLink?

AWS PrivateLink provides private connectivity to supported services through VPC endpoints.

Traffic can remain on the AWS network instead of traversing the public Internet.

---

# 31. What is VPC Flow Logs?

VPC Flow Logs capture information about IP traffic to and from network interfaces.

They are useful for:

* Troubleshooting
* Security investigation
* Traffic analysis
* Network visibility

They can be published to supported destinations such as CloudWatch Logs or Amazon S3.

---

# 32. What is Transit Gateway?

AWS Transit Gateway is a network transit hub that can connect multiple VPCs and on-premises networks.

Instead of creating many individual peering connections:

```text
VPC-A ----\
VPC-B -----\ 
VPC-C ------ Transit Gateway
VPC-D -----/
```

This can simplify large-scale network architecture.

---

# 33. What is a Default Route?

A default route matches traffic when a more specific route does not exist.

IPv4:

```text
0.0.0.0/0
```

IPv6:

```text
::/0
```

Example:

```text
0.0.0.0/0 → Internet Gateway
```

---

# 34. What is the difference between `port` and `targetPort`?

This terminology is especially important in Kubernetes, not native AWS VPC routing.

For an AWS Load Balancer:

* Listener port receives client traffic.
* Target group port is where traffic is forwarded to targets.

Example:

```text
Client
  |
  | TCP 443
  v
Load Balancer
  |
  | TCP 8080
  v
Application
```

---

# 35. How does an EC2 instance get Internet access?

Typical requirements include:

```text
EC2
 |
Subnet
 |
Route Table
 |
0.0.0.0/0
 |
Internet Gateway
 |
Internet
```

The EC2 also needs appropriate public IPv4 addressing and Security Group/NACL configuration.

---

# 36. Why can't my EC2 access the Internet?

Check:

```text
1. EC2 state
2. Private/public IP
3. Subnet
4. Route table
5. Internet Gateway
6. Security Group
7. NACL
8. OS firewall
9. DNS
10. Application
```

Useful commands:

```bash
ip addr
ip route
ss -lntp
curl -I https://example.com
dig example.com
```

---

# 37. EC2 has a public IP but cannot be reached. Why?

A public IP alone is not sufficient.

Check:

```text
Public IP
    ↓
Subnet route
    ↓
Internet Gateway
    ↓
Security Group
    ↓
NACL
    ↓
OS firewall
    ↓
Application
    ↓
Port
```

---

# 38. Security Group allows port 80 but website doesn't work. What do you check?

Check:

### 1. Route table

```text
0.0.0.0/0 → IGW
```

### 2. Internet Gateway

Verify it is attached to the VPC.

### 3. Public IP

Verify the EC2 has a reachable public IPv4 address.

### 4. NACL

Check inbound and outbound rules.

### 5. OS firewall

```bash
sudo ufw status
```

### 6. Application

```bash
sudo systemctl status nginx
```

### 7. Listening port

```bash
sudo ss -lntp
```

---

# 39. Why does ping fail but curl work?

Because ping uses:

```text
ICMP
```

while curl commonly uses:

```text
TCP 80
TCP 443
```

ICMP can be blocked while HTTP/HTTPS remains allowed.

Therefore:

> Ping failure does not automatically mean the server is unreachable.

---

# 40. How would you troubleshoot a timeout?

Use a layered approach:

```text
DNS
 ↓
IP
 ↓
Route
 ↓
Gateway
 ↓
Security Group
 ↓
NACL
 ↓
OS Firewall
 ↓
Port
 ↓
Application
```

Test:

```bash
dig example.com
```

```bash
ping <IP>
```

```bash
nc -vz <IP> <PORT>
```

```bash
curl -v http://<IP>:<PORT>
```

---

# 41. What is the difference between a timeout and connection refused?

### Timeout

Usually indicates traffic is being dropped or a network path/security control is preventing a response.

Possible causes:

* Security Group
* NACL
* Route
* Firewall
* Network path

### Connection refused

Usually means the host was reachable but nothing accepted the connection on that port.

Possible cause:

```text
Application not listening
```

---

# 42. How do you check whether a port is listening on Linux?

```bash
ss -lntp
```

Example:

```bash
ss -lntp | grep ':80'
```

---

# 43. How do you test TCP connectivity?

```bash
nc -vz <IP> <PORT>
```

Example:

```bash
nc -vz 10.0.2.10 8080
```

---

# 44. How do you troubleshoot DNS?

Use:

```bash
dig example.com
```

```bash
nslookup example.com
```

```bash
getent hosts example.com
```

Check resolver configuration:

```bash
cat /etc/resolv.conf
```

---

# 45. How do you inspect VPCs using AWS CLI?

```bash
aws ec2 describe-vpcs
```

---

# 46. How do you inspect subnets?

```bash
aws ec2 describe-subnets
```

---

# 47. How do you inspect route tables?

```bash
aws ec2 describe-route-tables
```

---

# 48. How do you inspect Security Groups?

```bash
aws ec2 describe-security-groups
```

---

# 49. How do you inspect Network ACLs?

```bash
aws ec2 describe-network-acls
```

---

# 50. How do you inspect EC2 networking?

```bash
aws ec2 describe-instances \
  --instance-ids <instance-id>
```

---

# 51. How do you find an EC2 private IP?

```bash
aws ec2 describe-instances \
  --instance-ids <instance-id> \
  --query "Reservations[].Instances[].PrivateIpAddress" \
  --output text
```

---

# 52. How do you find an EC2 public IP?

```bash
aws ec2 describe-instances \
  --instance-ids <instance-id> \
  --query "Reservations[].Instances[].PublicIpAddress" \
  --output text
```

---

# 53. How do you find the Security Groups attached to an EC2 instance?

```bash
aws ec2 describe-instances \
  --instance-ids <instance-id> \
  --query "Reservations[].Instances[].SecurityGroups"
```

---

# 54. How do you find an EC2 network interface?

```bash
aws ec2 describe-network-interfaces \
  --filters "Name=attachment.instance-id,Values=<instance-id>"
```

---

# 55. What is the difference between stateful and stateless filtering?

### Stateful

The firewall remembers connection state.

Example:

```text
Security Group
```

### Stateless

Each direction is evaluated independently.

Example:

```text
Network ACL
```

---

# 56. Can a Security Group deny traffic?

No.

Security Groups support **allow rules**.

Traffic that does not match an applicable allow rule is implicitly denied.

---

# 57. Can a NACL explicitly deny traffic?

Yes.

NACLs support:

```text
ALLOW
DENY
```

Rules are evaluated in rule-number order.

---

# 58. Why use multiple Availability Zones?

For:

* High availability
* Fault tolerance
* Resilience
* Disaster recovery

Example:

```text
Region
 |
 +--- AZ-A
 |     |
 |    EC2
 |
 +--- AZ-B
       |
      EC2
```

---

# 59. How would you design a highly available web application?

Example:

```text
                 Internet
                    |
                    v
              Route 53
                    |
                    v
             Application
           Load Balancer
             /        \
            /          \
        AZ-A            AZ-B
         |                |
       EC2              EC2
         \                /
          \              /
             Database
```

Use:

* Multiple AZs
* Load Balancer
* Private application subnets
* Appropriate Security Groups
* Highly available database architecture

---

# 60. Why put application servers in private subnets?

Benefits:

* Reduced direct Internet exposure
* Better security boundaries
* Controlled outbound access
* Separation of tiers

Typical architecture:

```text
Internet
   |
   v
ALB
   |
   v
Private EC2
   |
   v
Private Database
```

---

# 61. Should a database be publicly accessible?

Generally, no.

A common architecture is:

```text
Internet
   |
   v
Public Load Balancer
   |
   v
Private Application
   |
   v
Private Database
```

The database Security Group should allow database traffic only from the application tier.

---

# 62. Scenario: Application cannot connect to database

Suppose:

```text
Application
10.0.1.10

Database
10.0.2.10

Database Port
3306
```

Check:

### Application Security Group

Does it allow outbound traffic?

### Database Security Group

Does it allow:

```text
TCP 3306
Source: Application Security Group
```

### Routes

Do both subnets have valid routes?

### NACL

Are inbound and outbound rules allowing the connection?

### Database

Is the database listening?

### DNS

Does the database hostname resolve correctly?

---

# 63. Scenario: Private EC2 cannot download packages

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

Check:

```text
1. NAT Gateway exists
2. NAT Gateway is available
3. NAT Gateway is in a public subnet
4. Public subnet route points to IGW
5. Private subnet route points to NAT Gateway
6. Security rules allow traffic
7. DNS works
```

---

# 64. Scenario: Two VPCs cannot communicate

Check:

```text
VPC CIDRs
     ↓
Peering / Transit Gateway
     ↓
Route Tables
     ↓
Security Groups
     ↓
NACLs
     ↓
Application Ports
```

Also ensure the VPC CIDRs do not overlap when using architectures that require routable connectivity between them.

---

# 65. Scenario: EC2 can reach the Internet but cannot reach another EC2

Check:

```text
Source subnet
Destination subnet
Route tables
Security Groups
NACLs
OS firewall
Destination application
```

Remember:

> VPC connectivity is not the same as application-level connectivity.

---

# 66. Scenario: HTTP works but HTTPS doesn't

Check:

```text
TCP 443
```

Security Group:

```text
Inbound TCP 443
```

Then check:

```text
TLS certificate
Load Balancer listener
Web server
Application
NACL
OS firewall
```

Test:

```bash
curl -v https://example.com
```

---

# 67. Scenario: DNS name does not resolve

Check:

```text
1. DNS record
2. Hosted Zone
3. Nameservers
4. VPC DNS settings for internal resolution
5. Resolver configuration
6. Network connectivity
```

Useful:

```bash
dig example.com
```

---

# 68. What is a public route table?

There is no special AWS resource type called a "public route table."

A route table is effectively associated with a public subnet when the subnet has a route to an Internet Gateway.

---

# 69. What is a private route table?

Similarly, there is no separate AWS route-table resource type called "private route table."

It is a route table whose routes do not provide direct Internet Gateway access for the associated private subnet.

It may contain:

```text
0.0.0.0/0 → NAT Gateway
```

---

# 70. What is the difference between public and private IP communication?

### Public

Used for Internet-facing connectivity.

### Private

Used within private networks such as VPCs.

Example:

```text
Public:
Internet → Public IP → EC2

Private:
EC2-A → Private IP → EC2-B
```

---

# 71. What is AWS networking best practice?

Important practices:

* Use multiple AZs.
* Keep application and database tiers private where possible.
* Avoid unnecessary public IP addresses.
* Restrict Security Groups.
* Avoid `0.0.0.0/0` for SSH.
* Use least privilege.
* Use VPC Flow Logs where appropriate.
* Use VPC Endpoints for supported AWS services where beneficial.
* Monitor network traffic.
* Document CIDR allocations.
* Avoid overlapping CIDRs.
* Clean up unused resources.

---

# 72. What is least privilege in networking?

Allow only the traffic that is actually required.

Bad:

```text
0.0.0.0/0
All ports
```

Better:

```text
TCP 443
Source: required clients
```

Best for internal tiers:

```text
Database
TCP 3306
Source: Application Security Group
```

---

# 73. Explain AWS VPC in an interview

### Interview-ready answer

> "Amazon VPC is a logically isolated virtual network in AWS. I can define its CIDR range and divide it into subnets across Availability Zones. I use route tables to control traffic flow, Internet Gateways for Internet connectivity from public subnets, and NAT Gateways when private resources need outbound Internet access. Security Groups provide stateful resource-level filtering, while Network ACLs provide stateless subnet-level filtering. I can also use Route 53, Load Balancers, VPC Peering, VPC Endpoints, and Transit Gateway depending on the architecture."

---

# 74. Explain Public vs Private Subnet

### Interview-ready answer

> "A public subnet has a route to an Internet Gateway. A private subnet does not have a direct route to an Internet Gateway. Private resources can use a NAT Gateway for outbound Internet access when required. In a typical production architecture, load balancers are placed in public subnets while application and database resources are kept in private subnets."

---

# 75. Explain Security Group vs NACL

### Interview-ready answer

> "Security Groups are stateful and operate at the resource or network-interface level. They support allow rules. Network ACLs operate at the subnet level and are stateless, supporting both allow and deny rules. I generally use Security Groups as the primary workload-level firewall and NACLs when subnet-level filtering is required."

---

# 76. Explain How Internet Traffic Reaches EC2

### Interview-ready answer

> "For an Internet-facing EC2 instance, the subnet must use a route table with a default route to an Internet Gateway. The instance needs appropriate public IPv4 addressing, and the Security Group and NACL must permit the traffic. The traffic then reaches the instance through its Elastic Network Interface."

---

# 77. Explain Private EC2 Internet Access

### Interview-ready answer

> "A private EC2 instance does not receive direct inbound Internet connectivity through an Internet Gateway. If it needs outbound Internet access, its subnet route table can send default traffic to a NAT Gateway in a public subnet. The NAT Gateway then uses the Internet Gateway to reach the Internet."

---

# 78. Explain AWS Networking Troubleshooting

### Interview-ready answer

> "I troubleshoot layer by layer. First I verify DNS and IP addressing, then the subnet and route table, followed by the Internet or NAT Gateway if applicable. Next I check Security Groups and NACLs, then the EC2 network interface, OS firewall, listening port, and finally the application. I use tools such as AWS CLI, ip route, ss, curl, nc, dig, traceroute, and tcpdump."

---

# 79. Advanced: Why are overlapping VPC CIDRs a problem?

Suppose:

```text
VPC-A
10.0.0.0/16

VPC-B
10.0.0.0/16
```

Routing between these networks becomes problematic because the same destination IP ranges exist in both networks.

For interconnected environments, plan non-overlapping CIDRs.

---

# 80. Advanced: How would you design a multi-account AWS network?

A common enterprise pattern is:

```text
                Transit Gateway
                /      |      \
               /       |       \
        Account-A  Account-B  Account-C
          VPC-A      VPC-B      VPC-C
```

Centralized networking can provide:

* Controlled connectivity
* Central routing
* Easier management
* Segmentation

---

# 81. Advanced: How would you secure a three-tier application?

Architecture:

```text
                 Internet
                    |
                    v
              Public ALB
                    |
                    v
          Private Application
                    |
                    v
           Private Database
```

Security:

```text
Internet
   |
   | 443
   v
ALB-SG
   |
   | Application port
   v
APP-SG
   |
   | 3306
   v
DB-SG
```

Each tier should allow only the traffic required from the previous tier.

---

# 82. Advanced: What is defense in depth?

Defense in depth means using multiple security layers.

Example:

```text
Internet
   ↓
WAF
   ↓
Load Balancer
   ↓
Security Group
   ↓
NACL
   ↓
Private Application
   ↓
Database Security Group
```

If one control fails, other controls provide additional protection.

---

# 83. Advanced: How would you reduce NAT Gateway costs?

Depending on architecture and requirements:

* Use VPC Endpoints for supported AWS services.
* Reduce unnecessary Internet-bound traffic.
* Centralize NAT architecture where appropriate.
* Monitor NAT data processing.
* Use private service connectivity where possible.

Always validate the architecture against availability, security, and operational requirements.

---

# 84. Advanced: How would you monitor AWS network traffic?

Use services and tools such as:

* VPC Flow Logs
* CloudWatch
* CloudTrail for API activity
* Load Balancer logs
* Route 53 logging/features where appropriate
* AWS Network Firewall where required
* Traffic Mirroring for specific advanced use cases

---

# 85. Top 20 Questions to Revise Before Interview

```text
1. What is VPC?
2. What is CIDR?
3. What is a subnet?
4. Public vs private subnet?
5. What is a route table?
6. What is an Internet Gateway?
7. What is a NAT Gateway?
8. IGW vs NAT Gateway?
9. What is a Security Group?
10. What is a NACL?
11. Security Group vs NACL?
12. What is an ENI?
13. Public IP vs private IP?
14. What is Route 53?
15. What is VPC Peering?
16. What is a VPC Endpoint?
17. What is VPC Flow Logs?
18. Why use multiple AZs?
19. How do you troubleshoot unreachable EC2?
20. How do you design a secure three-tier architecture?
```

---

# 86. AWS Networking Mental Model

Remember this:

```text
                    AWS REGION
                        |
                AVAILABILITY ZONE
                        |
                      VPC
                  10.0.0.0/16
                        |
             +----------+----------+
             |                     |
       Public Subnet          Private Subnet
        10.0.1.0/24           10.0.2.0/24
             |                     |
       Route Table            Route Table
             |                     |
            IGW                  NAT GW
             |                     |
         Internet                 IGW
                                   |
                               Internet
```

Security:

```text
Resource
   |
Security Group
   |
ENI
   |
Subnet
   |
NACL
```

---

# 87. Final Interview Checklist

Before saying:

> "I know AWS Networking"

make sure you can explain:

### Fundamentals

* [ ] VPC
* [ ] Region
* [ ] Availability Zone
* [ ] CIDR
* [ ] Subnet

### Routing

* [ ] Route Table
* [ ] Local Route
* [ ] Default Route
* [ ] Internet Gateway
* [ ] NAT Gateway

### Security

* [ ] Security Group
* [ ] NACL
* [ ] Stateful
* [ ] Stateless
* [ ] Least privilege

### Connectivity

* [ ] ENI
* [ ] Private IP
* [ ] Public IP
* [ ] Elastic IP
* [ ] DNS

### Advanced

* [ ] Load Balancer
* [ ] VPC Peering
* [ ] VPC Endpoint
* [ ] PrivateLink
* [ ] Transit Gateway
* [ ] VPC Flow Logs

### Troubleshooting

* [ ] `aws ec2 describe-*`
* [ ] `ip addr`
* [ ] `ip route`
* [ ] `ss`
* [ ] `ping`
* [ ] `nc`
* [ ] `curl`
* [ ] `dig`
* [ ] `tcpdump`

---

# 🏆 Final DevOps Interview Answer

If the interviewer asks:

**"How strong are you in AWS Networking?"**

A strong answer is:

> "I understand AWS networking from both the architecture and troubleshooting perspectives. I can work with VPCs, CIDR ranges, public and private subnets, route tables, Internet and NAT Gateways, Security Groups, NACLs, ENIs, DNS, Load Balancers, VPC Endpoints, and VPC connectivity patterns. For troubleshooting, I follow the traffic path from DNS and IP addressing through routing, gateways, Security Groups, NACLs, the operating system, ports, and finally the application. I also use AWS CLI and Linux networking tools such as `ip`, `ss`, `curl`, `nc`, `dig`, and `tcpdump`."

---

# 🚀 Chapter 32 Complete

```text
32-AWS-Networking/
│
├── README.md
├── notes.md
├── commands.md
├── practical-lab.md
└── interview-questions.md
```

AWS Networking is now covered from:

```text
Theory
   ↓
Commands
   ↓
Practical Lab
   ↓
Troubleshooting
   ↓
Interview Preparation
```

**Next chapter → `33-CI-CD-Networking`**
