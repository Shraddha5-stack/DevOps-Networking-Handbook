# 🧪 Practical Lab – Network Devices

This practical lab helps understand network devices using Linux networking commands and real-world scenarios.

---

# 🎯 Lab Objectives

By completing this lab, you will learn:

- Identify network interfaces.
- Check IP configuration.
- Understand routing.
- Test connectivity.
- Analyze network services.
- Explore Docker networking.

---

# Lab 1: Identify Network Interfaces

## Command

```bash
ip link show
```

## Objective

View all available network interfaces.

## Expected Output

Example:

```
wlo1
docker0
eth0
```

## Understanding

- `wlo1` → Wireless interface
- `eth0` → Ethernet interface
- `docker0` → Docker bridge interface

---

# Lab 2: Check IP Address Configuration

## Command

```bash
ip addr show
```

## Objective

Find IP addresses assigned to network devices.

## Example:

```
inet 192.168.1.5/24
```

## Understanding:

- IP address identifies the device.
- Subnet defines the network range.

---

# Lab 3: Check Routing Table

## Command

```bash
ip route
```

## Objective

Understand how packets travel through networks.

Example:

```
default via 192.168.1.1
```

## Understanding:

- Default gateway forwards traffic outside the local network.

---

# Lab 4: Test Network Connectivity

## Command

```bash
ping google.com
```

## Objective

Verify communication between systems.

## Understanding:

Successful response means:

- Network connection exists.
- DNS resolution works.

---

# Lab 5: Check ARP Table

## Command

```bash
ip neigh
```

## Objective

View IP-to-MAC address mapping.

Example:

```
192.168.1.1 dev wlo1 lladdr xx:xx:xx
```

## Understanding:

Devices inside LAN communicate using MAC addresses.

---

# Lab 6: Check Active Network Services

## Command

```bash
ss -tuln
```

## Objective

Find listening ports.

Example:

```
0.0.0.0:22
```

## Understanding:

- Port 22 → SSH service
- Port 80 → HTTP service

---

# Lab 7: Docker Network Investigation

## List Docker Networks

```bash
docker network ls
```

Example:

```
bridge
host
none
```

---

## Inspect Bridge Network

```bash
docker network inspect bridge
```

Understanding:

- Docker bridge works like a virtual switch.
- Containers communicate through virtual networking.

---

# Lab 8: Network Troubleshooting Practice

## Scenario:

Application is not accessible.

Follow these steps:

### Step 1: Check Interface

```bash
ip link show
```

---

### Step 2: Check IP

```bash
ip addr show
```

---

### Step 3: Check Route

```bash
ip route
```

---

### Step 4: Check Connectivity

```bash
ping google.com
```

---

### Step 5: Check Application Port

```bash
ss -tuln
```

---

# 📸 Screenshots

Add practical screenshots here:

```
screenshots/
│
├── 01-ip-link-show.png
├── 02-ip-addr-show.png
├── 03-ip-route.png
├── 04-ping-google.png
├── 05-ip-neigh.png
└── 06-ss-tuln.png
```

---

# ✅ Lab Completion Checklist

- [x] Checked network interfaces
- [x] Verified IP address
- [x] Checked routing table
- [x] Tested connectivity
- [x] Viewed ARP table
- [x] Checked listening ports
- [x] Explored Docker networking

---

# 🔑 Learning Outcome

After completing this lab, you understand how network devices communicate and how DevOps engineers troubleshoot network problems in Linux environments.

