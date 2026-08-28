# 🔥 Chapter 22 – Firewall

## 📚 Overview

A **firewall** is a network security mechanism that controls incoming and outgoing network traffic based on predefined rules.

In DevOps, firewalls are important for protecting servers, applications, databases, containers, and cloud infrastructure.

---

## 🎯 Learning Objectives

By completing this chapter, you will understand:

* What a firewall is
* Why firewalls are important in DevOps
* Inbound vs outbound traffic
* Firewall rules
* UFW
* iptables
* nftables
* How to check listening ports
* How to allow and deny network traffic
* Basic firewall troubleshooting
* Real-world DevOps firewall scenarios

---

## 📂 Chapter Contents

| File                     | Description                                 |
| ------------------------ | ------------------------------------------- |
| `README.md`              | Chapter overview                            |
| `notes.md`               | Firewall concepts and theory                |
| `commands.md`            | Hands-on firewall commands and observations |
| `practical-lab.md`       | Practical firewall troubleshooting lab      |
| `interview-questions.md` | Firewall interview questions                |
| `screenshots/`           | Screenshots from practical work             |

---

## 🔥 What is a Firewall?

A firewall controls network traffic between systems based on security rules.

Basic flow:

```text
Client
   ↓
Network
   ↓
Firewall
   ↓
Server
   ↓
Application
```

The firewall decides whether traffic should be:

```text
ALLOW
DENY
```

---

## 🚪 Inbound vs Outbound Traffic

### Inbound Traffic

Traffic coming **into** a server.

Example:

```text
Internet → Server:22
```

Port 22 is commonly used for SSH.

### Outbound Traffic

Traffic going **from** the server to another system.

Example:

```text
Server → Internet:443
```

Port 443 is commonly used for HTTPS.

---

## 🛠️ Common Linux Firewall Tools

### UFW

Simple firewall management tool commonly used on Ubuntu.

```bash
sudo ufw status
```

### iptables

A traditional Linux packet-filtering framework.

```bash
sudo iptables -L -n -v
```

### nftables

Modern Linux packet-filtering framework.

```bash
sudo nft list ruleset
```

---

## 🔍 Important Troubleshooting Commands

Check listening ports:

```bash
sudo ss -ltnp
```

Check TCP and UDP listening ports:

```bash
sudo ss -tulnp
```

Check UFW:

```bash
sudo ufw status verbose
```

Check iptables:

```bash
sudo iptables -L -n -v
```

---

## 💼 DevOps Use Cases

Firewalls are commonly involved when:

* SSH connections fail
* Web applications cannot be reached
* HTTP/HTTPS traffic is blocked
* Database access needs restriction
* Docker applications expose ports
* Kubernetes services cannot be reached
* CI/CD servers need network access
* Production servers require restricted access

---

## 🧠 Troubleshooting Approach

When an application cannot be reached, check step by step:

```text
Application running?
       ↓
Process running?
       ↓
Port listening?
       ↓
Service reachable?
       ↓
Firewall allowing traffic?
       ↓
Routing correct?
       ↓
Cloud security rules correct?
```

---

## 🔐 Security Principle

A good firewall strategy follows:

```text
Deny by default
       ↓
Allow only required traffic
```

For example, a web server might need:

```text
22   → SSH
80   → HTTP
443  → HTTPS
```

Other unnecessary ports should not be exposed.

---

## 🎯 Chapter Goal

After completing this chapter, you should be able to:

> **Check firewall configuration, understand firewall rules, identify blocked ports, and troubleshoot basic network connectivity problems on Linux servers.**
