o
# 🧪 Chapter 14 – DHCP Practical Lab

## 📑 Table of Contents

1. Lab Objective
2. Lab Environment
3. Identify Network Interface
4. Check Current IP Address
5. Check Routing Information
6. Check DNS Configuration
7. Check NetworkManager
8. Inspect DHCP Information
9. Renew Network Connection
10. Inspect Network Logs
11. Capture DHCP Traffic
12. Test Internet Connectivity
13. Verify DNS
14. Troubleshooting Exercise
15. Expected DHCP Flow
16. Lab Summary
17. Key Takeaways

---

# 🎯 1. Lab Objective

The objective of this lab is to understand how a Linux machine receives network configuration through DHCP.

We will inspect:

- Network interface
- IP address
- Default gateway
- DNS configuration
- DHCP information
- NetworkManager
- DHCP logs
- DHCP packets
- Internet connectivity

The main DHCP process is:

```text
Discover
   ↓
Offer
   ↓
Request
   ↓
ACK
```

This is commonly called **DORA**.

---

# 💻 2. Lab Environment

### Operating System

```text
Ubuntu Linux
```

### Tools

```text
ip
nmcli
resolvectl
journalctl
tcpdump
ping
curl
```

### Network

This lab uses the local network connection of the Linux machine.

> Interface names can differ between systems. In the commands below, replace `wlo1` with your actual interface if necessary.

Find your interface:

```bash
ip link show
```

---

# 🔎 3. Identify Network Interface

Run:

```bash
ip link show
```

Example:

```text
1: lo
2: wlo1
```

Here:

```text
lo   → Loopback
wlo1 → Wi-Fi interface
```

Check the interface state:

```bash
ip link show wlo1
```

Look for:

```text
state UP
```

### Observation

Record your interface name:

```text
Interface: __________________
```

---

# 🌐 4. Check Current IP Address

Run:

```bash
ip addr show
```

Or:

```bash
ip addr show wlo1
```

Look for:

```text
inet 192.168.1.x/24
```

Example:

```text
inet 192.168.1.10/24
```

This means the interface has:

```text
IP Address:
192.168.1.10

Prefix:
24
```

### Observation

Record:

```text
IP Address: __________________
Prefix: ______________________
```

---

# 🚪 5. Check Routing Information

Run:

```bash
ip route
```

Example:

```text
default via 192.168.1.1 dev wlo1
```

This tells us that:

```text
Default Gateway = 192.168.1.1
```

The default gateway is normally the router used to reach networks outside the local subnet.

### Observation

Record:

```text
Default Gateway: __________________
Interface: ________________________
```

---

# 🌍 6. Check DNS Configuration

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

Also run:

```bash
resolvectl status
```

This can show:

```text
DNS Servers
DNS Domain
Network Interface
```

### Observation

Record:

```text
DNS Server: __________________
```

---

# ⚙️ 7. Check NetworkManager

Check whether NetworkManager is running:

```bash
systemctl status NetworkManager
```

Look for:

```text
Active: active (running)
```

Then run:

```bash
nmcli device status
```

Example:

```text
DEVICE  TYPE      STATE      CONNECTION
wlo1    wifi      connected  Home-WiFi
lo      loopback  connected  lo
```

This tells us:

```text
Device
Type
State
Connection
```

---

# 🔍 8. Inspect DHCP Information

Run:

```bash
nmcli device show wlo1
```

Look for:

```text
IP4.ADDRESS
IP4.GATEWAY
IP4.DNS
DHCP4.OPTION
```

The DHCP information may include options such as:

```text
requested_domain_name
requested_domain_name_servers
requested_subnet_mask
requested_routers
lease_time
```

The exact output depends on the network and NetworkManager version.

---

# 🔄 9. Renew Network Connection

First identify the connection name:

```bash
nmcli connection show
```

Example:

```text
NAME       UUID                                  TYPE
Home-WiFi  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  wifi
```

To reconnect:

```bash
nmcli connection down "Home-WiFi"
```

Then:

```bash
nmcli connection up "Home-WiFi"
```

After reconnecting, check:

```bash
ip addr show wlo1
```

Then:

```bash
ip route
```

And:

```bash
nmcli device show wlo1
```

### Important

Do not disconnect your active network connection if you are working remotely over SSH.

---

# 📋 10. Inspect Network Logs

NetworkManager logs are useful for troubleshooting DHCP.

Run:

```bash
journalctl -u NetworkManager -n 100
```

Search specifically for DHCP:

```bash
journalctl -u NetworkManager | grep -i dhcp
```

Follow logs live:

```bash
journalctl -u NetworkManager -f
```

Look for messages related to:

```text
DHCP
lease
IP configuration
timeout
gateway
DNS
```

---

# 🕵️ 11. Capture DHCP Traffic

This is one of the most useful practical exercises.

First identify your interface:

```bash
ip link show
```

Then run:

```bash
sudo tcpdump -i wlo1 -n 'udp port 67 or udp port 68'
```

Keep the terminal running.

Now reconnect the network connection from another terminal:

```bash
nmcli connection down "Home-WiFi"
```

Then:

```bash
nmcli connection up "Home-WiFi"
```

Watch the `tcpdump` terminal.

You may observe DHCP traffic corresponding to:

```text
DHCP Discover
DHCP Offer
DHCP Request
DHCP ACK
```

The exact packet exchange can vary depending on the existing lease and network state.

Stop packet capture with:

```text
Ctrl + C
```

---

# 🔬 12. Understand the DHCP Packet Flow

Conceptually:

```text
                 DHCP Server
                      |
                      |
Client                |
  |                   |
  |---- Discover ---->|
  |                   |
  |<----- Offer ------|
  |                   |
  |---- Request ----->|
  |                   |
  |<------ ACK -------|
  |                   |
```

Remember:

```text
D → Discover
O → Offer
R → Request
A → Acknowledgement
```

---

# 🌐 13. Test Internet Connectivity

After obtaining an IP address, test connectivity.

### Test by IP

```bash
ping -c 4 8.8.8.8
```

If successful:

```text
Network connectivity is working.
```

### Test by hostname

```bash
ping -c 4 google.com
```

If this works:

```text
Network connectivity
        +
DNS resolution
```

are both working.

---

# 🔎 14. Verify DNS

Run:

```bash
nslookup google.com
```

Or:

```bash
dig google.com
```

If `dig` is installed:

```bash
dig +short google.com
```

Compare this with:

```bash
ping -c 4 google.com
```

This helps demonstrate the relationship between:

```text
Hostname
   ↓
DNS
   ↓
IP Address
```

---

# 🧪 15. Troubleshooting Exercise

Now imagine the machine has no usable IP address.

Start with:

```bash
ip addr show
```

### Step 1 – Check interface

```bash
ip link show
```

Is it:

```text
UP
```

or:

```text
DOWN
```

?

---

### Step 2 – Check IP

```bash
ip addr show wlo1
```

Do you have an IPv4 address?

---

### Step 3 – Check route

```bash
ip route
```

Is there a:

```text
default via ...
```

route?

---

### Step 4 – Check NetworkManager

```bash
systemctl status NetworkManager
```

---

### Step 5 – Check device

```bash
nmcli device status
```

---

### Step 6 – Check DHCP information

```bash
nmcli device show wlo1
```

---

### Step 7 – Check logs

```bash
journalctl -u NetworkManager | grep -i dhcp
```

---

### Step 8 – Capture DHCP traffic

```bash
sudo tcpdump -i wlo1 -n 'udp port 67 or udp port 68'
```

This helps determine whether DHCP traffic is reaching the machine.

---

# 🚨 16. Example Troubleshooting Results

## Case 1 – No IP Address

```text
Interface → UP
IP → Missing
Route → Missing
```

Possible causes:

```text
DHCP failure
Network problem
DHCP server unavailable
VLAN problem
Authentication issue
```

---

## Case 2 – IP Exists but No Internet

```text
IP → Present
Route → Missing
```

Possible problem:

```text
Default gateway
```

Check:

```bash
ip route
```

---

## Case 3 – Internet by IP Works but Domain Fails

```text
ping 8.8.8.8 → Works
ping google.com → Fails
```

Possible problem:

```text
DNS
```

Check:

```bash
cat /etc/resolv.conf
resolvectl status
```

---

## Case 4 – DHCP Packets Not Seen

If:

```bash
sudo tcpdump -i wlo1 -n 'udp port 67 or udp port 68'
```

shows no expected DHCP traffic while reconnecting, investigate:

- Interface
- NetworkManager
- Wi-Fi association
- VLAN
- DHCP relay
- Network infrastructure

---

# 📊 17. Lab Results

Fill in your actual results after performing the lab.

```text
Operating System:
_________________________

Interface:
_________________________

IP Address:
_________________________

Subnet Prefix:
_________________________

Default Gateway:
_________________________

DNS Server:
_________________________

NetworkManager:
_________________________

DHCP Information:
_________________________

Internet Connectivity:
_________________________

DNS Resolution:
_________________________
```

---

# 🧠 18. What This Lab Demonstrates

This lab connects DHCP theory with real Linux networking.

We observed:

```text
Network Interface
       ↓
DHCP Configuration
       ↓
IP Address
       ↓
Default Gateway
       ↓
DNS
       ↓
Internet Connectivity
```

The important idea is that DHCP does not simply give the machine an IP address.

It can provide the information needed for the machine to participate in the network.

---

# 🎯 19. Key Takeaways

### DHCP

```text
Dynamic Host Configuration Protocol
```

### DORA

```text
Discover
Offer
Request
ACK
```

### Ports

```text
UDP 67 → DHCP Server
UDP 68 → DHCP Client
```

### Useful Linux commands

```bash
ip addr
ip link
ip route
nmcli
resolvectl
journalctl
tcpdump
```

### Troubleshooting sequence

```text
Interface
   ↓
IP Address
   ↓
Route
   ↓
DHCP
   ↓
DNS
   ↓
Internet
```

---

# 🏁 Lab Completion

After completing the exercises, you should be able to:

- Identify your network interface.
- Find the IP address assigned to the interface.
- Find the default gateway.
- Identify DNS configuration.
- Inspect DHCP information.
- Check NetworkManager.
- Inspect DHCP-related logs.
- Capture DHCP traffic.
- Understand DORA.
- Troubleshoot common DHCP problems.

> **Learn → Practice → Break → Debug → Document → Explain**
