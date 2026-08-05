# 🌐 Chapter 10 – MAC Address

## 📖 Overview

A **MAC (Media Access Control) Address** is a unique hardware identifier assigned to a network interface card (NIC). It operates at the **Data Link Layer (Layer 2)** of the OSI Model and is used for communication between devices on the same local network.

Unlike IP addresses, which can change depending on the network, MAC addresses are generally permanent and uniquely identify a network interface. Switches use MAC addresses to forward Ethernet frames efficiently within a Local Area Network (LAN).

Understanding MAC addresses is essential for Network Engineers, Linux Administrators, Cloud Engineers, DevOps Engineers, and Site Reliability Engineers (SREs). It also forms the foundation for learning ARP (Address Resolution Protocol), switching, VLANs, and network troubleshooting.

---

## 📑 Contents

- 📘 notes.md
- 💻 commands.md
- 🧪 practical-lab.md
- 🎤 interview-questions.md
- 🌍 real-world-usecases.md
- 🛠️ troubleshooting.md
- 📸 screenshots/

---

## 🎯 Learning Objectives

After completing this chapter, you will understand:

- What is a MAC Address?
- Why MAC Addresses are Needed
- MAC Address Format
- Structure of a MAC Address
- Types of MAC Addresses
- Unicast, Multicast, and Broadcast MAC Addresses
- MAC Address vs IP Address
- How Switches Learn MAC Addresses
- CAM (MAC Address) Table
- MAC Address Spoofing
- Finding MAC Addresses in Linux
- DevOps Networking Use Cases

---

## ☁️ DevOps Relevance

MAC addresses are important in:

- Ethernet communication
- Linux server networking
- ARP (Address Resolution Protocol)
- Layer 2 Switching
- VLAN configuration
- Docker bridge networking
- Kubernetes node networking
- Virtual machine networking
- Network troubleshooting
- Enterprise LAN design

---

## 📚 Prerequisites

Before studying this chapter, you should understand:

- Networking Fundamentals
- OSI Model
- TCP/IP Model
- TCP vs UDP
- IP Addressing
- Subnetting

---

## 📂 Repository Structure

```text
10-MAC-Address
├── README.md
├── commands.md
├── interview-questions.md
├── notes.md
├── practical-lab.md
├── real-world-usecases.md
├── screenshots
│   ├── 01-ip-link-show.png
│   ├── 02-ip-addr-show.png
│   ├── 03-ip-neigh.png
│   ├── 04-arp-a.png
│   ├── 05-hostname.png
│   ├── 06-hostname-ip.png
│   └── 07-ip-route.png
└── troubleshooting.md
```

---

## 🚀 Chapter Status

- [ ] Notes
- [ ] Commands
- [ ] Practical Lab
- [ ] Interview Questions
- [ ] Real-World Use Cases
- [ ] Troubleshooting
- [ ] Screenshots
