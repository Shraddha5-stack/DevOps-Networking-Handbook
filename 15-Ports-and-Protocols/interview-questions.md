# 🎯 Chapter 15 – Ports & Protocols Interview Questions

## 1. What is a port?

A port is a logical communication endpoint identified by a number from **0 to 65535**. It helps the operating system deliver network traffic to the correct application or service.

Example:

```text
192.168.1.10:22
```

`192.168.1.10` identifies the machine, while `22` identifies the SSH service.

---

## 2. Why are ports required?

A server can run multiple network services simultaneously.

For example:

```text
22   → SSH
80   → HTTP
443  → HTTPS
3306 → MySQL
5432 → PostgreSQL
```

Ports allow the operating system to distinguish between these services.

---

## 3. What is a protocol?

A protocol is a defined set of rules that determines how devices or applications communicate over a network.

Examples:

```text
HTTP
HTTPS
SSH
DNS
DHCP
TCP
UDP
```

---

## 4. What is the difference between a port and a protocol?

**Port:** Identifies a logical communication endpoint.

**Protocol:** Defines the rules for communication.

Example:

```text
HTTPS → Protocol
443   → Conventional port
```

---

## 5. What is the port range?

TCP and UDP ports range from:

```text
0–65535
```

They are commonly divided into:

```text
0–1023       → Well-known ports
1024–49151   → Registered ports
49152–65535  → Dynamic/private ports
```

---

## 6. What is a well-known port?

Ports `0–1023` are known as well-known ports and are traditionally associated with standard services.

Examples:

```text
22  → SSH
25  → SMTP
53  → DNS
80  → HTTP
443 → HTTPS
```

---

## 7. What is an ephemeral port?

An ephemeral port is a temporary port typically selected by the operating system for client-side connections.

Example:

```text
192.168.1.5:51542
        ↓
server:443
```

Here `51542` can be an ephemeral client port.

---

## 8. What is port 22?

Port `22` is the conventional port for **SSH — Secure Shell**.

It is commonly used for secure remote administration of Linux servers.

Example:

```bash
ssh user@server
```

---

## 9. What is port 80?

Port `80` is the conventional port for **HTTP**.

Example:

```text
http://example.com
```

HTTP traffic on port 80 is not encrypted by TLS.

---

## 10. What is port 443?

Port `443` is the conventional port for **HTTPS**.

HTTPS uses TLS to protect HTTP communication.

Example:

```text
https://example.com
```

---

## 11. What is port 53?

Port `53` is used by DNS.

DNS can use both:

```text
UDP 53
TCP 53
```

UDP is common for ordinary DNS queries, while TCP is used in cases such as larger responses and zone transfers.

---

## 12. What are DHCP ports?

DHCP commonly uses:

```text
UDP 67 → Server
UDP 68 → Client
```

DHCP automatically provides network configuration such as:

```text
IP address
Subnet mask
Default gateway
DNS server
```

---

## 13. What is port 25?

Port `25` is associated with SMTP.

SMTP is used for sending email, particularly mail-server-to-mail-server communication.

Common submission ports include:

```text
587
465
```

---

## 14. What is port 123?

Port `123` is the conventional port for NTP.

NTP commonly uses:

```text
UDP 123
```

It synchronizes system clocks.

---

## 15. What is port 3306?

Port `3306` is the conventional port for MySQL.

Example:

```text
Application
    ↓
TCP 3306
    ↓
MySQL
```

---

## 16. What is port 5432?

Port `5432` is the conventional port for PostgreSQL.

Example:

```text
Application
    ↓
TCP 5432
    ↓
PostgreSQL
```

---

## 17. What is port 6379?

Port `6379` is the conventional port commonly used by Redis.

Redis is often used for:

* Caching
* Sessions
* Queues
* Fast key-value operations

---

## 18. What is TCP?

TCP is a connection-oriented transport protocol.

It provides mechanisms for:

* Reliable delivery
* Ordered data
* Retransmission
* Flow control
* Congestion control

---

## 19. What is UDP?

UDP is a connectionless transport protocol with low protocol overhead.

It does not provide TCP's connection-oriented reliability and ordering mechanisms.

Applications can implement their own reliability or tolerate packet loss when appropriate.

---

## 20. TCP vs UDP?

| Feature     | TCP                 | UDP                    |
| ----------- | ------------------- | ---------------------- |
| Connection  | Connection-oriented | Connectionless         |
| Reliability | Yes                 | No TCP-style guarantee |
| Ordering    | Yes                 | No guarantee           |
| Handshake   | Yes                 | No TCP handshake       |
| Overhead    | Higher              | Lower                  |
| Examples    | SSH, HTTP/HTTPS     | DNS, DHCP              |

---

## 21. How do you check listening ports in Linux?

Use:

```bash
ss -tuln
```

This displays listening TCP and UDP sockets.

---

## 22. How do you identify which process is using a port?

Use:

```bash
sudo ss -tulpn
```

or:

```bash
sudo lsof -i :22
```

---

## 23. How do you check whether port 443 is reachable?

Using netcat:

```bash
nc -zv example.com 443
```

Using curl:

```bash
curl -I https://example.com
```

These test different aspects of connectivity.

---

## 24. What does `nc -zv` do?

```bash
nc -zv host port
```

`nc` is Netcat.

```text
-z → Scan/check without sending application data
-v → Verbose output
```

It is commonly used to test TCP connectivity.

---

## 25. What does `ss -tulpn` mean?

```text
-t → TCP
-u → UDP
-l → Listening
-p → Process information
-n → Numeric addresses/ports
```

Therefore:

```bash
sudo ss -tulpn
```

shows listening TCP/UDP sockets and the processes associated with them.

---

## 26. What is a listening port?

A listening port is a port on which a service is waiting for incoming connections.

Example:

```text
0.0.0.0:22
```

This indicates that an SSH service may be listening on TCP port 22 on all IPv4 interfaces.

---

## 27. What is a socket?

A socket is a software communication endpoint.

A TCP connection can be identified by information such as:

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
server:443
```

---

## 28. What is the difference between a port and a socket?

A **port** is a numbered logical endpoint.

A **socket** represents a communication endpoint and includes addressing information used for network communication.

Simple interview answer:

> A port is a logical numbered endpoint, while a socket is a software endpoint associated with network communication.

---

## 29. How would you troubleshoot an unreachable application?

I would troubleshoot layer by layer:

```text
DNS
 ↓
IP connectivity
 ↓
Routing
 ↓
Firewall
 ↓
Port
 ↓
Process
 ↓
Application
```

Useful commands:

```bash
nslookup example.com
ping <ip>
ip route
sudo ss -tulpn
nc -zv <host> <port>
curl -v <url>
sudo ufw status
```

---

## 30. What would you check if port 8080 is not reachable?

I would check:

### 1. Is the application running?

```bash
sudo systemctl status <service>
```

### 2. Is port 8080 listening?

```bash
sudo ss -tulpn | grep :8080
```

### 3. Can I connect locally?

```bash
nc -zv localhost 8080
```

### 4. Can I connect remotely?

```bash
nc -zv <server-ip> 8080
```

### 5. Is the firewall blocking it?

```bash
sudo ufw status
```

### 6. Is a cloud security rule blocking it?

For AWS, I would check the relevant **Security Group** and network ACL configuration.

---

## 31. What is port forwarding?

Port forwarding maps traffic arriving on one address/port to another internal address/port.

Example:

```text
Internet
   ↓
Public-IP:443
   ↓
Router / Load Balancer
   ↓
Private-IP:8443
```

It is commonly used in NAT, routers, load balancers, and container environments.

---

## 32. What is Docker port mapping?

Example:

```bash
docker run -p 8080:80 nginx
```

This means:

```text
Host:8080
    ↓
Container:80
    ↓
Nginx
```

The host port and container port do not have to be the same.

---

## 33. What is Kubernetes `targetPort`?

In Kubernetes, a Service can expose a port and forward traffic to the application's target port.

Conceptually:

```text
Client
  ↓
Service port
  ↓
targetPort
  ↓
Pod
```

Example:

```text
Service port → 80
targetPort   → 8080
```

The application inside the Pod can therefore listen on `8080` while the Service exposes `80`.

---

## 34. Why should database ports not normally be exposed publicly?

Database services such as MySQL and PostgreSQL should generally be accessible only from trusted application networks.

For example:

```text
Internet
   ↓
Load Balancer
   ↓
Application
   ↓
Database
```

Instead of:

```text
Internet
   ↓
Database:5432
```

This reduces the attack surface.

---

# ⭐ Scenario-Based Interview Questions

## 35. The application works on localhost but not from another machine. What do you check?

I would check:

```text
1. Listening address
2. Port
3. Host firewall
4. Cloud security group
5. Network ACL
6. Routing
7. Application configuration
```

For example:

```bash
ss -tulpn
sudo ufw status
nc -zv <server-ip> <port>
```

A service listening only on:

```text
127.0.0.1:8080
```

is reachable only locally.

A service listening on an appropriate non-loopback interface can accept connections from other hosts, subject to firewall and routing rules.

---

## 36. Ping works but port 443 does not. Why?

`ping` uses ICMP, while HTTPS normally uses TCP port 443.

Therefore:

```text
Ping works
      ↓
IP-level connectivity exists
      ↓
But TCP 443 may still be blocked or unavailable
```

Possible causes:

* Firewall
* Security group
* Service not listening
* Wrong destination
* Network policy
* Application failure

Test with:

```bash
nc -zv <host> 443
```

---

## 37. Port 443 is listening, but the website still does not work. What do you check?

I would check:

```text
TCP connectivity
 ↓
TLS handshake
 ↓
Certificate
 ↓
HTTP response
 ↓
Reverse proxy
 ↓
Backend application
```

Useful command:

```bash
curl -v https://example.com
```

---

## 38. How would you find all listening ports on a Linux server?

I would use:

```bash
sudo ss -tulpn
```

Then I would review:

```text
Port
Protocol
Local address
Process
PID
```

I would also verify whether each exposed service is actually required.

---

## 39. Why can the same port number be used by TCP and UDP?

TCP and UDP maintain separate transport-layer namespaces.

Therefore:

```text
TCP 53
```

and:

```text
UDP 53
```

are different endpoints.

DNS is a common example.

---

# 🎯 Strong Interview Answer

### "How do you troubleshoot a port connectivity issue?"

> First, I verify that the application or service is running. Then I check whether it is listening on the expected port using `ss -tulpn`. I test local connectivity with `nc`, followed by remote connectivity. If the port is unreachable, I check the host firewall, cloud security groups or network policies, routing, and the service binding address. Finally, I use application-level tools such as `curl` to determine whether the problem is at the network layer or application layer.

---

# 🧠 Quick Revision

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
8080  → Common alternate application/HTTP port
```

Most important commands:

```bash
ss -tuln
sudo ss -tulpn
nc -zv host port
curl -I https://example.com
curl -v https://example.com
sudo lsof -i :PORT
ip route
sudo ufw status
```
