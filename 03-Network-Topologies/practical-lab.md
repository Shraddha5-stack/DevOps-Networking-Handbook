# 🧪 Practical Lab – Network Topologies

## 🎯 Objective

The goal of this lab is to observe your system's network interfaces, IP addresses, routing information, and connectivity using Linux networking commands. These activities help you understand how devices communicate within different network topologies.

---

# 🛠 Lab Requirements

- Ubuntu/Linux System
- Terminal Access
- Internet Connection

---

# 🧪 Lab 1 – Display Network Interfaces

## Command

```bash
ip link show
```

### Expected Outcome

- View all available network interfaces.
- Identify Ethernet and Wi-Fi interfaces.
- Check whether interfaces are UP or DOWN.

---

# 🧪 Lab 2 – Display IP Addresses

## Command

```bash
ip addr show
```

### Expected Outcome

- View IPv4 and IPv6 addresses.
- Identify your system's IP address.
- Observe subnet information.

---

# 🧪 Lab 3 – View Routing Table

## Command

```bash
ip route
```

### Expected Outcome

- Display the default gateway.
- Observe how packets are routed.
- Understand communication between different networks.

---

# 🧪 Lab 4 – Test Network Connectivity

## Command

```bash
ping google.com
```

### Expected Outcome

- Verify Internet connectivity.
- Observe packet transmission and response time.
- Check packet loss statistics.

---

# 🧪 Lab 5 – Display ARP Table

## Command

```bash
ip neigh
```

### Expected Outcome

- View IP-to-MAC address mappings.
- Observe neighboring devices on the local network.

---

# 🧪 Lab 6 – Display Active Listening Ports

## Command

```bash
ss -tuln
```

### Expected Outcome

- View active TCP and UDP ports.
- Identify services currently listening for network connections.

---

# 📋 Lab Summary

In this lab, you learned how to:

- Identify network interfaces.
- View IP address configuration.
- Understand routing information.
- Verify Internet connectivity.
- Examine ARP entries.
- Check active network services.

These are essential networking skills for Linux Administrators, Network Engineers, and DevOps Engineers.
