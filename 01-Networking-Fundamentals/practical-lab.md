# 🧪 Networking Fundamentals - Practical Lab

## 🎯 Objective

The objective of this lab is to understand basic networking concepts using Linux commands. You will learn how to identify your IP address, verify network connectivity, inspect routing information, and check DNS configuration.

---

# 🛠 Lab Requirements

- Ubuntu/Linux Machine
- Terminal Access
- Internet Connection

---

# 📋 Lab 1: Check Your IP Address

## Command

```bash
ip addr show
```

## Expected Result

- Display all network interfaces.
- Identify your IPv4 address.
- Identify the subnet mask.

### Sample Output

```text
2: enp0s3:
    inet 192.168.1.15/24
```

### Observation

- Interface Name: `enp0s3`
- IP Address: `192.168.1.15`
- Subnet Mask: `/24`

---

# 📋 Lab 2: Display Network Interfaces

## Command

```bash
ip link show
```

## Expected Result

Display all available network interfaces.

### Observation

Identify:

- Loopback Interface (`lo`)
- Ethernet Interface
- Wi-Fi Interface (if available)

---

# 📋 Lab 3: Test Internet Connectivity

## Command

```bash
ping google.com
```

## Expected Result

Receive replies from Google's server.

### Sample Output

```text
64 bytes from google.com...
```

### Observation

If replies are received, the internet connection is working correctly.

---

# 📋 Lab 4: Display Routing Table

## Command

```bash
ip route
```

## Expected Result

View the default gateway and routing information.

### Sample Output

```text
default via 192.168.1.1 dev enp0s3
```

### Observation

- Default Gateway
- Network Interface

---

# 📋 Lab 5: Check DNS Configuration

## Command

```bash
cat /etc/resolv.conf
```

## Expected Result

Display configured DNS servers.

### Sample Output

```text
nameserver 8.8.8.8
```

### Observation

Verify the configured DNS server.

---

# 📋 Lab 6: Display Listening Ports

## Command

```bash
ss -tuln
```

## Expected Result

Display active TCP and UDP listening ports.

### Observation

Identify commonly used ports such as:

- 22 (SSH)
- 80 (HTTP)
- 443 (HTTPS)

---

# 📸 Screenshots

Capture screenshots of:

- `ip addr show`
- `ip link show`
- `ping google.com`
- `ip route`
- `cat /etc/resolv.conf`
- `ss -tuln`

Save them in:

```text
01-Networking-Fundamentals/screenshots/
```

---

# 📝 Lab Summary

In this lab, you learned how to:

- Identify IP addresses
- View network interfaces
- Test network connectivity
- Display routing information
- Check DNS configuration
- View active network ports

These commands are the foundation of Linux networking and are frequently used by Linux Administrators, Cloud Engineers, and DevOps Engineers.

---

# 🎯 Challenge Exercise

Complete the following tasks on your own:

- Find your machine's IP address.
- Identify your default gateway.
- Check whether the internet is reachable using `ping`.
- View all active network interfaces.
- Find which ports are currently listening.

---

# 💡 DevOps Connection

These commands are used daily by DevOps Engineers to:

- Troubleshoot server connectivity
- Verify Docker host networking
- Debug Kubernetes nodes
- Configure cloud instances
- Check production server health
