# Chapter 20 — Gateway

## Table of Contents

1. [What is a Gateway?](#1-what-is-a-gateway)
2. [What is a Default Gateway?](#2-what-is-a-default-gateway)
3. [Why Do We Need a Gateway?](#3-why-do-we-need-a-gateway)
4. [How a Gateway Works](#4-how-a-gateway-works)
5. [Gateway vs Router](#5-gateway-vs-router)
6. [Default Route](#6-default-route)
7. [Gateway in Linux](#7-gateway-in-linux)
8. [Finding the Gateway in Linux](#8-finding-the-gateway-in-linux)
9. [Gateway and ARP](#9-gateway-and-arp)
10. [Gateway and DNS](#10-gateway-and-dns)
11. [Gateway and NAT](#11-gateway-and-nat)
12. [Gateway in AWS](#12-gateway-in-aws)
13. [Internet Gateway](#13-internet-gateway)
14. [NAT Gateway](#14-nat-gateway)
15. [Transit Gateway](#15-transit-gateway)
16. [Gateway in Docker](#16-gateway-in-docker)
17. [Gateway in Kubernetes](#17-gateway-in-kubernetes)
18. [Gateway vs Internet Gateway vs NAT Gateway](#18-gateway-vs-internet-gateway-vs-nat-gateway)
19. [Production Troubleshooting](#19-production-troubleshooting)
20. [Important Commands](#20-important-commands)
21. [Key Points to Remember](#21-key-points-to-remember)

---

# 1. What is a Gateway?

A **gateway** is a device or network point that provides a path for traffic to move from one network to another.

In simple words:

> A gateway is the way out of your local network to another network.

Example:

```text
Your Laptop
192.168.1.10
      |
      ↓
Gateway
192.168.1.1
      |
      ↓
Internet
```

Here:

```text
192.168.1.1
```

is the gateway for the laptop.

---

# 2. What is a Default Gateway?

A **default gateway** is the device that a host sends packets to when the destination is outside the host's local network.

Example:

```text
Laptop
192.168.1.10
     |
     ↓
Default Gateway
192.168.1.1
     |
     ↓
Internet
```

If the laptop wants to communicate with:

```text
8.8.8.8
```

and that destination is not part of the local network, the laptop sends the packet to its default gateway.

---

# 3. Why Do We Need a Gateway?

Suppose your laptop has:

```text
IP:
192.168.1.10

Subnet:
192.168.1.0/24
```

It can communicate directly with devices such as:

```text
192.168.1.20
192.168.1.30
192.168.1.50
```

because they are in the same network.

But if it wants to reach:

```text
8.8.8.8
```

that destination is outside the local network.

The laptop needs a gateway:

```text
192.168.1.10
      |
      ↓
192.168.1.1
      |
      ↓
Other Networks
```

---

# 4. How a Gateway Works

Imagine:

```text
Laptop
192.168.1.10
      |
      ↓
Gateway
192.168.1.1
      |
      ↓
Router
      |
      ↓
Internet
```

The laptop checks its routing table.

If the destination is local:

```text
192.168.1.20
```

it communicates directly.

If the destination is external:

```text
8.8.8.8
```

it uses the default route and sends the packet to the gateway.

The simplified process is:

```text
Destination
    ↓
Check routing table
    ↓
Is destination local?
   / \
 Yes  No
  |    |
  ↓    ↓
Direct Gateway
       |
       ↓
   Other Network
```

---

# 5. Gateway vs Router

A **router** is a networking device that forwards packets between networks.

A **gateway** is a broader concept. It acts as an entry or exit point between networks and can perform additional functions depending on the system.

A router can act as a gateway.

Example:

```text
Laptop
   |
   ↓
Router
   |
   ↓
Internet
```

The router is also the laptop's default gateway.

### Simple Memory Trick

```text
Router → Forwards traffic between networks

Gateway → Entry/exit point to another network
```

In many basic network setups, the same device performs both roles.

---

# 6. Default Route

The default route tells the operating system where to send traffic when there is no more specific route.

In IPv4:

```text
0.0.0.0/0
```

means:

> Any IPv4 destination.

Example:

```text
default via 192.168.1.1 dev wlo1
```

This means:

```text
Any destination
      |
      ↓
Gateway: 192.168.1.1
      |
      ↓
Interface: wlo1
```

---

# 7. Gateway in Linux

Linux uses a routing table to decide where packets should go.

Check the routing table:

```bash
ip route
```

Example:

```text
default via 192.168.1.1 dev wlo1
192.168.1.0/24 dev wlo1 proto kernel scope link src 192.168.1.10
```

The first line is the default route:

```text
default via 192.168.1.1 dev wlo1
```

Here:

```text
Gateway:
192.168.1.1

Interface:
wlo1
```

---

# 8. Finding the Gateway in Linux

The easiest command is:

```bash
ip route
```

Look for:

```text
default via <gateway-ip>
```

For example:

```text
default via 192.168.1.1 dev wlo1
```

You can also run:

```bash
ip route | grep default
```

Example:

```text
default via 192.168.1.1 dev wlo1
```

This is one of the most important commands for network troubleshooting.

---

# 9. Gateway and ARP

Before sending an Ethernet frame to a gateway on the local network, the host needs the gateway's MAC address.

For IPv4, ARP is used to discover the MAC address.

Example:

```text
Laptop
192.168.1.10
    |
    | ARP:
    | "Who has 192.168.1.1?"
    ↓
Gateway
192.168.1.1
MAC: aa:bb:cc:dd:ee:ff
```

Check the neighbor table:

```bash
ip neigh
```

Example:

```text
192.168.1.1 dev wlo1 lladdr aa:bb:cc:dd:ee:ff REACHABLE
```

This shows the gateway's IP-to-MAC mapping.

---

# 10. Gateway and DNS

A gateway and DNS server perform different jobs.

### Gateway

Moves packets between networks.

### DNS

Translates domain names into IP addresses.

Example:

```text
google.com
     |
     ↓
DNS
     |
     ↓
142.x.x.x
```

Then the system uses its routing table and gateway to reach that IP.

So:

```text
DNS
↓
Find destination IP

Gateway
↓
Reach destination network
```

---

# 11. Gateway and NAT

Gateway and NAT are related but are not the same thing.

### Gateway

Provides a path to another network.

### NAT

Translates IP addresses and/or ports.

Example:

```text
Private Server
192.168.1.10
      |
      ↓
Default Gateway
192.168.1.1
      |
      ↓
NAT
      |
      ↓
Public IP
      |
      ↓
Internet
```

A home router can perform both gateway and NAT functions.

---

# 12. Gateway in AWS

AWS has several gateway-related services.

Important ones include:

* Internet Gateway
* NAT Gateway
* Transit Gateway
* Virtual Private Gateway
* Egress-only Internet Gateway

These services have different purposes.

---

# 13. Internet Gateway

An **Internet Gateway (IGW)** provides a connection between a VPC and the Internet.

A common public subnet architecture is:

```text
EC2
 |
 ↓
Route Table
 |
 ↓
Internet Gateway
 |
 ↓
Internet
```

For a resource to communicate directly with the Internet, the appropriate routing and public addressing must also be configured.

A typical public subnet route is:

```text
0.0.0.0/0 → Internet Gateway
```

---

# 14. NAT Gateway

A **NAT Gateway** allows resources in private subnets to initiate outbound Internet connections.

Architecture:

```text
Private EC2
     |
     ↓
Private Route Table
     |
     ↓
NAT Gateway
     |
     ↓
Internet Gateway
     |
     ↓
Internet
```

A private subnet commonly has:

```text
0.0.0.0/0 → NAT Gateway
```

The NAT Gateway is placed in a public subnet with connectivity through an Internet Gateway.

---

# 15. Transit Gateway

AWS **Transit Gateway** is used to connect multiple networks through a central networking hub.

Example:

```text
VPC A
   \
    \
VPC B ---- Transit Gateway ---- VPC C
    /
   /
On-Premises Network
```

It can simplify large network architectures.

Instead of creating many individual connections between every network, networks can connect through the Transit Gateway.

### DevOps Use Case

An organization may have:

```text
Production VPC
Development VPC
Testing VPC
Shared Services VPC
On-Premises Network
```

A Transit Gateway can provide centralized connectivity between them.

---

# 16. Gateway in Docker

Docker bridge networks have a gateway.

Check:

```bash
docker network inspect bridge
```

You may see something similar to:

```text
Subnet:
172.17.0.0/16

Gateway:
172.17.0.1
```

The Docker gateway provides a path between the container network and the Docker host/network.

Example:

```text
Container
172.17.0.2
     |
     ↓
Docker Gateway
172.17.0.1
     |
     ↓
Docker Host
     |
     ↓
NAT
     |
     ↓
Internet
```

---

# 17. Gateway in Kubernetes

Kubernetes networking can involve gateways at different levels.

For example:

```text
Pod
 |
 ↓
Node
 |
 ↓
Network Gateway
 |
 ↓
External Network
```

Kubernetes clusters may also use:

* CNI plugins
* Ingress
* Gateway API
* Cloud load balancers
* NAT
* Routing

The exact networking path depends on the cluster architecture and CNI.

### Kubernetes Gateway API

The **Gateway API** is a Kubernetes project for configuring traffic routing and exposing applications.

A simplified architecture:

```text
Client
  |
  ↓
Gateway
  |
  ↓
Route
  |
  ↓
Service
  |
  ↓
Pod
```

This is different from the basic concept of a Linux default gateway.

---

# 18. Gateway vs Internet Gateway vs NAT Gateway

| Gateway            | Purpose                                                                         |
| ------------------ | ------------------------------------------------------------------------------- |
| Default Gateway    | Sends traffic from a host to another network                                    |
| Internet Gateway   | Connects an AWS VPC to the Internet                                             |
| NAT Gateway        | Allows private AWS resources to initiate outbound Internet connections          |
| Transit Gateway    | Connects multiple networks/VPCs                                                 |
| Docker Gateway     | Provides a gateway for a Docker network                                         |
| Kubernetes Gateway | Provides traffic-routing functionality depending on the Kubernetes architecture |

### Important

Do not treat all gateways as the same thing.

The word **gateway** describes a role, while specific services such as AWS Internet Gateway and NAT Gateway provide particular networking functions.

---

# 19. Production Troubleshooting

Imagine a production server cannot access an external API.

Start with:

```text
Application
    |
    ↓
Network Interface
    |
    ↓
Routing Table
    |
    ↓
Default Gateway
    |
    ↓
NAT / Firewall
    |
    ↓
Internet
    |
    ↓
External API
```

### Step 1 — Check IP

```bash
ip addr
```

### Step 2 — Check interface

```bash
ip link
```

### Step 3 — Check route

```bash
ip route
```

### Step 4 — Check default gateway

```bash
ip route | grep default
```

### Step 5 — Check gateway reachability

Replace the address with your actual gateway:

```bash
ping -c 4 192.168.1.1
```

### Step 6 — Check Internet

```bash
ping -c 4 8.8.8.8
```

### Step 7 — Check DNS

```bash
ping -c 4 google.com
```

### Step 8 — Check application connectivity

```bash
curl -I https://google.com
```

---

# 20. Important Commands

### Display IP address

```bash
ip addr
```

### Display interfaces

```bash
ip link
```

### Display routing table

```bash
ip route
```

### Display default gateway

```bash
ip route | grep default
```

### Find route to a specific destination

```bash
ip route get 8.8.8.8
```

### Display ARP/neighbor table

```bash
ip neigh
```

### Test gateway

```bash
ping -c 4 <gateway-ip>
```

### Test Internet

```bash
ping -c 4 8.8.8.8
```

### Test DNS

```bash
ping -c 4 google.com
```

### Trace path

```bash
tracepath google.com
```

### Check listening ports

```bash
ss -tuln
```

### Inspect Docker gateway

```bash
docker network inspect bridge
```

---

# 21. Key Points to Remember

```text
Gateway
↓
Entry/exit point between networks
```

```text
Default Gateway
↓
Used when destination is outside the local network
```

```text
Default Route
↓
0.0.0.0/0
```

```text
Linux
↓
ip route
```

```text
Find gateway
↓
ip route | grep default
```

```text
Find route to destination
↓
ip route get 8.8.8.8
```

```text
Gateway + NAT
↓
Commonly used together for Internet access
```

### DevOps Connection

```text
Linux
   ↓
Gateway
   ↓
Routing
   ↓
NAT
   ↓
AWS VPC
   ↓
Docker
   ↓
Kubernetes
   ↓
Production Networking
```

---

# Final Understanding

If someone asks:

> "What is a gateway?"

A simple interview answer is:

**A gateway is a network point that provides a path from one network to another. A default gateway is used by a host to forward traffic when the destination is outside its local network.**

The most important Linux command to remember is:

```bash
ip route
```

And the most important line to recognize is:

```text
default via 192.168.1.1 dev wlo1
```

This tells you:

```text
default
   ↓
Any destination without a more specific route

via 192.168.1.1
   ↓
Send it to the gateway

dev wlo1
   ↓
Use the wlo1 interface
```