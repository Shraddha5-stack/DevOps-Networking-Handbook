# 🌐 Chapter 4 – Network Devices

![Networking](https://img.shields.io/badge/Topic-Network%20Devices-blue)
![Level](https://img.shields.io/badge/Level-Beginner%20to%20Advanced-green)
![DevOps](https://img.shields.io/badge/Focus-DevOps-orange)

---

# 📖 Overview

Network devices are hardware or software components that allow computers, servers, applications, and cloud resources to communicate with each other.

They perform important networking functions such as:

- Connecting devices
- Forwarding packets
- Routing traffic
- Securing communication
- Improving availability and performance

Understanding network devices is essential for:

- Linux Administrators
- Network Engineers
- Cloud Engineers
- DevOps Engineers
- Site Reliability Engineers (SRE)

---

# 🎯 Learning Objectives

After completing this chapter, you will understand:

- What network devices are.
- Why network devices are required.
- How different network devices work.
- Differences between common networking devices.
- Real-world usage in enterprise environments.
- Cloud and DevOps networking concepts.

---

# 📚 Topics Covered

| No. | Topic |
|---|---|
| 1 | Introduction to Network Devices |
| 2 | Hub |
| 3 | Switch |
| 4 | Router |
| 5 | Modem |
| 6 | Access Point |
| 7 | Repeater |
| 8 | Bridge |
| 9 | Gateway |
| 10 | Firewall |
| 11 | Load Balancer |
| 12 | Proxy Server |
| 13 | Network Interface Card (NIC) |
| 14 | Device Comparison |
| 15 | Real-World Examples |
| 16 | DevOps Perspective |
| 17 | Interview Questions |

---

# 📂 Chapter Structure

```
04-Network-Devices
│
├── README.md
├── notes.md
├── commands.md
├── practical-lab.md
├── interview-questions.md
├── real-world-usecases.md
├── troubleshooting.md
└── screenshots/
```

---

# 🖥️ Network Devices Covered

## 🔌 Hub

- Layer 1 device
- Broadcasts data to all connected devices

---

## 🔀 Switch

- Layer 2 device
- Uses MAC addresses
- Connects devices inside a LAN

---

## 🌐 Router

- Layer 3 device
- Uses IP addresses
- Connects different networks

---

## 🔥 Firewall

- Controls network traffic
- Protects systems from unauthorized access

---

## ⚖️ Load Balancer

- Distributes traffic across multiple servers
- Provides high availability

---

## 🛡️ Proxy Server

- Acts as an intermediary
- Provides security and traffic control

---

## 💻 NIC

- Enables network communication
- Provides MAC address identity

---

# ☁️ DevOps & Cloud Connection

Network devices are implemented as virtual services in cloud platforms.

Examples:

| Traditional Device | Cloud Equivalent |
|---|---|
| Firewall | AWS Security Group |
| Router | Virtual Router |
| Gateway | Internet Gateway |
| Load Balancer | AWS ALB/NLB |
| NIC | Elastic Network Interface |
| Proxy | Nginx Reverse Proxy |
| Bridge | Docker Bridge Network |

---

# 🛠️ Linux Networking Commands

Useful commands:

### Check Network Interfaces

```bash
ip link show
```

### Check IP Address

```bash
ip addr show
```

### Check Routing Table

```bash
ip route
```

### Test Connectivity

```bash
ping google.com
```

### Check Listening Ports

```bash
ss -tuln
```

---

# 🧪 Practical Labs

This chapter includes hands-on practice:

- Identifying network interfaces
- Understanding IP addresses
- Checking routing information
- Testing connectivity
- Exploring network services

---

# 🎤 Interview Preparation

Important interview topics:

- Hub vs Switch vs Router
- Router vs Gateway
- Firewall purpose
- Load Balancer working
- Forward Proxy vs Reverse Proxy
- Network devices in AWS
- Network troubleshooting commands

---

# 🔑 Key Takeaways

- Network devices enable communication between systems.
- Each device has a specific role.
- Switches use MAC addresses.
- Routers use IP addresses.
- Firewalls provide security.
- Load Balancers provide scalability.
- Cloud platforms use virtual networking devices.
- Networking knowledge is essential for DevOps engineers.

---

# 📚 Related Chapters

Previous:

⬅️ [Chapter 3 – Network Topologies](../03-Network-Topologies)

Next:

➡️ [Chapter 5 – OSI Model](../05-OSI-Model)

---

# 🚀 Author

**Shraddha Wankhade**

DevOps Networking Handbook Journey  
Learning • Practicing • Building 🚀
