# 🧪 Subnetting Practical Lab

## 🎯 Objective

The objective of this lab is to understand subnetting by calculating network addresses, broadcast addresses, usable host ranges, and CIDR-based subnet information using Linux networking tools.

---

# 📋 Prerequisites

- Ubuntu/Linux system
- Internet connection
- Terminal access
- `ipcalc` installed
- Basic understanding of IP addressing

Verify that `ipcalc` is installed:

```bash
ipcalc --version
```

---

# 🧪 Lab 1 – View Network Interfaces

## Command

```bash
ip addr show
```

### Expected Result

Displays all network interfaces along with their assigned IPv4 and IPv6 addresses.

### Learning Outcome

Learn how to identify the IP address assigned to each network interface.

---

# 🧪 Lab 2 – View Local IP Address

## Command

```bash
hostname -I
```

### Expected Result

Displays the local IP address of the current machine.

### Learning Outcome

Quickly identify the system's IP address.

---

# 🧪 Lab 3 – View Routing Table

## Command

```bash
ip route
```

### Expected Result

Displays the routing table, including the default gateway.

### Learning Outcome

Understand how packets are routed to different networks.

---

# 🧪 Lab 4 – Calculate a /24 Network

## Command

```bash
ipcalc 192.168.1.10/24
```

### Observe

- Network Address
- Broadcast Address
- Subnet Mask
- Host Range

### Learning Outcome

Understand the structure of a /24 subnet.

---

# 🧪 Lab 5 – Calculate a /16 Network

## Command

```bash
ipcalc 10.0.0.0/16
```

### Observe

- Network Address
- Broadcast Address
- Number of Hosts

### Learning Outcome

Understand how larger networks support more hosts.

---

# 🧪 Lab 6 – Calculate a /28 Network

## Command

```bash
ipcalc 172.16.10.25/28
```

### Observe

- Network Address
- Broadcast Address
- First Host
- Last Host

### Learning Outcome

Understand small subnet allocation.

---

# 🧪 Lab 7 – Calculate a /26 Network

## Command

```bash
ipcalc 192.168.10.0/26
```

### Observe

- Network Address
- Broadcast Address
- Usable Host Range

### Learning Outcome

Learn how subnetting divides a larger network into smaller segments.

---

# 📊 Observation Table

| Lab | Command | Status |
|-----|---------|--------|
| 1 | `ip addr show` | ✅ Completed |
| 2 | `hostname -I` | ✅ Completed |
| 3 | `ip route` | ✅ Completed |
| 4 | `ipcalc 192.168.1.10/24` | ✅ Completed |
| 5 | `ipcalc 10.0.0.0/16` | ✅ Completed |
| 6 | `ipcalc 172.16.10.25/28` | ✅ Completed |
| 7 | `ipcalc 192.168.10.0/26` | ✅ Completed |

---

# 🌍 Real-World Scenario

A company has an AWS VPC with the CIDR block:

```text
10.0.0.0/16
```

The network team needs separate subnets for:

- Public Subnet
- Application Subnet
- Database Subnet

Using subnetting, they create:

```text
10.0.1.0/24
10.0.2.0/24
10.0.3.0/24
```

This improves network organization, security, and scalability.

---

# 💡 Key Learnings

- Subnetting divides large networks into smaller subnetworks.
- CIDR notation determines the network size.
- `ipcalc` simplifies subnet calculations.
- Proper subnet planning reduces IP address waste.
- Subnetting is widely used in AWS, Azure, GCP, Docker, and Kubernetes.

---

# ✅ Lab Summary

In this lab, you learned how to inspect IP configuration, view routing information, and calculate subnet details using `ipcalc`. These practical exercises strengthen your understanding of subnet masks, CIDR notation, host ranges, and network planning for real-world cloud and DevOps environments.
