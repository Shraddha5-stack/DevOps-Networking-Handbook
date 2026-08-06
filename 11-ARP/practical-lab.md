# 🧪 ARP Practical Lab

## 🎯 Objective

The objective of this lab is to understand how the Address Resolution Protocol (ARP) works, how Linux maintains the ARP cache, and how IP addresses are mapped to MAC addresses for communication within a Local Area Network (LAN).

---

# 📋 Prerequisites

- Ubuntu/Linux system
- Terminal access
- Active network connection
- Basic knowledge of IP Addressing and MAC Addresses

Verify network connectivity:

```bash
ping -c 4 google.com
```

---

# 🧪 Lab 1 – View the ARP Cache

## Command

```bash
arp -a
```

### Expected Result

Displays the ARP cache containing IP-to-MAC address mappings.

Example:

```text
_gateway (192.168.1.1) at 3c:f7:5d:9d:6c:c0 [ether] on wlo1
```

### Learning Outcome

Understand how Linux stores recently learned IP-to-MAC mappings.

---

# 🧪 Lab 2 – View the Neighbor Table

## Command

```bash
ip neigh
```

### Expected Result

Displays neighboring devices with their MAC addresses and entry states.

Example:

```text
192.168.1.1 dev wlo1 lladdr 3c:f7:5d:9d:6c:c0 REACHABLE
```

### Learning Outcome

Learn how Linux tracks neighboring devices on the local network.

---

# 🧪 Lab 3 – View IP and MAC Address Information

## Command

```bash
ip addr show
```

### Expected Result

Displays:

- Network interfaces
- IPv4 addresses
- IPv6 addresses
- MAC addresses
- Interface state

### Learning Outcome

See how IP addresses and MAC addresses are associated with the same interface.

---

# 🧪 Lab 4 – View Network Interfaces

## Command

```bash
ip link show
```

### Expected Result

Displays network interfaces with their MAC addresses and operational status.

### Learning Outcome

Identify interface names and verify their MAC addresses.

---

# 🧪 Lab 5 – Test Connectivity to the Default Gateway

## Command

```bash
ping -c 4 192.168.1.1
```

### Expected Result

Successful replies from the gateway.

### Learning Outcome

Observe that communicating with the gateway creates or refreshes ARP entries.

---

# 🧪 Lab 6 – Test Internet Connectivity

## Command

```bash
ping -c 4 google.com
```

### Expected Result

Successful replies confirming internet and DNS connectivity.

### Learning Outcome

Verify external connectivity after successful local network communication.

---

# 🧪 Lab 7 – View the Routing Table

## Command

```bash
ip route
```

### Expected Result

Displays:

- Default gateway
- Local routes
- Network routes

### Learning Outcome

Understand how packets are routed after ARP resolves the destination MAC address.

---

# 📊 Observation Table

| Lab | Command | Status |
|-----|---------|--------|
| 1 | `arp -a` | ✅ Completed |
| 2 | `ip neigh` | ✅ Completed |
| 3 | `ip addr show` | ✅ Completed |
| 4 | `ip link show` | ✅ Completed |
| 5 | `ping -c 4 192.168.1.1` | ✅ Completed |
| 6 | `ping -c 4 google.com` | ✅ Completed |
| 7 | `ip route` | ✅ Completed |

---

# 🌍 Real-World Scenario

## Scenario

A Linux server cannot communicate with another device on the same subnet.

### Investigation Steps

1. Verify interface status.

```bash
ip link show
```

2. Check the assigned IP address.

```bash
ip addr show
```

3. View the ARP cache.

```bash
arp -a
```

4. Inspect the neighbor table.

```bash
ip neigh
```

5. Test connectivity to the gateway.

```bash
ping -c 4 192.168.1.1
```

6. Verify the routing table.

```bash
ip route
```

### Result

After confirming the ARP entry and route, communication is restored.

---

# 💡 Key Learnings

- ARP maps IPv4 addresses to MAC addresses.
- ARP works only within a Local Area Network (LAN).
- Linux stores ARP entries in the neighbor table.
- Successful communication updates the ARP cache.
- ARP is essential for Ethernet communication.

---

# 📝 Lab Summary

In this lab, you explored how Linux resolves IP addresses to MAC addresses using ARP, viewed ARP cache entries, inspected the neighbor table, verified interface information, tested connectivity, and examined the routing table. These practical exercises strengthen your understanding of Layer 2 communication and prepare you for troubleshooting real-world networking issues.
