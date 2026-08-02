# 🧪 Practical Lab – TCP/IP Model

## 🎯 Objective

The objective of this lab is to understand how the TCP/IP Model works practically by using Linux networking commands.

In this lab, we will verify:

- Network interfaces
- MAC communication
- IP addressing
- Routing
- TCP/UDP ports
- DNS resolution
- HTTP connectivity

---

# 📋 Lab Environment

## Operating System

```text
Ubuntu Linux
```

## Required Tools

```bash
ip
ping
ss
curl
dig
nslookup
nc
```

---

# ✅ Task 1 – Check Network Access Layer

## Check Network Interfaces

Command:

```bash
ip link show
```

### Objective

Verify that the network interface is active.

### Expected Result

Example:

```text
wlo1: <BROADCAST,MULTICAST,UP,LOWER_UP>
```

### Observation

- Interface exists
- Interface status is UP

---

# ✅ Task 2 – Check MAC Address Communication

## Command

```bash
ip neigh
```

### Objective

View IP-to-MAC address mappings.

### Expected Result

Example:

```text
192.168.1.1 dev wlo1 lladdr xx:xx:xx REACHABLE
```

### Observation

The system can identify nearby network devices.

---

# ✅ Task 3 – Verify IP Configuration

## Command

```bash
ip addr show
```

### Objective

Check assigned IPv4 and IPv6 addresses.

### Verify:

- IP address
- Network interface
- Broadcast address

---

# ✅ Task 4 – Check Routing

## Command

```bash
ip route
```

### Objective

Understand how packets leave the local network.

Example:

```text
default via 192.168.1.1
```

### Verify:

- Default gateway
- Network routes

---

# ✅ Task 5 – Test Network Connectivity

## Command

```bash
ping google.com
```

### Objective

Verify Internet connectivity using ICMP.

### Expected Result

Example:

```text
64 bytes from google.com
```

---

# ✅ Task 6 – Check TCP/UDP Ports

## Command

```bash
ss -tuln
```

### Objective

Identify active services and listening ports.

Example:

```text
LISTEN 0 128 0.0.0.0:22
```

### Verify:

- Running services
- Open ports

---

# ✅ Task 7 – Test Application Connectivity

## Command

```bash
curl -I https://google.com
```

### Objective

Verify HTTP/HTTPS communication.

Expected:

```text
HTTP/2 200
```

or

```text
HTTP/1.1 301
```

---

# ✅ Task 8 – Test DNS Resolution

## Commands

```bash
nslookup google.com
```

or

```bash
dig google.com
```

### Objective

Verify domain name resolution.

Expected:

```text
Name: google.com
Address: xxx.xxx.xxx.xxx
```

---

# 📊 Observation Table

| TCP/IP Layer | Command | Purpose |
|--------------|---------|---------|
| Network Access | `ip link show` | Check interfaces |
| Network Access | `ip neigh` | Check MAC mapping |
| Internet | `ip addr show` | Check IP address |
| Internet | `ip route` | Check routing |
| Internet | `ping` | Test connectivity |
| Transport | `ss -tuln` | Check ports |
| Application | `curl` | Test HTTP |
| Application | `nslookup` | Test DNS |

---

# 🌍 Real-World Scenario

## Problem

A user cannot access a web application.

A DevOps engineer follows TCP/IP troubleshooting:

### Step 1: Check Interface

```bash
ip link show
```

Is the network available?

↓

### Step 2: Check IP Address

```bash
ip addr show
```

Does the machine have an IP?

↓

### Step 3: Check Routing

```bash
ip route
```

Is the gateway configured?

↓

### Step 4: Test Connectivity

```bash
ping server-ip
```

Can the server be reached?

↓

### Step 5: Check Ports

```bash
ss -tuln
```

Is the application listening?

↓

### Step 6: Test Application

```bash
curl -I http://application-url
```

Is the service responding?

---

# ☁️ DevOps Perspective

TCP/IP troubleshooting is used in:

- AWS EC2 connectivity issues
- Docker container networking
- Kubernetes service communication
- Load balancer debugging
- API connectivity problems
- Database connection issues

---

# 🎯 Lab Summary

In this practical lab, we learned how to:

- Check network interfaces
- Verify MAC communication
- Inspect IP addresses
- Understand routing
- Test connectivity
- Check ports
- Troubleshoot DNS
- Verify application communication

---

# ✅ Conclusion

The TCP/IP Model provides a practical framework for understanding how data moves across networks.

By using Linux commands layer by layer, DevOps engineers can quickly identify and fix networking problems.
