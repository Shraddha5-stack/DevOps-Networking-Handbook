# 💼 Networking Fundamentals - Interview Questions

This section contains commonly asked networking interview questions, ranging from beginner to advanced level.

---

# 🟢 Beginner Level

## 1. What is computer networking?

### Answer

Computer networking is the process of connecting two or more devices so they can communicate and exchange data using networking protocols such as TCP/IP.

---

## 2. Why is networking important?

### Answer

Networking allows devices to communicate, share resources, access the internet, and exchange data efficiently. It is the foundation of modern applications, cloud computing, and DevOps.

---

## 3. What is a computer network?

### Answer

A computer network is a collection of connected devices that communicate with each other to share data and resources.

---

## 4. Name some devices used in networking.

### Answer

- Computer
- Server
- Router
- Switch
- Modem
- Firewall
- Access Point

---

## 5. What are the main goals of networking?

### Answer

- Communication
- Resource Sharing
- Reliability
- Scalability
- Security
- Remote Access

---

# 🟡 Intermediate Level

## 6. What is the difference between a client and a server?

### Answer

A client sends requests for services or resources, while a server receives those requests and provides the required services or data.

**Example:**

- Browser → Client
- Web Server → Server

---

## 7. What is the difference between Client-Server and Peer-to-Peer architecture?

### Answer

| Client-Server | Peer-to-Peer |
|---------------|--------------|
| Centralized server | No central server |
| Better security | Less secure |
| Easy management | Difficult management |
| Used by websites | Used in small networks |

---

## 8. What are networking protocols?

### Answer

Networking protocols are a set of rules that define how devices communicate over a network.

Examples:

- HTTP
- HTTPS
- FTP
- SSH
- DNS
- DHCP
- TCP
- UDP

---

## 9. What is bandwidth?

### Answer

Bandwidth is the maximum amount of data that can be transmitted over a network in one second.

---

## 10. What is latency?

### Answer

Latency is the time taken for data to travel from the sender to the receiver.

Lower latency means faster communication.

---

# 🟠 Advanced Level

## 11. How does data travel from your browser to a website?

### Answer

The process generally follows these steps:

1. User enters a URL.
2. Browser sends a DNS request.
3. DNS resolves the domain name to an IP address.
4. Browser establishes a TCP connection.
5. HTTP/HTTPS request is sent.
6. Server processes the request.
7. Server sends a response.
8. Browser displays the webpage.

---

## 12. Why is networking important for DevOps?

### Answer

Networking enables communication between:

- Linux servers
- Docker containers
- Kubernetes pods
- Cloud services
- CI/CD pipelines
- Monitoring tools

Without networking, DevOps tools cannot communicate effectively.

---

## 13. What are some common networking metrics?

### Answer

- Bandwidth
- Latency
- Throughput
- Jitter
- Packet Loss

---

## 14. What is packet loss?

### Answer

Packet loss occurs when one or more data packets fail to reach their destination, resulting in slower or interrupted communication.

---

## 15. Which Linux commands are commonly used for networking?

### Answer

- `ip addr show`
- `ip link show`
- `ip route`
- `ping`
- `ss -tuln`
- `hostname`
- `cat /etc/resolv.conf`

---

# 🔴 Scenario-Based Questions

## 16. You cannot access a website. What will you check first?

### Answer

- Check internet connectivity using `ping`.
- Verify the IP address using `ip addr show`.
- Check the routing table using `ip route`.
- Verify DNS configuration using `cat /etc/resolv.conf`.
- Ensure the destination server is reachable.

---

## 17. A server is unreachable. How would you troubleshoot it?

### Answer

1. Check network connectivity.
2. Verify the server IP address.
3. Check routing information.
4. Test DNS resolution.
5. Verify firewall rules.
6. Check if required services are running.

---

## 18. Which networking knowledge is important for a DevOps Engineer?

### Answer

A DevOps Engineer should understand:

- OSI Model
- TCP/IP Model
- DNS
- DHCP
- Routing
- Switching
- Linux Networking
- Docker Networking
- Kubernetes Networking
- AWS Networking
- Network Troubleshooting

---

# ⭐ Quick Revision

Remember these key points:

- Networking connects devices.
- Protocols define communication rules.
- Clients send requests.
- Servers provide services.
- DNS converts domain names into IP addresses.
- TCP provides reliable communication.
- UDP provides faster communication.
- Every cloud platform depends on networking.

---

# 🎯 Interview Tip

> If an interviewer asks **"What is networking?"**, don't stop at the definition. Explain **why networking is needed**, give **one real-world example**, and mention **how DevOps tools such as Docker, Kubernetes, and AWS rely on networking**. This demonstrates practical understanding rather than memorization.
