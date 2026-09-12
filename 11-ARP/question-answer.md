# 🎤 ARP Interview Questions

This document contains frequently asked ARP interview questions for Linux, Networking, Cloud, DevOps, Kubernetes, and Site Reliability Engineer (SRE) roles.

---

# 1. What is ARP?

### Answer

**ARP (Address Resolution Protocol)** is a network protocol used to map an **IPv4 address** to its corresponding **MAC address** within a Local Area Network (LAN).

Example:

```text
192.168.1.10
        ↓
      ARP
        ↓
08:00:27:AA:BB:CC
```

---

# 2. What is the full form of ARP?

### Answer

**Address Resolution Protocol**

---

# 3. Which OSI layer does ARP work on?

### Answer

ARP operates between the **Network Layer (Layer 3)** and the **Data Link Layer (Layer 2)**. It is commonly associated with **Layer 2** because it resolves MAC addresses for Ethernet communication.

---

# 4. Why is ARP required?

### Answer

Devices communicate using:

- **IP addresses** at Layer 3
- **MAC addresses** at Layer 2

ARP translates the destination IP address into a MAC address so Ethernet frames can be delivered correctly within a LAN.

---

# 5. How does ARP work?

### Answer

1. A device checks its ARP cache.
2. If no entry exists, it broadcasts an ARP Request.
3. The destination device replies with an ARP Reply containing its MAC address.
4. The sender stores the mapping in its ARP cache.
5. Communication begins using the resolved MAC address.

---

# 6. What is an ARP Request?

### Answer

An **ARP Request** is a **broadcast** message sent to all devices on the local network asking:

> "Who has this IP address?"

The destination MAC address of an ARP Request is:

```text
FF:FF:FF:FF:FF:FF
```

---

# 7. What is an ARP Reply?

### Answer

An **ARP Reply** is a **unicast** message sent directly to the requesting device.

It contains:

- Sender IP address
- Sender MAC address

---

# 8. What is an ARP Cache?

### Answer

The ARP cache is a temporary table that stores recently learned IP-to-MAC address mappings.

Linux commands:

```bash
arp -a
```

or

```bash
ip neigh
```

---

# 9. What is Gratuitous ARP?

### Answer

Gratuitous ARP is an unsolicited ARP message where a device announces its own IP-to-MAC mapping.

Uses:

- Detect duplicate IP addresses
- Update ARP caches
- Support High Availability (HA)

---

# 10. What is Proxy ARP?

### Answer

Proxy ARP allows a router to respond to ARP requests on behalf of another device located on a different network.

---

# 11. What is the difference between ARP and RARP?

| ARP | RARP |
|------|------|
| Resolves IP → MAC | Resolves MAC → IP |
| Commonly used | Mostly obsolete |
| Used in IPv4 networks | Replaced by BOOTP and DHCP |

---

# 12. What is ARP Spoofing?

### Answer

ARP Spoofing (ARP Poisoning) is an attack where an attacker sends fake ARP replies to redirect traffic through their system.

Possible impacts:

- Man-in-the-Middle (MITM)
- Data theft
- Session hijacking
- Traffic interception

---

# 13. How can ARP Spoofing be prevented?

### Answer

Common protection methods include:

- Dynamic ARP Inspection (DAI)
- Static ARP entries (where appropriate)
- Secure switch configuration
- Network monitoring and intrusion detection

---

# 14. Which Linux commands display ARP information?

### Answer

```bash
arp -a
```

```bash
ip neigh
```

---

# 15. What is stored in the ARP Cache?

### Answer

The ARP cache stores:

- IP Address
- MAC Address
- Interface
- Entry state (such as REACHABLE or STALE)

---

# 16. Does ARP work across the Internet?

### Answer

No.

ARP works only within the same **Local Area Network (LAN)** or broadcast domain.

Communication across different networks is handled by routers.

---

# 17. Why is ARP important in DevOps?

### Answer

ARP helps DevOps Engineers troubleshoot:

- Linux networking
- Docker bridge networks
- Kubernetes networking
- Virtual machine communication
- Layer 2 connectivity
- Hybrid cloud networking

---

# 18. What happens if the destination IP is not in the ARP cache?

### Answer

The sender broadcasts an ARP Request to discover the destination MAC address. After receiving the ARP Reply, the mapping is stored in the ARP cache for future use.

---

# 19. What command displays the neighbor table in Linux?

### Answer

```bash
ip neigh
```

---

# 20. What is the destination MAC address used in an ARP Request?

### Answer

```text
FF:FF:FF:FF:FF:FF
```

This is the Ethernet broadcast address, ensuring every device on the LAN receives the ARP Request.

---

# 💡 Interview Tip

Interviewers often ask you to explain the complete ARP process from memory.

A strong answer should include:

- Why ARP is needed
- ARP Request (Broadcast)
- ARP Reply (Unicast)
- ARP Cache
- Difference between ARP and RARP
- ARP Spoofing and prevention
- Linux commands: `arp -a` and `ip neigh`

Being able to explain the ARP workflow step by step demonstrates a solid understanding of Layer 2 networking.
