# 💻 Linux Networking Commands – Network Topologies

This section introduces Linux commands that help you understand network topology, interfaces, routing, connectivity, and active network services.

---

# 1️⃣ Display Network Interfaces

## Command

```bash
ip link show
```

### Purpose

Displays all available network interfaces.

### Real-World Use Case

Identifies active Ethernet and Wi-Fi interfaces when analyzing a network.

---

# 2️⃣ Display IP Addresses

## Command

```bash
ip addr show
```

### Purpose

Displays IPv4 and IPv6 addresses assigned to network interfaces.

### Real-World Use Case

Helps identify devices connected within a network topology.

---

# 3️⃣ Display Routing Table

## Command

```bash
ip route
```

### Purpose

Shows how packets travel between different networks.

### Real-World Use Case

Useful for understanding communication between different network segments.

---

# 4️⃣ Test Connectivity

## Command

```bash
ping google.com
```

### Purpose

Checks network connectivity and packet transmission.

### Real-World Use Case

Verifies whether the network path is functioning correctly.

---

# 5️⃣ Display ARP Table

## Command

```bash
ip neigh
```

### Purpose

Displays IP-to-MAC address mappings.

### Real-World Use Case

Helps understand how devices communicate within the same local network.

---

# 6️⃣ Display Listening Ports

## Command

```bash
ss -tuln
```

### Purpose

Displays active TCP and UDP listening ports.

### Real-World Use Case

Checks which network services are currently available.

---

# 📌 Summary

These commands help visualize network communication, connectivity, routing, and device relationships, which are essential when studying network topologies.
