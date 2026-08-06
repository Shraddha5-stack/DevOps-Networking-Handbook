# 🌐 Chapter 11 – Address Resolution Protocol (ARP)

## 📖 Overview

**Address Resolution Protocol (ARP)** is a Layer 2 networking protocol used to map an **IPv4 address** to its corresponding **MAC (Media Access Control) address** within a Local Area Network (LAN).

Whenever a device wants to communicate with another device on the same network, it first needs the destination's MAC address. If only the IP address is known, ARP sends a request asking, **"Who has this IP address?"** The device with that IP replies with its MAC address, allowing communication to proceed.

ARP acts as the bridge between **Layer 3 (IP Addressing)** and **Layer 2 (MAC Addressing)**, making local network communication possible.

Understanding ARP is essential for Linux Administrators, Network Engineers, Cloud Engineers, DevOps Engineers, Kubernetes Administrators, and Site Reliability Engineers (SREs), as it plays a critical role in network troubleshooting and connectivity.

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

- What is ARP?
- Why ARP is Needed
- How ARP Works
- ARP Request and ARP Reply
- ARP Cache (Neighbor Table)
- Types of ARP
- Gratuitous ARP
- Proxy ARP
- ARP vs RARP
- ARP Spoofing (ARP Poisoning)
- Linux Commands for ARP
- ARP in DevOps and Cloud Networking

---

## ☁️ DevOps Relevance

ARP is important in:

- Linux server networking
- Layer 2 communication
- Docker bridge networking
- Kubernetes networking
- Virtual machine networking
- Enterprise LANs
- Cloud networking
- Network troubleshooting
- Security analysis
- Switch and router communication

---

## 📚 Prerequisites

Before studying this chapter, you should understand:

- Networking Fundamentals
- OSI Model
- TCP/IP Model
- TCP vs UDP
- IP Addressing
- Subnetting
- MAC Address

---

## 📂 Repository Structure

```text
11-ARP
├── README.md
├── commands.md
├── interview-questions.md
├── notes.md
├── practical-lab.md
├── real-world-usecases.md
├── screenshots
│   ├── 01-arp-a.png
│   ├── 02-ip-neigh.png
│   ├── 03-ip-addr-show.png
│   ├── 04-ip-link-show.png
│   ├── 05-ping-gateway.png
│   ├── 06-ping-google.png
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
- [x] Screenshots
