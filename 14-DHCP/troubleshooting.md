# 🛠️ Chapter 14 – DHCP Troubleshooting

## 📑 Table of Contents

1. DHCP Troubleshooting Flow
2. Check Network Interface
3. Check IP Address
4. Check Default Gateway
5. Check DHCP Configuration
6. Check NetworkManager
7. Check DHCP Logs
8. Check DHCP Traffic
9. Check DNS
10. Test Local Connectivity
11. Test Internet Connectivity
12. Common DHCP Problems
13. DHCP Pool Exhaustion
14. DHCP Server Unavailable
15. DHCP Relay Failure
16. Duplicate IP Address
17. Troubleshooting Decision Tree
18. Practical Commands
19. Key Takeaways

---

# 1. DHCP Troubleshooting Flow

When a Linux machine cannot obtain network configuration, use a structured troubleshooting process:

```text
Network Interface
       ↓
Link Status
       ↓
IP Address
       ↓
DHCP
       ↓
Default Gateway
       ↓
DNS
       ↓
Internet Connectivity
```

Do not immediately restart everything.

First identify where the failure occurs.

---

# 2. Check Network Interface

Start with:

```bash
ip link show
```

For a specific interface:

```bash
ip link show wlo1
```

Look for:

```text
state UP
```

If the interface is down, investigate the physical or wireless connection.

Check NetworkManager:

```bash
nmcli device status
```

Example:

```text
DEVICE  TYPE  STATE      CONNECTION
wlo1    wifi  connected  Airtel_shar_9515
```

---

# 3. Check IP Address

Run:

```bash
ip addr show wlo1
```

Look for:

```text
inet 192.168.1.5/24
```

If there is no IPv4 address, investigate DHCP or static network configuration.

You can also use:

```bash
nmcli device show wlo1
```

Check:

```text
IP4.ADDRESS
```

---

# 4. Check Default Gateway

Run:

```bash
ip route
```

Look for:

```text
default via 192.168.1.1
```

The default route is required for traffic destined for networks outside the local subnet.

If the IP address exists but there is no default route, investigate the network configuration.

---

# 5. Check DHCP Configuration

Check the NetworkManager connection:

```bash
nmcli connection show
```

For the active connection:

```bash
nmcli connection show "Airtel_shar_9515"
```

Check the IPv4 method:

```bash
nmcli connection show "Airtel_shar_9515" | grep ipv4.method
```

If the connection is configured for automatic IPv4 configuration, DHCP is normally used.

You can also inspect:

```bash
nmcli -f DHCP4 device show wlo1
```

The exact DHCP fields displayed depend on the NetworkManager configuration and available lease information.

---

# 6. Check NetworkManager

Check whether NetworkManager is running:

```bash
systemctl status NetworkManager
```

Look for:

```text
Active: active (running)
```

Then:

```bash
nmcli device status
```

Check whether the interface is:

```text
connected
```

---

# 7. Check DHCP Logs

NetworkManager logs can provide useful information.

Run:

```bash
journalctl -u NetworkManager
```

Search for DHCP:

```bash
journalctl -u NetworkManager | grep -i dhcp
```

Show recent DHCP-related messages:

```bash
journalctl -u NetworkManager | grep -i dhcp | tail -20
```

Follow NetworkManager logs live:

```bash
journalctl -u NetworkManager -f
```

Look for messages related to:

```text
DHCP
lease
timeout
IP configuration
gateway
DNS
```

---

# 8. Check DHCP Traffic

DHCP uses UDP ports:

```text
UDP 67 → DHCP Server
UDP 68 → DHCP Client
```

Capture DHCP traffic:

```bash
sudo tcpdump -i wlo1 -n 'udp port 67 or udp port 68'
```

Then reconnect the NetworkManager connection if appropriate:

```bash
nmcli connection down "Airtel_shar_9515"
nmcli connection up "Airtel_shar_9515"
```

Watch the `tcpdump` output.

You may observe DHCP traffic associated with:

```text
Discover
Offer
Request
ACK
```

The exact exchange can vary depending on the existing lease and network state.

Stop the capture with:

```text
Ctrl + C
```

> Do not disconnect an active interface if you are connected to the machine remotely through that interface.

---

# 9. Check DNS

If the machine has an IP address but cannot resolve domain names, check DNS.

Run:

```bash
cat /etc/resolv.conf
```

Also:

```bash
resolvectl status
```

Check DNS resolution:

```bash
nslookup google.com
```

or:

```bash
dig google.com
```

---

# 10. Test Local Connectivity

First test the default gateway:

```bash
ping -c 4 192.168.1.1
```

If this succeeds, the machine can communicate with the local router.

If it fails, investigate:

```text
Wi-Fi
Interface
IP configuration
Subnet
Gateway
Local network
```

---

# 11. Test Internet Connectivity

Test an external IP:

```bash
ping -c 4 8.8.8.8
```

If this works:

```text
Local network → Working
Gateway → Working
Internet routing → Likely working
```

Then test a hostname:

```bash
ping -c 4 google.com
```

If:

```text
8.8.8.8 → Works
google.com → Fails
```

then DNS is a likely problem.

---

# 12. Common DHCP Problems

## Problem 1 – No IP Address

Symptoms:

```text
Interface → UP
IP Address → Missing
```

Possible causes:

```text
DHCP server unavailable
DHCP relay failure
Network connection problem
Incorrect VLAN
Wi-Fi authentication problem
DHCP client problem
```

Check:

```bash
ip addr
nmcli device status
journalctl -u NetworkManager | grep -i dhcp
```

---

# 13. DHCP Pool Exhaustion

A DHCP server may have a limited pool.

Example:

```text
192.168.1.100 - 192.168.1.200
```

This provides a finite number of addresses.

If all addresses are leased:

```text
New Client
    ↓
DHCP Discover
    ↓
No Available Address
    ↓
Client Cannot Obtain Configuration
```

Possible solution:

```text
Expand DHCP Pool
Reduce Lease Duration
Remove Stale Leases
Add Another DHCP Scope
```

The exact solution depends on the network design.

---

# 14. DHCP Server Unavailable

If the DHCP server is down:

```text
Client
   ↓
DHCP Discover
   ↓
No DHCP Response
```

New clients may fail to obtain network configuration.

Existing clients may continue using valid leases for some time.

Troubleshoot:

```text
DHCP Server
DHCP Service
Network Connectivity
DHCP Relay
Firewall
VLAN
```

---

# 15. DHCP Relay Failure

Consider:

```text
Client
   ↓
VLAN
   ↓
Layer 3 Device
   ↓
DHCP Relay
   ↓
DHCP Server
```

If the relay is incorrectly configured:

```text
DHCP Discover
       ↓
     Client
       ↓
   Relay Problem
       X
   DHCP Server
```

Possible causes:

```text
Incorrect relay configuration
Wrong DHCP server address
VLAN problem
Routing problem
Firewall filtering
```

---

# 16. Duplicate IP Address

A duplicate IP occurs when two devices use the same address.

Example:

```text
Device A → 192.168.1.50
Device B → 192.168.1.50
```

This can cause:

```text
Intermittent connectivity
ARP conflicts
Unstable connections
Application failures
```

Investigate:

```bash
ip neigh
arp -a
```

Check whether the same IP is associated with unexpected MAC addresses.

---

# 17. Troubleshooting Decision Tree

Use this decision process:

```text
Does the interface exist?
        |
       YES
        ↓
Is the interface UP?
        |
       YES
        ↓
Does it have an IP?
     /       \
   YES        NO
    |          |
    ↓          ↓
Check route   Check DHCP
    |
    ↓
Is there a default route?
     /       \
   YES        NO
    |          |
    ↓          ↓
Test gateway  Check route/config
    |
    ↓
Can gateway be reached?
     /       \
   YES        NO
    |          |
    ↓          ↓
Test Internet  Check local network
    |
    ↓
Can 8.8.8.8 be reached?
     /       \
   YES        NO
    |          |
    ↓          ↓
Test DNS      Check routing
    |
    ↓
Can google.com resolve?
     /       \
   YES        NO
    |          |
    ↓          ↓
Network OK   Troubleshoot DNS
```

---

# 18. Practical Commands

### Interface

```bash
ip link show
```

### IP address

```bash
ip addr show
```

### Routing

```bash
ip route
```

### NetworkManager

```bash
nmcli device status
```

### Connection

```bash
nmcli connection show --active
```

### DHCP

```bash
nmcli -f DHCP4 device show wlo1
```

### Network logs

```bash
journalctl -u NetworkManager
```

### DHCP logs

```bash
journalctl -u NetworkManager | grep -i dhcp
```

### DHCP packet capture

```bash
sudo tcpdump -i wlo1 -n 'udp port 67 or udp port 68'
```

### DNS

```bash
resolvectl status
```

### DNS testing

```bash
nslookup google.com
```

### Gateway test

```bash
ping -c 4 192.168.1.1
```

### Internet test

```bash
ping -c 4 8.8.8.8
```

### Hostname test

```bash
ping -c 4 google.com
```

---

# 19. Key Takeaways

When troubleshooting DHCP, follow a structured process:

```text
1. Interface
2. Link
3. IP Address
4. DHCP
5. Route
6. Gateway
7. DNS
8. Internet
9. Packet Capture
10. Logs
```

Do not assume every connectivity problem is DHCP.

Separate the problem into layers:

```text
Interface Problem
       ↓
Addressing Problem
       ↓
Routing Problem
       ↓
DNS Problem
       ↓
Application Problem
```

The goal of troubleshooting is to identify the **first layer that fails**.

---

# 🎯 DevOps Troubleshooting Principle

A strong DevOps engineer does not simply restart services.

Instead:

```text
Observe
  ↓
Measure
  ↓
Identify Failure
  ↓
Test Hypothesis
  ↓
Fix
  ↓
Verify
  ↓
Document
```

> **Learn → Practice → Break → Debug → Document → Explain**
