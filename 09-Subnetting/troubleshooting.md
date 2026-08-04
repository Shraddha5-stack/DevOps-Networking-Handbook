# 🛠️ Subnetting Troubleshooting Guide

## 📖 Introduction

Subnetting issues are a common cause of network connectivity problems in enterprise networks and cloud environments. Incorrect subnet masks, overlapping subnets, invalid gateways, or routing mistakes can prevent systems from communicating.

This guide covers common subnetting problems, their causes, and practical troubleshooting steps using Linux networking tools.

---

# 🚨 Issue 1: Device Cannot Communicate with Another Device

## Symptoms

- Ping fails between two devices.
- SSH connection cannot be established.
- Services hosted on another server are unreachable.

## Possible Causes

- Different subnets
- Incorrect subnet mask
- Incorrect IP configuration

## Troubleshooting Commands

```bash
ip addr show
hostname -I
```

### Solution

- Verify both devices are in the correct subnet.
- Check the subnet mask.
- Confirm IP address configuration.

---

# 🚨 Issue 2: Incorrect Subnet Mask

## Symptoms

- Devices on the same LAN cannot communicate.
- Gateway is unreachable.

## Troubleshooting Command

```bash
ipcalc 192.168.1.10/24
```

### Verify

- Network Address
- Broadcast Address
- Host Range
- Subnet Mask

---

# 🚨 Issue 3: Incorrect Default Gateway

## Symptoms

- Local communication works.
- Internet access fails.

## Troubleshooting Command

```bash
ip route
```

### Solution

Verify that the default gateway belongs to the same subnet as the device.

---

# 🚨 Issue 4: Overlapping Subnets

## Symptoms

- Intermittent connectivity.
- Routing issues.
- IP conflicts.

## Example

Incorrect:

```text
192.168.1.0/24
192.168.1.128/24
```

Correct:

```text
192.168.1.0/25
192.168.1.128/25
```

### Solution

Redesign the subnet plan to avoid overlapping address ranges.

---

# 🚨 Issue 5: Wrong CIDR Notation

## Symptoms

- Incorrect number of hosts.
- Routing errors.

## Example

Expected:

```text
192.168.10.0/26
```

Configured:

```text
192.168.10.0/24
```

### Solution

Use the correct CIDR notation and verify it with:

```bash
ipcalc
```

---

# 🚨 Issue 6: Duplicate IP Address

## Symptoms

- Random connectivity loss.
- ARP conflicts.
- Network instability.

## Troubleshooting Commands

```bash
ip neigh
```

```bash
arp -a
```

### Solution

Assign unique IP addresses to every device.

---

# 🚨 Issue 7: AWS VPC Subnet Misconfiguration

## Symptoms

- EC2 instances cannot communicate.
- Internet Gateway does not work.
- NAT Gateway is unreachable.

## Checks

- VPC CIDR block
- Subnet CIDR block
- Route Tables
- Internet Gateway
- Security Groups
- Network ACLs

---

# 🚨 Issue 8: Kubernetes Pod Communication Failure

## Symptoms

- Pods cannot communicate.
- Services are unreachable.

## Checks

- Pod CIDR
- Service CIDR
- CNI plugin
- Network Policies

---

# 📋 Useful Troubleshooting Commands

| Command | Purpose |
|---------|---------|
| `ip addr show` | Display network interfaces and IP addresses |
| `hostname -I` | Show local IP address |
| `ip route` | Display routing table |
| `ipcalc` | Calculate subnet information |
| `ip neigh` | Display ARP/neighbor table |
| `ping 8.8.8.8` | Test Internet connectivity |
| `ping google.com` | Test DNS resolution |
| `ss -tuln` | Display listening ports |

---

# ☁️ DevOps Troubleshooting Scenario

## Scenario

A DevOps Engineer deploys an application across multiple AWS subnets. The web server is accessible, but the application server cannot connect to the database.

### Troubleshooting Steps

### Step 1

Verify the subnet configuration.

```bash
ipcalc 10.0.2.15/24
```

---

### Step 2

Verify routing.

```bash
ip route
```

---

### Step 3

Check network connectivity.

```bash
ping <database-private-ip>
```

---

### Step 4

Verify firewall rules and security groups.

---

### Step 5

Check Network ACLs and route tables.

---

### Step 6

Confirm that all servers are using the correct subnet.

---

# 💡 Best Practices

- Plan subnet allocation before deployment.
- Avoid overlapping subnet ranges.
- Use CIDR notation consistently.
- Keep documentation of subnet assignments.
- Use private subnets for databases and internal services.
- Place Internet-facing resources in public subnets.
- Validate subnet calculations using `ipcalc`.

---

# 📌 Key Learnings

- Incorrect subnetting is a common source of connectivity issues.
- Proper subnet planning simplifies troubleshooting.
- Linux networking commands help identify routing and addressing problems.
- Cloud networking depends heavily on correct subnet design.

---

# 📝 Summary

Subnetting troubleshooting involves verifying IP addresses, subnet masks, CIDR notation, routing tables, gateways, and network segmentation. A systematic troubleshooting approach helps quickly identify and resolve issues in Linux, enterprise, cloud, Docker, and Kubernetes environments.
