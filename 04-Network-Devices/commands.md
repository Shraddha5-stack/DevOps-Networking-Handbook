# 💻 Linux Networking Commands – Network Devices

This section contains important Linux commands used by DevOps engineers to inspect and troubleshoot network devices and communication.

---

# 1️⃣ Display Network Interfaces

## Command

```bash
ip link show
```

## Purpose

Displays all available network interfaces on the system.

## Example

```
wlo1
docker0
eth0
```

## Use Case

Used to identify:

- Ethernet interfaces
- Wi-Fi interfaces
- Virtual interfaces

---

# 2️⃣ Display IP Addresses

## Command

```bash
ip addr show
```

## Purpose

Shows IP addresses assigned to network interfaces.

## Use Case

Helps identify:

- Device IP address
- Network configuration
- Interface status

---

# 3️⃣ Display Routing Table

## Command

```bash
ip route
```

## Purpose

Displays how packets travel between networks.

## Use Case

Used for troubleshooting:

- Router configuration
- Default gateway
- Network paths

---

# 4️⃣ Test Network Connectivity

## Command

```bash
ping google.com
```

## Purpose

Checks whether a device can communicate with another host.

## Use Case

Verifies:

- Internet connectivity
- Network availability

---

# 5️⃣ Display ARP Table

## Command

```bash
ip neigh
```

## Purpose

Shows IP address and MAC address mapping.

## Use Case

Helps understand communication between devices in a LAN.

---

# 6️⃣ Display Listening Ports

## Command

```bash
ss -tuln
```

## Purpose

Displays active TCP and UDP listening ports.

## Use Case

Used to identify running network services.

---

# 7️⃣ Check DNS Configuration

## Command

```bash
cat /etc/resolv.conf
```

## Purpose

Shows configured DNS servers.

## Use Case

Troubleshooting DNS-related issues.

---

# 8️⃣ Check Network Path

## Command

```bash
traceroute google.com
```

## Purpose

Shows the path packets take to reach a destination.

## Use Case

Identifies network delays and routing problems.

---

# 🐳 Docker Networking Commands

## List Docker Networks

```bash
docker network ls
```

---

## Inspect Docker Network

```bash
docker network inspect bridge
```

---

# ☁️ AWS Networking Related Commands

## Check Public IP

```bash
curl ifconfig.me
```

---

## Check Local Hostname

```bash
hostname -I
```

---

# 📌 Summary

These commands help DevOps engineers:

- Identify network interfaces
- Check IP addresses
- Understand routing
- Troubleshoot connectivity
- Analyze network services
- Work with Docker and cloud networking
