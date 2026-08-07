# 🧪 ICMP Practical Lab

## 📖 Introduction

This practical lab demonstrates how ICMP works using Linux networking commands.

The goal is to understand:

- ICMP Echo Request and Echo Reply
- Network connectivity testing
- Gateway communication
- DNS connectivity
- Network path discovery
- Troubleshooting using ICMP tools

---

# Lab 1: Test Localhost Connectivity

## Objective

Verify that the local TCP/IP stack is working correctly.

## Command

```bash
ping -c 4 localhost
```

or:

```bash
ping -c 4 127.0.0.1
```

## Expected Result

You should receive ICMP Echo Replies.

Example:

```text
64 bytes from 127.0.0.1:
icmp_seq=1 ttl=64 time=0.04 ms
```

## Learning

If localhost ping fails, the local networking stack may have a problem.

---

# Lab 2: Ping a Public IP Address

## Objective

Test Internet connectivity without depending on DNS.

## Command

```bash
ping -c 4 8.8.8.8
```

## Expected Result

Successful ICMP replies:

```text
64 bytes from 8.8.8.8:
icmp_seq=1 ttl=117 time=20 ms
```

## Learning

If this works but domain ping fails, the issue is probably DNS.

---

# Lab 3: Ping a Domain Name

## Objective

Test both DNS resolution and network connectivity.

## Command

```bash
ping -c 4 google.com
```

## Process

```text
google.com
      |
      ↓
DNS Resolution
      |
      ↓
IP Address
      |
      ↓
ICMP Echo Request
```

## Learning

This verifies:

- DNS resolution
- Network connectivity
- Remote host reachability

---

# Lab 4: Test Default Gateway

## Objective

Check communication with the local router.

## Step 1: Find Gateway

Command:

```bash
ip route
```

Example:

```text
default via 192.168.1.1 dev wlo1
```

## Step 2: Ping Gateway

Command:

```bash
ping -c 4 192.168.1.1
```

## Learning

If gateway ping fails:

Possible causes:

- Wi-Fi disconnected
- Wrong IP configuration
- Router unavailable
- Network interface issue

---

# Lab 5: Check Network Interface

## Objective

Verify IP configuration.

## Command

```bash
ip addr show
```

Check:

- Interface status
- IPv4 address
- IPv6 address
- MAC address

Example:

```text
wlo1:
inet 192.168.1.5/24
```

---

# Lab 6: Check Routing Information

## Objective

Understand where packets are sent.

## Command

```bash
ip route
```

Example:

```text
default via 192.168.1.1 dev wlo1
```

## Learning

The routing table decides the next hop for packets.

---

# Lab 7: Discover Network Path Using traceroute

## Objective

Find the routers between your system and a destination.

## Command

```bash
traceroute google.com
```

## How It Works

Traceroute uses:

- Increasing TTL values
- ICMP Time Exceeded messages

Example:

```text
Your System

    |
    ↓

Router 1

    |
    ↓

Router 2

    |
    ↓

Google Server
```

---

# Lab 8: Use tracepath

## Objective

Discover path and Path MTU.

## Command

```bash
tracepath google.com
```

## Learning

tracepath helps identify:

- Network hops
- Latency
- MTU problems

---

# Lab 9: Check Neighbor Table

## Objective

View Layer 2 neighbor information.

## Command

```bash
ip neigh
```

Example:

```text
192.168.1.1 dev wlo1
lladdr 3c:f7:5d:9d:6c:c0
REACHABLE
```

## Learning

For IPv4 networks, this information is related to ARP.

---

# Lab 10: Troubleshoot Connectivity Failure

## Scenario

You cannot access a server.

Follow this workflow:

---

## Step 1: Check Interface

```bash
ip addr show
```

Question:

Is the interface UP?

---

## Step 2: Check Route

```bash
ip route
```

Question:

Is there a default gateway?

---

## Step 3: Ping Gateway

```bash
ping -c 4 gateway-ip
```

Question:

Can you reach your router?

---

## Step 4: Ping Public IP

```bash
ping -c 4 8.8.8.8
```

Question:

Does Internet connectivity work?

---

## Step 5: Test DNS

```bash
ping -c 4 google.com
```

Question:

Can DNS resolve names?

---

# DevOps Scenario: Server Connectivity Issue

## Problem

Application server is unreachable.

## Investigation

### Check Network

```bash
ip addr show
```

### Check Routing

```bash
ip route
```

### Test Server

```bash
ping -c 4 server-ip
```

### Check Path

```bash
traceroute server-ip
```

### Check Firewall

Verify:

- Security groups
- Firewall rules
- Network policies

---

# ☁️ Cloud and DevOps Practice

ICMP troubleshooting is useful in:

## AWS

Check:

- Security Groups
- Network ACLs
- Route Tables

## Docker

Check:

```bash
docker network inspect bridge
```

## Kubernetes

Check:

```bash
kubectl get pods
```

Network troubleshooting may include:

- Pod connectivity
- Node communication
- CNI configuration

---

# 📸 Practical Screenshots

This chapter includes:

```text
screenshots/

01-ping-ip.png
02-ping-google.png
03-ping-gateway.png
04-traceroute-google.png
05-ping-localhost.png
```

---

# 📌 Lab Summary

In this practical lab, we learned:

- How to test ICMP connectivity
- How ping works
- How traceroute discovers network paths
- How to verify routing
- How to troubleshoot connectivity issues
- How ICMP helps DevOps engineers diagnose networks

---

# 🎯 Final Challenge

Perform this troubleshooting sequence:

```bash
ping -c 4 localhost

ping -c 4 gateway-ip

ping -c 4 8.8.8.8

ping -c 4 google.com

traceroute google.com

ip route

ip neigh
```

Explain what each command proves.
