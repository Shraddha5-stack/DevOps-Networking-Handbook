# Chapter 19 — NAT (Network Address Translation)

## Table of Contents

1. [What is NAT?](#1-what-is-nat)
2. [Why NAT is Needed](#2-why-nat-is-needed)
3. [Private and Public IP Addresses](#3-private-and-public-ip-addresses)
4. [How NAT Works](#4-how-nat-works)
5. [Types of NAT](#5-types-of-nat)
6. [Static NAT](#6-static-nat)
7. [Dynamic NAT](#7-dynamic-nat)
8. [PAT](#8-pat)
9. [SNAT](#9-snat)
10. [DNAT](#10-dnat)
11. [SNAT vs DNAT](#11-snat-vs-dnat)
12. [NAT Gateway](#12-nat-gateway)
13. [NAT in AWS](#13-nat-in-aws)
14. [NAT in Docker](#14-nat-in-docker)
15. [NAT in Kubernetes](#15-nat-in-kubernetes)
16. [NAT vs Firewall](#16-nat-vs-firewall)
17. [Advantages of NAT](#17-advantages-of-nat)
18. [Limitations of NAT](#18-limitations-of-nat)
19. [DevOps Production Scenario](#19-devops-production-scenario)
20. [Important Commands](#20-important-commands)
21. [Key Points to Remember](#21-key-points-to-remember)

---

# 1. What is NAT?

**NAT stands for Network Address Translation.**

NAT is a networking technique that changes IP addresses, and sometimes port numbers, while network traffic passes through a router, firewall, or NAT device.

The most common use of NAT is:

```text
Private IP → Public IP
```

Example:

```text
Laptop
192.168.1.10
     |
     | NAT
     ↓
Router
Public IP: 49.x.x.x
     |
     ↓
Internet
```

The laptop uses a private IP address, while the Internet sees the public IP address.

---

# 2. Why NAT is Needed

IPv4 has a limited number of public IP addresses.

Private IP addresses can be reused inside different private networks.

NAT allows many devices with private IP addresses to communicate with the Internet using one or more public IP addresses.

Example:

```text
Device 1 → 192.168.1.10
Device 2 → 192.168.1.11
Device 3 → 192.168.1.12
                 |
                 ↓
              Router
                 |
                 ↓
          Public IP: 49.x.x.x
                 |
                 ↓
              Internet
```

This reduces the need for a unique public IPv4 address for every device.

---

# 3. Private and Public IP Addresses

## Private IP Address

Private IP addresses are used inside private networks.

The main IPv4 private ranges are:

```text
10.0.0.0/8

172.16.0.0/12

192.168.0.0/16
```

Examples:

```text
10.0.0.10
172.16.1.20
192.168.1.10
```

These addresses are not directly routable across the public Internet.

## Public IP Address

A public IP address is globally routable on the Internet.

Example:

```text
49.x.x.x
```

A public IP can be used to communicate with systems outside the private network.

---

# 4. How NAT Works

Suppose a laptop has:

```text
Private IP:
192.168.1.10
```

It wants to communicate with:

```text
Google DNS:
8.8.8.8
```

The original packet can look like:

```text
Source:
192.168.1.10

Destination:
8.8.8.8
```

The router performs NAT.

The Internet may see:

```text
Source:
49.x.x.x

Destination:
8.8.8.8
```

The router keeps track of the translation.

When the response returns, the router translates it back to the private IP.

```text
Internet
   |
   ↓
49.x.x.x
   |
   | NAT
   ↓
192.168.1.10
```

---

# 5. Types of NAT

Common NAT types include:

1. Static NAT
2. Dynamic NAT
3. PAT

NAT can also be discussed in terms of:

* SNAT
* DNAT

---

# 6. Static NAT

Static NAT creates a fixed one-to-one mapping between a private IP and a public IP.

Example:

```text
Private IP       Public IP

192.168.1.10  →  49.x.x.10
```

The mapping remains fixed.

### Use Case

A company has an internal server that must be reachable through a specific public IP.

```text
Internet
    |
    ↓
49.x.x.10
    |
    ↓
192.168.1.10
```

---

# 7. Dynamic NAT

Dynamic NAT maps private IP addresses to public IP addresses from a pool.

Example:

```text
Private IP       Public IP

192.168.1.10  →  49.x.x.10
192.168.1.11  →  49.x.x.11
192.168.1.12  →  49.x.x.12
```

The NAT device chooses an available public IP from the pool.

---

# 8. PAT

**PAT stands for Port Address Translation.**

PAT allows multiple private devices to share a single public IP address.

It uses different port numbers to identify individual connections.

Example:

```text
192.168.1.10:5000
192.168.1.11:5001
192.168.1.12:5002
```

can be translated to:

```text
49.x.x.x:30001
49.x.x.x:30002
49.x.x.x:30003
```

PAT is also commonly called:

```text
NAT Overload
```

PAT is widely used in home and enterprise networks.

---

# 9. SNAT

**SNAT stands for Source Network Address Translation.**

SNAT changes the source IP address of a packet.

Example:

```text
Private Server
10.0.1.20
     |
     | SNAT
     ↓
Public IP
54.x.x.x
     |
     ↓
Internet
```

The source address changes from:

```text
10.0.1.20
```

to:

```text
54.x.x.x
```

### Common Use

Private servers need to initiate outbound connections to the Internet.

Examples:

* Downloading software packages
* Accessing external APIs
* Downloading updates
* Pulling container images

---

# 10. DNAT

**DNAT stands for Destination Network Address Translation.**

DNAT changes the destination IP address of a packet.

Example:

```text
Internet
    |
    ↓
Public IP
54.x.x.x
    |
    | DNAT
    ↓
Private Server
10.0.1.20
```

The destination changes from:

```text
54.x.x.x
```

to:

```text
10.0.1.20
```

DNAT is commonly used for forwarding traffic from a public address to an internal server.

---

# 11. SNAT vs DNAT

| Feature          | SNAT                                 | DNAT                                    |
| ---------------- | ------------------------------------ | --------------------------------------- |
| Full name        | Source Network Address Translation   | Destination Network Address Translation |
| Changes          | Source IP                            | Destination IP                          |
| Common direction | Outbound                             | Inbound                                 |
| Example          | Private server → Internet            | Internet → Private server               |
| Common use       | Private resources accessing Internet | Port/address forwarding                 |

### Easy Memory Trick

```text
SNAT → Source changes

DNAT → Destination changes
```

---

# 12. NAT Gateway

A NAT Gateway provides a way for resources in a private network to access external networks.

A common architecture is:

```text
Private Server
      |
      ↓
 NAT Gateway
      |
      ↓
   Internet
```

The private server does not need its own public IP for outbound Internet access.

---

# 13. NAT in AWS

NAT is very important in AWS networking.

A common AWS architecture looks like:

```text
                    Internet
                       |
                       ↓
               Internet Gateway
                       |
                Public Subnet
                       |
                  NAT Gateway
                       |
                Private Subnet
                       |
                 EC2 Instance
```

A private EC2 instance can use the NAT Gateway for outbound Internet access.

For example:

```text
EC2
10.0.2.15
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

### Why use a NAT Gateway?

Private instances can:

* Download updates
* Install packages
* Access external APIs
* Download dependencies
* Pull container images

without requiring public IP addresses on the instances.

### Important AWS Components

When troubleshooting NAT in AWS, check:

```text
VPC
↓
Subnet
↓
Route Table
↓
NAT Gateway
↓
Internet Gateway
```

---

# 14. NAT in Docker

Docker networking also uses NAT.

Check Docker networks:

```bash
docker network ls
```

Inspect the default bridge network:

```bash
docker network inspect bridge
```

A Docker container may have an IP such as:

```text
172.17.0.2
```

The Docker host may have another IP such as:

```text
192.168.1.10
```

Docker networking can use NAT rules to allow containers to communicate outside their container network.

Inspect NAT rules:

```bash
sudo iptables -t nat -L -n -v
```

On systems using nftables:

```bash
sudo nft list ruleset
```

---

# 15. NAT in Kubernetes

NAT can also appear in Kubernetes networking.

A simplified example:

```text
Pod
10.244.x.x
   |
   ↓
Kubernetes Node
192.168.x.x
   |
   ↓
Internet
```

Depending on the CNI and network configuration, traffic leaving the cluster may be translated.

Important Kubernetes networking concepts related to NAT include:

* Pod IP
* Service IP
* ClusterIP
* Node IP
* NodePort
* LoadBalancer
* kube-proxy
* iptables
* IPVS
* CNI

### Production Troubleshooting Example

If a Pod can communicate with another Pod but cannot access the Internet, investigate:

```text
Pod IP
↓
Node routing
↓
NAT
↓
Firewall
↓
Internet
```

---

# 16. NAT vs Firewall

NAT and firewalls are different concepts.

### NAT

NAT translates addresses and/or ports.

```text
Private IP → Public IP
```

### Firewall

A firewall controls whether network traffic is allowed or denied.

```text
Allow → Traffic passes

Deny → Traffic blocked
```

A device can perform both NAT and firewall functions.

---

# 17. Advantages of NAT

### 1. Conserves IPv4 addresses

Many private devices can share public IP addresses.

### 2. Allows private resources to access the Internet

Private systems can communicate externally without individual public IPs.

### 3. Hides private addressing

Internal IP addresses are not directly exposed to the Internet.

### 4. Useful in cloud environments

NAT is commonly used with private subnets.

### 5. Useful in container networking

Docker and Kubernetes networking can involve address translation.

---

# 18. Limitations of NAT

NAT also has disadvantages.

### 1. Adds complexity

Troubleshooting becomes more difficult because addresses are translated.

### 2. Can affect end-to-end connectivity

Applications may need additional configuration when direct connections are required.

### 3. Port limitations

PAT relies on port numbers and therefore has scalability limits.

### 4. Troubleshooting can be harder

You may need to inspect:

```text
Source IP
Destination IP
Source Port
Destination Port
NAT rules
Routing
Firewall rules
```

---

# 19. DevOps Production Scenario

Imagine a production application:

```text
                         Internet
                            |
                            ↓
                       Load Balancer
                            |
                            ↓
                     Public Subnet
                            |
              -------------------------
              |                       |
              ↓                       ↓
        Private EC2              Private EC2
        10.0.2.10                10.0.2.11
              \                       /
               \                     /
                ↓                   ↓
                    NAT Gateway
                         |
                         ↓
                      Internet
```

The application servers are private.

They do not need public IP addresses.

But they may need Internet access for:

```text
apt update
pip install
npm install
docker pull
API calls
software updates
```

The NAT Gateway provides outbound connectivity.

### Production troubleshooting

If the EC2 instance cannot access the Internet, check:

```text
1. EC2 private IP
2. Network interface
3. Default route
4. Route table
5. NAT Gateway
6. NAT Gateway subnet
7. Internet Gateway
8. Security Group
9. Network ACL
10. DNS
```

---

# 20. Important Commands

### Display IP addresses

```bash
ip addr
```

### Display network interfaces

```bash
ip link
```

### Display routing table

```bash
ip route
```

### Display listening ports

```bash
ss -tuln
```

### Test Internet connectivity

```bash
ping -c 4 8.8.8.8
```

### Test DNS resolution

```bash
ping -c 4 google.com
```

### Trace network path

```bash
traceroute google.com
```

or:

```bash
tracepath google.com
```

### Inspect iptables NAT rules

```bash
sudo iptables -t nat -L -n -v
```

### Inspect nftables rules

```bash
sudo nft list ruleset
```

### Inspect Docker networks

```bash
docker network ls
```

### Inspect Docker bridge network

```bash
docker network inspect bridge
```

---

# 21. Key Points to Remember

```text
NAT
→ Network Address Translation

Private IP
→ Used inside private networks

Public IP
→ Globally routable address

Static NAT
→ One private IP ↔ one public IP

Dynamic NAT
→ Private IP → public IP from a pool

PAT
→ Many private IPs → one public IP using ports

SNAT
→ Changes source address

DNAT
→ Changes destination address

NAT Gateway
→ Allows private resources to initiate outbound Internet connections
```

## DevOps Connection

```text
Linux
   ↓
Networking
   ↓
NAT
   ↓
AWS VPC
   ↓
Private Subnets
   ↓
NAT Gateway
   ↓
Docker Networking
   ↓
Kubernetes Networking
```

Understanding NAT is important for **Linux networking, AWS, Docker, Kubernetes, and production troubleshooting**.
