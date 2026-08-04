# 🌐 Subnetting

## 📑 Table of Contents

1. Introduction
2. What is Subnetting?
3. Why Do We Need Subnetting?
4. Network ID
5. Host ID
6. Subnet Mask
7. CIDR Notation
8. Default Subnet Masks
9. Borrowing Host Bits
10. Number of Subnets Formula
11. Number of Hosts Formula
12. Subnetting Example
13. FLSM (Fixed Length Subnet Mask)
14. VLSM (Variable Length Subnet Mask)
15. Public vs Private Subnets
16. AWS VPC Subnetting
17. DevOps Perspective
18. Key Takeaways
19. Summary
20. Interview Tip

---

# 📖 Introduction

Subnetting is the process of dividing a large IP network into smaller, manageable networks called **subnets**. Instead of using one large network for every device, subnetting creates multiple smaller networks that improve performance, security, and IP address utilization.

Subnetting is one of the most important concepts in computer networking. It is widely used in enterprise networks, cloud platforms such as AWS, Azure, and Google Cloud, as well as Docker, Kubernetes, and modern DevOps infrastructures.

Understanding subnetting helps engineers design scalable, secure, and efficient networks while reducing unnecessary broadcast traffic.

---

# 🌐 What is Subnetting?

Subnetting is the technique of splitting a network into multiple smaller subnetworks.

Instead of:

```text
192.168.1.0/24
```

you can divide it into smaller networks such as:

```text
192.168.1.0/26
192.168.1.64/26
192.168.1.128/26
192.168.1.192/26
```

Each subnet has its own:

- Network Address
- Broadcast Address
- Usable Host Range

---

# ❓ Why Do We Need Subnetting?

Subnetting provides several advantages:

- Better IP address utilization
- Reduced broadcast traffic
- Improved network performance
- Increased security
- Easier troubleshooting
- Better traffic management
- Scalable network design

---

# 🏠 Network ID

The **Network ID** identifies the subnet.

Example:

```text
192.168.10.25/24
```

Network ID:

```text
192.168.10.0
```

All devices in the same subnet share the same Network ID.

---

# 💻 Host ID

The **Host ID** identifies a specific device within a subnet.

Example:

```text
192.168.10.25/24
```

Host ID:

```text
25
```

Each host must have a unique Host ID.

---

# 🎭 Subnet Mask

A subnet mask separates the network portion from the host portion of an IP address.

Example:

```text
255.255.255.0
```

Equivalent CIDR:

```text
/24
```

Common subnet masks:

| CIDR | Subnet Mask |
|------|-------------|
| /8 | 255.0.0.0 |
| /16 | 255.255.0.0 |
| /24 | 255.255.255.0 |
| /25 | 255.255.255.128 |
| /26 | 255.255.255.192 |
| /27 | 255.255.255.224 |
| /28 | 255.255.255.240 |
| /29 | 255.255.255.248 |
| /30 | 255.255.255.252 |

---

# 📏 CIDR Notation

CIDR (Classless Inter-Domain Routing) represents the number of network bits.

Example:

```text
192.168.1.0/24
```

Here:

- 24 bits = Network
- 8 bits = Host

CIDR allows flexible subnet sizes and efficient IP allocation.

---

# 🏷️ Default Subnet Masks

| Class | Default Mask | CIDR |
|------|---------------|------|
| A | 255.0.0.0 | /8 |
| B | 255.255.0.0 | /16 |
| C | 255.255.255.0 | /24 |

---

# 🔄 Borrowing Host Bits

Subnetting works by borrowing bits from the host portion.

Example:

```text
/24 → /26
```

Borrowed bits:

```text
2 bits
```

This creates:

- 4 subnets
- 62 usable hosts per subnet

---

# 🧮 Number of Subnets Formula

```text
Number of Subnets = 2^n
```

Where:

- **n** = borrowed bits

Example:

Borrow 3 bits:

```text
2³ = 8 subnets
```

---

# 🧮 Number of Hosts Formula

```text
Hosts = 2^h − 2
```

Where:

- **h** = host bits

Example:

```text
/26
```

Host bits:

```text
6
```

Hosts:

```text
2⁶ − 2 = 62
```

---

# 📊 Subnetting Example

Network:

```text
192.168.1.0/24
```

Divide into four `/26` subnets:

| Subnet | Host Range | Broadcast |
|--------|------------|-----------|
| 192.168.1.0/26 | 1–62 | 192.168.1.63 |
| 192.168.1.64/26 | 65–126 | 192.168.1.127 |
| 192.168.1.128/26 | 129–190 | 192.168.1.191 |
| 192.168.1.192/26 | 193–254 | 192.168.1.255 |

---

# 🌍 FLSM (Fixed Length Subnet Mask)

FLSM uses the **same subnet mask** for all subnets.

### Advantages

- Simple design
- Easy management

### Disadvantages

- Wastes IP addresses

---

# 🌐 VLSM (Variable Length Subnet Mask)

VLSM allows **different subnet sizes** based on requirements.

### Advantages

- Efficient IP usage
- Flexible network design

### Example

- HR: /26
- Finance: /27
- IT: /28

---

# ☁️ Public vs Private Subnets

### Public Subnet

- Has Internet access
- Uses an Internet Gateway
- Hosts web servers and load balancers

### Private Subnet

- No direct Internet access
- Uses NAT Gateway for outbound traffic
- Hosts databases and application servers

---

# ☁️ AWS VPC Subnetting

Example VPC:

```text
10.0.0.0/16
```

Subnets:

```text
10.0.1.0/24
10.0.2.0/24
10.0.3.0/24
```

Typical design:

- Public Subnet
- Private Application Subnet
- Private Database Subnet

---

# 💼 DevOps Perspective

Subnetting is used daily in:

- AWS VPCs
- Azure VNets
- Google Cloud VPC
- Kubernetes Networking
- Docker Networks
- VPN Configuration
- Routing
- Firewalls
- Security Groups
- Enterprise Data Centers

Understanding subnetting helps build scalable and secure cloud infrastructure.

---

# 📌 Key Takeaways

- Subnetting divides large networks into smaller networks.
- CIDR notation defines network size.
- Network ID identifies the subnet.
- Host ID identifies the device.
- VLSM is more efficient than FLSM.
- Subnetting is essential for cloud and DevOps.

---

# 📝 Summary

Subnetting improves network efficiency, security, and scalability by dividing large networks into smaller subnets. Mastering subnet masks, CIDR notation, host calculations, and subnet design is an essential skill for Linux, Cloud, Networking, and DevOps professionals.

---

# 💼 Interview Tip

Be prepared to explain:

- CIDR notation
- Network ID vs Host ID
- FLSM vs VLSM
- Number of hosts in a subnet
- Public vs Private Subnets
- AWS VPC subnet design

Practice calculating subnet ranges manually as well as using the `ipcalc` command.
