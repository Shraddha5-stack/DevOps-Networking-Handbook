# 🌐 Chapter 13 – Domain Name System (DNS)

![DNS](https://img.shields.io/badge/Networking-DNS-blue)
![Chapter](https://img.shields.io/badge/Chapter-13-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📖 Overview

**DNS (Domain Name System)** is one of the fundamental services of the Internet.

DNS translates human-readable domain names such as:

```text
google.com
github.com
example.com
```

into network addresses such as:

```text
IP Address
```

This allows users and applications to communicate with servers without needing to remember numerical IP addresses.

---

# 🎯 What I Learned

In this chapter, I learned:

- What DNS is
- Why DNS is required
- Domain names vs IP addresses
- DNS resolution
- DNS hierarchy
- Root DNS servers
- TLD DNS servers
- Authoritative DNS servers
- Recursive DNS resolvers
- DNS caching
- DNS TTL
- DNS record types
- Forward DNS
- Reverse DNS
- Recursive vs iterative queries
- DNS over UDP and TCP
- DNS ports
- DNS troubleshooting
- DNS in DevOps
- DNS in AWS
- DNS in Kubernetes

---

# 🏗️ DNS Resolution

A simplified DNS resolution process:

```text
User
 ↓
Browser
 ↓
Browser / OS Cache
 ↓
Recursive DNS Resolver
 ↓
Root DNS
 ↓
TLD DNS
 ↓
Authoritative DNS
 ↓
DNS Record
 ↓
IP Address
 ↓
Server
```

If the answer is already cached, the resolver may return it without querying the complete hierarchy.

---

# 🌳 DNS Hierarchy

```text
                    .
                 Root DNS
                    |
          -------------------
          |        |        |
         .com     .org     .in
           |
        example
           |
          www
```

DNS is hierarchical and distributed.

---

# 📋 Important DNS Records

| Record | Purpose |
|---|---|
| A | Maps hostname to IPv4 |
| AAAA | Maps hostname to IPv6 |
| CNAME | Creates hostname alias |
| MX | Mail server |
| NS | Authoritative name server |
| TXT | Text/verification information |
| PTR | Reverse DNS |

---

# 💻 Important Commands

### Check DNS Configuration

```bash
cat /etc/resolv.conf
```

### Check Resolver Status

```bash
resolvectl status
```

### Basic DNS Lookup

```bash
nslookup google.com
```

### Detailed DNS Lookup

```bash
dig google.com
```

### Short DNS Answer

```bash
dig +short google.com
```

### Query Specific DNS Server

```bash
dig @8.8.8.8 google.com
```

### Reverse DNS

```bash
dig -x 8.8.8.8
```

### Trace DNS Delegation

```bash
dig +trace example.com
```

### Simple Lookup

```bash
host google.com
```

---

# 🧪 Practical Lab

The practical lab demonstrates:

```text
DNS configuration
      ↓
nslookup
      ↓
dig
      ↓
DNS record queries
      ↓
Reverse DNS
      ↓
Specific DNS resolver
      ↓
DNS trace
      ↓
Troubleshooting
```

See:

👉 [`practical-lab.md`](./practical-lab.md)

---

# 🛠️ DNS Troubleshooting

A basic troubleshooting workflow:

```text
Check IP
   ↓
Check Route
   ↓
Check DNS Configuration
   ↓
Test DNS Resolution
   ↓
Test Specific Resolver
   ↓
Inspect DNS Records
   ↓
Test IP Connectivity
   ↓
Test Application
```

Useful commands:

```bash
ip addr
ip route
cat /etc/resolv.conf
dig
nslookup
host
ping
curl
```

---

# 🚀 DNS in DevOps

DNS is important in DevOps because modern infrastructure depends heavily on service names.

Examples:

```text
api.example.com
app.example.com
db.example.com
```

DNS is used with:

- Cloud infrastructure
- Load balancers
- APIs
- Microservices
- Containers
- Kubernetes
- CDNs
- CI/CD
- Disaster recovery

---

# ☁️ DNS in AWS

DNS can be used with AWS services such as:

```text
Route 53
Load Balancers
CloudFront
EC2
EKS
```

Example:

```text
api.example.com
       ↓
Route 53
       ↓
Load Balancer
       ↓
Application
```

---

# ☸️ DNS in Kubernetes

Kubernetes uses DNS for service discovery.

Example:

```text
backend.default.svc.cluster.local
```

Conceptually:

```text
Application Pod
      ↓
Kubernetes DNS
      ↓
Service
      ↓
Backend Pods
```

CoreDNS is commonly used for DNS inside Kubernetes clusters.

---

# 🌍 Real-World Use Cases

DNS is used for:

### Websites

```text
www.example.com
```

### APIs

```text
api.example.com
```

### Databases

```text
db.example.com
```

### Email

```text
MX records
```

### Kubernetes

```text
service.namespace.svc.cluster.local
```

### Disaster Recovery

```text
Primary Region
      ↓
DNS
      ↓
Secondary Region
```

---

# 📚 Chapter Files

| File | Description |
|---|---|
| `README.md` | Chapter overview |
| `notes.md` | DNS concepts and theory |
| `commands.md` | DNS Linux commands |
| `practical-lab.md` | Hands-on DNS experiments |
| `interview-questions.md` | DNS interview preparation |
| `real-world-usecases.md` | Real-world DevOps applications |
| `troubleshooting.md` | DNS troubleshooting guide |
| `screenshots/` | Practical lab screenshots |

---

# 📸 Screenshots

Practical screenshots are stored in:

```text
screenshots/
```

Recommended naming:

```text
01-resolv-conf.png
02-nslookup.png
03-dig-basic.png
04-dig-a-record.png
05-dig-aaaa-record.png
06-dig-mx-record.png
07-dig-ns-record.png
08-dig-txt-record.png
09-reverse-dns.png
10-specific-dns-server.png
11-dig-trace.png
12-dns-troubleshooting.png
```

---

# 💼 Interview Question

### What happens when you type `google.com` into a browser?

A strong simplified answer:

```text
Browser / OS Cache
        ↓
Recursive DNS Resolver
        ↓
Root DNS
        ↓
TLD DNS
        ↓
Authoritative DNS
        ↓
IP Address
        ↓
Browser connects to server
```

Caching can make the actual lookup shorter.

---

# 🧠 Key Takeaways

```text
DNS = Domain Name System

Domain Name
     ↓
DNS
     ↓
IP Address
```

Important concepts:

```text
Root
TLD
Authoritative DNS
Recursive Resolver
Cache
TTL
DNS Records
Forward DNS
Reverse DNS
```

Most useful commands:

```bash
dig
nslookup
host
resolvectl
```

---

# 🎯 DevOps Perspective

DNS is not just a networking concept.

It is a critical dependency in:

```text
Cloud
  ↓
DevOps
  ↓
CI/CD
  ↓
Containers
  ↓
Kubernetes
  ↓
Microservices
  ↓
Production Systems
```

Understanding DNS helps DevOps engineers troubleshoot real production problems involving **applications, APIs, load balancers, cloud infrastructure, Kubernetes, and service discovery**.

---

# ✅ Chapter Status

**Chapter 13 – DNS: Completed ✅**

---

## 🔗 Related Chapters

- Chapter 1 – Networking Fundamentals
- Chapter 9 – Subnetting
- Chapter 10 – MAC Address
- Chapter 11 – ARP
- Chapter 12 – ICMP
- Chapter 13 – DNS

---

> **Learn → Practice → Break → Debug → Document → Explain**
>
> This chapter follows the same approach by combining theory, Linux commands, practical labs, troubleshooting, and interview preparation.
