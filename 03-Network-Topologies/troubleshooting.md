# 🛠 Network Topology Troubleshooting

This section covers common network topology issues, their possible causes, and solutions. These scenarios are useful for practical learning and DevOps interviews.

---

# 1️⃣ Unable to Ping Another Device

## Problem

A device cannot communicate with another device on the network.

### Possible Causes

- Incorrect IP address
- Network cable disconnected
- Device is powered off
- Firewall blocking traffic
- Incorrect subnet mask

### Solution

- Verify the IP address using:

```bash
ip addr show
```

- Check connectivity:

```bash
ping <IP_ADDRESS>
```

- Verify firewall rules.
- Ensure both devices are connected to the network.

---

# 2️⃣ Network Interface is Down

## Problem

The network interface is not active.

### Check

```bash
ip link show
```

### Solution

Bring the interface up:

```bash
sudo ip link set <interface-name> up
```

Example:

```bash
sudo ip link set wlo1 up
```

---

# 3️⃣ Incorrect Default Gateway

## Problem

The system can communicate within the local network but cannot access the Internet.

### Check

```bash
ip route
```

### Solution

Verify that the default gateway is configured correctly.

---

# 4️⃣ DNS Resolution Failure

## Problem

You can ping an IP address but cannot access websites using domain names.

### Check

```bash
cat /etc/resolv.conf
```

### Solution

Verify that valid DNS servers are configured.

---

# 5️⃣ Duplicate IP Address

## Problem

Two devices are using the same IP address.

### Symptoms

- Intermittent connectivity
- Network conflicts
- Connection drops

### Solution

Assign a unique IP address to each device.

---

# 6️⃣ Switch Failure (Star Topology)

## Problem

All connected devices lose communication.

### Cause

The central switch has failed.

### Solution

- Check switch power.
- Verify cable connections.
- Replace the faulty switch if necessary.

---

# 7️⃣ Backbone Cable Failure (Bus Topology)

## Problem

The entire network stops working.

### Cause

The backbone cable is damaged.

### Solution

Inspect and replace the backbone cable.

---

# 8️⃣ Slow Network Performance

## Possible Causes

- High network traffic
- Faulty cables
- Hardware issues
- Network congestion

### Solution

- Check interface status.
- Replace damaged cables.
- Upgrade network hardware if required.

---

# 📌 Troubleshooting Tips

- Always check physical connections first.
- Verify IP configuration.
- Confirm routing information.
- Test connectivity using `ping`.
- Check DNS configuration.
- Identify active network services.
- Review firewall settings before making major changes.

> **💡 DevOps Tip:** Troubleshooting should follow a systematic approach: **Check Physical Layer → Verify IP Configuration → Test Connectivity → Check Routing → Verify DNS → Inspect Services.**
