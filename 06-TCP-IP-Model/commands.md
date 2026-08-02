# 💻 Linux Networking Commands – TCP/IP Model

This section explains Linux networking commands used to understand and troubleshoot different layers of the TCP/IP Model.

These commands are commonly used by Linux Administrators, Cloud Engineers, and DevOps Engineers.

---

# 📊 TCP/IP Layer and Command Mapping

| TCP/IP Layer | Purpose | Linux Commands |
|--------------|---------|----------------|
| Network Access Layer | Interface and MAC communication | `ip link show`, `ip neigh` |
| Internet Layer | IP addressing and routing | `ip addr`, `ip route`, `ping` |
| Transport Layer | Ports and connections | `ss`, `netstat` |
| Application Layer | Services and protocols | `curl`, `dig`, `nslookup` |

---

# 1️⃣ Network Access Layer Commands

## Check Network Interfaces

### Command

```bash
ip link show
```

### Purpose

Displays network interfaces and their current status.

### Example

```text
wlo1: <BROADCAST,MULTICAST,UP,LOWER_UP>
```

### Use Case

Used to verify whether Ethernet or Wi-Fi interfaces are active.

---

## Check MAC Address

### Command

```bash
ip link show
```

### Purpose

Displays MAC addresses assigned to network interfaces.

Example:

```text
link/ether 00:11:22:33:44:55
```

### Use Case

Useful for troubleshooting Layer 2 communication.

---

## View Neighbor Table

### Command

```bash
ip neigh
```

### Purpose

Displays IP-to-MAC address mappings.

Example:

```text
192.168.1.1 dev wlo1 lladdr xx:xx:xx:xx REACHABLE
```

### Use Case

Checks local network device communication.

---

# 2️⃣ Internet Layer Commands

## Display IP Address

### Command

```bash
ip addr show
```

### Purpose

Displays IPv4 and IPv6 addresses assigned to interfaces.

### Use Case

Checks whether a system has a valid IP address.

---

## Display Routing Table

### Command

```bash
ip route
```

### Purpose

Shows how packets are forwarded to different networks.

Example:

```text
default via 192.168.1.1
```

### Use Case

Troubleshooting gateway and routing issues.

---

## Test Network Connectivity

### Command

```bash
ping google.com
```

### Purpose

Uses ICMP protocol to test connectivity.

### Use Case

Checks whether another host is reachable.

---

# 3️⃣ Transport Layer Commands

## Display Listening Ports

### Command

```bash
ss -tuln
```

### Purpose

Shows active TCP and UDP listening ports.

Example:

```text
LISTEN 0 128 0.0.0.0:22
```

### Use Case

Checks whether services are running.

---

## Check Specific Port

### Command

```bash
ss -tulnp | grep 80
```

### Purpose

Checks which process is using a specific port.

---

## Test Port Connectivity

### Command

```bash
nc -zv google.com 443
```

### Purpose

Tests whether a TCP port is reachable.

---

# 4️⃣ Application Layer Commands

## Test HTTP Service

### Command

```bash
curl -I https://google.com
```

### Purpose

Checks HTTP/HTTPS response headers.

Example:

```text
HTTP/2 200
```

### Use Case

Troubleshooting web servers and APIs.

---

## DNS Lookup

### Command

```bash
nslookup google.com
```

or

```bash
dig google.com
```

### Purpose

Checks domain name resolution.

### Use Case

Troubleshooting DNS problems.

---

## Check DNS Configuration

### Command

```bash
cat /etc/resolv.conf
```

### Purpose

Displays configured DNS servers.

---

# 🔄 TCP/IP Troubleshooting Flow

```
Network Access Layer
        |
        ↓
ip link show
ip neigh

        |
        ↓

Internet Layer
        |
        ↓
ip addr show
ip route
ping

        |
        ↓

Transport Layer
        |
        ↓
ss -tuln

        |
        ↓

Application Layer
        |
        ↓
curl
dig
nslookup
```

---

# ☁️ DevOps Real-World Usage

## Scenario 1: Website Not Opening

Commands:

```bash
ping google.com

curl -I https://website.com
```

Checks:

- Network connectivity
- Application response

---

## Scenario 2: Application Port Not Working

Commands:

```bash
ss -tuln

nc -zv server-ip port
```

Checks:

- Service availability
- Firewall rules

---

## Scenario 3: DNS Issue

Commands:

```bash
nslookup domain.com

dig domain.com
```

Checks:

- DNS resolution
- DNS server configuration

---

# 📌 Summary

These Linux commands help engineers troubleshoot TCP/IP communication from the lowest layer to the application layer.

Understanding these commands is essential for:

- Linux Administration
- Cloud Networking
- Docker Networking
- Kubernetes Networking
- DevOps Troubleshooting
