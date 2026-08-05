# 🌐 MAC Address

## 📑 Table of Contents

1. Introduction
2. What is a MAC Address?
3. Why Do We Need a MAC Address?
4. MAC Address Format
5. Structure of a MAC Address
6. Types of MAC Addresses
7. Unicast, Multicast & Broadcast MAC Addresses
8. MAC Address vs IP Address
9. How MAC Addresses Work
10. MAC Address Table (CAM Table)
11. MAC Address Learning
12. MAC Address Spoofing
13. Finding MAC Addresses in Linux
14. DevOps Perspective
15. Key Takeaways
16. Summary
17. Interview Tip

---

# 📖 Introduction

Every device connected to a network has a unique hardware identifier known as a **MAC (Media Access Control) Address**. It operates at the **Data Link Layer (Layer 2)** of the OSI Model and enables communication between devices on the same Local Area Network (LAN).

When your computer communicates with another device on the same network, data is delivered using MAC addresses. Even though IP addresses identify devices across networks, actual frame delivery within a LAN depends on MAC addresses.

MAC addresses are used by switches to forward Ethernet frames, making them one of the most fundamental concepts in networking.

---

# 🌐 What is a MAC Address?

A **MAC Address** is a unique 48-bit hardware address assigned to a network interface card (NIC) by the manufacturer.

It is also known as:

- Physical Address
- Hardware Address
- Ethernet Address
- Burned-In Address (BIA)

Example:

```text
3c:f7:5d:9d:6c:c0
```

Each network interface has its own MAC address.

---

# ❓ Why Do We Need a MAC Address?

MAC addresses are required because devices on the same network communicate using Layer 2 addresses.

They help:

- Identify devices uniquely
- Deliver Ethernet frames
- Enable switch forwarding
- Support ARP communication
- Prevent data from reaching the wrong device

Without MAC addresses, local network communication would not function correctly.

---

# 🔤 MAC Address Format

A MAC address consists of **48 bits (6 bytes)**.

Example:

```text
3C:F7:5D:9D:6C:C0
```

It is written as six groups of two hexadecimal digits separated by colons or hyphens.

Example formats:

```text
3C:F7:5D:9D:6C:C0
```

```text
3C-F7-5D-9D-6C-C0
```

---

# 🧩 Structure of a MAC Address

A MAC address has two parts:

### Organizationally Unique Identifier (OUI)

- First 24 bits
- Identifies the manufacturer

### Device Identifier

- Last 24 bits
- Unique identifier assigned by the manufacturer

Example:

```text
3C:F7:5D : 9D:6C:C0
```

- `3C:F7:5D` → Manufacturer
- `9D:6C:C0` → Device Identifier

---

# 🌍 Types of MAC Addresses

## 1. Unicast MAC Address

Used for communication between one sender and one receiver.

Example:

```text
3C:F7:5D:9D:6C:C0
```

---

## 2. Multicast MAC Address

Used to send data to a specific group of devices.

Example:

```text
01:00:5E:00:00:01
```

---

## 3. Broadcast MAC Address

Sent to every device on the local network.

Example:

```text
FF:FF:FF:FF:FF:FF
```

---

# 📡 Unicast, Multicast & Broadcast

| Type | Destination |
|-------|-------------|
| Unicast | One device |
| Multicast | Selected group |
| Broadcast | All devices |

---

# ⚖️ MAC Address vs IP Address

| MAC Address | IP Address |
|-------------|------------|
| Layer 2 | Layer 3 |
| Physical Address | Logical Address |
| Usually permanent | Can change |
| Used inside LAN | Used across networks |
| Assigned by manufacturer | Assigned manually or by DHCP |

---

# ⚙️ How MAC Addresses Work

Suppose Laptop A wants to send data to Laptop B on the same network.

1. Laptop A knows Laptop B's IP address.
2. ARP is used to discover Laptop B's MAC address.
3. Laptop A creates an Ethernet frame.
4. The frame contains Laptop B's MAC address.
5. The switch forwards the frame using its MAC Address Table.
6. Laptop B receives the frame.

---

# 🗂️ MAC Address Table (CAM Table)

A switch maintains a **Content Addressable Memory (CAM) Table** that stores MAC addresses and the switch ports where devices are connected.

Example:

| MAC Address | Port |
|-------------|------|
| 3C:F7:5D:9D:6C:C0 | Fa0/1 |
| 08:00:27:AA:BB:CC | Fa0/2 |

This allows switches to forward frames efficiently.

---

# 📚 MAC Address Learning

Switches automatically learn MAC addresses.

Process:

1. Frame arrives on a port.
2. Switch records the source MAC address.
3. The MAC address is mapped to that port.
4. Future frames are forwarded directly.

This process reduces unnecessary network traffic.

---

# ⚠️ MAC Address Spoofing

MAC spoofing is the process of changing a device's MAC address through software.

Common uses:

- Privacy testing
- Network testing
- Security research

Risks:

- Unauthorized access
- Bypassing MAC filters
- Identity impersonation

Network administrators often use security features such as **Port Security** to prevent unauthorized MAC address changes.

---

# 🐧 Finding MAC Addresses in Linux

Useful commands:

```bash
ip link show
```

```bash
ip addr show
```

```bash
ip neigh
```

```bash
arp -a
```

These commands display MAC addresses, neighbors, and interface details.

---

# ☁️ DevOps Perspective

MAC addresses are important in:

- Linux networking
- Docker bridge networks
- Kubernetes node networking
- Virtual machines
- VLAN configuration
- Layer 2 switching
- ARP troubleshooting
- Enterprise LANs

Although cloud providers often abstract Layer 2 networking, understanding MAC addresses is essential for troubleshooting hybrid and on-premises environments.

---

# 📌 Key Takeaways

- MAC addresses uniquely identify network interfaces.
- MAC addresses operate at Layer 2.
- Switches forward frames using MAC addresses.
- ARP maps IP addresses to MAC addresses.
- Every network interface has its own MAC address.
- Broadcast MAC address is `FF:FF:FF:FF:FF:FF`.

---

# 📝 Summary

A MAC address is a unique hardware identifier used for communication within a Local Area Network. It enables switches to deliver Ethernet frames efficiently and works together with ARP to map IP addresses to physical devices. Understanding MAC addresses is fundamental for networking, cloud computing, Linux administration, and DevOps.

---

# 💼 Interview Tip

Be prepared to answer:

- What is a MAC address?
- Difference between MAC and IP address.
- How switches learn MAC addresses.
- What is a CAM table?
- What is ARP?
- What is MAC spoofing?
- Difference between unicast, multicast, and broadcast MAC addresses.
