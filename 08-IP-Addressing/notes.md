# 🌐 IP Addressing

## 📑 Table of Contents

1. Introduction
2. What is an IP Address?
3. Why Do We Need IP Addresses?
4. IPv4 Address
5. IPv6 Address
6. Structure of an IPv4 Address
7. Public vs Private IP Address
8. Static vs Dynamic IP Address
9. Loopback Address
10. APIPA Address
11. Network ID and Host ID
12. CIDR Notation
13. IPv4 Address Classes
14. Reserved IP Addresses
15. IPv4 vs IPv6
16. Real-World Examples
17. DevOps Perspective
18. Key Takeaways
19. Summary
20. Interview Tip

---

# 📖 Introduction

An Internet Protocol (IP) Address is a unique numerical identifier assigned to every device connected to a network. It enables devices such as computers, servers, smartphones, routers, printers, and IoT devices to communicate with each other.

Whenever data is transmitted over a network or the Internet, the source and destination devices are identified using IP addresses. Without IP addresses, devices would not know where to send or receive data.

IP addressing is one of the core concepts in computer networking and is widely used in Linux administration, cloud computing, DevOps, Docker, Kubernetes, and enterprise networking.

---

# 🌐 What is an IP Address?

An IP Address (Internet Protocol Address) is a logical address assigned to a network interface.

Its main purposes are:

- Identifying a device on a network
- Locating the destination device
- Enabling communication between devices
- Supporting packet routing across networks

### Example IPv4 Address

```text
192.168.1.10
```

### Example IPv6 Address

```text
2001:db8:85a3::8a2e:370:7334
```

---

# ❓ Why Do We Need IP Addresses?

IP addresses allow devices to communicate correctly across local networks and the Internet.

Without IP addresses:

- Computers cannot locate each other.
- Routers cannot forward packets.
- Websites cannot be reached.
- Cloud services cannot communicate.
- SSH and APIs would not work.

---

# 🌍 IPv4 Address

IPv4 (Internet Protocol Version 4) is the most widely used IP addressing scheme.

### Features

- 32-bit address
- Four octets
- Decimal format
- Approximately 4.3 billion addresses

### Example

```text
192.168.1.25
```

---

# 🌐 IPv6 Address

IPv6 was introduced to overcome IPv4 address exhaustion.

### Features

- 128-bit address
- Hexadecimal format
- Nearly unlimited address space
- Better routing efficiency
- Built-in support for IPsec

### Example

```text
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

---

# 🧩 Structure of an IPv4 Address

An IPv4 address consists of four octets separated by dots.

Example:

```text
192.168.1.25
```

| Octet | Value |
|-------|------:|
| First | 192 |
| Second | 168 |
| Third | 1 |
| Fourth | 25 |

Each octet ranges from **0 to 255**.

---

# 🌍 Public vs Private IP Address

## Public IP

A public IP address is assigned by an Internet Service Provider (ISP) and is reachable over the Internet.

Example:

```text
49.36.150.25
```

## Private IP

A private IP address is used within internal networks and is not directly accessible from the Internet.

Private IP ranges:

- 10.0.0.0/8
- 172.16.0.0 – 172.31.255.255
- 192.168.0.0/16

---

# 🔄 Static vs Dynamic IP Address

## Static IP

- Manually configured
- Does not change
- Used for servers, databases, and network devices

## Dynamic IP

- Assigned automatically by DHCP
- Can change over time
- Commonly used for end-user devices

---

# 🔁 Loopback Address

The loopback address is used to test the local network stack.

IPv4 Loopback:

```text
127.0.0.1
```

Hostname:

```text
localhost
```

---

# 📡 APIPA Address

APIPA stands for **Automatic Private IP Addressing**.

If a device cannot obtain an IP address from a DHCP server, it automatically assigns itself an address in the range:

```text
169.254.0.0/16
```

---

# 🏠 Network ID and Host ID

Every IPv4 address has two parts:

- **Network ID** – Identifies the network.
- **Host ID** – Identifies the device within that network.

Example:

```text
192.168.1.25/24
```

- Network ID: **192.168.1.0**
- Host ID: **25**

---

# 📏 CIDR Notation

CIDR (Classless Inter-Domain Routing) specifies the network prefix.

Common examples:

| CIDR | Subnet Mask |
|------|-------------|
| /8 | 255.0.0.0 |
| /16 | 255.255.0.0 |
| /24 | 255.255.255.0 |
| /32 | 255.255.255.255 |

---

# 🏷️ IPv4 Address Classes

| Class | Range | Default Mask |
|------|----------------|----------------|
| A | 1.0.0.0 – 126.255.255.255 | 255.0.0.0 |
| B | 128.0.0.0 – 191.255.255.255 | 255.255.0.0 |
| C | 192.0.0.0 – 223.255.255.255 | 255.255.255.0 |
| D | 224.0.0.0 – 239.255.255.255 | Multicast |
| E | 240.0.0.0 – 255.255.255.255 | Experimental |

---

# 🚫 Reserved IP Addresses

| Address | Purpose |
|----------|---------|
| 127.0.0.1 | Loopback |
| 0.0.0.0 | Default Route |
| 255.255.255.255 | Broadcast |
| 169.254.x.x | APIPA |

---

# ⚖️ IPv4 vs IPv6

| Feature | IPv4 | IPv6 |
|---------|------|------|
| Address Size | 32-bit | 128-bit |
| Format | Decimal | Hexadecimal |
| Address Space | ~4.3 Billion | Extremely Large |
| NAT Required | Often | Usually No |
| Header | Simpler | Improved |

---

# 🌍 Real-World Examples

- Home Wi-Fi networks use private IP addresses.
- Public websites use public IP addresses.
- AWS EC2 instances can have private and public IPs.
- Docker containers receive private IP addresses on bridge networks.
- Kubernetes assigns IP addresses to Pods and Services.

---

# ☁️ DevOps Perspective

DevOps Engineers work with IP addressing daily while:

- Connecting to Linux servers using SSH
- Configuring AWS VPCs
- Managing Docker bridge networks
- Deploying Kubernetes clusters
- Configuring Load Balancers
- Troubleshooting DNS and routing issues

A solid understanding of IP addressing is essential for designing and maintaining reliable cloud infrastructure.

---

# 📌 Key Takeaways

- Every device on a network requires an IP address.
- IPv4 is still widely used, while IPv6 is the future.
- Public and private IP addresses serve different purposes.
- CIDR notation defines network size.
- Network ID identifies the network; Host ID identifies the device.

---

# 📝 Summary

IP addressing enables communication between devices across local and global networks. Understanding IPv4, IPv6, private and public addresses, CIDR notation, and network identification is a fundamental skill for Network Engineers, Linux Administrators, Cloud Engineers, and DevOps professionals.

---

# 💼 Interview Tip

Interviewers often ask you to:

- Explain the difference between public and private IP addresses.
- Describe CIDR notation.
- Identify the network ID and host ID from an IP address.
- Compare IPv4 and IPv6.
- Explain why IPv6 was introduced.
