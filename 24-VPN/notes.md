# 🔐 Chapter 24 — VPN (Virtual Private Network)

## 1. What is a VPN?

VPN stands for **Virtual Private Network**.

A VPN creates a secure connection between a device/network and another private network over an untrusted network such as the Internet.

### Simple Example

```text
Laptop
   |
   | Encrypted VPN Tunnel
   |
Internet
   |
VPN Gateway
   |
Private Network
```

Instead of directly accessing a private network over the public Internet, the VPN creates a protected communication path.

---

# 2. Why Do We Use VPN?

Organizations use VPNs for secure connectivity.

### Main purposes

* Secure remote access
* Connect different offices
* Connect on-premises infrastructure to cloud networks
* Protect traffic over untrusted networks
* Access private services
* Connect distributed infrastructure
* Provide private network connectivity

### Example

An employee working from home can connect to the company's internal network using a VPN.

```text
Employee Laptop
       |
       | VPN
       ↓
VPN Gateway
       |
       ↓
Company Private Network
```

---

# 3. How VPN Works

A VPN generally involves:

1. VPN client
2. VPN gateway/server
3. Authentication
4. Encryption
5. Tunnel creation
6. Routing

### Basic Flow

```text
Client
  |
  | 1. Request VPN connection
  ↓
VPN Gateway
  |
  | 2. Authenticate
  ↓
Authentication
  |
  | 3. Establish secure tunnel
  ↓
Encrypted VPN Tunnel
  |
  ↓
Private Network
```

---

# 4. VPN Tunnel

A VPN tunnel is a logical communication path through which traffic is securely transported between endpoints.

Conceptually:

```text
Original Packet
      ↓
Encapsulation
      ↓
Encrypted VPN Packet
      ↓
Internet
      ↓
VPN Gateway
      ↓
Decryption
      ↓
Original Packet
```

The Internet carries the VPN traffic, while the VPN endpoints handle the secure tunnel.

---

# 5. Encryption

Encryption converts readable information into protected data.

```text
Plaintext
   ↓
Encryption
   ↓
Ciphertext
   ↓
Network
   ↓
Decryption
   ↓
Plaintext
```

Encryption helps prevent unauthorized parties from reading protected traffic.

The exact cryptographic algorithms depend on the VPN technology being used.

---

# 6. Authentication

Authentication verifies the identity of the user or device attempting to connect.

Common authentication mechanisms include:

* Username/password
* Certificates
* Pre-shared keys
* Multi-factor authentication
* Device credentials

### Example

```text
VPN Client
    |
    | Credentials
    ↓
VPN Gateway
    |
    ↓
Authentication
    |
    ├── Valid → Connection allowed
    |
    └── Invalid → Connection rejected
```

---

# 7. VPN Components

## VPN Client

Software or configuration running on the user's device.

Example:

```text
Laptop → VPN Client
```

## VPN Server / Gateway

The endpoint that accepts VPN connections and provides access to a private network.

```text
VPN Client → VPN Gateway → Private Network
```

## VPN Tunnel

The secure logical path between VPN endpoints.

## Authentication System

Verifies users or devices.

## Encryption

Protects traffic travelling through the tunnel.

---

# 8. Types of VPN

There are several common VPN deployment models.

## 8.1 Remote-Access VPN

A remote user connects to an organization's private network.

```text
Remote User
     |
     | VPN
     ↓
VPN Gateway
     |
     ↓
Private Network
```

### Use case

A developer working remotely needs access to:

* Internal Git server
* Jenkins
* Private database
* Internal applications

---

# 8.2 Site-to-Site VPN

A site-to-site VPN connects two networks.

```text
Office A                         Office B
10.1.0.0/16                     10.2.0.0/16
     |                               |
     ↓                               ↓
VPN Gateway ═══ Internet ═══ VPN Gateway
```

The two private networks can communicate through the VPN tunnel.

### Common use

Connecting:

* Headquarters
* Branch office
* Data center
* Cloud VPC/VNet

---

# 8.3 Client-to-Site VPN

An individual client connects to a private network.

```text
Developer Laptop
       |
       | VPN
       ↓
VPN Gateway
       |
       ↓
Private Network
```

This is commonly used for remote employees.

---

# 9. VPN Protocols and Technologies

## IPsec

**IPsec** is a suite of protocols used to secure IP communications.

It is commonly used for:

* Site-to-site VPN
* Remote-access VPN
* Cloud VPN connectivity

IPsec can provide:

* Authentication
* Integrity
* Confidentiality

---

# 10. WireGuard

**WireGuard** is a modern VPN protocol designed with a relatively simple architecture and strong cryptographic primitives.

Characteristics include:

* Simple configuration
* High performance
* Modern cryptography
* Small codebase
* Secure tunneling

Example architecture:

```text
Client
  |
  | WireGuard Tunnel
  |
Internet
  |
Server
```

---

# 11. OpenVPN

**OpenVPN** is a widely used VPN solution.

It can be used for:

* Remote-access VPN
* Site-to-site VPN
* Secure remote connectivity

OpenVPN commonly uses TLS-based security mechanisms for authentication and key exchange.

---

# 12. SSL/TLS VPN

Some remote-access VPN solutions use TLS to secure connections.

A simplified model:

```text
VPN Client
    |
    | TLS-secured connection
    ↓
VPN Gateway
    |
    ↓
Private Resources
```

These solutions are often used for remote users and application access.

---

# 13. VPN Routing

VPN connectivity is closely related to routing.

After connecting to a VPN, routes may be added or modified so traffic destined for private networks travels through the VPN interface.

Check routes with:

```bash
ip route
```

Example:

```text
10.10.0.0/16 dev tun0
```

This could indicate that traffic for `10.10.0.0/16` should use the VPN interface.

The exact interface and route depend on the VPN implementation.

---

# 14. Full Tunnel vs Split Tunnel

## Full Tunnel

Most or all client traffic is routed through the VPN.

```text
Laptop
   |
   ↓
VPN
   |
   +---- Private Network
   |
   +---- Internet
```

### Advantages

* Centralized traffic control
* Organization can apply security policies
* Internet traffic can be inspected centrally

### Disadvantages

* More bandwidth usage
* Higher latency may occur
* Greater VPN gateway load

---

# 15. Split Tunnel

Only selected traffic uses the VPN.

```text
Laptop
   |
   +---- Private Network → VPN
   |
   +---- Public Internet → Normal connection
```

Example:

```text
10.10.0.0/16 → VPN
Internet      → Local connection
```

### Advantages

* Reduced VPN bandwidth
* Potentially lower latency
* Local Internet access remains available

### Disadvantages

* More complex routing
* Requires careful security configuration

---

# 16. VPN and DNS

DNS is important when accessing private resources through a VPN.

For example:

```text
git.internal.example
```

may resolve only when connected to the organization's VPN.

Test DNS resolution with:

```bash
getent hosts git.internal.example
```

or:

```bash
nslookup git.internal.example
```

A VPN can therefore involve both:

```text
VPN Connectivity
       +
Routing
       +
DNS
```

---

# 17. VPN and Firewall

Firewalls can affect VPN connectivity.

Possible problems include:

* VPN port blocked
* VPN protocol blocked
* Private subnet traffic blocked
* Return traffic blocked
* Local firewall rules interfering with the tunnel

Useful command:

```bash
sudo ss -ltnup
```

Firewall configuration depends on the operating system and firewall software.

---

# 18. VPN in Cloud Computing

VPNs are frequently used to connect on-premises networks to cloud networks.

Example:

```text
On-Premises Data Center
          |
          |
     VPN Gateway
          |
          |
      Internet
          |
          |
     Cloud VPN
       Gateway
          |
          ↓
       VPC/VNet
          |
      +---+---+
      |       |
   Servers  Database
```

This allows private communication between environments.

---

# 19. VPN in AWS

In AWS, a common architecture is:

```text
On-Premises Network
        |
        ↓
Customer Gateway
        |
        |
   Internet
        |
        ↓
Virtual Private Gateway
        |
        ↓
VPC
```

Another AWS design can use a **Transit Gateway** for centralized connectivity.

VPN connectivity can be used to connect enterprise networks with AWS private networks.

---

# 20. VPN in DevOps

VPNs are important in DevOps because many resources should not be publicly accessible.

Example:

```text
Developer
    |
    | VPN
    ↓
Private Network
    |
    +---- Git Server
    |
    +---- Jenkins
    |
    +---- Kubernetes API
    |
    +---- Monitoring
    |
    +---- Database
```

Instead of exposing every service to the public Internet, organizations can keep them private and provide controlled network access through a VPN.

---

# 21. VPN and Kubernetes

VPNs can provide network connectivity between Kubernetes environments and external private networks.

Example:

```text
On-Premises
    |
    | VPN
    ↓
Cloud Network
    |
    ↓
Kubernetes Cluster
    |
    +---- Pods
    |
    +---- Services
```

A VPN can be part of the overall network architecture, but Kubernetes itself does not automatically require a VPN.

---

# 22. VPN and Docker

Docker networking and VPN networking are separate concepts, but they can interact.

Example:

```text
Host
 |
 | VPN
 ↓
Private Network
 |
 ↓
Docker Host
 |
 +---- Container A
 |
 +---- Container B
```

Whether containers can directly use or reach VPN networks depends on routing, Docker networking configuration, firewall rules, and the VPN implementation.

---

# 23. VPN vs Proxy

| Feature                | VPN                                         | Proxy                              |
| ---------------------- | ------------------------------------------- | ---------------------------------- |
| Main purpose           | Secure/private network connectivity         | Forward traffic                    |
| Scope                  | Can affect system/network traffic           | Often application-specific         |
| Encryption             | Commonly provides encrypted tunnel          | Depends on proxy type              |
| Private network access | Yes                                         | Usually not its primary purpose    |
| Common use             | Remote access and site-to-site connectivity | Web forwarding, filtering, caching |

---

# 24. VPN vs SSH

| Feature           | VPN                           | SSH                          |
| ----------------- | ----------------------------- | ---------------------------- |
| Main purpose      | Secure network connectivity   | Secure remote administration |
| Typical scope     | Network/private subnet        | Individual server/session    |
| Remote shell      | Not its primary purpose       | Yes                          |
| Tunneling         | Yes                           | Yes, through SSH forwarding  |
| Common DevOps use | Private infrastructure access | Server administration        |

---

# 25. VPN Troubleshooting

When a VPN does not work, troubleshoot systematically.

## Step 1 — Check network connectivity

```bash
ping <gateway-ip>
```

## Step 2 — Check interfaces

```bash
ip addr
```

Look for VPN interfaces such as:

```text
tun0
wg0
```

depending on the VPN technology.

## Step 3 — Check routing

```bash
ip route
```

Confirm that private network routes exist.

## Step 4 — Check DNS

```bash
cat /etc/resolv.conf
```

and:

```bash
getent hosts <hostname>
```

## Step 5 — Check listening ports

```bash
sudo ss -ltnup
```

## Step 6 — Check firewall

Inspect the firewall rules appropriate to your Linux distribution.

## Step 7 — Check VPN logs

Logs can reveal:

* Authentication failure
* Certificate problems
* Routing problems
* Handshake failures
* Configuration errors

---

# 26. Common VPN Problems

## Authentication Failure

Possible causes:

* Wrong credentials
* Expired certificate
* Incorrect key
* Incorrect configuration
* MFA failure

---

## Routing Failure

VPN connects, but private resources cannot be reached.

Check:

```bash
ip route
```

---

## DNS Failure

The VPN connects, but internal hostnames do not resolve.

Test:

```bash
getent hosts <internal-hostname>
```

---

## Firewall Failure

The tunnel may be established, but traffic can still be blocked by firewall rules.

---

## MTU Problems

Incorrect MTU settings can cause some traffic to fail even when basic connectivity works.

Symptoms can include:

* Some websites work while others fail
* Large packets fail
* Intermittent connectivity

---

# 27. Important Linux Networking Commands

Check interfaces:

```bash
ip addr
```

Check routes:

```bash
ip route
```

Check DNS:

```bash
cat /etc/resolv.conf
```

Test DNS:

```bash
getent hosts example.com
```

Test connectivity:

```bash
ping <ip-address>
```

Check listening TCP ports:

```bash
ss -ltn
```

Check listening TCP/UDP ports:

```bash
sudo ss -ltnup
```

Trace network path:

```bash
traceroute <destination>
```

or:

```bash
tracepath <destination>
```

---

# 28. Real-World DevOps Scenario

Imagine a company has a private Kubernetes cluster and a private database.

They do not want either service exposed directly to the public Internet.

Architecture:

```text
Developer Laptop
       |
       | VPN
       ↓
Corporate Network
       |
       +----------------+
       |                |
       ↓                ↓
 Kubernetes         Database
 Cluster             Server
```

The developer connects to the VPN and receives routes to the private infrastructure.

The workflow becomes:

```text
Developer
   ↓
VPN Authentication
   ↓
VPN Tunnel
   ↓
Private Network
   ↓
Kubernetes / Database / Internal Services
```

This is a common pattern for securing access to internal infrastructure.

---

# 29. Security Best Practices

When deploying a VPN:

* Use strong authentication
* Prefer modern cryptographic protocols
* Protect private keys
* Rotate credentials when required
* Use MFA where supported
* Limit access to required networks
* Avoid unnecessary public exposure
* Monitor VPN connections
* Keep VPN software updated
* Use firewall rules
* Apply least-privilege network access
* Monitor authentication failures

---

# 30. Key Terms

| Term              | Meaning                                 |
| ----------------- | --------------------------------------- |
| VPN               | Virtual Private Network                 |
| Tunnel            | Logical path carrying VPN traffic       |
| VPN Gateway       | Endpoint that provides VPN connectivity |
| Encryption        | Protects data from unauthorized reading |
| Authentication    | Verifies identity                       |
| IPsec             | Suite for securing IP communication     |
| WireGuard         | Modern VPN protocol                     |
| OpenVPN           | VPN solution using TLS-based security   |
| Remote-Access VPN | User-to-private-network connection      |
| Site-to-Site VPN  | Network-to-network connection           |
| Full Tunnel       | Most/all traffic goes through VPN       |
| Split Tunnel      | Only selected traffic uses VPN          |

---

# 31. Quick Revision

### What is a VPN?

A VPN creates secure network connectivity over an untrusted network.

### What is VPN tunneling?

It is the process of carrying network traffic through a logical VPN tunnel.

### Why is encryption used?

To protect traffic from unauthorized access.

### What is a site-to-site VPN?

It connects two private networks.

### What is a remote-access VPN?

It allows an individual user to securely access a private network.

### What is split tunneling?

Only selected traffic is routed through the VPN.

### What command shows routes?

```bash
ip route
```

### What command shows interfaces?

```bash
ip addr
```

### What command checks listening ports?

```bash
sudo ss -ltnup
```

---

# 🎯 Chapter 24 Summary

A VPN provides secure connectivity between users, networks, and private infrastructure.

The most important concepts are:

```text
VPN
 |
 +-- Authentication
 |
 +-- Encryption
 |
 +-- Tunneling
 |
 +-- Routing
 |
 +-- Remote Access
 |
 +-- Site-to-Site
 |
 +-- Cloud Connectivity
 |
 +-- Security
```

For a DevOps engineer, understanding VPNs is important because production infrastructure often contains private:

* Kubernetes clusters
* Databases
* CI/CD servers
* Git servers
* Monitoring systems
* Internal APIs
* Cloud resources

A VPN can provide controlled and secure access to these private environments.
