# 🌐 TCP vs UDP

## 📑 Table of Contents

1. Introduction
2. What is TCP?
3. What is UDP?
4. Why Do We Need TCP and UDP?
5. Features of TCP
6. Features of UDP
7. TCP Three-Way Handshake
8. TCP Connection Termination
9. TCP vs UDP Comparison
10. Common Port Numbers
11. Real-World Examples
12. DevOps Perspective
13. Key Takeaways
14. Summary
15. Interview Tip

---

# 📖 Introduction

The Transport Layer of the TCP/IP Model is responsible for end-to-end communication between applications running on different devices. The two major protocols used at this layer are Transmission Control Protocol (TCP) and User Datagram Protocol (UDP).

Although both protocols are used to transmit data across networks, they are designed for different purposes. TCP focuses on reliability, ordered delivery, and error recovery, while UDP focuses on speed, simplicity, and low latency.

Every time you browse a website, transfer files, stream a video, play an online game, use DNS, or communicate with cloud services, either TCP or UDP is working behind the scenes.

Understanding the differences between TCP and UDP is essential for Linux Administrators, Network Engineers, Cloud Engineers, DevOps Engineers, Kubernetes Administrators, and Site Reliability Engineers (SREs). Choosing the correct protocol directly affects application performance, reliability, and scalability.

---

# 🌐 What is TCP?

**Transmission Control Protocol (TCP)** is a connection-oriented transport layer protocol that provides reliable communication between two devices.

Before any data is transmitted, TCP establishes a connection using a process called the **Three-Way Handshake**. Once the connection is established, TCP ensures that all packets are delivered successfully, in the correct order, and without duplication.

### Key Characteristics

- Connection-oriented
- Reliable communication
- Ordered packet delivery
- Error detection and recovery
- Flow control
- Congestion control

### Common TCP Applications

- HTTP
- HTTPS
- SSH
- FTP
- SMTP
- MySQL
- PostgreSQL

### Advantages

- Guaranteed delivery
- Error recovery
- Ordered transmission
- High reliability

### Disadvantages

- Higher overhead
- Slower than UDP
- More bandwidth usage

---

# ⚡ What is UDP?

**User Datagram Protocol (UDP)** is a connectionless transport layer protocol designed for fast data transmission.

Unlike TCP, UDP does not establish a connection before sending data. It simply sends packets (datagrams) without waiting for acknowledgements. This makes UDP significantly faster but less reliable.

UDP is ideal for applications where speed is more important than guaranteed delivery.

### Key Characteristics

- Connectionless
- Lightweight
- Low latency
- No acknowledgements
- No retransmissions
- No packet ordering

### Common UDP Applications

- DNS
- DHCP
- VoIP
- Online Gaming
- Video Streaming
- Live Broadcasting
- SNMP

### Advantages

- Very fast
- Low overhead
- Minimal delay
- Suitable for real-time communication

### Disadvantages

- No guaranteed delivery
- No ordering
- No retransmission
- Possible packet loss

---

# ❓ Why Do We Need TCP and UDP?

Different applications have different networking requirements.

TCP is chosen when **reliability and data integrity** are critical, while UDP is preferred when **speed and low latency** are more important.

### Use TCP When

- Downloading files
- Online banking
- Web browsing (HTTP/HTTPS)
- Email services
- Remote server access (SSH)

### Use UDP When

- Video conferencing
- Online gaming
- Live streaming
- Voice calls (VoIP)
- DNS lookups

---

# ✅ Features of TCP

- Connection-oriented communication
- Three-Way Handshake
- Reliable delivery
- Packet sequencing
- Error checking
- Flow control
- Congestion control
- Automatic retransmission
- Acknowledgement mechanism


## TCP Header Fields

The TCP header contains several important fields that enable reliable communication.

- Source Port
- Destination Port
- Sequence Number
- Acknowledgement Number
- Data Offset
- Flags (SYN, ACK, FIN, RST, PSH, URG)
- Window Size
- Checksum
- Urgent Pointer


---

# ⚡ Features of UDP

- Connectionless communication
- Faster transmission
- No acknowledgements
- No retransmission
- Lower overhead
- No congestion control
- Suitable for real-time applications


## UDP Header Fields

The UDP header is much smaller than the TCP header and contains only four fields:

- Source Port
- Destination Port
- Length
- Checksum

The UDP header is only **8 bytes**, making it lightweight and fast.


---

# 🤝 TCP Three-Way Handshake

Before transmitting data, TCP establishes a connection using three steps:


```text
Client                     Server

SYN  --------------------->

      <-------------------  SYN + ACK

ACK  --------------------->
```


### Step 1 – SYN
The client sends a SYN packet to request a connection.

### Step 2 – SYNACK

The server acknowledges the request and responds with a SYN-ACK packet.

### Step 3 – ACK

The client sends an ACK packet, completing the connection.

After this process, data transfer begins.

---

# 🔚 TCP Connection Termination

TCP closes a connection using a **Four-Way Handshake**:

```text
Client                     Server

FIN  --------------------->

      <-------------------  ACK

      <-------------------  FIN

ACK  --------------------->
```

This ensures both devices have finished transmitting data before closing the connection.

---

# 📊 TCP vs UDP Comparison

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Connection-oriented | Connectionless |
| Reliability | High | Low |
| Speed | Slower | Faster |
| Packet Ordering | Yes | No |
| Acknowledgement | Yes | No |
| Retransmission | Yes | No |
| Header Size | 20–60 Bytes | 8 Bytes |
| Best For | Web, SSH, Email | DNS, VoIP, Gaming, Streaming |

---

# 🔢 Common Port Numbers

| Protocol | Port | Transport Protocol |
|----------|-----:|-------------------|
| SSH | 22 | TCP |
| HTTP | 80 | TCP |
| HTTPS | 443 | TCP |
| FTP | 21 | TCP |
| SMTP | 25 | TCP |
| DNS | 53 | UDP/TCP |
| DHCP | 67/68 | UDP |
| NTP | 123 | UDP |
| MySQL | 3306 | TCP |
| PostgreSQL | 5432 | TCP |

---

# 🌍 Real-World Examples

- **Web Browsing:** HTTPS uses TCP for reliable communication.
- **DNS Lookup:** Uses UDP for fast name resolution.
- **Video Streaming:** Often uses UDP to reduce latency.
- **SSH:** Uses TCP to ensure every command reaches the server.
- **Online Gaming:** Uses UDP to prioritize speed over perfect reliability.

---

# ☁️ DevOps Perspective

DevOps engineers work with TCP and UDP daily while managing:

- Linux servers
- AWS Load Balancers
- Docker container networking
- Kubernetes Services
- APIs and Microservices
- SSH access
- Database connectivity
- Monitoring and logging systems

Understanding when to use TCP or UDP helps in troubleshooting application connectivity, optimizing performance, and designing reliable cloud infrastructure.

---

# 📌 Key Takeaways

- TCP provides reliable, connection-oriented communication.
- UDP provides fast, connectionless communication.
- Use TCP when data integrity is essential.
- Use UDP when low latency is more important than reliability.
- Both protocols are fundamental to cloud, DevOps, and modern networking.

---

# 📝 Summary

TCP and UDP are the two primary transport layer protocols of the TCP/IP Model. TCP emphasizes reliability and ordered delivery, while UDP prioritizes speed and efficiency. Choosing the right protocol depends on the application's requirements and is a core networking skill for every DevOps engineer.

---

# 💼 Interview Tip

In interviews, don't just list differences between TCP and UDP. Explain **why** a protocol is used.

Examples:

- **HTTPS → TCP** because reliable delivery is required.
- **DNS → UDP** because queries must be answered quickly with minimal overhead.
- **Video Streaming → UDP** because occasional packet loss is preferable to playback delays.
- **SSH → TCP** because every command must reach the server accurately.



> **Interview Tip:** Be prepared to explain not only the differences between TCP and UDP, but also why a specific application chooses one over the other.
