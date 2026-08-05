# 🎤 MAC Address Interview Questions

This document contains commonly asked MAC Address interview questions for Linux, Networking, Cloud, DevOps, and Site Reliability Engineer (SRE) roles.

---

# 1. What is a MAC Address?

### Answer

A **MAC (Media Access Control) Address** is a unique 48-bit hardware address assigned to a Network Interface Card (NIC). It operates at the **Data Link Layer (Layer 2)** of the OSI Model and uniquely identifies a device on a Local Area Network (LAN).

Example:

```text
3C:F7:5D:9D:6C:C0
```

---

# 2. What is the full form of MAC?

### Answer

**Media Access Control**

---

# 3. At which OSI layer does a MAC Address operate?

### Answer

MAC addresses operate at the **Data Link Layer (Layer 2)**.

---

# 4. What is the size of a MAC Address?

### Answer

A MAC Address is:

- 48 bits
- 6 Bytes
- Written as six hexadecimal pairs

Example:

```text
3C:F7:5D:9D:6C:C0
```

---

# 5. What are the two parts of a MAC Address?

### Answer

1. **OUI (Organizationally Unique Identifier)** – First 24 bits (manufacturer).
2. **Device Identifier** – Last 24 bits (unique device number).

---

# 6. What is the difference between a MAC Address and an IP Address?

| MAC Address | IP Address |
|-------------|------------|
| Physical address | Logical address |
| Layer 2 | Layer 3 |
| Usually permanent | Can change |
| Assigned by manufacturer | Assigned manually or by DHCP |
| Used within a LAN | Used across different networks |

---

# 7. What are the types of MAC Addresses?

### Answer

- **Unicast** – One sender to one receiver.
- **Multicast** – One sender to a selected group.
- **Broadcast** – One sender to all devices.

---

# 8. What is the Broadcast MAC Address?

### Answer

```text
FF:FF:FF:FF:FF:FF
```

Every device on the local network receives frames sent to this address.

---

# 9. What is MAC Address Spoofing?

### Answer

MAC Address Spoofing is changing the MAC address of a network interface through software.

Common uses:

- Privacy testing
- Network testing
- Security research

---

# 10. What is a CAM Table?

### Answer

A **CAM (Content Addressable Memory) Table** is maintained by a network switch. It stores MAC addresses and the switch ports where devices are connected, allowing efficient frame forwarding.

---

# 11. How does a switch learn MAC Addresses?

### Answer

When a frame enters a switch:

1. The switch reads the source MAC address.
2. It stores the MAC address with the incoming port in the CAM table.
3. Future frames are forwarded directly to the correct port.

---

# 12. Which command displays MAC Addresses in Linux?

### Answer

```bash
ip link show
```

or

```bash
ip addr show
```

---

# 13. Which command displays the ARP cache?

### Answer

```bash
arp -a
```

or

```bash
ip neigh
```

---

# 14. What is ARP?

### Answer

**ARP (Address Resolution Protocol)** maps an IP address to a MAC address within a Local Area Network (LAN).

Example:

```text
192.168.1.1 → 3C:F7:5D:9D:6C:C0
```

---

# 15. Why are MAC Addresses important?

### Answer

MAC addresses:

- Uniquely identify network interfaces.
- Enable communication within a LAN.
- Help switches forward frames.
- Work with ARP for IP-to-MAC mapping.

---

# 16. Can two devices have the same MAC Address?

### Answer

Normally, **No**. Manufacturers assign globally unique MAC addresses. However, duplicate MAC addresses can occur due to manual configuration or MAC spoofing, causing network issues.

---

# 17. How are MAC Addresses used in DevOps?

### Answer

MAC addresses are used in:

- Linux networking
- Docker bridge networks
- Kubernetes node networking
- Virtual machines
- VLAN configuration
- Network troubleshooting
- ARP debugging

---

# 18. Which devices use MAC Addresses?

### Answer

Devices with network interfaces, such as:

- Laptops
- Desktops
- Servers
- Routers
- Switches
- Printers
- Virtual Machines
- Containers

---

# 19. What happens if a switch does not know the destination MAC Address?

### Answer

The switch floods the frame to all ports (except the incoming port). Once the destination replies, the switch learns its MAC address and updates the CAM table.

---

# 20. How can you find your system's MAC Address?

### Answer

Use:

```bash
ip link show
```

or

```bash
ip addr show
```

Look for the `link/ether` field.

---

# 💡 Interview Tip

Interviewers often ask you to explain:

- MAC Address vs IP Address
- CAM Table
- ARP process
- Unicast, Multicast, and Broadcast MAC addresses
- MAC Address Spoofing
- How switches forward Ethernet frames

Understanding these concepts will also make **Chapter 11 – ARP** much easier.
