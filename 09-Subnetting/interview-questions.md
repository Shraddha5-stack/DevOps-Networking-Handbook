# 🎤 Subnetting Interview Questions

This document contains commonly asked subnetting interview questions for Linux, Networking, Cloud, DevOps, and Site Reliability Engineer (SRE) roles.

---

# 1. What is subnetting?

**Answer:**

Subnetting is the process of dividing a large IP network into smaller logical networks called subnets. It improves network performance, security, and efficient IP address utilization.

---

# 2. Why is subnetting important?

**Answer:**

Subnetting helps to:

- Reduce broadcast traffic
- Improve network performance
- Increase security
- Utilize IP addresses efficiently
- Simplify network management

---

# 3. What is a subnet?

**Answer:**

A subnet is a smaller network created by dividing a larger network using a subnet mask or CIDR notation.

---

# 4. What is a subnet mask?

**Answer:**

A subnet mask separates the network portion and host portion of an IP address.

Example:

```text
255.255.255.0
```

Equivalent CIDR:

```text
/24
```

---

# 5. What is CIDR notation?

**Answer:**

CIDR (Classless Inter-Domain Routing) represents the number of network bits in an IP address.

Example:

```text
192.168.1.0/24
```

The `/24` means the first 24 bits are used for the network.

---

# 6. What is the Network ID?

**Answer:**

The Network ID identifies the subnet.

Example:

```text
IP Address: 192.168.1.25/24
Network ID: 192.168.1.0
```

---

# 7. What is the Host ID?

**Answer:**

The Host ID identifies a specific device within a subnet.

Example:

```text
IP Address: 192.168.1.25/24
Host ID: 25
```

---

# 8. What is the formula to calculate the number of subnets?

**Answer:**

```text
Number of Subnets = 2ⁿ
```

Where **n** is the number of borrowed host bits.

---

# 9. What is the formula to calculate usable hosts?

**Answer:**

```text
Usable Hosts = 2ʰ − 2
```

Where **h** is the number of host bits.

---

# 10. Why do we subtract 2?

**Answer:**

Two IP addresses are reserved:

- Network Address
- Broadcast Address

Therefore:

```text
Usable Hosts = Total Hosts − 2
```

---

# 11. What is FLSM?

**Answer:**

FLSM (Fixed Length Subnet Mask) uses the same subnet mask for all subnets.

### Advantages

- Easy to configure
- Simple to manage

### Disadvantages

- Wastes IP addresses

---

# 12. What is VLSM?

**Answer:**

VLSM (Variable Length Subnet Mask) allows different subnet sizes based on requirements.

### Advantages

- Better IP utilization
- Flexible design
- Commonly used in enterprise and cloud environments

---

# 13. What is the difference between FLSM and VLSM?

| FLSM | VLSM |
|------|------|
| Same subnet size | Different subnet sizes |
| Simple configuration | Flexible allocation |
| Wastes IP addresses | Efficient IP usage |
| Limited scalability | Highly scalable |

---

# 14. What is the difference between `/24` and `/26`?

| CIDR | Usable Hosts |
|------|-------------:|
| /24 | 254 |
| /26 | 62 |

A `/26` network is smaller and supports fewer hosts.

---

# 15. What command calculates subnet information?

**Answer:**

```bash
ipcalc 192.168.1.10/24
```

---

# 16. What command displays IP addresses?

**Answer:**

```bash
ip addr show
```

---

# 17. What command displays the routing table?

**Answer:**

```bash
ip route
```

---

# 18. What command displays the local IP address?

**Answer:**

```bash
hostname -I
```

---

# 19. How is subnetting used in AWS?

**Answer:**

Subnetting is used to divide a VPC into multiple subnets such as:

- Public Subnet
- Private Application Subnet
- Private Database Subnet

This improves security, scalability, and network organization.

---

# 20. Where is subnetting used in DevOps?

**Answer:**

Subnetting is commonly used in:

- AWS VPCs
- Azure VNets
- Google Cloud VPCs
- Kubernetes clusters
- Docker networking
- VPN design
- Enterprise LANs
- Firewall planning
- Load balancers

---

# 💡 Interview Tip

Interviewers often ask you to:

- Calculate the Network Address.
- Find the Broadcast Address.
- Determine the usable host range.
- Explain CIDR notation.
- Compare FLSM and VLSM.
- Design subnets for a cloud environment.

Practice subnet calculations manually and verify them using the `ipcalc` command.
