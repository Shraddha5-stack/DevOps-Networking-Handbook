# 🎯 Chapter 14 – DHCP Interview Questions

## Basic Questions

### 1. What is DHCP?

DHCP stands for **Dynamic Host Configuration Protocol**.

It automatically provides network configuration to clients, such as:

- IP address
- Subnet mask
- Default gateway
- DNS server
- Lease information

---

### 2. Why is DHCP used?

DHCP eliminates the need to manually configure network settings on every device.

Instead of:

```text
Manually configure every device
```

we can use:

```text
DHCP Server
     ↓
Automatic Network Configuration
```

This reduces configuration effort and human errors.

---

### 3. What is DORA?

DORA represents the four main steps of DHCP:

```text
D → Discover
O → Offer
R → Request
A → Acknowledgement
```

Flow:

```text
Client
  ↓ Discover
Server
  ↓ Offer
Client
  ↓ Request
Server
  ↓ ACK
Client
```

---

### 4. What is DHCP Discover?

DHCP Discover is the initial message sent by a DHCP client to find available DHCP servers.

The client does not initially know the DHCP server's address, so the initial discovery uses broadcast mechanisms.

---

### 5. What is DHCP Offer?

A DHCP Offer is sent by a DHCP server in response to a DHCP Discover.

It may contain:

```text
IP Address
Subnet Mask
Gateway
DNS Server
Lease Time
```

---

### 6. What is DHCP Request?

The DHCP Request indicates that the client wants to use the offered configuration.

---

### 7. What is DHCP ACK?

ACK means **Acknowledgement**.

The DHCP server sends the ACK to confirm the client's network configuration.

---

### 8. Which transport protocol does DHCP use?

DHCP uses:

```text
UDP
```

---

### 9. Which ports does DHCP use?

```text
UDP 67 → DHCP Server
UDP 68 → DHCP Client
```

A common interview answer is:

> DHCP server listens on UDP port 67, while the DHCP client uses UDP port 68.

---

### 10. What is a DHCP lease?

A DHCP lease is the period for which a client is allowed to use an assigned IP address.

Example:

```text
IP:
192.168.1.100

Lease:
8 hours
```

The client can renew the lease before it expires.

---

## Intermediate Questions

### 11. What is a DHCP pool?

A DHCP pool is the range of IP addresses available for dynamic allocation.

Example:

```text
192.168.1.100
-
192.168.1.200
```

The DHCP server allocates addresses from this range.

---

### 12. What is a DHCP scope?

A DHCP scope defines the address range and associated network configuration that a DHCP server can provide for a particular network.

It may include:

```text
IP Range
Subnet Mask
Gateway
DNS
Lease Duration
```

---

### 13. What is DHCP reservation?

A DHCP reservation allows a specific client to consistently receive a particular IP address.

A reservation can be associated with a device identifier such as its MAC address.

Example:

```text
Device
  ↓
MAC Address
  ↓
Reserved IP
  ↓
192.168.1.50
```

Useful for:

```text
Printers
Servers
Cameras
Infrastructure Devices
```

---

### 14. What is DHCP relay?

A DHCP relay forwards DHCP requests between a client network and a DHCP server across a routed network.

This is necessary because DHCP broadcasts normally do not cross routers.

Example:

```text
Client
  ↓
Router / L3 Switch
  ↓
DHCP Relay
  ↓
DHCP Server
```

---

### 15. Why is DHCP relay required?

Imagine:

```text
VLAN 10
   |
   ↓
Router
   |
   ↓
DHCP Server
```

The DHCP Discover from the client is initially broadcast.

Routers normally do not forward that broadcast.

A DHCP relay allows the request to reach a DHCP server located on another network.

---

### 16. What is DHCP renewal?

A DHCP client does not normally wait until the lease completely expires.

It attempts to renew its lease according to the DHCP protocol.

Conceptually:

```text
Client
  ↓
Renew Request
  ↓
DHCP Server
  ↓
ACK
  ↓
Lease continues
```

---

### 17. What happens if a DHCP lease expires?

If the client cannot successfully renew or obtain another lease before expiration, it eventually must stop using the expired configuration and attempt to obtain valid network configuration again.

---

### 18. What is DHCP release?

A DHCP client can send a DHCP Release message to indicate that it is giving up its leased address.

The server can then make that address available for reuse.

---

### 19. What information can DHCP provide?

DHCP can provide:

```text
IP Address
Subnet Mask
Default Gateway
DNS Server
Domain Name
Lease Information
Other DHCP Options
```

---

### 20. What is the difference between DHCP and DNS?

DHCP provides network configuration.

DNS resolves names to addresses.

```text
DHCP
 ↓
Network Configuration

DNS
 ↓
Name Resolution
```

Example:

```text
DHCP:
192.168.1.5
Gateway:
192.168.1.1
DNS:
192.168.1.1

DNS:
google.com
 ↓
IP Address
```

---

## Scenario-Based Questions

### 21. A Linux machine has no IP address. How would you troubleshoot it?

I would follow a structured process:

```bash
ip link show
```

Check whether the interface is up.

Then:

```bash
ip addr show
```

Check whether an IPv4 address exists.

Then:

```bash
nmcli device status
```

Check the connection state.

Then:

```bash
nmcli device show wlo1
```

Inspect network and DHCP-related information.

Then:

```bash
journalctl -u NetworkManager
```

Check network logs.

Finally, if necessary:

```bash
sudo tcpdump -i wlo1 -n 'udp port 67 or udp port 68'
```

to inspect DHCP traffic.

---

### 22. The machine has an IP but cannot access the Internet. What do you check?

First:

```bash
ip route
```

Check for a default route.

For example:

```text
default via 192.168.1.1
```

Then test the gateway:

```bash
ping -c 4 192.168.1.1
```

Then test Internet connectivity by IP:

```bash
ping -c 4 8.8.8.8
```

---

### 23. The machine can ping 8.8.8.8 but cannot ping google.com. What is likely wrong?

The likely problem is **DNS resolution**.

Check:

```bash
cat /etc/resolv.conf
```

and:

```bash
resolvectl status
```

Then test:

```bash
nslookup google.com
```

or:

```bash
dig google.com
```

---

### 24. How would you inspect DHCP traffic on Linux?

Use `tcpdump`:

```bash
sudo tcpdump -i wlo1 -n 'udp port 67 or udp port 68'
```

This allows us to inspect DHCP packets.

We can look for traffic corresponding to:

```text
Discover
Offer
Request
ACK
```

---

### 25. How do you check whether NetworkManager is running?

```bash
systemctl status NetworkManager
```

You can also check devices with:

```bash
nmcli device status
```

---

### 26. How do you reconnect a NetworkManager connection?

First identify the connection:

```bash
nmcli connection show --active
```

Then:

```bash
nmcli connection down "connection-name"
```

and:

```bash
nmcli connection up "connection-name"
```

---

### 27. What is the difference between DHCP and static IP configuration?

### DHCP

```text
Automatic
Lease-based
Centralized
Easy to manage at scale
```

### Static

```text
Manually configured
Fixed until changed
More administrative work
Useful for certain infrastructure
```

---

### 28. Can a DHCP client have the same IP every time?

Yes.

A DHCP reservation can be configured so that a particular client consistently receives the same IP address.

---

### 29. Can DHCP provide DNS information?

Yes.

DHCP can provide the client with DNS server information.

For example:

```text
DNS Server:
192.168.1.1
```

---

### 30. What is the role of the default gateway provided by DHCP?

The default gateway tells the client where to send traffic destined for networks outside its local subnet.

Example:

```text
Laptop
192.168.1.5
    ↓
Gateway
192.168.1.1
    ↓
Internet
```

---

# 💼 DevOps-Focused Questions

### 31. Why should a DevOps engineer understand DHCP?

Because DevOps engineers work with:

```text
Linux
Virtual Machines
Cloud
Bare Metal
Networking
Containers
CI/CD Runners
Kubernetes Infrastructure
```

Network configuration problems can affect application deployment and infrastructure.

---

### 32. How can DHCP affect a server?

If a server depends on DHCP and receives a different IP address, applications or other systems that expect the previous address may be affected.

For infrastructure that requires a stable address, organizations often use static addressing, reservations, or other controlled network designs.

---

### 33. How does DHCP relate to cloud infrastructure?

Cloud environments automatically provide network configuration to virtual network interfaces through the cloud networking platform.

The exact implementation differs between cloud providers.

---

### 34. What happens if the DHCP server is unavailable?

Existing clients may continue using their valid leases for some time.

New clients may fail to obtain network configuration.

Clients whose leases expire without successful renewal may eventually lose valid network configuration.

---

### 35. How would you explain DHCP in an interview?

A strong answer:

> DHCP stands for Dynamic Host Configuration Protocol. It automatically provides network configuration to clients. The client and server commonly follow the DORA process: Discover, Offer, Request, and Acknowledgement. DHCP uses UDP, with port 67 used by the server and port 68 by the client. DHCP can provide an IP address, subnet mask, default gateway, DNS server and other network options.

---

# 🧠 Quick Interview Revision

Remember:

```text
DHCP
 ↓
Automatic Network Configuration
```

```text
D → Discover
O → Offer
R → Request
A → ACK
```

```text
UDP 67 → Server
UDP 68 → Client
```

```text
DHCP Pool
 ↓
Available IP Addresses
```

```text
DHCP Reservation
 ↓
Consistent IP for a Specific Client
```

```text
DHCP Relay
 ↓
Allows DHCP requests to reach servers
across routed networks
```

---

# 🎯 One-Minute Interview Answer

> DHCP automatically configures network clients. When a client joins a network, it uses the DORA process: Discover, Offer, Request, and Acknowledgement. The DHCP server can provide an IP address, subnet mask, default gateway, DNS server and other options. DHCP uses UDP ports 67 and 68. In larger networks, DHCP relay can forward client requests to a centralized DHCP server.

---

> **Learn → Practice → Break → Debug → Document → Explain**
