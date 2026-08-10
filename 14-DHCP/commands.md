# 💻 Chapter 14 – DHCP Commands

## 📑 Table of Contents

1. Introduction
2. Check IP Address
3. Check Network Interface
4. Check Interface State
5. Check Default Route
6. Check DNS Configuration
7. Check NetworkManager
8. Check DHCP Connection
9. Renew DHCP Lease
10. Release DHCP Lease
11. Check DHCP Lease Information
12. Check Network Events
13. Check Listening DHCP Ports
14. Check DHCP Packets
15. Useful Command Summary
16. Troubleshooting Flow

---

# 📖 1. Introduction

DHCP automatically provides network configuration to a client.

On Linux, DHCP troubleshooting usually involves checking:

```text
IP Address
Interface
Route
DNS
NetworkManager
DHCP Lease
Network Logs
DHCP Packets
```

Different Linux distributions use different networking tools, so some commands may not be installed or may behave differently.

---

# 🌐 2. Check IP Address

The most important command is:

```bash
ip addr show
```

Short form:

```bash
ip a
```

Example:

```text
wlo1:
    inet 192.168.1.10/24
```

This tells us that the interface received:

```text
IP Address:
192.168.1.10
```

---

# 📡 3. Check Network Interface

Run:

```bash
ip link show
```

This displays network interfaces.

Example:

```text
1: lo
2: wlo1
```

Common interfaces include:

```text
lo
eth0
ens33
enp0s3
wlan0
wlo1
```

The exact interface name depends on the system.

---

# 🟢 4. Check Interface State

Run:

```bash
ip link show wlo1
```

Replace `wlo1` with your actual interface.

Look for:

```text
state UP
```

`UP` means the interface is operational.

---

# 🚪 5. Check Default Route

Run:

```bash
ip route
```

Example:

```text
default via 192.168.1.1 dev wlo1
```

This shows the default gateway.

The gateway is usually provided as part of the network configuration.

---

# 🌐 6. Check DNS Configuration

Run:

```bash
cat /etc/resolv.conf
```

Look for:

```text
nameserver
```

Example:

```text
nameserver 192.168.1.1
```

You can also check:

```bash
resolvectl status
```

This provides detailed DNS configuration information.

---

# ⚙️ 7. Check NetworkManager

Many modern Linux desktop distributions use **NetworkManager**.

Check its status:

```bash
systemctl status NetworkManager
```

If NetworkManager is running, you can use:

```bash
nmcli
```

---

## Show Network Devices

```bash
nmcli device status
```

Example:

```text
DEVICE  TYPE      STATE      CONNECTION
wlo1    wifi      connected  Home-WiFi
lo      loopback  connected  lo
```

---

# 🔍 8. Check DHCP Connection

Show active connections:

```bash
nmcli connection show
```

Show details of a connection:

```bash
nmcli connection show "Home-WiFi"
```

The exact connection name will be different on your machine.

You can also inspect a device:

```bash
nmcli device show wlo1
```

Look for information such as:

```text
IP4.ADDRESS
IP4.GATEWAY
IP4.DNS
DHCP4.OPTION
```

---

# 🔄 9. Renew DHCP Lease

With NetworkManager, you can reconnect the connection:

```bash
nmcli connection down "Home-WiFi"
nmcli connection up "Home-WiFi"
```

This can cause the interface to obtain its network configuration again.

Another approach on systems using NetworkManager is:

```bash
nmcli device reapply wlo1
```

The exact behavior depends on the current connection state and configuration.

---

# 📴 10. Release DHCP Lease

If your system uses `dhclient`, you may see commands such as:

```bash
sudo dhclient -r
```

This requests release of the DHCP lease.

To request a new lease:

```bash
sudo dhclient
```

However, `dhclient` is not installed or used by every modern Linux distribution.

Check first:

```bash
which dhclient
```

---

# 📄 11. Check DHCP Lease Information

The location of DHCP lease files depends on the networking software.

With NetworkManager, lease information can often be inspected through:

```bash
nmcli device show wlo1
```

Look for:

```text
DHCP4.OPTION
```

For systems using other DHCP clients, lease files may exist under locations such as:

```text
/var/lib/dhcp/
```

or:

```text
/var/lib/NetworkManager/
```

Do not assume one location applies to every Linux distribution.

---

# 📋 12. Check Network Events

NetworkManager logs can help diagnose DHCP problems.

Run:

```bash
journalctl -u NetworkManager
```

For recent logs:

```bash
journalctl -u NetworkManager -n 100
```

Follow logs live:

```bash
journalctl -u NetworkManager -f
```

Look for messages related to:

```text
DHCP
IP configuration
timeout
lease
gateway
DNS
```

---

# 🔌 13. Check Listening DHCP Ports

DHCP uses:

```text
UDP 67
UDP 68
```

You can inspect UDP sockets with:

```bash
ss -uln
```

To filter for DHCP ports:

```bash
ss -uln | grep -E ':67|:68'
```

On a normal DHCP client, you may not always see a permanently listening socket on UDP 68 because the DHCP client implementation and network manager determine how sockets are handled.

---

# 🕵️ 14. Check DHCP Packets

Packet capture is extremely useful when DHCP is not working.

First identify the interface:

```bash
ip link
```

Then capture DHCP traffic:

```bash
sudo tcpdump -i wlo1 -n 'udp port 67 or udp port 68'
```

Replace:

```text
wlo1
```

with your actual interface.

---

## DHCP Packet Flow

You may observe traffic corresponding to:

```text
DHCP Discover
        ↓
DHCP Offer
        ↓
DHCP Request
        ↓
DHCP ACK
```

Conceptually:

```text
Client                         DHCP Server

   |------ Discover ---------->|
   |<------- Offer ------------|
   |------ Request ----------->|
   |<--------- ACK -------------|
```

This is one of the best ways to understand what is actually happening on the network.

---

# 🧪 15. Useful Command Summary

## IP Address

```bash
ip addr show
```

## Interfaces

```bash
ip link show
```

## Routing

```bash
ip route
```

## DNS

```bash
cat /etc/resolv.conf
```

## Resolver Status

```bash
resolvectl status
```

## NetworkManager Status

```bash
systemctl status NetworkManager
```

## Network Devices

```bash
nmcli device status
```

## Connections

```bash
nmcli connection show
```

## Device Details

```bash
nmcli device show wlo1
```

## NetworkManager Logs

```bash
journalctl -u NetworkManager
```

## DHCP Client Check

```bash
which dhclient
```

## DHCP Release

```bash
sudo dhclient -r
```

## DHCP Request

```bash
sudo dhclient
```

## DHCP Packet Capture

```bash
sudo tcpdump -i wlo1 -n 'udp port 67 or udp port 68'
```

---

# 🛠️ 16. DHCP Troubleshooting Flow

If a Linux machine does not receive an IP address:

```text
                 Start
                   ↓
           Check interface
                   ↓
             ip link show
                   ↓
             Interface UP?
              /          \
            No            Yes
            ↓              ↓
        Fix link      Check IP address
                           ↓
                       ip addr
                           ↓
                    IP assigned?
                    /          \
                  No            Yes
                  ↓              ↓
            Check DHCP      Check route
            configuration        ↓
                  ↓          ip route
            nmcli / logs
                  ↓
            Check DHCP traffic
                  ↓
              tcpdump
                  ↓
       Discover → Offer → Request → ACK
```

---

# 🎯 Example Troubleshooting Session

Suppose your laptop suddenly has no network connection.

### Step 1

Check the interface:

```bash
ip link show
```

### Step 2

Check the IP:

```bash
ip addr show
```

### Step 3

Check the route:

```bash
ip route
```

### Step 4

Check NetworkManager:

```bash
systemctl status NetworkManager
```

### Step 5

Check connection:

```bash
nmcli device status
```

### Step 6

Inspect DHCP information:

```bash
nmcli device show wlo1
```

### Step 7

Check logs:

```bash
journalctl -u NetworkManager -n 100
```

### Step 8

If necessary, capture DHCP traffic:

```bash
sudo tcpdump -i wlo1 -n 'udp port 67 or udp port 68'
```

---

# 🧠 Important Reminder

Do not run commands blindly.

Before changing network configuration, identify:

```text
1. Interface name
2. Current IP
3. Default gateway
4. DNS configuration
5. Network manager
6. DHCP client
```

Useful commands:

```bash
ip addr
ip route
resolvectl status
nmcli device status
```

---

# 📌 Final Command Cheat Sheet

```bash
# IP address
ip addr show

# Interfaces
ip link show

# Routes
ip route

# DNS
cat /etc/resolv.conf

# DNS status
resolvectl status

# NetworkManager
systemctl status NetworkManager

# Network devices
nmcli device status

# Network connections
nmcli connection show

# Device details
nmcli device show wlo1

# NetworkManager logs
journalctl -u NetworkManager -n 100

# Check dhclient
which dhclient

# Release DHCP lease (if dhclient is used)
sudo dhclient -r

# Request DHCP lease (if dhclient is used)
sudo dhclient

# Capture DHCP traffic
sudo tcpdump -i wlo1 -n 'udp port 67 or udp port 68'
```

---

# 🎯 Interview Tip

If asked:

> **How do you troubleshoot a Linux machine that did not receive an IP from DHCP?**

A good answer is:

```text
First check the interface using ip link and ip addr.
Then check the routing table with ip route.
I check NetworkManager and DHCP information using nmcli.
I inspect NetworkManager logs using journalctl.
If the problem is still unclear, I capture UDP ports 67 and 68
with tcpdump to determine whether the DHCP Discover, Offer,
Request and ACK exchange is happening.
```

> **Learn → Practice → Break → Debug → Document → Explain**
