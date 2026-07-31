# 🌍 Real-World Use Cases – Types of Networks

## 📖 Introduction

Different types of networks are used in our daily lives, businesses, educational institutions, cloud platforms, and DevOps environments. Understanding where each network type is used helps bridge the gap between theory and practical implementation.

---

# 🏠 1. Home Network (LAN)

## Scenario

A family uses multiple devices connected to the same Wi-Fi router.

### Devices

- Laptop
- Smartphone
- Smart TV
- Printer

### Network Type

**LAN (Local Area Network)**

### Why?

All devices are connected within a small geographical area and can share Internet access and files.

---

# 🏢 2. Office Network (LAN)

## Scenario

Employees in an office connect to shared resources.

### Devices

- Desktop Computers
- Servers
- Network Printers
- IP Phones

### Network Type

**LAN**

### Benefits

- Fast communication
- File sharing
- Printer sharing
- Centralized management

---

# 🏫 3. University Campus (CAN/LAN)

## Scenario

Different departments are connected through a common network.

### Example

- Administration Building
- Library
- Computer Labs
- Hostels

### Network Type

- Campus Area Network (CAN)
- Multiple LANs connected together

---

# 🌆 4. Bank Branches Across a City (MAN)

## Scenario

A bank has several branches in the same city.

### Network Type

**MAN (Metropolitan Area Network)**

### Benefits

- Centralized database
- Secure communication
- Fast branch connectivity

---

# 🌍 5. Global Company (WAN)

## Scenario

A multinational company has offices in different countries.

### Network Type

**WAN (Wide Area Network)**

### Benefits

- Connects offices worldwide
- Enables remote collaboration
- Supports centralized services

---

# 📱 6. Bluetooth Devices (PAN)

## Scenario

A smartphone is connected to wireless earbuds.

### Network Type

**PAN (Personal Area Network)**

### Benefits

- Short-range communication
- Low power consumption
- Easy device pairing

---

# ☁️ 7. Cloud Computing (WAN + LAN)

## Scenario

A user accesses an application hosted on AWS.

### Network Types Used

- LAN inside AWS data centers
- WAN (Internet) between users and AWS

### Why It Matters

Cloud services rely on both local and wide-area networks for communication.

---

# 🐳 8. Docker Networking

## Scenario

Multiple Docker containers communicate within the same application.

### Network Type

Virtual LAN (Bridge Network)

### Example

- Web Container
- Database Container
- API Container

All containers communicate over Docker's virtual network.

---

# ☸️ 9. Kubernetes Networking

## Scenario

Pods communicate with each other inside a Kubernetes cluster.

### Network Type

Cluster Network

### Benefits

- Pod-to-Pod communication
- Service discovery
- High availability

---

# 🚀 10. DevOps CI/CD Pipeline

## Scenario

A developer pushes code to GitHub.

```text
Developer
      │
      ▼
GitHub
      │
      ▼
GitHub Actions
      │
      ▼
Docker
      │
      ▼
Kubernetes
      │
      ▼
AWS
```

### Where Networking Is Used

- Git push to GitHub
- CI/CD pipeline communication
- Docker image transfer
- Kubernetes deployment
- Cloud infrastructure access

Networking enables every stage of the deployment process.

---

# 🎯 Key Takeaways

- LAN is commonly used in homes and offices.
- MAN connects locations across a city.
- WAN connects networks across countries and continents.
- PAN is used for personal devices.
- Modern DevOps tools such as Docker, Kubernetes, GitHub, and AWS rely heavily on networking for communication and automation.
