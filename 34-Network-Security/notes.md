# 🔐 Network Security — Detailed Notes

## Chapter 34 — DevOps Networking Handbook

---

# 1. What Is Network Security?

Network Security is the practice of protecting:

* Networks
* Servers
* Applications
* Devices
* Data
* APIs
* Cloud infrastructure
* Containers
* Kubernetes clusters

from unauthorized access, attacks, misuse, and disruption.

A simple model:

```text
Internet
   |
   v
Firewall
   |
   v
Load Balancer
   |
   v
Application
   |
   v
Database
```

Security should exist at every layer.

---

# 2. Security Goals

The three fundamental security goals are known as the **CIA Triad**:

```text
          Confidentiality
              /\
             /  \
            /    \
           /      \
          /________\
     Integrity     Availability
```

---

# 3. Confidentiality

Confidentiality means:

> Only authorized people or systems can access information.

Examples:

* Encryption
* Passwords
* SSH keys
* Access control
* IAM
* TLS
* Secrets management

Example:

```text
User
 |
 | Authentication
 v
Application
 |
 | Authorization
 v
Protected Data
```

---

# 4. Integrity

Integrity means:

> Data should not be modified without authorization.

Examples:

* Hashes
* Checksums
* Digital signatures
* File integrity monitoring
* Git commit history

Example:

```text
Original File
     |
     v
    Hash
     |
     v
Compare Later
```

If the calculated hash changes unexpectedly, the data may have been modified.

---

# 5. Availability

Availability means:

> Systems should remain accessible when users need them.

Examples:

* High availability
* Load balancing
* Multiple instances
* Backups
* Failover
* DDoS protection
* Auto scaling

Architecture:

```text
             Load Balancer
              /          \
             v            v
         Server 1      Server 2
```

If Server 1 fails, Server 2 can continue serving traffic.

---

# 6. Authentication

Authentication answers:

> Who are you?

Examples:

* Username/password
* SSH keys
* MFA
* Certificates
* Tokens
* Biometrics

Example:

```text
User
 |
 v
Authentication
 |
 +---- Invalid → Reject
 |
 +---- Valid
       |
       v
   Authorization
```

---

# 7. Authorization

Authorization answers:

> What are you allowed to do?

Example:

```text
Developer
   |
   +---- Read Code
   |
   +---- Create Build
   |
   X---- Delete Production
```

Authentication and authorization are different.

| Concept        | Question         |
| -------------- | ---------------- |
| Authentication | Who are you?     |
| Authorization  | What can you do? |

---

# 8. Least Privilege

Least privilege means:

> Give users, applications, and systems only the permissions they actually need.

Example:

A CI runner that only needs to deploy to one Kubernetes namespace should not automatically receive unrestricted cluster-admin permissions.

Bad:

```text
CI Runner
   |
   +----> Everything
```

Better:

```text
CI Runner
   |
   +----> Required namespace
```

---

# 9. Defense in Depth

Defense in depth means using multiple security controls.

Example:

```text
Internet
   |
   v
WAF
   |
   v
Load Balancer
   |
   v
Firewall
   |
   v
Security Group
   |
   v
Application
   |
   v
NetworkPolicy
   |
   v
Database
```

If one control fails, another layer can still provide protection.

---

# 10. Firewall

A firewall controls network traffic based on rules.

Rules can consider:

* Source
* Destination
* Protocol
* Port
* Direction

Example:

```text
Internet
   |
   v
Firewall
   |
   +---- TCP 443 → ALLOW
   |
   +---- TCP 23  → DENY
```

---

# 11. Stateful vs Stateless Filtering

## Stateful Firewall

A stateful firewall tracks connection state.

Example:

```text
Client → Server
        |
        v
 Connection State
```

Return traffic can be automatically recognized as part of an established connection.

---

## Stateless Firewall

A stateless firewall evaluates packets independently according to configured rules.

AWS NACLs are a common example of a stateless network control.

---

# 12. Linux Firewall

Linux systems may use firewall frameworks and tools such as:

* nftables
* iptables
* UFW
* firewalld

Check UFW:

```bash
sudo ufw status
```

Example:

```bash
sudo ufw allow 22/tcp
```

Example:

```bash
sudo ufw allow 443/tcp
```

Always understand the effect of a firewall rule before applying it to a remote server.

---

# 13. Ports and Security

Every exposed port increases the attack surface.

Example:

```text
Server
 |
 +-- 22   SSH
 +-- 80   HTTP
 +-- 443  HTTPS
 +-- 3306 Database
```

Do not expose services unnecessarily.

A database port such as `3306` should generally not be publicly exposed.

---

# 14. Attack Surface

Attack surface means the collection of possible entry points an attacker could target.

Examples:

* Open ports
* Public APIs
* Public servers
* Vulnerable applications
* Exposed management interfaces
* Weak credentials

Reduce attack surface by:

* Closing unnecessary ports
* Removing unused services
* Restricting access
* Updating software
* Using authentication
* Segmenting networks

---

# 15. Network Segmentation

Network segmentation separates systems into different network zones.

Example:

```text
                Internet
                   |
                   v
             Public Subnet
                   |
                   v
             Load Balancer
                   |
                   v
             Private App
                Subnet
                   |
                   v
             Private DB
                Subnet
```

The database does not need direct Internet access.

---

# 16. Micro-Segmentation

Micro-segmentation applies security controls at a more granular level.

Example:

```text
Frontend
   |
   | allowed
   v
Backend
   |
   | allowed
   v
Database
```

But:

```text
Frontend
   |
   X
   |
Database
```

This reduces lateral movement.

---

# 17. Zero Trust

Zero Trust means:

> Do not automatically trust a connection simply because it comes from an internal network.

Core ideas:

* Verify identity
* Verify authorization
* Use least privilege
* Continuously monitor
* Minimize access

Traditional thinking:

```text
Inside = Trusted
Outside = Untrusted
```

Zero Trust:

```text
Every request
     |
     v
Verify
     |
     v
Authorize
     |
     v
Allow/Deny
```

---

# 18. Encryption

Encryption transforms readable data into protected data.

```text
Plaintext
   |
   v
Encryption
   |
   v
Ciphertext
```

Only an authorized party with the appropriate key can decrypt it.

---

# 19. Encryption in Transit

Encryption in transit protects data while it travels across a network.

Examples:

* HTTPS
* TLS
* SSH
* VPN

Example:

```text
Client
   |
   | Encrypted
   v
Server
```

---

# 20. Encryption at Rest

Encryption at rest protects stored data.

Examples:

* Encrypted disk
* Encrypted database
* Encrypted object storage
* Encrypted backups

Example:

```text
Application
     |
     v
Encrypted Storage
```

---

# 21. TLS

TLS provides secure communication over networks.

HTTPS commonly uses TLS.

Basic flow:

```text
Client
   |
   | TLS Handshake
   v
Server
   |
   v
Encrypted Communication
```

TLS helps provide:

* Confidentiality
* Integrity
* Server authentication

---

# 22. HTTPS

HTTPS is HTTP protected using TLS.

HTTP:

```text
Client → HTTP → Server
```

HTTPS:

```text
Client → TLS/HTTPS → Server
```

Common HTTPS port:

```text
443
```

---

# 23. SSH Security

SSH provides secure remote administration.

Default port:

```text
22
```

Useful security practices:

* Use SSH keys
* Disable unnecessary password authentication
* Restrict source IPs
* Avoid direct root login where appropriate
* Keep SSH software updated
* Use bastion hosts when appropriate
* Monitor authentication attempts

---

# 24. SSH Key Authentication

Instead of relying only on passwords:

```text
Private Key
     |
     | kept secret
     v
Client

Public Key
     |
     v
Server
```

The private key should never be shared.

---

# 25. VPN

VPN stands for Virtual Private Network.

A VPN creates a protected connection over an untrusted network.

Example:

```text
Employee
   |
   | Encrypted VPN
   v
Company Network
```

Common use cases:

* Remote access
* Site-to-site connectivity
* Private infrastructure access

---

# 26. Proxy

A proxy acts as an intermediary.

```text
Client
  |
  v
Proxy
  |
  v
Internet
```

Proxies can provide:

* Access control
* Logging
* Filtering
* Egress control

---

# 27. Reverse Proxy

A reverse proxy sits in front of backend servers.

```text
Client
   |
   v
Reverse Proxy
   |
   +----> Backend 1
   |
   +----> Backend 2
```

Common functions:

* TLS termination
* Load balancing
* Routing
* Authentication
* Security filtering

---

# 28. WAF

WAF stands for Web Application Firewall.

It protects web applications from certain types of malicious HTTP traffic.

Architecture:

```text
Internet
   |
   v
WAF
   |
   v
Load Balancer
   |
   v
Application
```

A WAF is different from a traditional network firewall.

---

# 29. DDoS

DDoS stands for Distributed Denial of Service.

Attackers use many sources to overwhelm a service.

```text
Attacker Sources
  \   |   /
   \  |  /
    \ | /
     \|/
  Application
```

Potential defenses:

* DDoS protection
* Rate limiting
* CDN
* WAF
* Load balancing
* Traffic filtering
* Auto scaling

---

# 30. Man-in-the-Middle Attack

A Man-in-the-Middle attack occurs when an attacker positions themselves between communicating parties.

Normal:

```text
Client -------- Server
```

Potential attack:

```text
Client ---- Attacker ---- Server
```

TLS helps protect communication against interception when correctly implemented.

---

# 31. Packet Sniffing

Packet sniffing means capturing network packets for analysis.

Legitimate security and troubleshooting example:

```bash
sudo tcpdump -i any
```

Specific port:

```bash
sudo tcpdump -i any port 443
```

Security teams can use packet analysis to identify suspicious traffic.

---

# 32. DNS Security

DNS security protects domain-name resolution.

Threats include:

* DNS spoofing
* DNS hijacking
* DNS tunneling
* Malicious domains

Possible controls:

* Trusted DNS resolvers
* DNS filtering
* DNSSEC where appropriate
* DNS monitoring

---

# 33. DNS Spoofing

DNS spoofing attempts to provide an incorrect IP address for a domain.

Normal:

```text
example.com
     |
     v
Correct IP
```

Spoofed:

```text
example.com
     |
     v
Attacker-controlled IP
```

---

# 34. DNS Tunneling

DNS tunneling abuses DNS queries/responses to transport data.

It can be used for:

* Data exfiltration
* Command and control

Security teams can detect unusual DNS patterns such as:

* Very long subdomains
* High query frequency
* Random-looking domain labels
* Unusual DNS destinations

---

# 35. Brute-Force Attacks

A brute-force attack attempts many credentials until one succeeds.

Example:

```text
Username
   |
   +-- Password 1
   +-- Password 2
   +-- Password 3
   +-- ...
```

Defenses include:

* Strong authentication
* MFA
* Rate limiting
* Account lockout policies
* IP restrictions
* Monitoring

---

# 36. Rate Limiting

Rate limiting controls how many requests a client can make in a period.

Example:

```text
Client
  |
  | 1000 requests
  v
Rate Limiter
  |
  +---- Allowed
  |
  +---- Block/Delay
```

It can reduce abuse and help protect services from excessive traffic.

---

# 37. Network Monitoring

Monitoring provides visibility into network behavior.

Monitor:

* Connections
* Ports
* DNS queries
* Authentication
* Firewall events
* HTTP traffic
* Network flows
* Failed connections

Linux tools:

```bash
ss
ip
tcpdump
journalctl
```

---

# 38. Security Logging

Logs help identify suspicious activity.

Examples:

```bash
journalctl
```

SSH-related logs:

```bash
journalctl -u ssh
```

Depending on the distribution, authentication information may also be available through system authentication logs.

---

# 39. AWS Security Groups

AWS Security Groups provide virtual firewall functionality for associated resources/network interfaces.

Example:

```text
Internet
   |
   | TCP 443
   v
Security Group
   |
   v
EC2
```

Use narrowly scoped rules.

---

# 40. AWS Network ACL

Network ACLs operate at the subnet level.

```text
VPC
 |
 +-- Subnet
      |
      +-- EC2
      +-- EC2
```

The NACL controls traffic entering and leaving the subnet according to its rules.

---

# 41. Security Group vs NACL

| Feature | Security Group             | NACL                   |
| ------- | -------------------------- | ---------------------- |
| Scope   | Resource/network interface | Subnet                 |
| State   | Stateful                   | Stateless              |
| Rules   | Allow-focused              | Allow and deny         |
| Purpose | Resource-level filtering   | Subnet-level filtering |

Both can be part of a defense-in-depth architecture.

---

# 42. Private vs Public Subnets

A public subnet is generally associated with a route that can reach an Internet Gateway.

A private subnet does not provide direct Internet routing through an Internet Gateway for its resources.

Example:

```text
Internet
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
Application
```

---

# 43. NAT Gateway

A NAT Gateway can allow resources in a private subnet to initiate outbound Internet connections without making those resources directly reachable from the Internet.

Example:

```text
Private EC2
    |
    v
NAT Gateway
    |
    v
Internet
```

This is commonly used when private workloads need controlled outbound access.

---

# 44. VPC Endpoint

VPC endpoints can provide private connectivity from a VPC to supported AWS services.

Conceptually:

```text
Private Workload
      |
      v
VPC Endpoint
      |
      v
AWS Service
```

This can reduce the need for Internet-based paths for supported services.

---

# 45. Kubernetes Network Security

Kubernetes network security can include:

* NetworkPolicy
* Namespace isolation
* Service exposure controls
* Ingress controls
* CNI security features
* API server access controls
* TLS

Example:

```text
Frontend
   |
   | Allowed
   v
Backend
   |
   | Allowed
   v
Database
```

---

# 46. Kubernetes NetworkPolicy

NetworkPolicy defines allowed network communication for selected Pods.

Example concept:

```text
Frontend
   |
   | ALLOW
   v
Backend

Frontend
   |
   X
   |
Database
```

Policies should be designed carefully because behavior depends on the Kubernetes networking implementation/CNI.

---

# 47. Namespace Isolation

Namespaces provide logical separation.

Example:

```text
Cluster
 |
 +-- dev
 |
 +-- staging
 |
 +-- production
```

Namespaces are useful for organization and access control, but namespaces alone should not be treated as a complete network-security boundary.

---

# 48. Container Network Security

Container environments should restrict unnecessary communication.

Example:

```text
Frontend
   |
   v
Backend
   |
   v
Database
```

Avoid:

```text
Every Container
       |
       +----> Every Other Container
```

Use network segmentation and access controls.

---

# 49. CI/CD Network Security

CI/CD infrastructure can have powerful access.

Example:

```text
Developer
   |
   v
Git Repository
   |
   v
CI Runner
   |
   +----> Container Registry
   |
   +----> Cloud
   |
   +----> Kubernetes
```

If the runner is compromised, attackers may attempt lateral movement.

Therefore:

* Restrict network access
* Restrict credentials
* Use least privilege
* Protect secrets
* Monitor outbound traffic
* Segment runners
* Avoid unnecessary public exposure

---

# 50. Secrets Security

Never hard-code secrets into source code.

Bad:

```text
password=MyPassword123
```

Better:

```text
Application
    |
    v
Secret Manager
```

Examples of secrets:

* API tokens
* Passwords
* SSH private keys
* Cloud credentials
* Database credentials

---

# 51. Credential Rotation

Credentials should be rotated according to organizational security requirements.

Examples:

* API tokens
* Access keys
* Certificates
* Passwords

Short-lived credentials are generally preferable where practical.

---

# 52. Lateral Movement

Lateral movement means an attacker moves from one compromised system to other systems.

Example:

```text
Compromised Server
       |
       v
Backend
       |
       v
Database
       |
       v
Other Systems
```

Segmentation and least privilege can reduce lateral movement.

---

# 53. Bastion Host

A bastion host is a controlled access point used to reach private systems.

Example:

```text
Administrator
      |
      v
Bastion Host
      |
      v
Private Server
```

The bastion can provide:

* Controlled entry
* Logging
* Restricted access
* Reduced exposure of private servers

---

# 54. Security Monitoring

Security monitoring should detect abnormal behavior.

Examples:

```text
Normal:
CI Runner → Registry

Suspicious:
CI Runner → Unknown External Server
```

Monitoring should investigate unexpected destinations and traffic patterns.

---

# 55. Network Security Troubleshooting

Use a structured approach.

## Step 1 — Identify Source

```text
Who is connecting?
```

## Step 2 — Identify Destination

```text
Where is it connecting?
```

## Step 3 — Check DNS

```bash
dig example.com
```

## Step 4 — Check Routing

```bash
ip route
```

## Step 5 — Check Port

```bash
nc -vz example.com 443
```

## Step 6 — Check Firewall

```bash
sudo ufw status
```

## Step 7 — Check Proxy

```bash
echo $HTTPS_PROXY
echo $NO_PROXY
```

## Step 8 — Check Application

```bash
ss -lntp
```

## Step 9 — Capture Traffic

```bash
sudo tcpdump -i any port 443
```

---

# 56. Common Network Security Failure Patterns

## DNS Failure

```text
Domain
  X
DNS
```

Test:

```bash
dig domain.com
```

---

## Port Blocked

```text
Client
  |
  X
Firewall
  |
Server
```

Test:

```bash
nc -vz host port
```

---

## Service Not Listening

```text
Client
  |
  v
Server
  |
  X
Application
```

Test:

```bash
ss -lntp
```

---

## Proxy Problem

```text
Client
  |
  v
Wrong Proxy
  |
  X
Internet
```

Check:

```bash
echo $HTTP_PROXY
echo $HTTPS_PROXY
echo $NO_PROXY
```

---

# 57. Security Principles for DevOps

Always remember:

### 1. Least Privilege

Give minimum required access.

### 2. Defense in Depth

Use multiple security controls.

### 3. Network Segmentation

Separate environments and workloads.

### 4. Encryption

Protect data in transit and at rest.

### 5. Authentication

Verify identity.

### 6. Authorization

Verify permissions.

### 7. Monitoring

Know what is happening.

### 8. Logging

Keep useful security records.

### 9. Patch Management

Keep systems updated.

### 10. Secure Defaults

Do not expose services unnecessarily.

---

# 58. Secure DevOps Architecture

A simplified architecture:

```text
                         Internet
                            |
                            v
                           WAF
                            |
                            v
                      Load Balancer
                            |
                            v
                    Private App Subnet
                       /          \
                      /            \
                     v              v
                Backend 1       Backend 2
                      \            /
                       \          /
                        v        v
                       Database
```

CI/CD path:

```text
Developer
    |
    v
Git Repository
    |
    v
CI/CD Platform
    |
    v
Private Runner
    |
    +------> Registry
    |
    +------> Cloud APIs
    |
    +------> Kubernetes API
```

Security controls:

```text
TLS
Firewall
Security Groups
NACL
NetworkPolicy
IAM
Secrets Management
Monitoring
Logging
```

---

# 59. Network Security Checklist

Before exposing a service, ask:

```text
[ ] Is this service required?
[ ] Is the port required?
[ ] Who needs access?
[ ] From which network?
[ ] Can access be restricted?
[ ] Is authentication enabled?
[ ] Is encryption enabled?
[ ] Is logging enabled?
[ ] Is monitoring enabled?
[ ] Is the service patched?
```

---

# 60. Important Commands

## Interfaces

```bash
ip addr
```

## Routes

```bash
ip route
```

## Listening Ports

```bash
ss -lntp
```

## Connections

```bash
ss -ant
```

## DNS

```bash
dig example.com
```

## Connectivity

```bash
nc -vz example.com 443
```

## HTTPS

```bash
curl -v https://example.com
```

## Firewall

```bash
sudo ufw status
```

## Packet Capture

```bash
sudo tcpdump -i any
```

## Logs

```bash
journalctl
```

## SSH Service

```bash
systemctl status ssh
```

---

# 61. Interview Mental Model

When asked:

> How do you secure a network?

Think:

```text
Identity
   ↓
Authentication
   ↓
Authorization
   ↓
Least Privilege
   ↓
Network Segmentation
   ↓
Firewall
   ↓
Encryption
   ↓
Monitoring
   ↓
Logging
   ↓
Incident Response
```

---

# 62. Final Mental Model

Network Security is not a single tool.

It is a layered system:

```text
                  NETWORK SECURITY
                         |
        +----------------+----------------+
        |                |                |
     Identity         Network            Data
        |                |                |
 Authentication      Firewall          Encryption
 Authorization       Segmentation      TLS
        |                |                |
        +----------------+----------------+
                         |
                     Monitoring
                         |
                     Detection
                         |
                      Response
```

The DevOps security mindset is:

> **Protect every connection, expose only what is required, verify every identity, use least privilege, encrypt sensitive communication, and monitor the environment continuously.**
