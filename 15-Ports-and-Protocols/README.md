# 🌐 Chapter 15 – Ports & Protocols

> **Understand how network services communicate, identify ports, troubleshoot connectivity, and apply port knowledge in real-world DevOps environments.**

---

## 📌 Overview

In computer networking, an **IP address identifies a host**, while a **port identifies a logical communication endpoint used by a service or application**.

A **protocol** defines the rules that systems follow to communicate.

For example:

```text
192.168.1.10:443
       │     │
       │     └── Port → HTTPS service
       │
       └──────── IP → Identifies the host
```

Understanding ports and protocols is essential for:

* Linux administration
* Cloud infrastructure
* Docker
* Kubernetes
* Firewalls
* Load balancers
* Security Groups
* CI/CD
* Network troubleshooting
* Microservices

---

# 🎯 Learning Objectives

By completing this chapter, you will understand:

* What a network port is
* What a network protocol is
* Difference between ports and protocols
* TCP and UDP
* Port number ranges
* Well-known ports
* Registered ports
* Dynamic/ephemeral ports
* Common service ports
* Listening ports
* Sockets
* Port troubleshooting
* Docker port mapping
* Kubernetes port concepts
* Firewall and security-group considerations

---

# 🧠 Core Concept

The basic mental model is:

```text
IP Address
    ↓
Identifies the host
    ↓
Port
    ↓
Identifies the service endpoint
    ↓
Protocol
    ↓
Defines communication rules
```

Example:

```text
Client
   │
   │ TCP 443
   ↓
Web Server
   │
   │ HTTPS
   ↓
Application
```

---

# 🔢 Port Number Ranges

TCP and UDP ports range from:

```text
0 – 65535
```

| Range       | Category        | Purpose                                  |
| ----------- | --------------- | ---------------------------------------- |
| 0–1023      | Well-known      | Common standard services                 |
| 1024–49151  | Registered      | Applications and services                |
| 49152–65535 | Dynamic/Private | Commonly used for ephemeral client ports |

---

# 🔑 Important Ports

| Port | Service                           | Typical Transport |
| ---: | --------------------------------- | ----------------- |
|   20 | FTP Data                          | TCP               |
|   21 | FTP Control                       | TCP               |
|   22 | SSH                               | TCP               |
|   23 | Telnet                            | TCP               |
|   25 | SMTP                              | TCP               |
|   53 | DNS                               | TCP/UDP           |
|   67 | DHCP Server                       | UDP               |
|   68 | DHCP Client                       | UDP               |
|   80 | HTTP                              | TCP               |
|  110 | POP3                              | TCP               |
|  123 | NTP                               | UDP               |
|  143 | IMAP                              | TCP               |
|  161 | SNMP                              | UDP               |
|  389 | LDAP                              | TCP/UDP           |
|  443 | HTTPS                             | TCP               |
| 3306 | MySQL                             | TCP               |
| 5432 | PostgreSQL                        | TCP               |
| 6379 | Redis                             | TCP               |
| 8080 | Common alternate application port | TCP               |

> Port numbers are conventional defaults. Applications can be configured to use different ports.

---

# 🔄 TCP vs UDP

| Feature     | TCP                          | UDP                             |
| ----------- | ---------------------------- | ------------------------------- |
| Connection  | Connection-oriented          | Connectionless                  |
| Reliability | Reliable delivery mechanisms | No TCP-style delivery guarantee |
| Ordering    | Ordered byte stream          | No ordering guarantee           |
| Handshake   | Yes                          | No TCP handshake                |
| Overhead    | Higher                       | Lower                           |
| Examples    | SSH, HTTP/HTTPS              | DNS, DHCP                       |

### TCP Example

```text
Client
  │
  │ SYN
  ↓
Server
  │
  │ SYN-ACK
  ↓
Client
  │
  │ ACK
  ↓
Connection Established
```

---

# 🛠️ Essential Linux Commands

### View listening ports

```bash
ss -tuln
```

### View ports and processes

```bash
sudo ss -tulpn
```

### Test a TCP port

```bash
nc -zv host port
```

Example:

```bash
nc -zv google.com 443
```

### Find the process using a port

```bash
sudo lsof -i :22
```

### Check HTTP/HTTPS connectivity

```bash
curl -I https://example.com
```

Detailed troubleshooting:

```bash
curl -v https://example.com
```

### Check routing

```bash
ip route
```

### Check firewall

```bash
sudo ufw status
```

---

# 🐳 Docker Port Mapping

Docker can map a host port to a container port.

Example:

```bash
docker run -p 8080:80 nginx
```

Meaning:

```text
Host:8080
    ↓
Container:80
    ↓
Nginx
```

The host and container ports do not need to be identical.

---

# ☸️ Kubernetes Ports

Kubernetes commonly uses:

```text
containerPort
Service port
targetPort
nodePort
```

Typical flow:

```text
Client
   ↓
Service
   ↓
targetPort
   ↓
Pod
```

Understanding these port mappings is important when troubleshooting Kubernetes applications.

---

# ☁️ DevOps & Cloud Relevance

Ports are used throughout modern infrastructure.

Example:

```text
Internet
   │
   │ TCP 443
   ↓
Load Balancer
   │
   │ TCP 8080
   ↓
Application Server
   │
   │ TCP 5432
   ↓
PostgreSQL
```

Security should restrict access to only the required ports.

For example:

```text
Internet
   ↓
443
   ↓
Load Balancer
   ↓
Application
   ↓
5432
   ↓
Database
```

The database should generally **not** be directly exposed to the public Internet.

---

# 🧪 Practical Lab

The practical lab demonstrates:

1. Listing listening ports
2. Identifying processes
3. Checking SSH port 22
4. Testing local TCP connectivity
5. Testing HTTPS port 443
6. Using `curl`
7. Using `lsof`
8. Checking routing
9. Troubleshooting unreachable services

See:

📄 [`practical-lab.md`](practical-lab.md)

---

# 📚 Chapter Resources

| File                                               | Description                    |
| -------------------------------------------------- | ------------------------------ |
| [`notes.md`](notes.md)                             | Core concepts and explanations |
| [`commands.md`](commands.md)                       | Linux networking commands      |
| [`interview-questions.md`](interview-questions.md) | Interview preparation          |
| [`practical-lab.md`](practical-lab.md)             | Hands-on exercises             |
| [`real-world-usecases.md`](real-world-usecases.md) | DevOps scenarios               |
| [`troubleshooting.md`](troubleshooting.md)         | Port troubleshooting guide     |
| `screenshots/`                                     | Practical lab evidence         |

---

# 🎯 Interview Cheat Sheet

```text
22    → SSH
25    → SMTP
53    → DNS
67    → DHCP Server
68    → DHCP Client
80    → HTTP
110   → POP3
123   → NTP
143   → IMAP
443   → HTTPS
3306  → MySQL
5432  → PostgreSQL
6379  → Redis
8080  → Common alternate application port
```

### Most important commands

```bash
ss -tuln
sudo ss -tulpn
nc -zv host port
curl -I https://example.com
curl -v https://example.com
sudo lsof -i :PORT
ip route
sudo ufw status
```

---

# 🔍 Troubleshooting Mental Model

When an application is unreachable:

```text
DNS
 ↓
IP Address
 ↓
Routing
 ↓
Firewall
 ↓
Port
 ↓
Process
 ↓
Application
```

Do not immediately restart the server.

First identify **which layer is failing**.

---

# 💼 Real-World DevOps Scenario

### Problem

> "The application is running, but users cannot access it."

### Investigation

```bash
sudo ss -tulpn | grep :8080
```

Check whether the application is listening.

Then:

```bash
nc -zv localhost 8080
```

Test local connectivity.

Then:

```bash
nc -zv <server-ip> 8080
```

Test remote connectivity.

Then check:

```bash
sudo ufw status
```

and, in cloud environments, verify:

* Security Groups
* Network ACLs
* Load balancer listeners
* Routing
* Network policies

Finally:

```bash
curl -v http://localhost:8080
```

This determines whether the service is responding at the application layer.

---

# 🏆 Key Takeaways

> **IP identifies the host.**

> **Port identifies the service endpoint.**

> **Protocol defines the communication rules.**

> **TCP provides connection-oriented reliable delivery mechanisms.**

> **UDP is connectionless and has lower protocol overhead.**

> **`ss` is one of the most important Linux tools for inspecting sockets and listening ports.**

> **Port troubleshooting is a fundamental DevOps skill.**

---

## 🚀 DevOps Skill Progression

```text
Networking Fundamentals
        ↓
IP Addressing
        ↓
Subnetting
        ↓
ARP
        ↓
ICMP
        ↓
DNS
        ↓
DHCP
        ↓
Ports & Protocols  ← You are here
        ↓
Routing
        ↓
Switching
        ↓
VLAN
        ↓
NAT
        ↓
Firewall
        ↓
Docker Networking
        ↓
Kubernetes Networking
        ↓
AWS Networking
```

**Next Chapter → Routing**
