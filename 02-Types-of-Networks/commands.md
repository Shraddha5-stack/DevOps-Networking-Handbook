# 💻 Linux Networking Commands – Types of Networks

This section introduces useful Linux commands for identifying network interfaces, IP addresses, routing information, and network connectivity.

---

# 1️⃣ Display Network Interfaces

## Command

```bash
ip link show
```

### Purpose

Displays all available network interfaces on the system.

### Example Output

```text
2: wlo1: <BROADCAST,MULTICAST,UP,LOWER_UP>
```

### Explanation

- `wlo1` → Wireless network interface
- `UP` → Interface is active
- `LOWER_UP` → Physical connection is available

### Real-World Use Case

Used to identify active network interfaces before configuring a LAN connection.

### Interview Tip

**Q:** Which command displays network interfaces?

**A:** `ip link show`

---

# 2️⃣ Display IP Addresses

## Command

```bash
ip addr show
```

### Purpose

Displays IPv4 and IPv6 addresses assigned to network interfaces.

### Real-World Use Case

Useful for checking whether the system belongs to a LAN.

---

# 3️⃣ Display Routing Table

## Command

```bash
ip route
```

### Purpose

Shows how packets are routed to different networks.

### Real-World Use Case

Helps determine how your computer reaches other LANs or WANs.

---

# 4️⃣ Test Network Connectivity

## Command

```bash
ping google.com
```

### Purpose

Tests connectivity between your system and another host.

### Real-World Use Case

Checks whether the system has Internet (WAN) connectivity.

---

# 5️⃣ Display DNS Configuration

## Command

```bash
cat /etc/resolv.conf
```

### Purpose

Displays the configured DNS servers.

### Real-World Use Case

Useful when troubleshooting website access.

---

# 6️⃣ Display Listening Ports

## Command

```bash
ss -tuln
```

### Purpose

Shows active TCP and UDP listening ports.

### Real-World Use Case

Helps identify which network services are running.

---

# 📌 Summary

These commands help identify network interfaces, IP addresses, routing, DNS configuration, connectivity, and active network services—essential skills for Linux administrators and DevOps engineers.
