# 🧪 MAC Address Practical Lab

## 🎯 Objective

The objective of this lab is to understand how MAC addresses work in Linux, how to identify them, how ARP maps IP addresses to MAC addresses, and how switches use MAC addresses for communication within a Local Area Network (LAN).

---

# 📋 Prerequisites

- Ubuntu/Linux system
- Terminal access
- Internet connection
- Basic understanding of OSI Model and TCP/IP Model

Verify your network connectivity:

```bash
ping -c 4 google.com
```

---

# 🧪 Lab 1 – View Network Interfaces

## Command

```bash
ip link show
```

### Expected Result

Displays all available network interfaces, their MAC addresses, MTU, and interface status.

### Learning Outcome

Learn how Linux stores MAC addresses for each network interface.

---

# 🧪 Lab 2 – View IP and MAC Addresses

## Command

```bash
ip addr show
```

### Expected Result

Displays:

- Interface name
- IPv4 address
- IPv6 address
- MAC address
- Interface state

### Learning Outcome

Understand how IP addresses and MAC addresses are associated with a network interface.

---

# 🧪 Lab 3 – View Neighbor (ARP) Table

## Command

```bash
ip neigh
```

### Expected Result

Displays IP-to-MAC address mappings for neighboring devices.

Example:

```text
192.168.1.1 dev wlo1 lladdr 3c:f7:5d:9d:6c:c0 REACHABLE
```

### Learning Outcome

Understand how Linux keeps track of neighboring devices.

---

# 🧪 Lab 4 – View ARP Cache

## Command

```bash
arp -a
```

### Expected Result

Displays cached ARP entries.

Example:

```text
_gateway (192.168.1.1) at 3c:f7:5d:9d:6c:c0 [ether] on wlo1
```

### Learning Outcome

Learn how IP addresses are mapped to MAC addresses using ARP.

---

# 🧪 Lab 5 – Display Hostname

## Command

```bash
hostname
```

### Expected Result

Displays the system hostname.

### Learning Outcome

Identify the Linux machine on the network.

---

# 🧪 Lab 6 – Display Local IP Address

## Command

```bash
hostname -I
```

### Expected Result

Displays the local IPv4 address assigned to the system.

### Learning Outcome

Identify the current IP address used by the machine.

---

# 🧪 Lab 7 – View Routing Table

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

Understand how packets leave the local network.

---

# 📊 Observation Table

| Lab | Command | Status |
|-----|---------|--------|
| 1 | `ip link show` | ✅ Completed |
| 2 | `ip addr show` | ✅ Completed |
| 3 | `ip neigh` | ✅ Completed |
| 4 | `arp -a` | ✅ Completed |
| 5 | `hostname` | ✅ Completed |
| 6 | `hostname -I` | ✅ Completed |
| 7 | `ip route` | ✅ Completed |

---

# 🌍 Real-World Scenario

A DevOps Engineer cannot connect to another server on the same network.

### Investigation

1. Check the interface status.

```bash
ip link show
```

2. Verify the IP address.

```bash
hostname -I
```

3. Check the ARP cache.

```bash
arp -a
```

4. Verify neighbor entries.

```bash
ip neigh
```

5. Confirm the routing table.

```bash
ip route
```

After identifying the correct MAC address and route, communication is restored.

---

# 💡 Key Learnings

- Every network interface has a unique MAC address.
- MAC addresses are used for communication within a LAN.
- ARP maps IP addresses to MAC addresses.
- Linux provides commands to inspect interfaces, neighbors, and routing information.
- Understanding MAC addresses is essential for troubleshooting Layer 2 network issues.

---

# ✅ Lab Summary

In this lab, you explored MAC addresses, ARP, neighbor tables, routing, and Linux networking commands. These practical exercises provide a solid foundation for understanding Layer 2 communication and prepare you for the next chapter on **ARP (Address Resolution Protocol)**.
