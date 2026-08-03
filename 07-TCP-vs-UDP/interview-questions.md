# 🎤 TCP vs UDP Interview Questions

This document contains commonly asked interview questions related to TCP and UDP for Linux, Networking, Cloud, DevOps, and SRE roles.

---

# 1. What is TCP?

**Answer:**

TCP (Transmission Control Protocol) is a connection-oriented transport layer protocol that provides reliable, ordered, and error-checked delivery of data between devices.

---

# 2. What is UDP?

**Answer:**

UDP (User Datagram Protocol) is a connectionless transport layer protocol designed for fast communication without guaranteeing delivery or packet order.

---

# 3. What is the main difference between TCP and UDP?

**Answer:**

| TCP | UDP |
|------|-----|
| Connection-oriented | Connectionless |
| Reliable | Best effort |
| Slower | Faster |
| Ordered delivery | No ordering |
| Uses acknowledgements | No acknowledgements |

---

# 4. Why is TCP considered reliable?

**Answer:**

TCP ensures:

- Packet ordering
- Error detection
- Retransmission of lost packets
- Acknowledgements
- Flow control
- Congestion control

---

# 5. Why is UDP faster?

**Answer:**

UDP does not establish a connection, send acknowledgements, or retransmit lost packets, reducing overhead and latency.

---

# 6. What is the TCP Three-Way Handshake?

**Answer:**

The TCP connection is established in three steps:

1. Client → SYN
2. Server → SYN + ACK
3. Client → ACK

After these steps, data transmission begins.

---

# 7. What is TCP Connection Termination?

**Answer:**

TCP closes a connection using a Four-Way Handshake:

1. FIN
2. ACK
3. FIN
4. ACK

This ensures all data has been transmitted before the connection closes.

---

# 8. Which protocol does HTTP use?

**Answer:**

HTTP uses TCP because reliable delivery is required.

---

# 9. Which protocol does HTTPS use?

**Answer:**

HTTPS uses TCP, along with TLS/SSL for secure communication.

---

# 10. Which protocol does DNS use?

**Answer:**

DNS primarily uses UDP (port 53) for queries but may use TCP for zone transfers or large responses.

---

# 11. Which protocol does SSH use?

**Answer:**

SSH uses TCP on port 22 because secure, reliable communication is essential.

---

# 12. Which protocol is used for online gaming?

**Answer:**

Most online games use UDP to minimize latency.

---

# 13. Which protocol is preferred for video streaming?

**Answer:**

Live streaming often uses UDP because small packet losses are preferable to playback delays.

---

# 14. What is a port number?

**Answer:**

A port number identifies a specific service or application running on a device, allowing multiple services to communicate over the same IP address.

---

# 15. Name some common TCP ports.

**Answer:**

- SSH – 22
- HTTP – 80
- HTTPS – 443
- FTP – 21
- SMTP – 25
- MySQL – 3306
- PostgreSQL – 5432

---

# 16. Name some common UDP ports.

**Answer:**

- DNS – 53
- DHCP – 67/68
- NTP – 123
- SNMP – 161

---

# 17. What command shows listening TCP and UDP ports?

**Answer:**

```bash
ss -tuln
```

---

# 18. What command shows all TCP connections?

**Answer:**

```bash
ss -tan
```

---

# 19. What command shows all UDP sockets?

**Answer:**

```bash
ss -uan
```

---

# 20. What command tests if a remote TCP port is open?

**Answer:**

```bash
nc -zv hostname port
```

Example:

```bash
nc -zv google.com 443
```

---

# 21. What command retrieves only HTTP response headers?

**Answer:**

```bash
curl -I https://example.com
```

---

# 22. When should TCP be used?

**Answer:**

Use TCP when reliability, ordered delivery, and error recovery are important, such as web browsing, email, SSH, and file transfers.

---

# 23. When should UDP be used?

**Answer:**

Use UDP when speed and low latency are more important than guaranteed delivery, such as DNS, VoIP, gaming, and live streaming.

---

# 24. What is flow control in TCP?

**Answer:**

Flow control prevents a sender from overwhelming a receiver by adjusting the amount of data sent based on the receiver's capacity.

---

# 25. What is congestion control?

**Answer:**

Congestion control reduces network traffic when congestion is detected, helping maintain network stability and performance.

---

# 💡 Interview Tip

Instead of only listing differences between TCP and UDP, explain **why** an application chooses one protocol over the other. Interviewers value practical reasoning and real-world examples.
