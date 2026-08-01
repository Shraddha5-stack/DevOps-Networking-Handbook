# 💻 Linux Networking Commands – OSI Model

This section introduces Linux commands that help troubleshoot networking problems based on the OSI Model layers.

---

# 📊 OSI Layer Mapping

| OSI Layer | Purpose | Linux Commands |
|-----------|---------|----------------|
| Layer 1 – Physical | Check interfaces | `ip link show` |
| Layer 2 – Data Link | Check MAC address | `ip link show`, `ip neigh` |
| Layer 3 – Network | Check IP & routing | `ip addr show`, `ip route`, `ping` |
| Layer 4 – Transport | Check ports | `ss -tuln` |
| Layer 5–7 | Check applications | `curl`, `wget`, `dig`, `nslookup` |

---

# 1️⃣ Check Physical Layer

## Command

```bash
ip link show
```

### Purpose

Displays all available network interfaces and their status.

### Example Output

```text
2: wlo1: <BROADCAST,MULTICAST,UP,LOWER_UP>
```

### Real-World Use Case

Verify whether the network interface is up before troubleshooting higher layers.

---

# 2️⃣ Check Data Link Layer

## Command

```bash
ip neigh
```

### Purpose

Displays the ARP/neighbor table showing IP-to-MAC address mappings.

### Example

```text
192.168.1.1 dev wlo1 lladdr 50:5A:65:B8:91:1D REACHABLE
```

### Real-World Use Case

Verify that devices on the same LAN can resolve MAC addresses correctly.

---

# 3️⃣ Check Network Layer

## Display IP Address

```bash
ip addr show
```

Displays IPv4 and IPv6 addresses assigned to interfaces.

---

## Display Routing Table

```bash
ip route
```

Shows how packets are routed to different networks.

---

## Test Connectivity

```bash
ping google.com
```

Checks whether the destination is reachable.

---

# 4️⃣ Check Transport Layer

## Command

```bash
ss -tuln
```

### Purpose

Displays active TCP and UDP listening ports.

### Example

```text
LISTEN 0 128 0.0.0.0:22
```

### Real-World Use Case

Verify that an application is listening on the expected port.

---

# 5️⃣ Check DNS (Application Layer)

## Command

```bash
nslookup google.com
```

or

```bash
dig google.com
```

### Purpose

Tests DNS name resolution.

---

# 6️⃣ Check HTTP/HTTPS Connectivity

## Command

```bash
curl -I https://google.com
```

### Purpose

Sends an HTTP request and displays the response headers.

### Real-World Use Case

Useful for checking whether a web server is reachable.

---

# 7️⃣ Download a Web Page

## Command

```bash
wget https://example.com
```

### Purpose

Downloads content from a web server.

---

# 📋 Quick Troubleshooting Flow

```text
Physical
   │
ip link show
   │
Data Link
   │
ip neigh
   │
Network
   │
ip addr show
ip route
ping
   │
Transport
   │
ss -tuln
   │
Application
   │
curl
dig
nslookup
```

---

# 📌 Summary

These Linux commands map directly to different OSI layers and help troubleshoot networking issues systematically. This layer-by-layer approach is commonly used by Linux administrators, Network Engineers, and DevOps engineers.
