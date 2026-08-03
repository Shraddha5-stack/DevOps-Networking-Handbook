# 🧪 IP Addressing Practical Lab

## 🎯 Objective

The objective of this lab is to understand IP addressing concepts and practice using Linux commands to inspect network interfaces, routing information, public and private IP addresses, and subnet calculations.

---

# 📋 Prerequisites

- Ubuntu/Linux system
- Internet connection
- Terminal access
- `iproute2` package
- `curl`
- `ipcalc`
- Basic knowledge of TCP/IP networking

Verify the required tools:

```bash
ip -V
curl --version
ipcalc --version
```

---

# 🧪 Lab 1 – Display Network Interfaces

## Command

```bash
ip addr show
```

### Expected Result

Displays all available network interfaces along with their IPv4 and IPv6 addresses.

### Learning Outcome

Understand how Linux assigns IP addresses to network interfaces.

---

# 🧪 Lab 2 – Display Local IP Address

## Command

```bash
hostname -I
```

### Expected Result

Displays the IP address(es) assigned to the local machine.

### Learning Outcome

Learn how to quickly identify the server's IP address.

---

# 🧪 Lab 3 – Display Routing Table

## Command

```bash
ip route
```

### Expected Result

Displays the default gateway and routing information.

### Learning Outcome

Understand how packets are routed to other networks.

---

# 🧪 Lab 4 – Display Public IP Address

## Command

```bash
curl ifconfig.me
```

### Expected Result

Displays the public IP address assigned by your ISP.

### Learning Outcome

Understand the difference between private and public IP addresses.

---

# 🧪 Lab 5 – Test Connectivity Using an IP Address

## Command

```bash
ping -c 4 8.8.8.8
```

### Expected Result

Four successful replies from Google's public DNS server.

### Learning Outcome

Verify Internet connectivity without relying on DNS.

---

# 🧪 Lab 6 – Test Connectivity Using a Domain Name

## Command

```bash
ping -c 4 google.com
```

### Expected Result

Four successful replies from `google.com`.

### Learning Outcome

Verify both Internet connectivity and DNS name resolution.

---

# 🧪 Lab 7 – Calculate Network Information

## Command

```bash
ipcalc 192.168.1.10/24
```

### Expected Result

Displays:

- Network Address
- Broadcast Address
- Subnet Mask
- CIDR Prefix
- Number of Hosts

### Learning Outcome

Understand subnet calculations and CIDR notation.

---

# 📊 Observation Table

| Lab | Command | Status |
|------|---------|--------|
| 1 | `ip addr show` | ✅ Completed |
| 2 | `hostname -I` | ✅ Completed |
| 3 | `ip route` | ✅ Completed |
| 4 | `curl ifconfig.me` | ✅ Completed |
| 5 | `ping -c 4 8.8.8.8` | ✅ Completed |
| 6 | `ping -c 4 google.com` | ✅ Completed |
| 7 | `ipcalc 192.168.1.10/24` | ✅ Completed |

---

# 🌍 Real-World Scenario

A DevOps engineer deploys a web application to a cloud server, but users cannot access it.

### Troubleshooting Steps

1. Check the server's IP address.

```bash
hostname -I
```

2. Verify the routing table.

```bash
ip route
```

3. Test Internet connectivity.

```bash
ping -c 4 8.8.8.8
```

4. Verify DNS resolution.

```bash
ping -c 4 google.com
```

5. Confirm the public IP address.

```bash
curl ifconfig.me
```

These steps help determine whether the issue is related to network configuration, routing, or DNS.

---

# 💡 Key Learnings

- Every network device requires an IP address.
- Linux provides powerful tools to inspect IP configuration.
- Routing tables determine packet paths.
- Public and private IP addresses have different purposes.
- CIDR notation simplifies subnet management.
- These commands are essential for Linux, AWS, Docker, Kubernetes, and DevOps troubleshooting.

---

# ✅ Lab Summary

In this practical lab, you learned how to inspect IP addresses, view routing information, identify public and private IPs, test connectivity, verify DNS resolution, and calculate subnet information. These are fundamental networking skills required for Linux administration, cloud computing, and DevOps engineering.
