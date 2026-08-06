# 🌐 Address Resolution Protocol (ARP)

## 📑 Table of Contents

1. Introduction
2. What is ARP?
3. Why Do We Need ARP?
4. How ARP Works
5. ARP Request
6. ARP Reply
7. ARP Cache (Neighbor Table)
8. Types of ARP
9. Gratuitous ARP
10. Proxy ARP
11. ARP vs RARP
12. ARP Spoofing (ARP Poisoning)
13. Finding ARP Entries in Linux
14. DevOps Perspective
15. Key Takeaways
16. Summary
17. Interview Tip

---

# 📖 Introduction

Computers communicate using **IP addresses** at Layer 3 and **MAC addresses** at Layer 2 of the OSI Model.

When a device wants to send data to another device on the same Local Area Network (LAN), it usually knows the destination's IP address but **does not know its MAC address**.

This is where **Address Resolution Protocol (ARP)** comes into play.

ARP translates an **IPv4 address** into its corresponding **MAC address**, allowing Ethernet frames to reach the correct destination.

Without ARP, devices on the same LAN would not be able to communicate.

---

# 🌐 What is ARP?

**Address Resolution Protocol (ARP)** is a Layer 2 protocol that maps an IPv4 address to a MAC address.

Example:

```text
IP Address:
192.168.1.10

↓

ARP

↓

MAC Address:
08:00:27:AA:BB:CC
```

ARP works only within the **same local network (broadcast domain)**.

---

# ❓ Why Do We Need ARP?

Applications communicate using IP addresses.

Network interfaces send Ethernet frames using MAC addresses.

ARP connects these two addressing systems.

Without ARP:

- Devices cannot discover destination MAC addresses.
- Ethernet frames cannot be delivered correctly.
- Communication inside a LAN fails.

---

# ⚙️ How ARP Works

Suppose:

```text
Laptop A
IP : 192.168.1.10

↓

Wants to communicate with

↓

Laptop B
IP : 192.168.1.20
```

Laptop A knows the IP address but not the MAC address.

### Step 1

Laptop A checks its ARP cache.

If an entry exists, it uses the stored MAC address.

If not, it sends an ARP Request.

### Step 2

ARP Request is broadcast to every device.

```text
Who has 192.168.1.20?
Tell 192.168.1.10
```

### Step 3

Laptop B recognizes its IP address.

It sends an ARP Reply.

```text
192.168.1.20 is at
08:00:27:AA:BB:CC
```

### Step 4

Laptop A stores the mapping in its ARP cache.

Future communication uses the cached MAC address without another broadcast.

---

# 📢 ARP Request

Characteristics:

- Broadcast frame
- Destination MAC:

```text
FF:FF:FF:FF:FF:FF
```

- Every device receives it.
- Only the owner of the requested IP replies.

---

# 📩 ARP Reply

Characteristics:

- Unicast frame
- Sent only to the requesting device.
- Contains the sender's MAC address.

Example:

```text
IP:
192.168.1.20

↓

MAC:
08:00:27:AA:BB:CC
```

---

# 🗂️ ARP Cache (Neighbor Table)

Linux stores recently learned IP-to-MAC mappings.

View using:

```bash
arp -a
```

or

```bash
ip neigh
```

Example:

```text
192.168.1.1 dev wlo1 lladdr 3c:f7:5d:9d:6c:c0 REACHABLE
```

Benefits:

- Reduces network broadcasts
- Faster communication
- Improves network performance

---

# 🌍 Types of ARP

## 1. Normal ARP

Maps IPv4 addresses to MAC addresses.

---

## 2. Gratuitous ARP

A device announces its own IP-to-MAC mapping without being asked.

Uses:

- Detect duplicate IP addresses
- Update ARP caches
- High Availability (HA)

---

## 3. Proxy ARP

A router answers ARP requests on behalf of another device.

Useful for:

- Network segmentation
- Legacy network compatibility

---

# ⚖️ ARP vs RARP

| ARP | RARP |
|------|------|
| IP → MAC | MAC → IP |
| Commonly used | Mostly obsolete |
| Used by IPv4 | Replaced by BOOTP/DHCP |

---

# ⚠️ ARP Spoofing (ARP Poisoning)

ARP Spoofing is a cyberattack where an attacker sends fake ARP replies.

Example:

```text
Victim

↓

Believes attacker's MAC belongs to gateway

↓

Traffic is redirected

↓

Attacker intercepts data
```

Risks:

- Man-in-the-Middle (MITM)
- Data theft
- Session hijacking
- Traffic interception

Protection:

- Dynamic ARP Inspection (DAI)
- Static ARP entries (where appropriate)
- Secure switch configurations
- Network monitoring

---

# 🐧 Finding ARP Entries in Linux

Useful commands:

```bash
arp -a
```

```bash
ip neigh
```

```bash
ip addr show
```

```bash
ip link show
```

---

# ☁️ DevOps Perspective

ARP is important for:

- Linux networking
- Docker bridge networks
- Kubernetes networking
- Virtual machines
- VMware
- Hyper-V
- AWS hybrid networking
- Layer 2 troubleshooting

Although cloud providers abstract much of the underlying Layer 2 networking, understanding ARP is valuable when troubleshooting on-premises infrastructure, hybrid environments, and container networking.

---

# 📌 Key Takeaways

- ARP maps IPv4 addresses to MAC addresses.
- ARP works only inside a Local Area Network.
- ARP Requests are broadcast.
- ARP Replies are unicast.
- Linux stores mappings in the ARP cache.
- ARP reduces repeated broadcasts by caching entries.
- ARP Spoofing is a common Layer 2 security attack.

---

# 📝 Summary

Address Resolution Protocol (ARP) enables communication within a Local Area Network by translating IPv4 addresses into MAC addresses. It acts as the bridge between Layer 3 and Layer 2, allowing Ethernet frames to reach the correct destination. ARP is fundamental to Linux networking, enterprise networks, cloud infrastructure, and DevOps troubleshooting.

---

# 💼 Interview Tip

Be prepared to answer:

- What is ARP?
- Why is ARP required?
- Difference between ARP Request and ARP Reply.
- Difference between ARP and RARP.
- What is Gratuitous ARP?
- What is Proxy ARP?
- What is ARP Spoofing?
- Which Linux commands display the ARP cache?
