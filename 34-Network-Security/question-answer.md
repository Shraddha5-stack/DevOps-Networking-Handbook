# 🔐 Chapter 34 — Network Security Interview Questions

## 📌 Overview

This document contains beginner, intermediate, advanced, and real-world DevOps interview questions for Network Security.

The goal is not only to memorize answers but to understand:

```text
Threat
   ↓
Control
   ↓
Configuration
   ↓
Monitoring
   ↓
Troubleshooting
```

---

# 🟢 Beginner Level

## 1. What is Network Security?

**Answer:**

Network Security is the practice of protecting networks, systems, applications, devices, and data from unauthorized access, attacks, misuse, and disruption.

It includes:

* Firewalls
* Authentication
* Authorization
* Encryption
* Network segmentation
* VPN
* Monitoring
* Logging
* Intrusion detection
* Access control

### Interview Answer

> Network security protects network resources and data by controlling access, encrypting communication, segmenting networks, monitoring traffic, and preventing unauthorized activity.

---

# 2. What are the three principles of the CIA Triad?

CIA stands for:

| Principle       | Meaning                                      |
| --------------- | -------------------------------------------- |
| Confidentiality | Only authorized users can access information |
| Integrity       | Data should not be modified improperly       |
| Availability    | Systems and data should remain accessible    |

Example:

```text
Confidentiality → Encryption
Integrity       → Hashing / signatures
Availability    → Redundancy / DDoS protection
```

---

# 3. What is Authentication?

Authentication verifies **who a user or system is**.

Examples:

* Password
* SSH key
* MFA
* Certificate
* Token

```text
Authentication = Who are you?
```

---

# 4. What is Authorization?

Authorization determines **what an authenticated user is allowed to do**.

```text
Authentication = Who are you?
Authorization  = What can you access?
```

Example:

A developer may authenticate successfully but may not have permission to delete production infrastructure.

---

# 5. What is Least Privilege?

Least privilege means giving users, applications, containers, and systems **only the permissions they actually need**.

Bad:

```text
User → Full Access
```

Better:

```text
User → Required Access Only
```

---

# 6. What is a Firewall?

A firewall controls network traffic based on security rules.

It can allow or deny traffic based on:

* Source IP
* Destination IP
* Port
* Protocol
* Interface
* Connection state

Example:

```text
Internet → TCP/443 → ALLOW
Internet → TCP/22  → DENY
```

---

# 7. What is a port?

A port identifies a network service endpoint.

Common examples:

| Port | Protocol | Common Use |
| ---: | -------- | ---------- |
|   22 | TCP      | SSH        |
|   53 | UDP/TCP  | DNS        |
|   80 | TCP      | HTTP       |
|  443 | TCP      | HTTPS      |
|   25 | TCP      | SMTP       |
| 3306 | TCP      | MySQL      |
| 5432 | TCP      | PostgreSQL |
| 6379 | TCP      | Redis      |

---

# 8. Why should unnecessary ports be closed?

Every exposed service increases the attack surface.

Example:

```text
Open unnecessary port
       ↓
Exposed service
       ↓
Potential vulnerability
       ↓
Potential attack
```

Therefore:

> Close services and ports that are not required.

---

# 9. What is attack surface?

Attack surface is the collection of exposed points through which an attacker could potentially interact with a system.

Examples:

* Open ports
* APIs
* Public IP addresses
* Web applications
* SSH
* Cloud services
* Exposed databases
* Kubernetes API

---

# 10. What is encryption?

Encryption converts readable data into protected ciphertext.

```text
Plaintext
   ↓
Encryption
   ↓
Ciphertext
```

Only an authorized party with the appropriate key can recover the original data.

---

# 11. What is encryption in transit?

Encryption in transit protects data while it is moving across a network.

Examples:

* HTTPS
* SSH
* TLS
* VPN

---

# 12. What is TLS?

TLS stands for **Transport Layer Security**.

It provides:

* Encryption
* Authentication
* Integrity protection

TLS is commonly used by HTTPS.

---

# 13. What is HTTPS?

HTTPS is HTTP protected using TLS.

```text
HTTP + TLS = HTTPS
```

HTTPS protects communication between clients and servers.

---

# 14. What is SSH?

SSH stands for **Secure Shell**.

It provides secure remote access to systems.

Default port:

```text
22/TCP
```

SSH encrypts the communication between client and server.

---

# 15. What is SSH key authentication?

SSH key authentication uses a key pair:

```text
Private Key → kept secret
Public Key  → stored on server
```

The private key should never be shared.

---

# 🟡 Intermediate Level

# 16. Stateful vs Stateless Firewall?

### Stateful

A stateful firewall tracks connection state.

Example:

```text
Client → Server
         ↓
Connection tracked
         ↓
Response allowed
```

### Stateless

A stateless firewall evaluates individual packets against rules without maintaining connection state.

AWS example:

```text
Security Group → Stateful
NACL           → Stateless
```

---

# 17. What is Network Segmentation?

Network segmentation divides a network into separate security zones.

Example:

```text
Internet
   |
Public Zone
   |
Application Zone
   |
Database Zone
```

Benefits:

* Limits lateral movement
* Reduces attack surface
* Controls communication
* Improves security

---

# 18. What is Micro-Segmentation?

Micro-segmentation applies fine-grained security controls between workloads.

For example:

```text
Frontend → Backend : ALLOW 8080
Frontend → Database: DENY

Backend → Database : ALLOW 3306
```

This is more granular than simply separating a network into broad zones.

---

# 19. What is Zero Trust?

Zero Trust follows the principle:

> **Never trust automatically; always verify.**

It assumes that network location alone does not establish trust.

Security decisions should consider:

* Identity
* Device
* Application
* Context
* Permissions
* Resource

---

# 20. What is Defense in Depth?

Defense in depth means using multiple security layers.

Example:

```text
WAF
 ↓
Load Balancer
 ↓
Firewall
 ↓
Security Group
 ↓
Private Subnet
 ↓
NetworkPolicy
 ↓
Application Authentication
 ↓
Database Access Control
```

If one layer fails, other layers still provide protection.

---

# 21. What is a VPN?

VPN stands for Virtual Private Network.

It creates an encrypted connection between networks or users.

Example:

```text
Employee
   |
Encrypted VPN Tunnel
   |
Company Network
```

Common uses:

* Remote access
* Site-to-site connectivity
* Secure private communication

---

# 22. What is a Proxy?

A forward proxy acts on behalf of clients.

```text
Client
   ↓
Proxy
   ↓
Internet
```

The proxy can provide:

* Access control
* Logging
* Filtering
* Caching
* Traffic inspection

---

# 23. What is a Reverse Proxy?

A reverse proxy sits in front of backend servers.

```text
Client
   ↓
Reverse Proxy
   ↓
Backend Servers
```

Examples of uses:

* TLS termination
* Load balancing
* Routing
* Security filtering
* Hiding backend servers

---

# 24. Proxy vs Reverse Proxy

| Proxy                     | Reverse Proxy            |
| ------------------------- | ------------------------ |
| Represents clients        | Represents servers       |
| Client → Proxy → Internet | Client → Proxy → Backend |
| Controls outbound traffic | Controls inbound traffic |
| Used by clients           | Used in front of servers |

---

# 25. What is a WAF?

WAF stands for **Web Application Firewall**.

It protects web applications from malicious HTTP/HTTPS requests.

It can help detect/block attacks such as:

* SQL injection
* Cross-site scripting
* Malicious HTTP requests
* Some automated attacks

---

# 26. What is DDoS?

DDoS stands for **Distributed Denial of Service**.

Attackers use many systems to generate large amounts of traffic toward a target.

Goal:

```text
Legitimate Users
       ↓
     Server
       ↑
Large Attack Traffic
```

The result can be resource exhaustion and service unavailability.

---

# 27. What is a Man-in-the-Middle attack?

A Man-in-the-Middle attack occurs when an attacker positions themselves between two communicating parties and attempts to intercept or manipulate communication.

TLS helps protect against this by providing encryption and server authentication when correctly implemented.

---

# 28. What is packet sniffing?

Packet sniffing means capturing network packets for analysis.

Tools include:

```bash
tcpdump
```

and:

```text
Wireshark
```

Packet capture is useful for:

* Troubleshooting
* Security investigations
* Protocol analysis

---

# 29. What is DNS spoofing?

DNS spoofing involves manipulating DNS resolution so a domain resolves to an incorrect or malicious destination.

Potential impact:

```text
User
 ↓
DNS
 ↓
Wrong IP
 ↓
Malicious Destination
```

---

# 30. What is DNS tunneling?

DNS tunneling abuses DNS queries/responses to carry data through DNS traffic.

It can be used for:

* Command and control
* Data exfiltration

Security monitoring can look for unusual DNS patterns.

---

# 31. What is rate limiting?

Rate limiting restricts how many requests a client can make during a specific period.

Example:

```text
100 requests/minute
```

After the limit is reached:

```text
Request → Rejected / Delayed
```

It can help reduce:

* Brute-force attacks
* API abuse
* Excessive traffic
* Resource exhaustion

---

# 32. What is a bastion host?

A bastion host is a hardened system used as a controlled entry point into a private environment.

Example:

```text
Admin
  |
  ↓
Bastion
  |
  ↓
Private Servers
```

It should have:

* Restricted access
* Strong authentication
* Logging
* Minimal software
* Limited permissions

---

# 🟠 AWS Network Security Questions

# 33. What is an AWS Security Group?

A Security Group is a virtual firewall associated with AWS resources such as network interfaces.

Important characteristics:

* Stateful
* Controls inbound traffic
* Controls outbound traffic
* Rules are allow-based

---

# 34. What is an AWS NACL?

A Network Access Control List is a subnet-level network control.

Characteristics:

* Stateless
* Supports allow and deny rules
* Evaluated using rule numbers
* Applies at subnet level

---

# 35. Security Group vs NACL?

| Feature    | Security Group        | NACL                   |
| ---------- | --------------------- | ---------------------- |
| Scope      | Resource/ENI          | Subnet                 |
| Stateful   | Yes                   | No                     |
| Rules      | Allow                 | Allow/Deny             |
| Evaluation | Rules collectively    | Rule number order      |
| Common use | Resource-level access | Subnet-level filtering |

### Interview Answer

> Security Groups provide stateful resource-level filtering, while NACLs provide stateless subnet-level filtering.

---

# 36. What is a public subnet?

A subnet is generally considered public when its route table has a route to an Internet Gateway and the resources also have appropriate addressing/configuration for Internet communication.

---

# 37. What is a private subnet?

A private subnet does not have a direct route to an Internet Gateway for the workload's Internet access.

Private workloads may use:

* NAT Gateway for outbound Internet access
* VPC endpoints for private access to supported AWS services

---

# 38. Why keep databases in private subnets?

Databases normally should not be directly accessible from the public Internet.

Typical architecture:

```text
Internet
   ↓
Load Balancer
   ↓
Application
   ↓
Database
```

The database is accessible only from the application tier.

---

# 39. What is a NAT Gateway?

NAT Gateway allows resources in private subnets to initiate outbound connections to the Internet while preventing unsolicited inbound Internet connections to those private resources through the NAT path.

Example:

```text
Private EC2
    ↓
NAT Gateway
    ↓
Internet
```

---

# 40. What is an Internet Gateway?

An Internet Gateway provides a path between a VPC and the Internet for appropriately configured resources and routes.

Example:

```text
VPC
 |
Internet Gateway
 |
Internet
```

---

# 41. What is a VPC Endpoint?

A VPC endpoint provides private connectivity from a VPC to supported AWS services without requiring Internet Gateway or NAT traversal for that service path.

---

# 🔵 Kubernetes Network Security

# 42. What is Kubernetes NetworkPolicy?

NetworkPolicy defines rules controlling traffic to and/or from selected Pods.

Example:

```text
Frontend → Backend : ALLOW
Frontend → Database: DENY
Backend  → Database: ALLOW
```

NetworkPolicy enforcement depends on the installed CNI.

---

# 43. Why is CNI important for NetworkPolicy?

Kubernetes defines the NetworkPolicy API, but actual enforcement is performed by the networking implementation/CNI.

Therefore:

```text
NetworkPolicy object
        ↓
CNI enforcement
        ↓
Actual network behavior
```

Always verify that your CNI supports the policies you depend on.

---

# 44. How do you troubleshoot Kubernetes NetworkPolicy?

Check:

```bash
kubectl get networkpolicy
```

Then:

```bash
kubectl describe networkpolicy <policy>
```

Check Pod labels:

```bash
kubectl get pods --show-labels
```

Check Service:

```bash
kubectl get svc
```

Check endpoints:

```bash
kubectl get endpoints
```

Check DNS:

```bash
kubectl exec <pod> -- nslookup <service>
```

Test connectivity:

```bash
kubectl exec <pod> -- wget -qO- http://<service>
```

---

# 45. Why are labels important in NetworkPolicy?

NetworkPolicy commonly selects Pods using labels.

Example:

```yaml
podSelector:
  matchLabels:
    app: backend
```

If the labels do not match, the policy will not select the intended Pods.

---

# 46. What is Kubernetes namespace isolation?

Namespaces logically separate Kubernetes resources.

They help organize:

* Applications
* Teams
* Environments
* Policies

For stronger network isolation, combine namespaces with NetworkPolicies and appropriate CNI capabilities.

---

# 🐳 Docker Network Security

# 47. How does Docker networking affect security?

Docker networking controls how containers communicate with:

* Other containers
* Host
* External networks

Security considerations include:

* Published ports
* Network isolation
* Container-to-container communication
* Host networking
* Network segmentation

---

# 48. Why should Docker ports not be published unnecessarily?

If you run:

```bash
docker run -p 8080:80 nginx
```

the container's service becomes reachable through the host's published port.

Only publish ports that users or other required systems actually need.

---

# 49. What is Docker network isolation?

Containers can be placed on separate Docker networks.

Example:

```text
frontend-network
    |
    ├── frontend
    └── proxy

database-network
    |
    └── database
```

This can reduce unnecessary communication paths.

---

# 50. What is Docker host networking?

With host networking, the container uses the host's network namespace rather than a normal isolated container network namespace.

Because isolation is reduced, use host networking only when it is actually required.

---

# 🟣 CI/CD Network Security

# 51. What are the network security risks in CI/CD?

Possible risks include:

* Exposed runners
* Stolen credentials
* Unrestricted outbound traffic
* Insecure webhooks
* Compromised dependencies
* Exposed artifact repositories
* Public container registries
* Secrets leakage

---

# 52. How should CI/CD runners be secured?

Use:

* Least privilege
* Short-lived credentials
* Network restrictions
* Trusted images
* Updated runners
* Secret management
* Logging
* Isolation between jobs where appropriate

---

# 53. Why should CI/CD runners have controlled outbound access?

If a runner is compromised, unrestricted Internet access can allow:

* Data exfiltration
* Command-and-control communication
* Malicious downloads

Therefore, outbound access should be controlled where practical.

---

# 54. How should secrets be protected in CI/CD?

Do not hard-code secrets:

```text
password=secret123
```

Instead use:

* Secret managers
* CI/CD secret stores
* IAM roles
* Short-lived credentials
* Environment-specific secret injection

Never commit secrets to Git.

---

# 55. What is credential rotation?

Credential rotation means periodically replacing credentials such as:

* Passwords
* API keys
* Access tokens
* Certificates
* SSH keys

Short-lived credentials are generally preferable where supported.

---

# 🔴 Advanced Questions

# 56. Explain a secure three-tier architecture.

Example:

```text
                    Internet
                       |
                       ↓
                  WAF / LB
                       |
                       ↓
                 Public Tier
                       |
                       ↓
                Private App Tier
                       |
                       ↓
                Private DB Tier
```

Security controls:

```text
Internet
   ↓
WAF
   ↓
Load Balancer
   ↓
Security Group
   ↓
Private Application
   ↓
NetworkPolicy
   ↓
Database
```

Each tier has limited communication permissions.

---

# 57. How would you secure a production web application?

I would consider:

1. HTTPS/TLS
2. WAF
3. Load balancer
4. Private application servers
5. Restricted security groups
6. Network segmentation
7. Database isolation
8. Least privilege
9. Authentication and authorization
10. Secrets management
11. Logging and monitoring
12. Rate limiting
13. Backup and recovery
14. Vulnerability management
15. Incident response

---

# 58. How would you secure SSH on production servers?

I would:

* Use SSH keys
* Restrict source networks
* Avoid unnecessary Internet exposure
* Disable direct root login where appropriate
* Use least privilege
* Keep OpenSSH updated
* Monitor authentication logs
* Use MFA or stronger access controls where supported
* Consider a bastion or private access path

Before changing SSH configuration:

```bash
sudo sshd -t
```

Then apply changes carefully and retain a recovery path.

---

# 59. How do you identify a compromised server?

I would investigate:

### Network

```bash
sudo ss -antup
```

### Processes

```bash
ps aux
```

### Routes

```bash
ip route
```

### Logs

```bash
sudo journalctl
```

### Network traffic

```bash
sudo tcpdump -i any
```

I would look for:

* Unknown processes
* Unexpected listening ports
* Suspicious outbound connections
* Failed login attempts
* Unexpected configuration changes
* Unusual traffic patterns

---

# 60. What would you do if you find an unexpected open port?

My approach:

```text
Identify port
    ↓
Identify process
    ↓
Understand business requirement
    ↓
Check configuration
    ↓
Restrict exposure if unnecessary
    ↓
Review logs
    ↓
Check for suspicious activity
    ↓
Document the change
```

Commands:

```bash
sudo ss -lntup
```

```bash
sudo lsof -i :<port>
```

---

# 61. How would you troubleshoot "connection refused"?

I would check:

```text
DNS
 ↓
IP
 ↓
Route
 ↓
Firewall
 ↓
Port
 ↓
Service
```

Commands:

```bash
dig <domain>
```

```bash
ip route
```

```bash
sudo ss -lntup
```

```bash
nc -vz <host> <port>
```

```bash
sudo systemctl status <service>
```

---

# 62. How would you troubleshoot a timeout?

A timeout may indicate that packets are being dropped or a path is unavailable.

I would check:

* DNS
* Routing
* Security Groups
* NACLs
* Firewall
* NetworkPolicy
* Service
* Network path

Commands:

```bash
ping -c 4 <host>
```

```bash
nc -vz <host> <port>
```

```bash
traceroute <host>
```

```bash
sudo tcpdump -i any
```

---

# 63. How would you troubleshoot DNS failure?

I would check:

```bash
cat /etc/resolv.conf
```

```bash
dig example.com
```

```bash
getent hosts example.com
```

Then test another resolver:

```bash
dig @8.8.8.8 example.com
```

I would investigate:

* DNS resolver
* Network connectivity
* Firewall
* DNS configuration
* DNS server availability

---

# 64. How would you troubleshoot HTTPS failure?

I would test:

```bash
curl -Iv https://example.com
```

Then check:

```text
DNS
 ↓
TCP/443
 ↓
TLS
 ↓
HTTP
```

Commands:

```bash
dig example.com
```

```bash
nc -vz example.com 443
```

```bash
sudo tcpdump -i any port 443
```

I would also check certificate validity and server configuration.

---

# 65. What is lateral movement?

Lateral movement occurs when an attacker moves from one compromised system to other systems within an environment.

Example:

```text
Compromised Web Server
        ↓
Application Server
        ↓
Database
```

Segmentation and least privilege help reduce lateral movement.

---

# 66. How does network segmentation reduce lateral movement?

Suppose an attacker compromises a frontend server.

Without segmentation:

```text
Frontend → Everything
```

With segmentation:

```text
Frontend → Backend : ALLOW
Frontend → Database: DENY
Frontend → Admin   : DENY
```

The attacker's movement becomes more restricted.

---

# 67. What is the difference between encryption and hashing?

### Encryption

Can be reversed with the appropriate key.

```text
Plaintext
   ↓
Encryption
   ↓
Ciphertext
```

### Hashing

Produces a hash value designed for one-way use.

```text
Data
 ↓
Hash
 ↓
Digest
```

Passwords should normally be stored using secure password-hashing algorithms rather than reversible encryption.

---

# 68. Why is HTTPS important?

HTTPS provides protection for web traffic through TLS.

It helps provide:

* Confidentiality
* Integrity
* Server authentication

Without encryption, sensitive HTTP traffic could potentially be observed or modified in transit.

---

# 69. What is TLS termination?

TLS termination means decrypting HTTPS traffic at a component such as:

* Load balancer
* Reverse proxy
* Ingress controller

Example:

```text
Client
  |
 HTTPS
  ↓
Load Balancer
  |
 HTTP/HTTPS
  ↓
Application
```

Whether traffic remains encrypted between the proxy and backend depends on the architecture and security requirements.

---

# 70. What is mutual TLS?

Mutual TLS, or mTLS, authenticates both sides of a connection using certificates.

Normal TLS commonly provides:

```text
Client → verifies server
```

mTLS provides:

```text
Client ↔ Server
both authenticate
```

It is useful for service-to-service authentication in some environments.

---

# 🧠 Scenario-Based Questions

# 71. Scenario: Database is publicly accessible

### Problem

A MySQL server is exposed:

```text
0.0.0.0:3306
```

### What would you do?

1. Confirm whether public access is required.
2. Remove unnecessary public exposure.
3. Place the database in a private subnet/network.
4. Restrict access to the application tier.
5. Review Security Groups/firewalls.
6. Review authentication and credentials.
7. Review logs for suspicious connections.

Desired architecture:

```text
Internet
   ↓
Load Balancer
   ↓
Application
   ↓
Database
```

Not:

```text
Internet
   ↓
Database
```

---

# 72. Scenario: Developer cannot access Kubernetes service

Check:

```bash
kubectl get pods
```

```bash
kubectl get svc
```

```bash
kubectl get endpoints
```

```bash
kubectl get networkpolicy
```

```bash
kubectl get pods --show-labels
```

Then test DNS and connectivity.

Possible causes:

* Wrong Service selector
* Pod not Ready
* No endpoints
* NetworkPolicy
* DNS failure
* Wrong port
* CNI issue

---

# 73. Scenario: Application cannot access database

Troubleshooting:

```text
Application
    ↓
DNS
    ↓
Database IP
    ↓
Route
    ↓
Firewall / SG / NACL
    ↓
Database Port
    ↓
Database Service
```

Check:

```bash
dig <db-hostname>
```

```bash
nc -vz <db-host> 3306
```

Check cloud security rules and database configuration.

---

# 74. Scenario: SSH suddenly stopped working

Do not immediately change random firewall rules.

Check:

```text
Is server running?
      ↓
Is IP correct?
      ↓
Is route available?
      ↓
Is port 22 listening?
      ↓
Is firewall allowing it?
      ↓
Is cloud Security Group allowing it?
      ↓
Is sshd running?
      ↓
Are authentication credentials valid?
```

If console access exists:

```bash
sudo systemctl status ssh
```

```bash
sudo ss -lntp | grep ':22'
```

```bash
sudo sshd -t
```

```bash
sudo journalctl -u ssh
```

---

# 75. Scenario: CI/CD pipeline cannot pull a Docker image

Check:

```text
DNS
 ↓
Internet/private network connectivity
 ↓
Registry DNS
 ↓
TCP/443
 ↓
Proxy
 ↓
Authentication
 ↓
Registry permissions
```

Commands:

```bash
dig <registry>
```

```bash
curl -Iv https://<registry>
```

```bash
docker login <registry>
```

Also check:

* Runner network
* Firewall
* Proxy
* Registry availability
* Credentials
* IAM permissions

---

# 76. Scenario: Application works inside Kubernetes but not from Internet

Possible causes:

* Service type
* Ingress configuration
* Load balancer
* Security Group
* Firewall
* NetworkPolicy
* DNS
* Route
* Port mismatch

Mental model:

```text
Internet
   ↓
DNS
   ↓
Load Balancer / Ingress
   ↓
Service
   ↓
Pods
```

Troubleshoot from outside to inside.

---

# 77. Scenario: Service works by IP but not hostname

Likely area:

```text
DNS
```

Check:

```bash
dig <hostname>
```

```bash
getent hosts <hostname>
```

In Kubernetes:

```bash
kubectl exec <pod> -- nslookup <service>
```

Then check DNS configuration and CoreDNS.

---

# 78. Scenario: Service works locally but not remotely

Example:

```text
curl http://127.0.0.1:8080
```

works, but:

```text
curl http://<server-ip>:8080
```

fails.

Check:

```bash
sudo ss -lntp | grep ':8080'
```

If service is listening on:

```text
127.0.0.1:8080
```

it is local-only.

If remote access is required, verify the service binding and firewall configuration.

---

# 79. What is your general network security troubleshooting methodology?

My methodology is:

```text
1. Understand the architecture
2. Identify source
3. Identify destination
4. Check DNS
5. Check IP
6. Check routing
7. Check firewall
8. Check cloud security controls
9. Check port
10. Check service
11. Check authentication
12. Check TLS
13. Check logs
14. Capture packets if necessary
15. Make the smallest required change
16. Retest
17. Document
```

---

# ⭐ Important Commands for Interviews

## Interface

```bash
ip addr
```

## Routing

```bash
ip route
```

## Listening ports

```bash
sudo ss -lntup
```

## DNS

```bash
dig example.com
```

## Connectivity

```bash
ping -c 4 example.com
```

## Port testing

```bash
nc -vz <host> <port>
```

## HTTP

```bash
curl -I https://example.com
```

## Detailed HTTPS

```bash
curl -Iv https://example.com
```

## Packet capture

```bash
sudo tcpdump -i any
```

## Firewall

```bash
sudo ufw status verbose
```

## SSH

```bash
sudo systemctl status ssh
```

## SSH configuration validation

```bash
sudo sshd -t
```

## Docker networks

```bash
docker network ls
```

## Kubernetes NetworkPolicy

```bash
kubectl get networkpolicy
```

## AWS Security Groups

```bash
aws ec2 describe-security-groups
```

## AWS NACLs

```bash
aws ec2 describe-network-acls
```

---

# 🎯 Top 20 Questions You Must Know

Before an interview, make sure you can answer these without looking at notes:

1. What is Network Security?
2. Explain CIA Triad.
3. Authentication vs Authorization.
4. What is Least Privilege?
5. What is a firewall?
6. Stateful vs Stateless firewall.
7. What is Network Segmentation?
8. What is Zero Trust?
9. What is Defense in Depth?
10. What is TLS?
11. HTTP vs HTTPS.
12. How does SSH work?
13. Security Group vs NACL.
14. Public vs Private Subnet.
15. What is NAT Gateway?
16. What is Kubernetes NetworkPolicy?
17. Why is CNI important?
18. How do you secure Docker networking?
19. How do you secure CI/CD networking?
20. How do you troubleshoot a connection timeout/refused error?

---

# 🏆 Final Interview Mental Model

When the interviewer asks any Network Security question, think:

```text
                    NETWORK SECURITY
                           |
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
       IDENTITY          NETWORK          DATA
          |                |                |
   Authentication     Firewall          Encryption
   Authorization      Segmentation      TLS
   Least Privilege    SG/NACL           SSH
          |                |                |
          └────────────────┼────────────────┘
                           ↓
                       MONITORING
                           |
                        Logging
                           |
                        Detection
                           |
                        Response
```

## The DevOps Security Formula

```text
Security
   =
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
Logging
+
Defense in Depth
```

---

# 🔥 One-Line Interview Answer

If the interviewer asks:

> **"How do you approach network security as a DevOps engineer?"**

Answer:

> "I follow a defense-in-depth approach: I minimize the attack surface, apply least privilege, segment networks, restrict ports and traffic using firewalls and cloud security controls, encrypt communication with TLS/SSH, secure containers and Kubernetes with appropriate network policies, protect CI/CD credentials, and continuously monitor logs and network activity for suspicious behavior."

---

# ✅ Chapter 34 Completion Checklist

* [x] README.md
* [x] notes.md
* [x] commands.md
* [x] practical-lab.md
* [x] interview-questions.md

**Chapter 34 — Network Security: COMPLETE ✅**
