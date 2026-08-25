# Chapter 20 — Gateway Commands

## Table of Contents

1. [Check IP Address](#1-check-ip-address)
2. [Check Network Interfaces](#2-check-network-interfaces)
3. [Check Routing Table](#3-check-routing-table)
4. [Find Default Gateway](#4-find-default-gateway)
5. [Find Route to a Specific Destination](#5-find-route-to-a-specific-destination)
6. [Check Gateway Reachability](#6-check-gateway-reachability)
7. [Check Internet Connectivity](#7-check-internet-connectivity)
8. [Check DNS Configuration](#8-check-dns-configuration)
9. [Check DNS Resolution](#9-check-dns-resolution)
10. [Check Neighbor Table](#10-check-neighbor-table)
11. [Check Interface Statistics](#11-check-interface-statistics)
12. [Trace Network Path](#12-trace-network-path)
13. [Check Listening Ports](#13-check-listening-ports)
14. [Check Processes Using Ports](#14-check-processes-using-ports)
15. [Test HTTPS Connectivity](#15-test-https-connectivity)
16. [Test a Specific TCP Port](#16-test-a-specific-tcp-port)
17. [Check Public IP](#17-check-public-ip)
18. [Check NetworkManager](#18-check-networkmanager)
19. [Check Network Connections](#19-check-network-connections)
20. [Check Firewall](#20-check-firewall)
21. [Check iptables NAT Rules](#21-check-iptables-nat-rules)
22. [Check nftables](#22-check-nftables)
23. [AWS Internet Gateway](#23-aws-internet-gateway)
24. [AWS NAT Gateway](#24-aws-nat-gateway)
25. [AWS Transit Gateway](#25-aws-transit-gateway)
26. [AWS Route Tables](#26-aws-route-tables)
27. [Docker Networks](#27-docker-networks)
28. [Inspect Docker Gateway](#28-inspect-docker-gateway)
29. [Inspect Docker Container](#29-inspect-docker-container)
30. [Find Docker Container IP](#30-find-docker-container-ip)
31. [Practical Gateway Troubleshooting](#31-practical-gateway-troubleshooting)
32. [Production Troubleshooting Workflow](#32-production-troubleshooting-workflow)
33. [Gateway Troubleshooting Decision Tree](#33-gateway-troubleshooting-decision-tree)
34. [Most Important Gateway Commands](#34-most-important-gateway-commands)

---

# 1. Check IP Address

```bash
ip addr
```

Short form:

```bash
ip a
```

### Purpose

Displays IP addresses assigned to network interfaces.

### Example

```text
wlo1:
    inet 192.168.1.10/24
```

### What to observe

```text
Interface:
IP address:
Subnet:
```

### Production Use

Use this command when you need to determine the server's IP address and identify which network interface is being used.

---

# 2. Check Network Interfaces

```bash
ip link
```

### Purpose

Displays network interfaces and their state.

Example:

```text
lo
wlo1
docker0
```

Look for:

```text
state UP
```

### Production Use

Useful when checking whether a network interface is active.

---

# 3. Check Routing Table

```bash
ip route
```

### Purpose

Displays the Linux routing table.

Example:

```text
default via 192.168.1.1 dev wlo1
192.168.1.0/24 dev wlo1 proto kernel scope link src 192.168.1.10
```

The important line is:

```text
default via 192.168.1.1 dev wlo1
```

This means:

```text
Gateway:
192.168.1.1

Interface:
wlo1
```

### Production Use

Use this when troubleshooting connectivity between networks.

---

# 4. Find Default Gateway

```bash
ip route | grep default
```

Example:

```text
default via 192.168.1.1 dev wlo1
```

### Meaning

```text
default
    ↓
Used when there is no more specific route

via 192.168.1.1
    ↓
Gateway

dev wlo1
    ↓
Network interface
```

### Production Use

One of the most important commands when troubleshooting Internet connectivity.

---

# 5. Find Route to a Specific Destination

```bash
ip route get 8.8.8.8
```

Example:

```text
8.8.8.8 via 192.168.1.1 dev wlo1 src 192.168.1.10
```

### This tells you

```text
Destination → 8.8.8.8
Gateway     → 192.168.1.1
Interface   → wlo1
Source IP   → 192.168.1.10
```

### Why is this important?

It shows the exact route Linux will use to reach a specific destination.

### Production Use

Very useful when a server has multiple network interfaces or multiple routes.

---

# 6. Check Gateway Reachability

Replace the IP with your actual gateway:

```bash
ping -c 4 192.168.1.1
```

### Purpose

Tests whether your machine can reach its local gateway.

### Successful result

```text
64 bytes from 192.168.1.1
```

### Failure

```text
Destination Host Unreachable
```

### Production Use

If the gateway cannot be reached, investigate the local network before investigating the Internet.

---

# 7. Check Internet Connectivity

```bash
ping -c 4 8.8.8.8
```

### Purpose

Tests basic IP connectivity to the Internet.

### Interpretation

If it works:

```text
IP connectivity → Working
```

If it fails, investigate:

```text
Routing
Gateway
Firewall
NAT
Network connectivity
```

---

# 8. Check DNS Configuration

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

### Purpose

Shows DNS resolver configuration.

---

# 9. Check DNS Resolution

Use:

```bash
getent hosts google.com
```

You can also use:

```bash
nslookup google.com
```

or:

```bash
dig google.com
```

### Purpose

Checks whether a domain name can be resolved to an IP address.

### Important troubleshooting example

If:

```bash
ping -c 4 8.8.8.8
```

works but:

```bash
ping -c 4 google.com
```

fails, investigate DNS.

---

# 10. Check Neighbor Table

```bash
ip neigh
```

Example:

```text
192.168.1.1 dev wlo1 lladdr aa:bb:cc:dd:ee:ff REACHABLE
```

### What this shows

```text
Gateway IP:
192.168.1.1

Gateway MAC:
aa:bb:cc:dd:ee:ff

State:
REACHABLE
```

### Purpose

Displays IP-to-MAC information for nearby devices.

For IPv4, this information is commonly learned using ARP.

---

# 11. Check Interface Statistics

```bash
ip -s link
```

### Look for

```text
RX packets
TX packets
errors
dropped
```

### Production Use

Useful when investigating:

- Packet drops
- Interface errors
- Network problems
- Hardware/interface issues

---

# 12. Trace Network Path

Use:

```bash
tracepath google.com
```

If `tracepath` is not installed:

```bash
traceroute google.com
```

### Purpose

Shows the network hops between your machine and the destination.

Example:

```text
1   192.168.1.1
2   ...
3   ...
4   ...
```

### Production Use

Useful for identifying where traffic stops or where latency increases.

---

# 13. Check Listening Ports

```bash
ss -tuln
```

### Purpose

Shows listening TCP and UDP ports.

Example:

```text
22
80
443
8080
```

Common ports:

```text
22   → SSH
80   → HTTP
443  → HTTPS
```

---

# 14. Check Processes Using Ports

```bash
sudo ss -ltnp
```

### Purpose

Shows listening TCP ports and associated processes.

### Example

If an application should listen on port `8080`:

```bash
sudo ss -ltnp | grep 8080
```

If nothing appears, the application may not be listening.

---

# 15. Test HTTPS Connectivity

```bash
curl -I https://google.com
```

For detailed information:

```bash
curl -v https://google.com
```

### What this can test

```text
DNS
 ↓
TCP
 ↓
TLS
 ↓
HTTP/HTTPS
```

### Production Use

Useful when `ping` works but the application still cannot communicate.

---

# 16. Test a Specific TCP Port

```bash
nc -zv google.com 443
```

### Purpose

Tests whether TCP port `443` is reachable.

Example:

```text
Connection to google.com 443 port [tcp/https] succeeded!
```

### Production Use

Useful for checking application ports without testing the full application.

---

# 17. Check Public IP

```bash
curl ifconfig.me
```

Another option:

```bash
curl https://api.ipify.org
```

### Purpose

Shows the public IP visible to an external service.

This is useful when investigating NAT.

Example:

```text
Private IP
192.168.1.10

       ↓

NAT

       ↓

Public IP
x.x.x.x
```

---

# 18. Check NetworkManager

```bash
nmcli device status
```

Example:

```text
DEVICE   TYPE      STATE
wlo1     wifi      connected
lo       loopback  connected
```

### Purpose

Shows network devices and their connection status.

---

# 19. Check Network Connections

```bash
nmcli connection show
```

### Purpose

Displays configured NetworkManager connections.

---

# 20. Check Firewall

On Ubuntu systems using UFW:

```bash
sudo ufw status
```

For more detailed output:

```bash
sudo ufw status verbose
```

### Purpose

Checks whether the host firewall is active and what rules are configured.

---

# 21. Check iptables NAT Rules

```bash
sudo iptables -t nat -L -n -v
```

### Look for

```text
SNAT
DNAT
MASQUERADE
```

### Purpose

Displays NAT rules configured through iptables.

### Production Use

Useful when investigating:

- NAT problems
- Port forwarding
- Docker networking
- Outbound connectivity

---

# 22. Check nftables

```bash
sudo nft list ruleset
```

### Purpose

Displays the nftables ruleset.

Modern Linux systems may use nftables instead of traditional iptables rules.

---

# AWS Gateway Commands

# 23. AWS Internet Gateway

List Internet Gateways:

```bash
aws ec2 describe-internet-gateways
```

### Purpose

Displays Internet Gateways in the AWS account/region used by the AWS CLI.

---

# 24. AWS NAT Gateway

List NAT Gateways:

```bash
aws ec2 describe-nat-gateways
```

### Purpose

Displays NAT Gateway information.

Useful when troubleshooting private subnet Internet access.

---

# 25. AWS Transit Gateway

List Transit Gateways:

```bash
aws ec2 describe-transit-gateways
```

### Purpose

Displays Transit Gateway information.

Transit Gateway is commonly used to connect multiple VPCs and networks through a central networking hub.

---

# 26. AWS Route Tables

List route tables:

```bash
aws ec2 describe-route-tables
```

### Look for

```text
Destination
Target
Gateway
NAT Gateway
Transit Gateway
Subnet
```

### Production Use

When an AWS instance cannot communicate with another network, route tables should be one of the first things checked.

---

# Docker Gateway Commands

# 27. List Docker Networks

```bash
docker network ls
```

Example:

```text
NETWORK ID     NAME      DRIVER
xxxxxx         bridge    bridge
xxxxxx         host      host
xxxxxx         none      null
```

### Purpose

Displays Docker networks.

---

# 28. Inspect Docker Gateway

```bash
docker network inspect bridge
```

Look for:

```text
Subnet
Gateway
Containers
```

Example:

```text
Subnet:
172.17.0.0/16

Gateway:
172.17.0.1
```

### Meaning

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
```

---

# 29. Inspect Docker Container

```bash
docker inspect <container-name>
```

Example:

```bash
docker inspect nginx
```

### Purpose

Displays detailed container configuration, including network information.

---

# 30. Find Docker Container IP

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container-name>
```

Example:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' nginx
```

### Purpose

Finds the container's IP address.

---

# 31. Practical Gateway Troubleshooting

Suppose a production server cannot access an external API.

Start with:

### Step 1 — Check IP

```bash
ip addr
```

### Step 2 — Check interface

```bash
ip link
```

### Step 3 — Check routing table

```bash
ip route
```

### Step 4 — Check default gateway

```bash
ip route | grep default
```

### Step 5 — Find exact route

```bash
ip route get <destination-ip>
```

### Step 6 — Check neighbor table

```bash
ip neigh
```

### Step 7 — Test gateway

```bash
ping -c 4 <gateway-ip>
```

### Step 8 — Test Internet by IP

```bash
ping -c 4 8.8.8.8
```

### Step 9 — Test DNS

```bash
getent hosts google.com
```

### Step 10 — Test application port

```bash
nc -zv <host> <port>
```

### Step 11 — Test application

```bash
curl -v https://<host>
```

### Step 12 — Check firewall

```bash
sudo ufw status verbose
```

### Step 13 — Check NAT

```bash
sudo iptables -t nat -L -n -v
```

### Step 14 — Check nftables

```bash
sudo nft list ruleset
```

---

# 32. Production Troubleshooting Workflow

When troubleshooting a gateway problem, follow this order:

```text
Application
    ↓
Network Interface
    ↓
IP Address
    ↓
Routing Table
    ↓
Default Gateway
    ↓
NAT / Firewall
    ↓
DNS
    ↓
Destination Port
    ↓
Remote Application
```

### Command Sequence

```bash
ip addr
```

```bash
ip link
```

```bash
ip route
```

```bash
ip route | grep default
```

```bash
ip route get <destination-ip>
```

```bash
ip neigh
```

```bash
ping -c 4 <gateway-ip>
```

```bash
ping -c 4 8.8.8.8
```

```bash
getent hosts google.com
```

```bash
nc -zv <host> <port>
```

```bash
curl -v https://<host>
```

```bash
sudo iptables -t nat -L -n -v
```

```bash
sudo nft list ruleset
```

---

# 33. Gateway Troubleshooting Decision Tree

```text
Application cannot connect
          |
          ↓
Does server have an IP?
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
Can gateway be reached?
       /       \
     Yes        No
      |          |
      ↓          ↓
Can Internet    Check local
be reached?     network
   /    \
 Yes     No
  |       |
  ↓       ↓
Check     Check
DNS       route/NAT/
          firewall
  |
  ↓
Can destination port
be reached?
  |
  ↓
Check application
```

---

# 34. Most Important Gateway Commands

If you cannot remember every command, remember these:

### Check IP

```bash
ip addr
```

### Check interfaces

```bash
ip link
```

### Check routes

```bash
ip route
```

### Find default gateway

```bash
ip route | grep default
```

### Find exact route

```bash
ip route get 8.8.8.8
```

### Check neighbor/ARP information

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
getent hosts google.com
```

### Check listening ports

```bash
ss -tuln
```

### Test TCP port

```bash
nc -zv <host> <port>
```

### Test application

```bash
curl -v https://<host>
```

### Check Docker gateway

```bash
docker network inspect bridge
```

### Check NAT

```bash
sudo iptables -t nat -L -n -v
```

### Check nftables

```bash
sudo nft list ruleset
```

---

# Gateway Command Cheat Sheet

| Command | Purpose |
|---|---|
| `ip addr` | Check IP addresses |
| `ip link` | Check network interfaces |
| `ip route` | Display routing table |
| `ip route \| grep default` | Find default gateway |
| `ip route get <IP>` | Find exact route |
| `ip neigh` | Check neighbor/ARP information |
| `ip -s link` | Check interface statistics |
| `ping <gateway>` | Test gateway connectivity |
| `ping 8.8.8.8` | Test Internet connectivity |
| `getent hosts google.com` | Test DNS resolution |
| `nslookup google.com` | Query DNS |
| `dig google.com` | Detailed DNS query |
| `tracepath` | Trace network path |
| `traceroute` | Trace network path |
| `ss -tuln` | Check listening ports |
| `ss -ltnp` | Check listening processes |
| `nc -zv` | Test TCP port |
| `curl -v` | Test application connectivity |
| `ip -s link` | Check packet/errors statistics |
| `nmcli device status` | Check NetworkManager devices |
| `docker network ls` | List Docker networks |
| `docker network inspect bridge` | Inspect Docker gateway |
| `docker inspect` | Inspect container networking |
| `iptables -t nat` | Inspect NAT rules |
| `nft list ruleset` | Inspect nftables |
| `aws ec2 describe-internet-gateways` | List AWS Internet Gateways |
| `aws ec2 describe-nat-gateways` | List AWS NAT Gateways |
| `aws ec2 describe-transit-gateways` | List AWS Transit Gateways |
| `aws ec2 describe-route-tables` | List AWS route tables |

---

# Important Production Rule

When troubleshooting a gateway problem, do not immediately assume that the gateway is broken.

Follow the path:

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

The most important Linux commands to remember are:

```bash
ip addr
ip route
ip route | grep default
ip route get <destination-ip>
ip neigh
ping <gateway-ip>
ping 8.8.8.8
getent hosts google.com
ss -tuln
curl -v https://<host>
```

These commands are useful for everyday Linux networking and DevOps production troubleshooting.