# 🛠️ IP Addressing Troubleshooting Guide

## 📖 Introduction

IP addressing issues are among the most common causes of network connectivity problems. Incorrect IP configurations, missing default gateways, DNS failures, subnet mismatches, and firewall rules can prevent systems from communicating.

This guide covers common IP-related problems, their causes, and practical troubleshooting steps using Linux networking tools.

---

# 🚨 Issue 1: No IP Address Assigned

## Symptoms

- No Internet connectivity
- Cannot communicate with other devices
- SSH connection fails

## Possible Causes

- DHCP server unavailable
- Network cable disconnected
- Wi-Fi disconnected
- Incorrect network configuration

## Troubleshooting Commands

```bash
ip addr show
```

```bash
hostname -I
```

```bash
sudo systemctl restart NetworkManager
```

---

# 🚨 Issue 2: Cannot Reach the Internet

## Symptoms

- Websites do not open
- Ping to external IP addresses fails

## Possible Causes

- Incorrect default gateway
- ISP outage
- Firewall restrictions
- Router issues

## Troubleshooting Commands

```bash
ip route
```

```bash
ping -c 4 8.8.8.8
```

---

# 🚨 Issue 3: DNS Resolution Failure

## Symptoms

- IP address is reachable
- Domain names do not work

Example:

```text
ping 8.8.8.8      ✅ Works
ping google.com   ❌ Fails
```

## Troubleshooting Commands

```bash
ping google.com
```

```bash
cat /etc/resolv.conf
```

```bash
nslookup google.com
```

---

# 🚨 Issue 4: Wrong Public IP

## Symptoms

- Unable to access server remotely
- VPN issues
- Firewall rules not matching

## Troubleshooting Command

```bash
curl ifconfig.me
```

---

# 🚨 Issue 5: Incorrect Subnet Mask

## Symptoms

- Devices on the same network cannot communicate
- Gateway unreachable

## Troubleshooting Command

```bash
ipcalc 192.168.1.10/24
```

### Verify

- Network Address
- Broadcast Address
- Subnet Mask
- Host Range

---

# 🚨 Issue 6: Incorrect Routing Table

## Symptoms

- Packets do not reach other networks
- Gateway unreachable

## Troubleshooting Command

```bash
ip route
```

Verify:

- Default gateway
- Destination network
- Interface

---

# 🚨 Issue 7: Duplicate IP Address

## Symptoms

- Intermittent connectivity
- Network conflicts
- ARP warnings

## Troubleshooting Commands

```bash
ip neigh
```

```bash
arp -a
```

---

# 🚨 Issue 8: SSH Not Reachable

## Symptoms

```text
Connection refused
No route to host
Connection timed out
```

## Troubleshooting Steps

Check the server IP:

```bash
hostname -I
```

Check if SSH is running:

```bash
sudo systemctl status ssh
```

Verify port 22:

```bash
ss -tuln
```

---

# 📋 Useful Troubleshooting Commands

| Command | Purpose |
|---------|---------|
| `ip addr show` | Display network interfaces and IP addresses |
| `hostname -I` | Show local IP address |
| `ip route` | Display routing table |
| `ping 8.8.8.8` | Test Internet connectivity |
| `ping google.com` | Test DNS resolution |
| `curl ifconfig.me` | Show public IP address |
| `ipcalc` | Calculate subnet information |
| `ip neigh` | Display ARP/neighbor table |
| `cat /etc/resolv.conf` | View DNS configuration |
| `ss -tuln` | Show listening ports |

---

# ☁️ DevOps Troubleshooting Scenario

## Scenario

A web application hosted on an AWS EC2 instance is not accessible.

### Troubleshooting Process

### Step 1

Check the server IP.

```bash
hostname -I
```

---

### Step 2

Verify routing.

```bash
ip route
```

---

### Step 3

Test Internet connectivity.

```bash
ping -c 4 8.8.8.8
```

---

### Step 4

Verify DNS.

```bash
ping google.com
```

---

### Step 5

Confirm the public IP.

```bash
curl ifconfig.me
```

---

### Step 6

Verify the web service.

```bash
ss -tuln
```

---

### Step 7

Check firewall rules.

```bash
sudo ufw status
```

---

# 💡 Best Practices

- Use static IPs for production servers.
- Use DHCP for end-user devices.
- Verify routing before checking applications.
- Confirm DNS resolution separately from Internet connectivity.
- Document IP address allocations.
- Avoid duplicate IP addresses.
- Use private IPs within internal networks.
- Protect public-facing services with firewalls and security groups.

---

# 📌 Key Learnings

- IP issues often originate from configuration, routing, or DNS problems.
- Troubleshooting should follow a step-by-step process.
- Linux networking tools provide quick insights into connectivity issues.
- Understanding IP addressing simplifies cloud and DevOps troubleshooting.

---

# 📝 Summary

Effective IP troubleshooting requires checking IP configuration, routing tables, DNS settings, subnet information, and connectivity. Linux commands such as `ip addr`, `ip route`, `hostname -I`, `ping`, `curl`, and `ipcalc` are essential tools for diagnosing and resolving networking issues in Linux, cloud, and DevOps environments.
