# 🔐 Network Security

## Chapter 34 — DevOps Networking Handbook

Network Security is the practice of protecting systems, networks, applications, and data from unauthorized access, attacks, misuse, and disruption.

For a DevOps engineer, network security is essential because modern infrastructure contains:

* Servers
* Cloud resources
* Containers
* Kubernetes clusters
* APIs
* Databases
* CI/CD pipelines
* Load balancers
* Internal services
* Internet-facing applications

---

# 🎯 Chapter Objectives

By completing this chapter, you will understand:

* Network security fundamentals
* CIA Triad
* Authentication and authorization
* Firewalls
* Security Groups
* NACLs
* Network segmentation
* Zero Trust
* VPN
* Proxy
* TLS/HTTPS
* SSH security
* Ports and protocols
* Network attacks
* DDoS
* DNS security
* Container security
* Kubernetes NetworkPolicy
* Cloud network security
* CI/CD security
* Network monitoring
* Troubleshooting security issues

---

# 🧠 What Is Network Security?

Network Security protects network infrastructure and communication from threats.

Simple model:

```text
Users
  |
  v
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

Security controls should protect every layer.

---

# 🔺 CIA Triad

The CIA Triad is one of the fundamental concepts of security.

```text
             Confidentiality
                  /\
                 /  \
                /    \
               /      \
              /        \
             /__________\
        Integrity      Availability
```

## 1. Confidentiality

Only authorized users should access information.

Examples:

* Encryption
* Access control
* Authentication

---

## 2. Integrity

Data should not be modified without authorization.

Examples:

* Hashing
* Digital signatures
* File integrity monitoring

---

## 3. Availability

Systems should remain available when required.

Examples:

* Load balancing
* Redundancy
* Backups
* DDoS protection

---

# 🔑 Authentication vs Authorization

## Authentication

Authentication answers:

> Who are you?

Examples:

* Password
* SSH key
* MFA
* Certificate

---

## Authorization

Authorization answers:

> What are you allowed to do?

Examples:

```text
User
 ↓
Authentication
 ↓
Authorization
 ↓
Resource
```

---

# 🧱 Firewall

A firewall controls network traffic according to security rules.

Example:

```text
Internet
   |
   v
Firewall
   |
   +---- Allowed
   |
   +---- Blocked
```

Rules may consider:

* Source IP
* Destination IP
* Protocol
* Port
* Direction

---

# ☁️ AWS Network Security

Important AWS security components include:

```text
VPC
 |
 +-- Security Groups
 |
 +-- Network ACLs
 |
 +-- Route Tables
 |
 +-- VPC Endpoints
 |
 +-- AWS Firewall services
```

---

# 🛡️ Security Group

AWS Security Groups act as virtual firewalls associated with resources such as network interfaces.

Example:

```text
Internet
   |
   | TCP 443
   v
Security Group
   |
   v
Application
```

A secure rule should expose only required traffic.

---

# 🚧 Network ACL

A Network ACL provides subnet-level traffic control.

Example:

```text
Subnet
 |
 +-- EC2
 +-- EC2
 +-- EC2
 |
Network ACL
```

Security Groups and NACLs provide different layers of protection.

---

# 🔒 Network Segmentation

Network segmentation divides infrastructure into separate security zones.

Example:

```text
Public Subnet
     |
     v
Load Balancer
     |
     v
Private Application Subnet
     |
     v
Private Database Subnet
```

The database should not normally be directly accessible from the public Internet.

---

# 🏰 Defense in Depth

Security should not depend on one control.

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

Each layer provides additional protection.

---

# 🔐 Encryption

Encryption protects data from unauthorized reading.

## Data in Transit

Protect network communication.

Examples:

* HTTPS
* TLS
* SSH
* VPN

## Data at Rest

Protect stored information.

Examples:

* Encrypted disks
* Encrypted databases
* Encrypted object storage

---

# 🌐 HTTPS and TLS

HTTP:

```text
Client → Server
```

HTTPS:

```text
Client
  |
  | TLS
  v
Server
```

HTTPS protects HTTP communication using TLS.

---

# 🔑 SSH Security

SSH is commonly used for secure remote administration.

Default port:

```text
22
```

Recommended security practices include:

* SSH keys
* Disable unnecessary password authentication
* Disable direct root login where appropriate
* Restrict source IPs
* Use bastion/jump hosts when appropriate
* Keep OpenSSH updated
* Monitor authentication logs

---

# 🛡️ VPN

A VPN creates a protected connection across an untrusted network.

Example:

```text
Employee
   |
   | Encrypted VPN
   v
Company Network
```

VPNs are commonly used for:

* Remote access
* Site-to-site connectivity
* Private infrastructure access

---

# 🔄 Proxy

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

# 🚫 Common Network Threats

Common threats include:

* Port scanning
* Brute-force attacks
* DDoS
* Man-in-the-middle attacks
* DNS attacks
* Packet sniffing
* Unauthorized access
* Malware communication
* Credential theft
* Lateral movement

---

# 💥 DDoS

DDoS stands for Distributed Denial of Service.

The goal is to overwhelm a service with traffic.

```text
Attacker
  \
   \
    +----> Application
   /
  /
Many sources
```

Possible protections include:

* Rate limiting
* Load balancing
* DDoS protection services
* Traffic filtering
* CDN
* WAF

---

# 🕵️ Port Scanning

Port scanning identifies accessible network ports.

For defensive administration, tools such as:

```bash
ss
```

can show locally listening services.

Security teams may use authorized scanning tools to assess exposed services.

The security goal is:

> Expose only what is required.

---

# 🌐 DNS Security

DNS is critical infrastructure.

Security concerns include:

* DNS spoofing
* DNS hijacking
* DNS tunneling
* Malicious domains

Security controls may include:

* DNS filtering
* DNSSEC where appropriate
* Trusted resolvers
* Monitoring DNS queries

---

# 🐳 Container Network Security

Containers should not automatically have unrestricted communication.

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

Unnecessary communication should be restricted.

Important concepts:

* Docker networks
* Network isolation
* Container ports
* Host firewall
* Registry security

---

# ☸️ Kubernetes Network Security

Kubernetes networking security commonly involves:

* NetworkPolicy
* Namespace isolation
* Service exposure
* Ingress controls
* CNI security features
* TLS
* API server access controls

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

NetworkPolicy can help enforce these communication rules.

---

# 🔄 CI/CD Network Security

CI/CD systems are highly privileged infrastructure.

Example:

```text
Git Repository
      |
      v
CI Runner
      |
      +----> Registry
      |
      +----> Cloud
      |
      +----> Kubernetes
```

A compromised CI runner could potentially affect multiple systems.

Therefore:

* Restrict runner network access
* Use short-lived credentials where possible
* Protect secrets
* Segment runners
* Monitor outbound traffic
* Restrict Kubernetes permissions
* Avoid unnecessary public exposure

---

# 🏗️ Secure DevOps Architecture

A basic secure architecture:

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
               Public/Edge Layer
                        |
                        v
                Private App Layer
                        |
                        v
                Private Data Layer
```

CI/CD:

```text
Developer
   |
   v
Git Repository
   |
   v
CI/CD
   |
   v
Private Runner
   |
   +----> Registry
   |
   +----> Kubernetes
   |
   +----> Cloud APIs
```

---

# 🔐 Zero Trust

Zero Trust follows the principle:

> Never automatically trust a network connection just because it is inside the network.

Important principles:

* Verify identity
* Verify authorization
* Use least privilege
* Continuously monitor
* Limit network access

Example:

```text
User
 ↓
Identity Verification
 ↓
Authorization
 ↓
Application
```

---

# 📊 Network Monitoring

Security requires visibility.

Monitor:

* Network connections
* Authentication attempts
* Firewall events
* DNS queries
* HTTP traffic
* Failed connections
* Unusual outbound traffic
* Kubernetes network activity
* Cloud flow logs

Useful Linux tools:

```bash
ss
ip
tcpdump
journalctl
```

---

# 🛠️ Important Commands

Check interfaces:

```bash
ip addr
```

Check routes:

```bash
ip route
```

Check listening services:

```bash
ss -lntp
```

Check firewall:

```bash
sudo ufw status
```

Check connections:

```bash
ss -ant
```

Capture traffic:

```bash
sudo tcpdump -i any
```

Check SSH service:

```bash
systemctl status ssh
```

Check authentication logs:

```bash
journalctl -u ssh
```

---

# 🧪 Practical Labs

In this chapter you will practice:

1. Linux firewall inspection
2. UFW rules
3. Port exposure
4. SSH security
5. Network traffic inspection
6. Docker network isolation
7. Kubernetes NetworkPolicy
8. AWS Security Groups
9. AWS NACL concepts
10. Secure CI/CD network design
11. Network security troubleshooting

---

# 🎯 DevOps Security Mindset

When designing infrastructure, always ask:

```text
Who can connect?
        ↓
From where?
        ↓
To what?
        ↓
Using which protocol?
        ↓
On which port?
        ↓
Why is access required?
        ↓
Can access be restricted?
        ↓
Can the activity be monitored?
```

---

# ⭐ Golden Rule

> **Do not expose what you do not need.**

A secure network follows:

```text
Least Privilege
      +
Segmentation
      +
Encryption
      +
Authentication
      +
Authorization
      +
Monitoring
      +
Defense in Depth
```

---

# 🚀 Chapter Outcome

After completing this chapter, you should be able to:

* Explain network security
* Explain CIA Triad
* Configure basic Linux firewall rules
* Understand AWS Security Groups
* Understand NACLs
* Explain network segmentation
* Secure SSH
* Explain TLS/HTTPS
* Understand VPN and proxies
* Explain common network attacks
* Understand Docker network isolation
* Understand Kubernetes NetworkPolicy
* Design a basic secure DevOps architecture
* Troubleshoot network security problems

---

# 🧠 Final Mental Model

```text
                 NETWORK SECURITY
                        |
        +---------------+---------------+
        |               |               |
     Identity        Network          Data
        |               |               |
 Authentication     Firewall        Encryption
 Authorization      Segmentation    TLS
        |               |               |
        +---------------+---------------+
                        |
                    Monitoring
                        |
                    Detection
                        |
                    Response
```

Network security is not one tool.

It is a combination of **identity, access control, network controls, encryption, segmentation, monitoring, and secure architecture**.
