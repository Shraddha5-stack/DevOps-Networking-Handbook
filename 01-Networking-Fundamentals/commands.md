# 💻 Networking Fundamentals - Commands

## 📑 Table of Contents

1. Check IP Address
2. Check Network Interfaces
3. Display Routing Table
4. Test Connectivity
5. Check DNS Resolution
6. View Active Network Connections
7. Display Hostname
8. Check Public IP Address
9. Command Summary

---

# 1️⃣ Check IP Address

## Command

```bash
ip addr show
```

### Purpose

Displays all network interfaces along with their IP addresses.

---

# 2️⃣ Check Network Interfaces

## Command

```bash
ip link show
```

### Purpose

Lists all available network interfaces and their current status.

---

# 3️⃣ Display Routing Table

## Command

```bash
ip route
```

### Purpose

Shows how packets are routed from your computer to other networks.

---

# 4️⃣ Test Connectivity

## Command

```bash
ping google.com
```

### Purpose

Checks whether your system can communicate with another host.

---

# 5️⃣ Check DNS Resolution

## Command

```bash
nslookup google.com
```

or

```bash
dig google.com
```

### Purpose

Resolves a domain name into its IP address.

---

# 6️⃣ View Active Network Connections

## Command

```bash
ss -tuln
```

### Purpose

Displays listening ports and active network connections.

---

# 7️⃣ Display Hostname

## Command

```bash
hostname
```

### Purpose

Shows the hostname of the current machine.

---

# 8️⃣ Check Public IP Address

## Command

```bash
curl ifconfig.me
```

### Purpose

Displays the public IP address assigned by your Internet Service Provider (ISP).

---

# 📋 Command Summary

| Command | Description |
|---------|-------------|
| `ip addr show` | Display IP addresses |
| `ip link show` | Display network interfaces |
| `ip route` | Show routing table |
| `ping google.com` | Test network connectivity |
| `nslookup google.com` | DNS lookup |
| `dig google.com` | Advanced DNS lookup |
| `ss -tuln` | View active connections |
| `hostname` | Display system hostname |
| `curl ifconfig.me` | Show public IP address |


# 1️⃣ Check IP Address

## Command

```bash
ip addr show
```

### Purpose

Displays all available network interfaces along with their IP addresses and network configuration.

### Syntax

```bash
ip addr show
```

### Example Output

```text
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP>
    inet 192.168.1.15/24 brd 192.168.1.255 scope global dynamic enp0s3
```

### Explanation

- **enp0s3** → Network interface name
- **inet** → IPv4 address
- **192.168.1.15** → Assigned IP address
- **/24** → Subnet mask (CIDR notation)
- **brd** → Broadcast address

### Real-World Use Case

A DevOps engineer uses this command to verify the server's IP address before configuring SSH access, Docker containers, Kubernetes nodes, or cloud networking.

### Interview Tip

**Q:** Which Linux command is commonly used to display the IP address of a system?

**A:** `ip addr show`

### Key Points

- Shows both IPv4 and IPv6 addresses.
- Displays all network interfaces.
- Useful for troubleshooting network connectivity.
- Replaces the older `ifconfig` command on most modern Linux distributions.
