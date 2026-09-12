# Chapter 20 — Gateway Interview Questions

## Table of Contents

1. [What is a Gateway?](#1-what-is-a-gateway)
2. [What is a Default Gateway?](#2-what-is-a-default-gateway)
3. [Why do we need a Gateway?](#3-why-do-we-need-a-gateway)
4. [What is a Default Route?](#4-what-is-a-default-route)
5. [How do you check the Gateway in Linux?](#5-how-do-you-check-the-gateway-in-linux)
6. [What does `default via` mean?](#6-what-does-default-via-mean)
7. [What is the difference between Gateway and Router?](#7-what-is-the-difference-between-gateway-and-router)
8. [What happens when a server sends traffic outside its network?](#8-what-happens-when-a-server-sends-traffic-outside-its-network)
9. [How does a host know whether a destination is local or remote?](#9-how-does-a-host-know-whether-a-destination-is-local-or-remote)
10. [What is the relationship between Gateway and Routing?](#10-what-is-the-relationship-between-gateway-and-routing)
11. [How do you find the exact route to a destination?](#11-how-do-you-find-the-exact-route-to-a-destination)
12. [What is the role of ARP when communicating with a Gateway?](#12-what-is-the-role-of-arp-when-communicating-with-a-gateway)
13. [How do you check ARP/neighbor information in Linux?](#13-how-do-you-check-arpneighbor-information-in-linux)
14. [What is the difference between Gateway and DNS?](#14-what-is-the-difference-between-gateway-and-dns)
15. [What is the relationship between Gateway and NAT?](#15-what-is-the-relationship-between-gateway-and-nat)
16. [How would you troubleshoot a server that cannot access the Internet?](#16-how-would-you-troubleshoot-a-server-that-cannot-access-the-internet)
17. [What if the server can ping the Gateway but cannot reach the Internet?](#17-what-if-the-server-can-ping-the-gateway-but-cannot-reach-the-internet)
18. [What if the server can ping an IP but cannot access a domain name?](#18-what-if-the-server-can-ping-an-ip-but-cannot-access-a-domain-name)
19. [What if there is no default Gateway?](#19-what-if-there-is-no-default-gateway)
20. [What if the Gateway is unreachable?](#20-what-if-the-gateway-is-unreachable)
21. [What is an AWS Internet Gateway?](#21-what-is-an-aws-internet-gateway)
22. [What is an AWS NAT Gateway?](#22-what-is-an-aws-nat-gateway)
23. [What is an AWS Transit Gateway?](#23-what-is-an-aws-transit-gateway)
24. [Internet Gateway vs NAT Gateway](#24-internet-gateway-vs-nat-gateway)
25. [What is a Docker Gateway?](#25-what-is-a-docker-gateway)
26. [How do you check the Docker Gateway?](#26-how-do-you-check-the-docker-gateway)
27. [What is the Gateway concept in Kubernetes?](#27-what-is-the-gateway-concept-in-kubernetes)
28. [What commands do you commonly use to troubleshoot Gateways?](#28-what-commands-do-you-commonly-use-to-troubleshoot-gateways)
29. [Production Scenario: Application cannot reach an external API](#29-production-scenario-application-cannot-reach-an-external-api)
30. [Interview Quick Revision](#30-interview-quick-revision)

---

# 1. What is a Gateway?

### Answer

A Gateway is a network point that provides a path from one network to another.

In simple words:

> A Gateway is the way out of one network to reach another network.

Example:

```text
Server
192.168.1.10
     |
     ↓
Gateway
192.168.1.1
     |
     ↓
Internet
```

---

# 2. What is a Default Gateway?

### Answer

A Default Gateway is the device or network address that a host uses to send traffic when the destination is outside its local network.

For example:

```text
default via 192.168.1.1
```

means the server sends traffic for destinations without a more specific route through `192.168.1.1`.

---

# 3. Why do we need a Gateway?

### Answer

A Gateway is needed because a host can communicate directly with devices in its local network, but it needs another network device to reach networks outside its local network.

Example:

```text
Server
192.168.1.10
     |
     ↓
192.168.1.1
Gateway
     |
     ↓
Other Network
```

---

# 4. What is a Default Route?

### Answer

A Default Route is the route used when there is no more specific route available for the destination.

In IPv4, it is represented as:

```text
0.0.0.0/0
```

Example:

```text
default via 192.168.1.1 dev wlo1
```

This means traffic that does not match another route is sent through `192.168.1.1`.

---

# 5. How do you check the Gateway in Linux?

### Answer

I use:

```bash
ip route
```

or:

```bash
ip route | grep default
```

Example:

```text
default via 192.168.1.1 dev wlo1
```

Here:

```text
192.168.1.1
```

is the default Gateway.

---

# 6. What does `default via` mean?

Suppose I run:

```bash
ip route
```

and get:

```text
default via 192.168.1.1 dev wlo1
```

It means:

```text
default
→ Any destination without a more specific route

via 192.168.1.1
→ Send the packet to this Gateway

dev wlo1
→ Use the wlo1 network interface
```

---

# 7. What is the difference between Gateway and Router?

### Answer

A Router is a device or system that forwards packets between networks.

A Gateway is an entry or exit point between networks.

A router can act as a Gateway.

Example:

```text
Server
   |
   ↓
Router / Gateway
   |
   ↓
Internet
```

### Simple way to remember

```text
Router → Forwards traffic

Gateway → Entry/exit point
```

---

# 8. What happens when a server sends traffic outside its network?

Suppose:

```text
Server:
192.168.1.10/24

Gateway:
192.168.1.1
```

The server wants to reach:

```text
8.8.8.8
```

The server checks its routing table.

It determines that `8.8.8.8` is outside the local network.

Then it uses the default route:

```text
Server
192.168.1.10
     |
     ↓
Gateway
192.168.1.1
     |
     ↓
Other Routers
     |
     ↓
8.8.8.8
```

---

# 9. How does a host know whether a destination is local or remote?

### Answer

The host uses its IP address and subnet mask/prefix to determine whether the destination belongs to the local network.

For example:

```text
IP:
192.168.1.10/24
```

Local network:

```text
192.168.1.0/24
```

A destination such as:

```text
192.168.1.20
```

is local.

But:

```text
8.8.8.8
```

is outside the local network.

Therefore, the server uses its Gateway.

---

# 10. What is the relationship between Gateway and Routing?

### Answer

Routing determines where packets should go.

The Gateway is often the next-hop device used by a route.

Example:

```text
default via 192.168.1.1
```

The routing table tells Linux:

> For destinations that do not match another route, send the traffic to `192.168.1.1`.

So:

```text
Routing Table
      ↓
Chooses Route
      ↓
Gateway
      ↓
Next Network
```

---

# 11. How do you find the exact route to a destination?

Use:

```bash
ip route get 8.8.8.8
```

Example:

```text
8.8.8.8 via 192.168.1.1 dev wlo1 src 192.168.1.10
```

This shows:

```text
Destination → 8.8.8.8
Gateway → 192.168.1.1
Interface → wlo1
Source IP → 192.168.1.10
```

This is especially useful on servers with multiple interfaces or routes.

---

# 12. What is the role of ARP when communicating with a Gateway?

### Answer

For IPv4 on an Ethernet-like local network, the host needs the Gateway's MAC address to send the Ethernet frame to the Gateway.

The host can use ARP to discover it.

Example:

```text
Server
192.168.1.10
     |
     | ARP:
     | "Who has 192.168.1.1?"
     ↓
Gateway
192.168.1.1
MAC: aa:bb:cc:dd:ee:ff
```

After learning the MAC address, the host can send frames to the Gateway.

---

# 13. How do you check ARP/neighbor information in Linux?

Use:

```bash
ip neigh
```

Example:

```text
192.168.1.1 dev wlo1 lladdr aa:bb:cc:dd:ee:ff REACHABLE
```

This shows:

```text
IP Address
MAC Address
Interface
State
```

---

# 14. What is the difference between Gateway and DNS?

### Answer

They perform different jobs.

### DNS

DNS converts domain names into IP addresses.

```text
google.com
     ↓
IP address
```

### Gateway

Gateway provides a path to another network.

```text
Server
   ↓
Gateway
   ↓
Other Network
```

### Simple answer

> DNS tells me where the destination is. The Gateway helps me reach the destination network.

---

# 15. What is the relationship between Gateway and NAT?

### Answer

Gateway and NAT are different functions, but they are commonly used together.

Gateway:

```text
Provides a path between networks
```

NAT:

```text
Translates IP addresses and/or ports
```

Example:

```text
Private Server
192.168.1.10
      |
      ↓
Gateway
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

A home router commonly performs both Gateway and NAT functions.

---

# 16. How would you troubleshoot a server that cannot access the Internet?

### Answer

I would troubleshoot from the lower network layers toward the application.

First:

```bash
ip addr
```

Check the IP address.

Then:

```bash
ip link
```

Check whether the interface is UP.

Then:

```bash
ip route
```

Check the routing table.

Then:

```bash
ip route | grep default
```

Check the default Gateway.

Then:

```bash
ping -c 4 <gateway-ip>
```

Check Gateway connectivity.

Then:

```bash
ping -c 4 8.8.8.8
```

Check Internet connectivity by IP.

Then:

```bash
getent hosts google.com
```

Check DNS.

Finally:

```bash
curl -v https://google.com
```

Check application-level connectivity.

---

# 17. What if the server can ping the Gateway but cannot reach the Internet?

### Answer

If the Gateway is reachable but the Internet is not, I would investigate:

- Routing
- NAT
- Firewall
- Upstream connectivity
- Cloud route tables
- Security rules
- Network ACLs

I would check:

```bash
ip route
```

and:

```bash
sudo iptables -t nat -L -n -v
```

or:

```bash
sudo nft list ruleset
```

In AWS, I would also check route tables, Internet Gateway or NAT Gateway configuration, security groups, and network ACLs as appropriate.

---

# 18. What if the server can ping an IP but cannot access a domain name?

### Answer

That usually points toward a DNS problem.

For example:

```bash
ping -c 4 8.8.8.8
```

works.

But:

```bash
ping -c 4 google.com
```

fails.

I would check:

```bash
cat /etc/resolv.conf
```

and:

```bash
getent hosts google.com
```

I would then investigate the configured DNS resolver.

---

# 19. What if there is no default Gateway?

### Answer

If the server needs to communicate with networks outside its local subnet and there is no suitable route, external connectivity may fail.

I would check:

```bash
ip route
```

If there is no default route, I would investigate the network configuration.

I would **not blindly add a Gateway in production**. I would first understand how the server is supposed to be routed and then make the approved configuration change.

---

# 20. What if the Gateway is unreachable?

### Answer

I would check:

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
ip neigh
```

Then test the Gateway:

```bash
ping -c 4 <gateway-ip>
```

I would investigate:

- Interface status
- IP configuration
- Subnet configuration
- VLAN configuration
- ARP/neighbor resolution
- Local firewall
- Physical or virtual network connectivity

---

# 21. What is an AWS Internet Gateway?

### Answer

An AWS Internet Gateway, or IGW, is a VPC component that provides connectivity between a VPC and the Internet.

A typical public subnet path is:

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

A route can look conceptually like:

```text
0.0.0.0/0 → Internet Gateway
```

The instance also needs appropriate public addressing and security configuration for Internet communication.

---

# 22. What is an AWS NAT Gateway?

### Answer

An AWS NAT Gateway allows resources in a private subnet to initiate connections to external networks such as the Internet without making those resources directly Internet-reachable.

Typical architecture:

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

---

# 23. What is an AWS Transit Gateway?

### Answer

AWS Transit Gateway is a centralized network hub used to connect multiple VPCs and other networks.

Example:

```text
VPC A
   \
    \
VPC B ---- Transit Gateway ---- VPC C
    /
   /
On-Premises
```

It can simplify large network architectures.

---

# 24. Internet Gateway vs NAT Gateway

| Feature | Internet Gateway | NAT Gateway |
|---|---|---|
| Main purpose | VPC Internet connectivity | Outbound Internet access for private resources |
| Common subnet | Public subnet path | Private subnet path |
| Direct Internet reachability | Supports it when routing/addressing/security are configured | Does not make private instances directly Internet-reachable |
| Typical route | `0.0.0.0/0 → IGW` | `0.0.0.0/0 → NAT Gateway` |

### Easy way to remember

```text
Public subnet
     ↓
Internet Gateway
     ↓
Internet
```

```text
Private subnet
     ↓
NAT Gateway
     ↓
Internet Gateway
     ↓
Internet
```

---

# 25. What is a Docker Gateway?

### Answer

A Docker network can have its own Gateway.

For the default bridge network, a common example is:

```text
Subnet:
172.17.0.0/16

Gateway:
172.17.0.1
```

The Gateway provides a path between the Docker container network and the Docker host/network.

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
```

---

# 26. How do you check the Docker Gateway?

Use:

```bash
docker network inspect bridge
```

Look for:

```text
Subnet
Gateway
Containers
```

You can also inspect a container:

```bash
docker inspect <container-name>
```

---

# 27. What is the Gateway concept in Kubernetes?

### Answer

Kubernetes networking can involve gateways at different levels depending on the cluster architecture and CNI.

A simplified path can be:

```text
Client
  |
  ↓
Gateway / Load Balancer
  |
  ↓
Service
  |
  ↓
Pod
```

Kubernetes also has the **Gateway API**, which provides a Kubernetes-native way to configure traffic routing.

The Kubernetes Gateway API concept should not be confused with the Linux default Gateway.

---

# 28. What commands do you commonly use to troubleshoot Gateways?

### Answer

The commands I commonly use are:

```bash
ip addr
```

Check IP addresses.

```bash
ip link
```

Check interfaces.

```bash
ip route
```

Check routing.

```bash
ip route | grep default
```

Find default Gateway.

```bash
ip route get <destination-ip>
```

Check the exact route.

```bash
ip neigh
```

Check neighbor/ARP information.

```bash
ping -c 4 <gateway-ip>
```

Test Gateway connectivity.

```bash
ping -c 4 8.8.8.8
```

Test Internet connectivity.

```bash
getent hosts google.com
```

Test DNS resolution.

```bash
ss -tuln
```

Check listening ports.

```bash
curl -v https://<host>
```

Test application connectivity.

---

# 29. Production Scenario: Application cannot reach an external API

### Scenario

A production application is running on a Linux server.

The application cannot connect to:

```text
https://api.example.com
```

### How would you troubleshoot?

I would follow a structured process.

### Step 1 — Check IP

```bash
ip addr
```

### Step 2 — Check interface

```bash
ip link
```

### Step 3 — Check routing

```bash
ip route
```

### Step 4 — Check Gateway

```bash
ip route | grep default
```

### Step 5 — Check exact route

First resolve the API hostname if needed:

```bash
getent hosts api.example.com
```

Then:

```bash
ip route get <api-ip>
```

### Step 6 — Check Gateway

```bash
ping -c 4 <gateway-ip>
```

### Step 7 — Check Internet connectivity

```bash
ping -c 4 8.8.8.8
```

### Step 8 — Check DNS

```bash
getent hosts api.example.com
```

### Step 9 — Check port

```bash
nc -zv api.example.com 443
```

### Step 10 — Check HTTPS

```bash
curl -v https://api.example.com
```

### Step 11 — Check firewall/NAT

```bash
sudo ufw status
```

```bash
sudo iptables -t nat -L -n -v
```

or:

```bash
sudo nft list ruleset
```

### Important

I would not immediately change configuration.

First I would collect evidence, identify where connectivity fails, and then make the appropriate approved change.

---

# 30. Interview Quick Revision

## What is a Gateway?

> A Gateway is a network point that provides a path from one network to another.

## What is a Default Gateway?

> It is the Gateway used when a destination is outside the local network and no more specific route exists.

## Linux command to check Gateway?

```bash
ip route
```

or:

```bash
ip route | grep default
```

## Linux command to check exact route?

```bash
ip route get <destination-ip>
```

## Linux command to check ARP/neighbor information?

```bash
ip neigh
```

## Gateway vs DNS?

> DNS resolves names to IP addresses, while a Gateway provides a path to another network.

## Gateway vs NAT?

> A Gateway provides a network path, while NAT translates addresses and/or ports. They are often used together.

## AWS Internet Gateway?

> Provides VPC connectivity to the Internet when routing, addressing, and security are configured appropriately.

## AWS NAT Gateway?

> Allows private subnet resources to initiate outbound connections through a NAT Gateway without giving those resources direct Internet reachability.

## AWS Transit Gateway?

> A centralized hub for connecting multiple VPCs and other networks.

## Docker Gateway?

> A Gateway address associated with a Docker network that provides a path between the container network and the host/network.

---

# Golden Interview Answer

If the interviewer asks:

> **"Explain Gateway in simple words."**

Answer:

> "A Gateway is a network entry or exit point that allows traffic to move between different networks. In Linux, a server normally uses a default Gateway for destinations outside its local network. I can check it using `ip route` or `ip route | grep default`. For troubleshooting, I check the IP address, interface, routing table, Gateway reachability, DNS, firewall, NAT, and destination port."

---

# Key Commands to Remember

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
ss -tuln
```

```bash
curl -v https://<host>
```

```bash
docker network inspect bridge
```

```bash
sudo iptables -t nat -L -n -v
```

```bash
sudo nft list ruleset
```

---

# Final Interview Tip

Do not try to memorize every answer word-for-word.

Understand this flow:

```text
Server
  ↓
IP Address
  ↓
Routing Table
  ↓
Default Gateway
  ↓
NAT / Firewall
  ↓
Destination Network
  ↓
Application
```

If you understand this flow, you can explain most Gateway troubleshooting questions confidently.