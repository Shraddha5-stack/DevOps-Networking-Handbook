# 🌐 Chapter 15 – Ports & Protocols

## 1. What is a Port?

A **port** is a logical communication endpoint used by applications and services on a computer.

An IP address identifies the **machine**, while a port identifies the **service/application** communicating on that machine.

### Simple example

```text
192.168.1.10:22
```

Here:

```text
192.168.1.10 → IP address → identifies the machine
22           → Port       → identifies the SSH service
```

Think of it like an apartment building:

```text
IP Address → Building
Port       → Apartment
```

The IP gets the traffic to the correct machine, and the port gets it to the correct service.

---

# 2. Why Do We Need Ports?

A single computer can run many network services at the same time.

For example:

```text
Server
│
├── SSH        → 22
├── HTTP       → 80
├── HTTPS      → 443
├── DNS        → 53
└── PostgreSQL → 5432
```

The operating system uses port numbers to deliver incoming network traffic to the appropriate application.

Without ports, the OS would not know which application should receive a network connection.

---

# 3. What is a Protocol?

A **protocol** is a defined set of rules that determines how devices communicate.

Examples:

```text
HTTP
HTTPS
SSH
DNS
DHCP
FTP
SMTP
TCP
UDP
```

Protocols define things such as:

* How communication starts
* How data is formatted
* How messages are exchanged
* How errors are handled
* How communication ends

### Simple analogy

Think of a protocol as a language.

Two people need a common language to communicate.

Similarly:

```text
Client
   ↓
Protocol rules
   ↓
Server
```

Both sides follow the same communication rules.

---

# 4. Port vs Protocol

These two concepts are different.

### Port

Identifies a logical communication endpoint.

### Protocol

Defines the communication rules.

Example:

```text
HTTPS → Protocol
443   → Port
```

Another example:

```text
SSH → Protocol
22  → Port
```

Remember:

```text
Protocol = How communication happens
Port     = Where the application receives communication
```

---

# 5. IP + Port

A network connection commonly identifies an endpoint using:

```text
IP Address + Port
```

Example:

```text
192.168.1.10:8080
```

This means:

```text
IP   → 192.168.1.10
Port → 8080
```

For IPv6, brackets are commonly used when specifying a port:

```text
[2001:db8::10]:443
```

---

# 6. Port Number Range

TCP and UDP ports range from:

```text
0–65535
```

They are commonly divided into three ranges.

## Well-Known Ports

```text
0–1023
```

These are traditionally associated with standard services and protocols.

Examples:

```text
22  → SSH
25  → SMTP
53  → DNS
80  → HTTP
443 → HTTPS
```

---

## Registered Ports

```text
1024–49151
```

These are commonly assigned to applications and services.

Examples include:

```text
3306 → MySQL
5432 → PostgreSQL
```

---

## Dynamic / Private Ports

```text
49152–65535
```

These are commonly used for temporary client-side connections.

For example:

```text
Client
192.168.1.5:51542
       ↓
Server
192.168.1.10:443
```

The client may use a temporary ephemeral port such as `51542`.

---

# 7. TCP Ports

TCP is connection-oriented.

Before data transfer, TCP establishes a connection.

Simplified process:

```text
Client
   |
   | SYN
   ↓
Server
   |
   | SYN-ACK
   ↓
Client
   |
   | ACK
   ↓
Connection Established
```

This is called the **TCP three-way handshake**.

Common TCP-based services include:

```text
SSH
HTTP
HTTPS
FTP
SMTP
```

---

# 8. UDP Ports

UDP is connectionless.

It does not establish a TCP-style connection before sending data.

Example:

```text
Client
   |
   | UDP packet
   ↓
Server
```

UDP is often preferred when low overhead and speed are important.

Examples include:

```text
DNS
DHCP
VoIP
Streaming
Online gaming
```

Some applications can use both TCP and UDP depending on the protocol or implementation.

---

# 9. TCP vs UDP

| Feature     | TCP                           | UDP                             |
| ----------- | ----------------------------- | ------------------------------- |
| Connection  | Connection-oriented           | Connectionless                  |
| Reliability | Reliable delivery mechanisms  | No TCP-style delivery guarantee |
| Ordering    | Maintains ordered byte stream | No ordering guarantee           |
| Handshake   | Yes                           | No TCP handshake                |
| Overhead    | Higher                        | Lower                           |
| Common use  | HTTP/HTTPS, SSH               | DNS, DHCP, real-time traffic    |

Important:

> UDP is not simply "faster TCP." It provides a different set of transport features, and the application decides how to handle reliability, ordering, retransmission, or loss if needed.

---

# 10. Common Ports

| Port | Protocol / Service         | Typical Transport |
| ---: | -------------------------- | ----------------- |
|   20 | FTP Data                   | TCP               |
|   21 | FTP Control                | TCP               |
|   22 | SSH                        | TCP               |
|   23 | Telnet                     | TCP               |
|   25 | SMTP                       | TCP               |
|   53 | DNS                        | TCP/UDP           |
|   67 | DHCP Server                | UDP               |
|   68 | DHCP Client                | UDP               |
|   80 | HTTP                       | TCP               |
|  110 | POP3                       | TCP               |
|  123 | NTP                        | UDP               |
|  143 | IMAP                       | TCP               |
|  161 | SNMP                       | UDP               |
|  389 | LDAP                       | TCP/UDP           |
|  443 | HTTPS                      | TCP               |
| 3306 | MySQL                      | TCP               |
| 5432 | PostgreSQL                 | TCP               |
| 6379 | Redis                      | TCP               |
| 8080 | Common alternate HTTP port | TCP               |

**Note:** Port numbers indicate conventional/default service assignments; modern applications can be configured to use different ports.

---

# 11. Port 22 – SSH

SSH stands for **Secure Shell**.

Default port:

```text
22
```

Used for secure remote administration.

Example:

```bash
ssh user@server
```

Network flow:

```text
Developer
   ↓
TCP 22
   ↓
Linux Server
   ↓
SSH Service
```

DevOps use cases:

* Remote server administration
* Troubleshooting
* File transfer with SCP/SFTP
* Automation
* Git operations over SSH

---

# 12. Port 80 – HTTP

HTTP stands for **Hypertext Transfer Protocol**.

Default port:

```text
80
```

It is commonly used for unencrypted HTTP communication.

Example:

```text
http://example.com
```

Flow:

```text
Client
   ↓
TCP 80
   ↓
Web Server
```

---

# 13. Port 443 – HTTPS

HTTPS is HTTP protected using TLS.

Default port:

```text
443
```

Example:

```text
https://example.com
```

Simplified flow:

```text
Client
   ↓
TCP 443
   ↓
TLS
   ↓
HTTP
   ↓
Web Server
```

HTTPS provides protection such as:

* Encryption
* Server authentication
* Integrity protection

---

# 14. Port 53 – DNS

DNS commonly uses:

```text
UDP 53
TCP 53
```

UDP is commonly used for normal DNS queries.

TCP can be used in situations such as:

* Larger DNS responses
* Zone transfers
* Protocol-specific fallback requirements

Example:

```text
Client
   ↓
DNS query
   ↓
Port 53
   ↓
DNS Server
```

---

# 15. Port 67 and 68 – DHCP

DHCP commonly uses UDP.

```text
UDP 67 → DHCP Server
UDP 68 → DHCP Client
```

Basic process:

```text
Client
   ↓
DHCP Discover
   ↓
Server
   ↓
DHCP Offer
   ↓
Client
   ↓
DHCP Request
   ↓
Server
   ↓
DHCP ACK
```

DHCP allows a client to obtain configuration such as:

```text
IP Address
Subnet Mask
Gateway
DNS Server
```

---

# 16. Port 25 – SMTP

SMTP stands for **Simple Mail Transfer Protocol**.

Port:

```text
25
```

It is commonly associated with mail server-to-mail server SMTP communication.

Other common mail submission ports include:

```text
587 → Message submission
465 → SMTP over TLS in common deployments
```

---

# 17. Port 110 – POP3

POP3 stands for **Post Office Protocol version 3**.

Default port:

```text
110
```

It is used for retrieving email.

Encrypted POP3 commonly uses:

```text
995
```

---

# 18. Port 143 – IMAP

IMAP stands for **Internet Message Access Protocol**.

Default port:

```text
143
```

It is used for accessing email stored on a mail server.

Encrypted IMAP commonly uses:

```text
993
```

---

# 19. Port 123 – NTP

NTP stands for **Network Time Protocol**.

Default:

```text
UDP 123
```

NTP synchronizes system clocks over a network.

Accurate time is important for:

```text
Logs
Authentication
Certificates
Distributed systems
Monitoring
CI/CD
```

---

# 20. Port 3306 – MySQL

MySQL commonly listens on:

```text
TCP 3306
```

Example:

```text
Application
     ↓
TCP 3306
     ↓
MySQL
```

In production, the database port should generally not be exposed publicly without a strong reason and appropriate security controls.

---

# 21. Port 5432 – PostgreSQL

PostgreSQL commonly listens on:

```text
TCP 5432
```

Example:

```text
Application
     ↓
TCP 5432
     ↓
PostgreSQL
```

In DevOps environments, firewall/security-group rules should restrict database access to trusted sources.

---

# 22. Port 6379 – Redis

Redis commonly uses:

```text
TCP 6379
```

Example:

```text
Application
     ↓
TCP 6379
     ↓
Redis
```

Redis is commonly used for:

* Caching
* Session storage
* Queues
* Fast key-value operations

---

# 23. Port 8080

Port `8080` is commonly used as an alternate HTTP/application port.

For example:

```text
Application
   ↓
8080
```

It is frequently seen in:

```text
Java applications
Development servers
Proxy servers
Testing environments
Docker containers
```

Unlike ports such as 80 and 443, `8080` is not a universal HTTP requirement. Applications choose it by configuration.

---

# 24. Listening Ports

A service that is waiting for incoming connections is said to be **listening** on a port.

Check listening TCP and UDP sockets:

```bash
ss -tuln
```

Example concept:

```text
0.0.0.0:22
0.0.0.0:80
0.0.0.0:443
```

This indicates services may be listening on those ports.

---

# 25. Identify the Process Using a Port

Use:

```bash
sudo ss -tulpn
```

This can show:

```text
Protocol
Local Address
Port
Process
PID
```

Example:

```text
LISTEN
0.0.0.0:22
sshd
```

---

# 26. Check a Specific Port

Using `nc`:

```bash
nc -zv localhost 22
```

Possible successful result:

```text
Connection to localhost 22 port [tcp/ssh] succeeded!
```

This tells you that something is accepting a TCP connection on that port.

---

# 27. Test a Remote Port

Example:

```bash
nc -zv example.com 443
```

This checks whether a TCP connection can be established to port `443`.

A failed connection can indicate:

```text
Service unavailable
Firewall blocking traffic
Security group blocking traffic
Routing problem
Wrong port
```

---

# 28. HTTP Port Testing with curl

Check HTTP headers:

```bash
curl -I http://example.com
```

Check HTTPS:

```bash
curl -I https://example.com
```

This helps verify:

```text
DNS resolution
TCP connectivity
TLS negotiation
HTTP response
```

---

# 29. Port vs Socket

A **port** is a logical number.

A **socket** represents a communication endpoint.

A TCP connection can be described using:

```text
Source IP
Source Port
Destination IP
Destination Port
Protocol
```

Example:

```text
192.168.1.5:51542
        ↓
142.250.x.x:443
```

This combination helps identify a specific network flow.

---

# 30. DevOps Importance of Ports

Ports are critical in:

```text
Cloud Security Groups
Firewalls
Docker
Kubernetes
Load Balancers
Web Servers
Databases
CI/CD
Monitoring
Microservices
```

Example AWS architecture:

```text
Internet
    ↓
TCP 443
    ↓
Load Balancer
    ↓
TCP 8080
    ↓
Application Server
    ↓
TCP 5432
    ↓
PostgreSQL
```

The database does not need to be exposed directly to the Internet.

---

# 31. Docker Port Mapping

Docker can map a host port to a container port.

Example:

```bash
docker run -p 8080:80 nginx
```

Meaning:

```text
Host Port 8080
      ↓
Container Port 80
      ↓
Nginx
```

So:

```text
localhost:8080
       ↓
Container:80
```

---

# 32. Kubernetes Port Concepts

Kubernetes commonly uses concepts such as:

```text
containerPort
Service port
targetPort
nodePort
```

For example:

```text
Client
  ↓
Service
  ↓
targetPort
  ↓
Pod
```

Understanding ports is essential for Kubernetes networking and troubleshooting.

---

# 33. Port Troubleshooting Flow

When an application is unreachable:

```text
1. Is the service running?
        ↓
2. Is it listening?
        ↓
3. Is the port correct?
        ↓
4. Can I connect locally?
        ↓
5. Can I connect remotely?
        ↓
6. Is a firewall blocking it?
        ↓
7. Is a cloud security group blocking it?
        ↓
8. Is routing correct?
```

Useful commands:

```bash
ss -tuln
```

```bash
sudo ss -tulpn
```

```bash
nc -zv host port
```

```bash
curl -I URL
```

---

# 34. Important Mental Model

Remember:

```text
IP Address
     ↓
Identifies the machine
     ↓
Port
     ↓
Identifies the service endpoint
     ↓
Protocol
     ↓
Defines communication rules
```

Example:

```text
192.168.1.10:443
       ↓
HTTPS
       ↓
Web Server
```

---

# 🎯 Interview Answer

### What is a port?

> A port is a logical communication endpoint identified by a number from 0 to 65535. It allows the operating system to deliver network traffic to the appropriate service or application. For example, an SSH server commonly listens on TCP port 22 and an HTTPS server commonly listens on TCP port 443.

### What is a protocol?

> A protocol is a defined set of rules that specifies how network devices and applications communicate. Examples include HTTP, HTTPS, SSH, DNS, TCP, and UDP.

### What is the difference between a port and a protocol?

> A port identifies the communication endpoint of a service, while a protocol defines the rules used for communication. For example, HTTPS is the protocol and TCP port 443 is its conventional transport port.

---

# 🧠 Quick Memory Table

```text
22    → SSH
25    → SMTP
53    → DNS
67    → DHCP Server
68    → DHCP Client
80    → HTTP
110   → POP3
123   → NTP
143   → IMAP
443   → HTTPS
3306  → MySQL
5432  → PostgreSQL
6379  → Redis
8080  → Common alternate HTTP/application port
```

> **Learn → Practice → Break → Debug → Document → Explain**
