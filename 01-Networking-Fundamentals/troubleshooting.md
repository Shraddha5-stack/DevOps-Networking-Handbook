# 🛠 Networking Fundamentals - Troubleshooting Guide

This guide covers common networking problems, their possible causes, and the steps to troubleshoot them using Linux networking commands.

---

# 📋 Scenario 1: No Internet Connection

## Problem

The system cannot access the internet.

## Possible Causes

- Network cable disconnected
- Wi-Fi is disabled
- Incorrect IP address
- Default gateway is missing
- DNS server issue

## Troubleshooting Steps

### 1. Check IP Address

```bash
ip addr show
```

Verify that your system has a valid IP address.

---

### 2. Check Network Interface

```bash
ip link show
```

Ensure the network interface is in the **UP** state.

---

### 3. Check Default Gateway

```bash
ip route
```

Verify that a default gateway is configured.

---

### 4. Test Internet Connectivity

```bash
ping 8.8.8.8
```

If this works but websites do not open, the issue is likely DNS.

---

### 5. Test DNS Resolution

```bash
ping google.com
```

If this fails but `ping 8.8.8.8` succeeds, the DNS configuration needs to be checked.

---

# 📋 Scenario 2: Unable to Resolve Domain Names

## Problem

The internet works using IP addresses, but domain names do not.

### Example

```text
ping 8.8.8.8     ✅ Works
ping google.com  ❌ Fails
```

## Possible Cause

DNS server configuration is incorrect.

## Solution

Check the DNS configuration:

```bash
cat /etc/resolv.conf
```

Verify that a valid DNS server is listed.

Example:

```text
nameserver 8.8.8.8
```

---

# 📋 Scenario 3: Network Interface is Down

## Problem

The system has no network connectivity.

## Check Interface Status

```bash
ip link show
```

If the interface is **DOWN**, bring it up:

```bash
sudo ip link set enp0s3 up
```

Replace `enp0s3` with your actual interface name.

---

# 📋 Scenario 4: Cannot Reach Another Machine

## Troubleshooting Steps

- Verify the destination IP address.
- Check internet connectivity.
- Ensure both machines are on the same network (if required).
- Verify firewall settings.
- Use `ping` to test connectivity.

Example:

```bash
ping 192.168.1.20
```

---

# 📋 Scenario 5: Check Open Network Ports

## Command

```bash
ss -tuln
```

## Purpose

Displays all listening TCP and UDP ports.

## Example

```text
22   SSH
80   HTTP
443  HTTPS
```

---

# 📋 Scenario 6: Verify Hostname

## Command

```bash
hostname
```

## Purpose

Displays the current hostname of the system.

---

# 📋 Common Networking Commands

| Command | Purpose |
|----------|---------|
| `ip addr show` | Display IP addresses |
| `ip link show` | Display network interfaces |
| `ip route` | Show routing table |
| `ping` | Test connectivity |
| `hostname` | Display system hostname |
| `cat /etc/resolv.conf` | View DNS configuration |
| `ss -tuln` | Display listening ports |

---

# 🚀 Troubleshooting Flow

```text
Network Problem
       │
       ▼
Check Interface
       │
       ▼
Check IP Address
       │
       ▼
Check Gateway
       │
       ▼
Ping IP Address
       │
       ▼
Check DNS
       │
       ▼
Verify Services & Ports
       │
       ▼
Problem Solved ✅
```

---

# 🌍 Real-World DevOps Example

Imagine an application deployed on AWS is not accessible.

A DevOps Engineer would typically:

1. Verify the server has a valid IP address.
2. Check the network interface status.
3. Verify the routing table.
4. Test internet connectivity.
5. Verify DNS resolution.
6. Check if the application port is listening.
7. Review firewall or security group rules.

Following these steps helps identify and resolve the issue efficiently.

---

# 🎯 Interview Tip

> **Question:** "A server cannot access the internet. How would you troubleshoot it?"

A strong answer is:

1. Check the network interface.
2. Verify the IP address.
3. Check the default gateway.
4. Test connectivity using `ping`.
5. Verify DNS settings.
6. Check open ports and firewall rules.

This structured approach demonstrates practical troubleshooting skills expected from a Linux Administrator or DevOps Engineer.
