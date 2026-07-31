# 🛠 Troubleshooting – Types of Networks

## 📖 Introduction

Network issues are common in Linux systems and DevOps environments. This guide covers frequently encountered networking problems, their possible causes, and practical solutions using Linux networking commands.

---

# 1️⃣ No Internet Connection

## Problem

The system cannot access the Internet.

### Possible Causes

- Wi-Fi or Ethernet is disconnected.
- Invalid IP address.
- Incorrect default gateway.
- DNS configuration issue.

### Troubleshooting Steps

```bash
ip link show
ip addr show
ip route
ping google.com
```

### Solution

- Ensure the network interface is **UP**.
- Verify the IP address.
- Check the default gateway.
- Confirm Internet connectivity.

---

# 2️⃣ Unable to Reach Another Device on LAN

## Problem

Cannot communicate with another computer on the same network.

### Possible Causes

- Incorrect IP address.
- Different subnet.
- Firewall blocking traffic.

### Troubleshooting Steps

```bash
ip addr show
ping <IP_ADDRESS>
```

### Solution

- Verify both devices are on the same subnet.
- Check firewall settings.
- Confirm the destination device is online.

---

# 3️⃣ DNS Resolution Failure

## Problem

Domain names cannot be resolved.

### Symptoms

```text
ping: google.com: Temporary failure in name resolution
```

### Troubleshooting Steps

```bash
cat /etc/resolv.conf
ping 8.8.8.8
```

### Solution

- Verify the configured DNS server.
- Restart the network service if required.
- Configure a valid DNS server.

---

# 4️⃣ Network Interface is Down

## Problem

The network interface is inactive.

### Troubleshooting Steps

```bash
ip link show
```

### Solution

If the interface is down, enable it:

```bash
sudo ip link set <interface-name> up
```

Example:

```bash
sudo ip link set wlo1 up
```

---

# 5️⃣ Incorrect Default Gateway

## Problem

The system cannot reach external networks.

### Troubleshooting Steps

```bash
ip route
```

### Solution

Verify the default gateway.

Example:

```text
default via 192.168.1.1 dev wlo1
```

If the gateway is missing or incorrect, update the network configuration.

---

# 🔍 Useful Troubleshooting Commands

| Command | Purpose |
|---------|---------|
| `ip link show` | Display network interfaces |
| `ip addr show` | Display IP addresses |
| `ip route` | Display routing table |
| `ping google.com` | Test Internet connectivity |
| `cat /etc/resolv.conf` | View DNS configuration |
| `ss -tuln` | Display listening ports |

---

# 💡 Troubleshooting Tips

- Verify the network interface status before checking other settings.
- Confirm that the IP address belongs to the correct subnet.
- Test connectivity using both an IP address and a domain name.
- Check DNS configuration if websites are unreachable.
- Use Linux networking commands to isolate the issue step by step.

---

# 🎯 Key Takeaways

- Most networking problems can be diagnosed using a few basic Linux commands.
- Always troubleshoot in a logical order: Interface → IP Address → Gateway → DNS → Connectivity.
- Strong troubleshooting skills are essential for Linux Administrators, Cloud Engineers, and DevOps Engineers.
