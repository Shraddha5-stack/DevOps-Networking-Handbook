# 🎤 OSI Model Interview Questions

This section contains commonly asked interview questions on the OSI Model for Linux, Networking, Cloud, and DevOps roles.

---

# 1. What is the OSI Model?

### Answer

The OSI (Open Systems Interconnection) Model is a conceptual framework developed by ISO that explains how data travels between devices over a network. It divides network communication into seven layers, with each layer performing a specific function.

---

# 2. Why was the OSI Model created?

### Answer

The OSI Model was created to standardize network communication so that devices from different vendors could communicate with each other. It also provides a structured approach for troubleshooting and designing networks.

---

# 3. Name the seven layers of the OSI Model.

### Answer

1. Physical
2. Data Link
3. Network
4. Transport
5. Session
6. Presentation
7. Application

---

# 4. Which layer is responsible for transmitting bits?

### Answer

The **Physical Layer (Layer 1)** transmits raw bits over cables, fiber optics, or wireless media.

---

# 5. Which layer uses MAC addresses?

### Answer

The **Data Link Layer (Layer 2)** uses MAC addresses for communication within the same local network (LAN).

---

# 6. Which layer uses IP addresses?

### Answer

The **Network Layer (Layer 3)** uses IP addresses to route packets between different networks.

---

# 7. Which device works at the Network Layer?

### Answer

A **Router** operates at Layer 3 and forwards packets based on IP addresses.

---

# 8. Which device works at the Data Link Layer?

### Answer

A **Switch** operates at Layer 2 and forwards frames using MAC addresses.

---

# 9. What is the data unit at each OSI layer?

| Layer | Data Unit |
|--------|-----------|
| Application | Data |
| Presentation | Data |
| Session | Data |
| Transport | Segment (TCP) / Datagram (UDP) |
| Network | Packet |
| Data Link | Frame |
| Physical | Bits |

---

# 10. What is the difference between TCP and UDP?

### Answer

TCP is connection-oriented, reliable, and guarantees ordered delivery.

UDP is connectionless, faster, and does not guarantee delivery.

---

# 11. Which layer uses port numbers?

### Answer

The **Transport Layer (Layer 4)** uses port numbers to deliver data to the correct application.

---

# 12. What is a port number?

### Answer

A port number identifies a specific application or service running on a device, such as HTTP (80), HTTPS (443), or SSH (22).

---

# 13. What is encapsulation?

### Answer

Encapsulation is the process of adding protocol headers as data moves from the Application Layer down to the Physical Layer before transmission.

---

# 14. What is decapsulation?

### Answer

Decapsulation is the process of removing protocol headers as data moves from the Physical Layer up to the Application Layer at the receiving device.

---

# 15. What is the difference between a MAC address and an IP address?

| MAC Address | IP Address |
|-------------|------------|
| Physical hardware address | Logical network address |
| Layer 2 | Layer 3 |
| Assigned to the NIC | Assigned by the network |

---

# 16. What is the role of the Session Layer?

### Answer

The Session Layer establishes, manages, synchronizes, and terminates communication sessions between applications.

---

# 17. What is the role of the Presentation Layer?

### Answer

The Presentation Layer handles data formatting, encryption, decryption, compression, and decompression.

---

# 18. What is the role of the Application Layer?

### Answer

The Application Layer provides network services directly to end-user applications through protocols such as HTTP, HTTPS, FTP, SMTP, and DNS.

---

# 19. What is the difference between the OSI Model and the TCP/IP Model?

| OSI Model | TCP/IP Model |
|-----------|--------------|
| 7 layers | 4 layers |
| Reference model | Practical networking model |
| Developed by ISO | Developed by DoD |

---

# 20. How does the OSI Model help in troubleshooting?

### Answer

The OSI Model allows engineers to troubleshoot one layer at a time.

Example:

- Check cables → Layer 1
- Check MAC addresses → Layer 2
- Check IP routing → Layer 3
- Check ports → Layer 4
- Check the application → Layer 7

---

# 💡 Interview Tip

When asked about the OSI Model:

1. Explain its purpose.
2. Name all seven layers.
3. Describe the function of each layer.
4. Mention the data unit for each layer.
5. Give examples of protocols and devices.
6. Explain how it helps in real-world troubleshooting.

This structured answer demonstrates both theoretical understanding and practical knowledge.
