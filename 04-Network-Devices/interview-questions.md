# 🎤 Interview Questions – Network Devices

This section contains important networking interview questions for Linux, Cloud, and DevOps roles.

---

# 1. What are network devices?

### Answer:

Network devices are hardware or software components that allow communication between computers, servers, and networks.

They perform functions like:

- Connecting devices
- Forwarding data
- Routing traffic
- Securing communication

Examples:

- Switch
- Router
- Firewall
- Load Balancer
- Gateway
- NIC

---

# 2. What is the difference between Hub and Switch?

### Answer:

| Hub | Switch |
|---|---|
| Works at Layer 1 | Works at Layer 2 |
| Broadcasts data to all devices | Sends data to the specific device |
| Uses no MAC address table | Uses MAC address table |
| Less secure | More efficient |

---

# 3. What is the difference between Switch and Router?

### Answer:

| Switch | Router |
|---|---|
| Works at Layer 2 | Works at Layer 3 |
| Uses MAC addresses | Uses IP addresses |
| Connects devices in a LAN | Connects different networks |
| Example: Office LAN | Example: Internet connection |

---

# 4. Why do we need a Router?

### Answer:

A router connects multiple networks and forwards packets based on IP addresses.

Examples:

- Connecting office network to Internet
- Connecting different cloud networks

---

# 5. What is the purpose of a Firewall?

### Answer:

A firewall controls incoming and outgoing traffic based on security rules.

It provides:

- Network protection
- Access control
- Traffic filtering

Examples:

- AWS Security Group
- Linux Firewall

---

# 6. What is a Load Balancer?

### Answer:

A Load Balancer distributes incoming traffic across multiple servers.

Benefits:

- High availability
- Scalability
- Better performance

Example:

```
Users
 |
Load Balancer
 |
---------------
|      |      |
Server Server Server
```

---

# 7. Difference between Forward Proxy and Reverse Proxy?

### Answer:

| Forward Proxy | Reverse Proxy |
|---|---|
| Works for clients | Works for servers |
| Hides client identity | Hides backend servers |
| Controls Internet access | Manages application traffic |

---

# 8. What is a Gateway?

### Answer:

A Gateway connects different networks that use different protocols.

Example:

- Internet Gateway
- VPN Gateway

---

# 9. What is NIC?

### Answer:

NIC (Network Interface Card) is a hardware component that allows a device to connect to a network.

Functions:

- Sends and receives data
- Provides MAC address
- Enables network communication

---

# 10. What is a MAC address?

### Answer:

A MAC address is a unique hardware address assigned to a network interface.

Example:

```
50:5A:65:B8:91:1D
```

It works at:

```
Layer 2 - Data Link Layer
```

---

# 11. How do you check network interfaces in Linux?

### Answer:

Command:

```bash
ip link show
```

---

# 12. How do you check IP address in Linux?

### Answer:

Command:

```bash
ip addr show
```

---

# 13. How do you check routing information?

### Answer:

Command:

```bash
ip route
```

---

# 14. How do you troubleshoot network connectivity?

### Answer:

Steps:

1. Check interface:

```bash
ip link show
```

2. Check IP:

```bash
ip addr show
```

3. Check route:

```bash
ip route
```

4. Test connectivity:

```bash
ping google.com
```

5. Check ports:

```bash
ss -tuln
```

---

# 15. How are network devices used in AWS?

### Answer:

AWS provides virtual networking services:

| Device | AWS Service |
|---|---|
| Firewall | Security Group |
| Gateway | Internet Gateway |
| Load Balancer | ALB/NLB |
| NIC | Elastic Network Interface |

---

# 16. How does Kubernetes handle networking?

### Answer:

Kubernetes uses:

- Services
- Ingress Controllers
- CNI plugins

Architecture:

```
User
 |
Ingress
 |
Service
 |
Pods
```

---

# 17. Scenario Question

## Application is running but users cannot access it. What will you check?

### Answer:

I will check:

1. Server network interface:

```bash
ip addr show
```

2. Application port:

```bash
ss -tuln
```

3. Firewall rules.

4. Routing:

```bash
ip route
```

5. Connectivity:

```bash
ping server-ip
```

---

# ⭐ Interview Tip

Do not only define network devices.

Explain:

- What it does
- Why we need it
- Which OSI layer it works on
- Real-world DevOps usage

```
Understand the purpose, not only the definition.
```
