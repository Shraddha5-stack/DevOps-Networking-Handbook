# 🛠️ ICMP Troubleshooting Guide

## 📑 Table of Contents

1. Introduction
2. Ping Command Fails
3. Destination Host Unreachable
4. Request Timeout
5. DNS Resolution Problems
6. High Latency Problems
7. Packet Loss Troubleshooting
8. Traceroute Analysis
9. Firewall and ICMP Blocking
10. Cloud ICMP Troubleshooting
11. Docker and Kubernetes ICMP Issues
12. DevOps Troubleshooting Workflow
13. Key Takeaways

---

# 📖 Introduction

ICMP troubleshooting helps identify network connectivity, routing, latency, and packet delivery problems.

Common ICMP troubleshooting tools:

```bash
ping
traceroute
tracepath
ip route
ip addr
ip neigh
```

A good troubleshooting approach checks the network layer first before investigating application issues.

---

# 🚨 Issue 1: Ping Command Fails

## Symptoms

Command:

```bash
ping -c 4 server-ip
```

Output:

```text
Destination Host Unreachable
```

or:

```text
Request timeout
```

---

## Possible Causes

- Network interface is down
- Incorrect IP address
- Missing route
- Firewall blocking ICMP
- Destination server unavailable

---

## Troubleshooting Steps

### Check Interface

```bash
ip addr show
```

Verify:

- Interface is UP
- Correct IP address exists

---

### Check Routing

```bash
ip route
```

Verify:

- Default gateway exists
- Correct route is configured

---

### Check Neighbor Table

```bash
ip neigh
```

---

# 🚨 Issue 2: Destination Host Unreachable

## Example

```text
From 192.168.1.5:
Destination Host Unreachable
```

## Meaning

Your system cannot reach the destination network.

---

## Check

### Gateway Connectivity

```bash
ping -c 4 gateway-ip
```

If gateway fails:

Possible problems:

- Wi-Fi issue
- Cable issue
- Router problem

---

### Check Route

```bash
ip route
```

---

# 🚨 Issue 3: Request Timeout

## Example

```text
Request timeout for icmp_seq 1
```

## Possible Causes

- Host is offline
- ICMP blocked
- Firewall rules
- Network congestion
- Packet loss

---

## Troubleshooting

Try:

```bash
ping -c 4 8.8.8.8
```

If this works:

Your Internet connection is working.

Problem may be:

- Destination firewall
- Server configuration

---

# 🚨 Issue 4: DNS Resolution Problem

## Symptom

Command:

```bash
ping google.com
```

Output:

```text
Name or service not known
```

---

## Test Without DNS

Use IP:

```bash
ping -c 4 8.8.8.8
```

If IP works but hostname fails:

Problem is DNS.

---

## Check DNS Configuration

```bash
cat /etc/resolv.conf
```

---

# 🚨 Issue 5: High Latency

## Symptom

Ping response is slow:

```text
time=500 ms
```

---

## Possible Causes

- Network congestion
- Long physical distance
- Wireless interference
- Routing problems

---

## Check Path

```bash
traceroute google.com
```

Look for hops with high delay.

---

# 🚨 Issue 6: Packet Loss

## Test

Send multiple packets:

```bash
ping -c 100 server-ip
```

Example:

```text
10% packet loss
```

---

## Possible Causes

- Weak Wi-Fi signal
- Network congestion
- Faulty hardware
- ISP problems

---

## Troubleshooting

Check:

```bash
ip link show
```

Check interface errors:

```bash
ip -s link
```

---

# 🚨 Issue 7: Traceroute Stops at a Hop

## Symptom

Example:

```text
1 192.168.1.1
2 *
3 *
```

---

## Possible Causes

- Router blocks ICMP
- Firewall filtering
- Network policy

---

## Important

A missing traceroute response does not always mean failure.

Some routers intentionally ignore ICMP probes.

---

# 🚨 Issue 8: Firewall Blocking ICMP

## Symptoms

- Server is running
- Application works
- Ping fails

Example:

```
ICMP  → Blocked
SSH   → Working
HTTP  → Working
```

---

## Check Firewall

Ubuntu:

```bash
sudo ufw status
```

---

## Cloud Firewalls

Check:

- AWS Security Groups
- Network ACLs
- Cloud firewall rules

---

# 🚨 Issue 9: AWS ICMP Troubleshooting

## Problem

EC2 instance cannot be pinged.

---

## Check Security Group

Allow:

```
Type:
Echo Request - IPv4

Protocol:
ICMP
```

---

## Check Network ACL

Verify:

- Inbound rules
- Outbound rules

---

## Check Route Table

```bash
ip route
```

---

# 🚨 Issue 10: Docker ICMP Problems

## Symptoms

Containers cannot communicate.

---

## Check Networks

```bash
docker network ls
```

---

Inspect:

```bash
docker network inspect bridge
```

---

Check container IP:

```bash
docker inspect container-name
```

---

# 🚨 Issue 11: Kubernetes ICMP Problems

## Symptoms

Pods cannot communicate.

---

## Check Pods

```bash
kubectl get pods -o wide
```

---

## Check Network

```bash
ip route
```

---

Possible causes:

- CNI plugin issue
- Network policy blocking traffic
- Incorrect pod networking

---

# 🔄 DevOps Troubleshooting Workflow

Follow this order:

## Step 1: Check Interface

```bash
ip addr show
```

---

## Step 2: Check Route

```bash
ip route
```

---

## Step 3: Check Gateway

```bash
ping -c 4 gateway-ip
```

---

## Step 4: Check Internet

```bash
ping -c 4 8.8.8.8
```

---

## Step 5: Check DNS

```bash
ping -c 4 google.com
```

---

## Step 6: Check Path

```bash
traceroute google.com
```

---

## Step 7: Test Application

Example:

```bash
curl http://server-ip
```

---

# 📊 Troubleshooting Checklist

| Problem | Command |
|---|---|
| Check IP | `ip addr show` |
| Check route | `ip route` |
| Test connectivity | `ping` |
| Find network path | `traceroute` |
| Check neighbors | `ip neigh` |
| Check DNS | `cat /etc/resolv.conf` |
| Check firewall | `ufw status` |

---

# 📌 Key Takeaways

- Ping failure does not always mean a server is down.
- Always check routing before blaming applications.
- Firewalls commonly block ICMP.
- Traceroute helps identify network paths.
- Cloud security rules can affect ICMP.
- A structured troubleshooting approach saves time.

---

# 📝 Summary

ICMP troubleshooting is an essential skill for DevOps and network engineers.

By combining:

```bash
ping
traceroute
ip route
ip addr
ip neigh
```

engineers can quickly identify network connectivity, routing, firewall, and performance issues in Linux, cloud, Docker, and Kubernetes environments.
