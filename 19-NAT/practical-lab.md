# Chapter 19 — NAT Practical Lab

## Objective

In this lab, we will practically investigate:

* Local IP addresses
* Network interfaces
* Default gateway
* Routing table
* Internet connectivity
* DNS connectivity
* Public IP
* NAT rules
* Docker networking
* Network path
* Production-style NAT troubleshooting

---

# Lab 1 — Check Your IP Address

Run:

```bash
ip addr
```

or:

```bash
ip a
```

### What to observe

Look for your active network interface.

Common interfaces include:

```text
lo
wlo1
eth0
enp0s3
docker0
```

Look for a line similar to:

```text
inet 192.168.x.x/24
```

### Record your observation

```text
Interface:
Private IP:
Subnet:
```

---

# Lab 2 — Check Network Interfaces

Run:

```bash
ip link
```

### What to observe

Check:

* Interface names
* Interface state
* MAC addresses

You may see:

```text
lo
wlo1
docker0
```

An active interface normally shows:

```text
state UP
```

---

# Lab 3 — Check the Routing Table

Run:

```bash
ip route
```

Example:

```text
default via 192.168.1.1 dev wlo1
192.168.1.0/24 dev wlo1
```

### Identify

```text
Default gateway:
Network:
Interface:
```

### Important observation

The default route:

```text
default via 192.168.1.1
```

is used when the destination does not match a more specific route.

---

# Lab 4 — Check Only the Default Route

Run:

```bash
ip route | grep default
```

Expected format:

```text
default via <gateway-ip> dev <interface>
```

Record:

```text
Gateway:
Interface:
```

---

# Lab 5 — Test Internet Connectivity Using an IP

Run:

```bash
ping -c 4 8.8.8.8
```

### Expected result

You should receive replies if ICMP connectivity is allowed.

Example:

```text
64 bytes from 8.8.8.8
```

### Observation

```text
Packets transmitted:
Packets received:
Packet loss:
```

---

# Lab 6 — Test DNS and Internet Connectivity

Run:

```bash
ping -c 4 google.com
```

### Compare

First:

```bash
ping -c 4 8.8.8.8
```

Then:

```bash
ping -c 4 google.com
```

### Interpretation

If both work:

```text
IP connectivity → Working
DNS → Working
```

If IP works but domain name fails:

```text
IP connectivity → Working
DNS → Investigate
```

---

# Lab 7 — Check DNS Configuration

Run:

```bash
cat /etc/resolv.conf
```

Look for:

```text
nameserver
```

Example:

```text
nameserver 127.0.0.53
```

or another DNS server.

---

# Lab 8 — Check Public IP

Run:

```bash
curl ifconfig.me
```

You can also run:

```bash
curl https://api.ipify.org
```

### Compare

Your local/private IP:

```text
192.168.x.x
```

Public IP:

```text
<public-ip>
```

### Observation

```text
Private IP:
Public IP:
```

This demonstrates the basic idea behind NAT:

```text
Private IP
    ↓
NAT
    ↓
Public IP
    ↓
Internet
```

---

# Lab 9 — Inspect NAT Rules

Run:

```bash
sudo iptables -t nat -L -n -v
```

### What to observe

Look for NAT chains such as:

```text
PREROUTING
INPUT
OUTPUT
POSTROUTING
```

You may also see Docker-related rules if Docker is installed.

---

# Lab 10 — Inspect POSTROUTING

Run:

```bash
sudo iptables -t nat -L POSTROUTING -n -v
```

### Why?

POSTROUTING is an important location for source NAT operations.

Look for rules involving:

```text
MASQUERADE
SNAT
```

---

# Lab 11 — Inspect PREROUTING

Run:

```bash
sudo iptables -t nat -L PREROUTING -n -v
```

### Why?

PREROUTING is commonly used for traffic transformations before the routing decision.

Look for:

```text
DNAT
```

or port-forwarding related rules.

---

# Lab 12 — Check nftables

Modern Linux systems may use nftables.

Run:

```bash
sudo nft list ruleset
```

### What to observe

Look for:

```text
table
chain
rule
```

If your system does not have a NAT table, that is okay.

Do not modify anything during this lab.

---

# Lab 13 — Check Network Neighbors

Run:

```bash
ip neigh
```

Example:

```text
192.168.1.1 dev wlo1 lladdr xx:xx:xx:xx:xx:xx REACHABLE
```

### What this tells you

It provides information about devices on the local network that your system has recently communicated with.

---

# Lab 14 — Check Listening Ports

Run:

```bash
ss -tuln
```

### Observe

Look for ports such as:

```text
22
80
443
8080
```

Remember:

```text
22  → SSH
80  → HTTP
443 → HTTPS
```

---

# Lab 15 — Check Processes Using Ports

Run:

```bash
sudo ss -ltnp
```

### Purpose

Shows listening TCP ports and associated processes.

This is very useful in production troubleshooting.

---

# Lab 16 — Test a Specific Port

Use:

```bash
nc -zv google.com 443
```

### Expected

You may see something similar to:

```text
Connection to google.com 443 port [tcp/https] succeeded!
```

This checks TCP connectivity to port 443.

---

# Lab 17 — Test HTTPS

Run:

```bash
curl -I https://google.com
```

### What this tests

```text
DNS
 ↓
Network connectivity
 ↓
TCP
 ↓
TLS
 ↓
HTTP/HTTPS
```

This is useful when troubleshooting application connectivity.

---

# Lab 18 — Trace the Network Path

Run:

```bash
traceroute google.com
```

If unavailable:

```bash
tracepath google.com
```

### What to observe

You may see multiple hops between your machine and the destination.

Example:

```text
1   192.168.1.1
2   ...
3   ...
4   ...
```

This helps identify where traffic is traveling.

---

# Lab 19 — Docker Network Investigation

First check whether Docker is installed:

```bash
docker --version
```

If Docker is running, list networks:

```bash
docker network ls
```

You may see:

```text
bridge
host
none
```

---

# Lab 20 — Inspect Docker Bridge

Run:

```bash
docker network inspect bridge
```

### Look for

```text
Subnet
Gateway
Containers
IP addresses
```

A common Docker bridge network may use:

```text
172.17.0.0/16
```

---

# Lab 21 — Check Docker NAT Rules

Run:

```bash
sudo iptables -t nat -L -n -v
```

Look for Docker-related rules.

You may see chains such as:

```text
DOCKER
DOCKER-USER
```

The exact output depends on your Docker and Linux configuration.

---

# Lab 22 — Create a Test Docker Container

If Docker is available, run:

```bash
docker run -d --name nat-test nginx
```

Check:

```bash
docker ps
```

Then inspect:

```bash
docker inspect nat-test
```

Find the container IP:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' nat-test
```

---

# Lab 23 — Check Container Network

Run:

```bash
docker exec nat-test ip addr
```

If the image does not contain `ip`, inspect the Docker network instead:

```bash
docker network inspect bridge
```

### Observe

Compare:

```text
Host IP
Container IP
Docker bridge IP
```

---

# Lab 24 — Test Container Internet Connectivity

Run:

```bash
docker exec nat-test curl -I https://google.com
```

If `curl` is not installed in the image, use another suitable test container.

The important concept is:

```text
Container
    ↓
Docker Network
    ↓
NAT
    ↓
Host
    ↓
Internet
```

---

# Lab 25 — Clean Up Docker Container

After completing the Docker lab:

```bash
docker stop nat-test
```

Then:

```bash
docker rm nat-test
```

Verify:

```bash
docker ps
```

---

# Lab 26 — Production-Style Troubleshooting

Imagine this situation:

> A private server cannot access the Internet.

Follow this sequence.

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

### Step 4 — Check gateway

```bash
ip route | grep default
```

### Step 5 — Test Internet by IP

```bash
ping -c 4 8.8.8.8
```

### Step 6 — Test DNS

```bash
ping -c 4 google.com
```

### Step 7 — Check DNS

```bash
cat /etc/resolv.conf
```

### Step 8 — Check NAT

```bash
sudo iptables -t nat -L -n -v
```

### Step 9 — Check firewall rules

```bash
sudo nft list ruleset
```

### Step 10 — Trace the path

```bash
tracepath google.com
```

---

# Lab 27 — Troubleshooting Decision Tree

```text
Cannot access Internet
        |
        ↓
Does system have an IP?
        |
       Yes
        ↓
Is interface UP?
        |
       Yes
        ↓
Is default route present?
        |
       Yes
        ↓
Can reach 8.8.8.8?
       / \
     Yes  No
      |    |
      |    ↓
      |  Check routing/NAT/firewall
      ↓
Can resolve google.com?
     / \
   Yes  No
    |    |
    |    ↓
    |  Check DNS
    ↓
Check application/port
```

---

# Lab 28 — Record Your Results

Complete this section after performing the lab.

```text
## My Results

### Network Interface

Interface:

### Private IP

Private IP:

### Default Gateway

Gateway:

### Default Route

Route:

### DNS Server

DNS:

### Public IP

Public IP:

### Docker Network

Docker subnet:

### Docker Gateway

Docker gateway:

### NAT Rules Found

NAT rules:

### Internet Connectivity

8.8.8.8:

### DNS Connectivity

google.com:

### HTTPS Connectivity

google.com:443:
```

---

# Lab 29 — Screenshots to Capture

Take screenshots of important practical results.

Recommended screenshots:

```text
01-ip-address.png
02-network-interfaces.png
03-routing-table.png
04-default-gateway.png
05-internet-connectivity.png
06-dns-test.png
07-public-ip.png
08-nat-rules.png
09-nftables.png
10-docker-networks.png
11-docker-network-inspect.png
12-docker-nat.png
13-traceroute.png
```

Store them in:

```text
19-NAT/screenshots/
```

---

# Lab 30 — Final Understanding

After completing this lab, you should be able to explain:

```text
Private IP
    ↓
Default Gateway
    ↓
Routing
    ↓
NAT
    ↓
Public IP
    ↓
Internet
```

You should also understand how similar concepts appear in:

```text
Linux
Docker
AWS
Kubernetes
```

## Key DevOps Skill

Do not just memorize NAT.

Be able to troubleshoot it.

When a production workload cannot communicate externally, identify:

```text
IP
↓
Interface
↓
Route
↓
Gateway
↓
NAT
↓
Firewall
↓
DNS
↓
Port
↓
Application
```
