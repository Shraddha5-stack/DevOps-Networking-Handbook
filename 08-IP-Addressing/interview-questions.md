# 🎤 IP Addressing Interview Questions

This document contains commonly asked interview questions on IP Addressing for Linux, Networking, Cloud, DevOps, and SRE roles.

---

# 1. What is an IP address?

**Answer:**

An IP (Internet Protocol) address is a unique logical address assigned to a device connected to a network. It allows devices to identify and communicate with each other.

---

# 2. Why is an IP address required?

**Answer:**

IP addresses are required to:

- Identify devices
- Locate destination systems
- Route network packets
- Enable communication across networks

---

# 3. What is IPv4?

**Answer:**

IPv4 (Internet Protocol Version 4) is a 32-bit addressing scheme that uses four decimal octets separated by dots.

Example:

```text
192.168.1.10
```

It supports approximately **4.3 billion unique addresses**.

---

# 4. What is IPv6?

**Answer:**

IPv6 is the latest version of the Internet Protocol. It uses 128-bit addresses and provides a much larger address space than IPv4.

Example:

```text
2001:db8::1
```

---

# 5. What is the difference between IPv4 and IPv6?

| IPv4 | IPv6 |
|------|------|
| 32-bit | 128-bit |
| Decimal format | Hexadecimal format |
| Limited address space | Very large address space |
| Uses NAT frequently | NAT is generally not required |
| Example: 192.168.1.10 | Example: 2001:db8::1 |

---

# 6. What is a public IP address?

**Answer:**

A public IP address is assigned by an Internet Service Provider (ISP) and is reachable over the Internet.

Example:

```text
49.36.150.25
```

---

# 7. What is a private IP address?

**Answer:**

A private IP address is used inside local networks and is not directly accessible from the Internet.

Private IP ranges:

- 10.0.0.0/8
- 172.16.0.0 – 172.31.255.255
- 192.168.0.0/16

---

# 8. What is a static IP address?

**Answer:**

A static IP address is manually assigned and does not change unless it is reconfigured.

Common uses:

- Web servers
- Database servers
- DNS servers
- Network devices

---

# 9. What is a dynamic IP address?

**Answer:**

A dynamic IP address is assigned automatically by a DHCP server and may change over time.

---

# 10. What is DHCP?

**Answer:**

DHCP (Dynamic Host Configuration Protocol) automatically assigns IP addresses, subnet masks, gateways, and DNS settings to devices on a network.

---

# 11. What is the loopback address?

**Answer:**

The loopback address is:

```text
127.0.0.1
```

It is used to test the local network stack and is commonly referred to as **localhost**.

---

# 12. What is APIPA?

**Answer:**

APIPA (Automatic Private IP Addressing) assigns an IP address automatically when a DHCP server is unavailable.

Range:

```text
169.254.0.0/16
```

---

# 13. What is CIDR notation?

**Answer:**

CIDR (Classless Inter-Domain Routing) is a method of representing IP addresses and their network prefixes.

Example:

```text
192.168.1.0/24
```

The `/24` indicates that the first 24 bits represent the network.

---

# 14. What is the difference between Network ID and Host ID?

**Answer:**

- **Network ID** identifies the network.
- **Host ID** identifies a specific device within that network.

Example:

```text
192.168.1.25/24
```

- Network ID → `192.168.1.0`
- Host ID → `25`

---

# 15. What command displays all IP addresses?

**Answer:**

```bash
ip addr show
```

---

# 16. What command displays only the local IP address?

**Answer:**

```bash
hostname -I
```

---

# 17. What command displays the routing table?

**Answer:**

```bash
ip route
```

---

# 18. What command displays your public IP address?

**Answer:**

```bash
curl ifconfig.me
```

---

# 19. What command calculates subnet information?

**Answer:**

```bash
ipcalc 192.168.1.10/24
```

---

# 20. What are the IPv4 address classes?

**Answer:**

| Class | Range | Default Mask |
|------|----------------|----------------|
| A | 1.0.0.0 – 126.255.255.255 | 255.0.0.0 |
| B | 128.0.0.0 – 191.255.255.255 | 255.255.0.0 |
| C | 192.0.0.0 – 223.255.255.255 | 255.255.255.0 |
| D | 224.0.0.0 – 239.255.255.255 | Multicast |
| E | 240.0.0.0 – 255.255.255.255 | Experimental |

---

# 21. What is the difference between public and private IP addresses?

**Answer:**

Public IP addresses are globally routable over the Internet, while private IP addresses are used only within local networks and require NAT to communicate with the Internet.

---

# 22. Why is IPv6 needed?

**Answer:**

IPv6 was introduced because IPv4 addresses are limited. IPv6 provides a much larger address space and improves routing efficiency and scalability.

---

# 23. Where is IP addressing used in DevOps?

**Answer:**

- Linux server administration
- AWS VPCs
- Azure Virtual Networks
- Google Cloud VPC
- Docker bridge networks
- Kubernetes Pods and Services
- Load Balancers
- Firewalls
- VPNs
- API communication

---

# 24. What is NAT?

**Answer:**

NAT (Network Address Translation) allows multiple private IP addresses to share a single public IP address for Internet access.

---

# 25. Explain IP addressing in simple terms.

**Answer:**

An IP address is like the postal address of a house. Just as a courier uses your address to deliver a package, devices on a network use IP addresses to send and receive data correctly.

---

# 💡 Interview Tip

Be ready to explain:

- IPv4 vs IPv6
- Public vs Private IP
- Static vs Dynamic IP
- CIDR notation
- Network ID and Host ID
- NAT and DHCP

Whenever possible, support your answers with Linux commands such as `ip addr`, `hostname -I`, `ip route`, and `ipcalc`.
