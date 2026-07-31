# 🧪 Practical Lab – Types of Networks

## 🎯 Objective

The objective of this lab is to understand different types of computer networks and learn how to identify your system's network configuration using basic Linux networking commands.

By completing this lab, you will gain practical experience with network interfaces, IP addresses, routing, DNS, and Internet connectivity.

---

# 🛠 Lab Environment

| Requirement | Details |
|-------------|---------|
| Operating System | Ubuntu Linux |
| Terminal | Bash |
| Internet Connection | Required |
| User Access | Normal User |

---

# 📚 Lab 1 – Identify Network Interfaces

## Objective

View all available network interfaces on your system.

### Command

```bash
ip link show
```

### Expected Output

```text
2: wlo1: <BROADCAST,MULTICAST,UP,LOWER_UP>
```

### Observation

- Identify the Wi-Fi or Ethernet interface.
- Check whether the interface status is **UP**.

### Learning Outcome

You learned how Linux identifies physical and virtual network interfaces.

---

# 🌐 Lab 2 – View IP Address

## Objective

Display the IP address assigned to your computer.

### Command

```bash
ip addr show
```

### Expected Output

```text
inet 192.168.1.5/24
```

### Observation

- Identify the IPv4 address.
- Identify the subnet mask.
- Observe any IPv6 addresses.

### Learning Outcome

You learned how Linux assigns IP addresses to network interfaces.

---

# 🚪 Lab 3 – Display Routing Table

## Objective

Understand how your computer reaches other networks.

### Command

```bash
ip route
```

### Expected Output

```text
default via 192.168.1.1 dev wlo1
```

### Observation

- Identify the default gateway.
- Identify the network interface being used.

### Learning Outcome

You learned how packets are routed from your computer to other networks.

---

# 📡 Lab 4 – Test Internet Connectivity

## Objective

Verify communication with an external server.

### Command

```bash
ping -c 4 google.com
```

### Expected Output

```text
4 packets transmitted
4 received
0% packet loss
```

### Observation

- Check whether packets are successfully transmitted.
- Observe response time (latency).

### Learning Outcome

You learned how to verify Internet (WAN) connectivity.

---

# 🔍 Lab 5 – Check DNS Configuration

## Objective

View the DNS servers configured on your Linux system.

### Command

```bash
cat /etc/resolv.conf
```

### Expected Output

```text
nameserver 192.168.1.1
```

### Observation

- Identify the configured DNS server.
- Understand how domain names are resolved.

### Learning Outcome

You learned how Linux performs DNS resolution.

---

# 🔌 Lab 6 – Display Listening Ports

## Objective

View services currently listening on the system.

### Command

```bash
ss -tuln
```

### Expected Output

```text
Netid State Local Address:Port
```

### Observation

- Identify TCP ports.
- Identify UDP ports.
- Observe active network services.

### Learning Outcome

You learned how to inspect listening network ports in Linux.

---

# 📝 Lab Summary

During this practical lab, you successfully learned how to:

- View network interfaces.
- Check IP addresses.
- Understand routing.
- Test Internet connectivity.
- Verify DNS configuration.
- Display listening network ports.

These commands are frequently used by Linux Administrators, System Engineers, Cloud Engineers, and DevOps Engineers for troubleshooting and network management.

---

# 💡 Real-World Scenario

Imagine a developer reports that an application cannot connect to the Internet.

As a DevOps Engineer, you would typically perform these checks:

1. Verify the network interface using `ip link show`.
2. Check the IP address using `ip addr show`.
3. Verify the default gateway using `ip route`.
4. Test connectivity using `ping google.com`.
5. Check DNS configuration using `cat /etc/resolv.conf`.
6. Verify running services using `ss -tuln`.

Following these steps helps identify whether the issue is related to the local network, routing, DNS, or the application itself.

---

# 🎯 Key Takeaways

- Linux provides powerful networking commands for troubleshooting.
- Understanding LAN and WAN connectivity is essential for DevOps.
- These commands form the foundation for Docker, Kubernetes, Cloud, and Production Networking.
- Hands-on practice is the best way to build networking skills.
