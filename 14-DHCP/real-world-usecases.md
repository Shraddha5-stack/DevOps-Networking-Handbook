# 🌍 Chapter 14 – DHCP Real-World Use Cases

## 📑 Table of Contents

1. Introduction
2. Home Networks
3. Enterprise Networks
4. Office Wi-Fi
5. DHCP in VLANs
6. DHCP Relay
7. Server Infrastructure
8. Cloud Environments
9. Containers and Docker
10. Kubernetes
11. CI/CD Runners
12. DevOps Troubleshooting
13. DHCP Reservations
14. Network Security
15. Real-World Failure Scenario
16. DevOps Interview Example
17. Key Takeaways

---

# 📖 1. Introduction

DHCP is used in many real-world environments to automatically provide network configuration to devices.

It can provide:

```text
IP Address
Subnet Mask
Default Gateway
DNS Server
Lease Information
Other Network Options
```

Instead of manually configuring every machine:

```text
Device 1 → Manual configuration
Device 2 → Manual configuration
Device 3 → Manual configuration
Device 4 → Manual configuration
```

DHCP allows:

```text
DHCP Server
      ↓
Automatic Configuration
      ↓
Many Clients
```

---

# 🏠 2. Home Networks

A typical home network contains:

```text
Laptop
Phone
TV
Printer
Tablet
     ↓
Wi-Fi Router
     ↓
Internet
```

The home router usually provides DHCP service.

For example:

```text
Router:
192.168.1.1

DHCP Pool:
192.168.1.100 - 192.168.1.200
```

When a laptop connects to Wi-Fi, it can automatically receive:

```text
IP:
192.168.1.105

Gateway:
192.168.1.1

DNS:
192.168.1.1
```

---

# 🏢 3. Enterprise Networks

Large organizations may have thousands of devices.

Manually configuring every machine would be difficult.

DHCP provides centralized network configuration.

Example:

```text
                  DHCP Server
                       |
          +------------+------------+
          |            |            |
        VLAN 10      VLAN 20      VLAN 30
          |            |            |
       Clients      Clients      Clients
```

Different networks can have different DHCP scopes.

---

# 📶 4. Office Wi-Fi

When an employee connects a laptop to office Wi-Fi:

```text
Laptop
   ↓
Access Point
   ↓
Network
   ↓
DHCP
   ↓
IP Configuration
```

The employee does not normally need to manually configure:

```text
IP
Gateway
DNS
```

The network provides the required configuration automatically.

---

# 🏷️ 5. DHCP in VLANs

Organizations commonly divide networks using VLANs.

Example:

```text
VLAN 10 → Developers
VLAN 20 → Operations
VLAN 30 → Finance
VLAN 40 → Guest
```

Each VLAN can have its own address range.

Example:

```text
VLAN 10
192.168.10.0/24

VLAN 20
192.168.20.0/24

VLAN 30
192.168.30.0/24
```

DHCP can provide addresses appropriate for each network.

---

# 🔄 6. DHCP Relay

DHCP servers are often centralized.

For example:

```text
Client VLAN
     |
     ↓
Layer 3 Switch
     |
     ↓
DHCP Relay
     |
     ↓
Central DHCP Server
```

The relay forwards DHCP requests between the client network and the DHCP server.

This allows one centralized DHCP infrastructure to serve multiple networks.

---

# 🖥️ 7. Server Infrastructure

DHCP can be useful for systems where addresses do not need to remain permanently fixed.

Examples:

```text
Temporary Servers
Test Machines
Development Machines
Lab Machines
```

For critical infrastructure, stable addressing is usually preferred.

Examples:

```text
Production Database
DNS Server
Load Balancer
Monitoring Server
```

These may use:

```text
Static IP
DHCP Reservation
Cloud-managed addressing
```

depending on the environment.

---

# ☁️ 8. Cloud Environments

Cloud platforms provide automated networking for virtual machines and other resources.

A virtual machine may receive:

```text
Private IP
Subnet
Default Route
DNS Configuration
```

The exact implementation depends on the cloud platform.

For a DevOps engineer, the important concept is:

```text
VM
 ↓
Virtual Network Interface
 ↓
Network Configuration
 ↓
Application
```

Understanding DHCP helps when troubleshooting connectivity inside virtual networks.

---

# 🐳 9. Containers and Docker

Docker also creates virtual networks.

For example:

```bash
docker network ls
```

You may see networks such as:

```text
bridge
host
none
```

Docker containers can receive IP addresses from Docker's internal network management.

Example:

```text
Docker Network
      ↓
Container
      ↓
Container IP
```

This is not necessarily the same as the host's normal LAN DHCP process.

Understanding the difference is important when troubleshooting containers.

---

# ☸️ 10. Kubernetes

Kubernetes networking is more complex than a simple DHCP LAN.

Kubernetes normally manages Pod networking through its networking model and CNI plugins.

For example:

```text
Node
 |
 +-- Pod
 |
 +-- Pod
 |
 +-- Pod
```

The Pod IP lifecycle is generally handled by the Kubernetes networking layer rather than simply by the physical network's DHCP server.

However, DHCP can still exist underneath the cluster infrastructure.

For example:

```text
Physical Network
       ↓
Node IP
       ↓
Kubernetes Node
       ↓
CNI
       ↓
Pod Network
```

---

# ⚙️ 11. CI/CD Runners

CI/CD runners need network connectivity to communicate with:

```text
GitHub / GitLab
Container Registry
Cloud APIs
Package Repositories
Internal Services
```

A self-hosted runner may receive its network configuration from DHCP.

Example:

```text
Self-hosted Runner
       ↓
Network
       ↓
DHCP
       ↓
IP Address
       ↓
Internet / Internal Services
```

If DHCP fails, the runner may not be able to:

```text
Download dependencies
Push images
Access repositories
Deploy applications
```

---

# 🛠️ 12. DevOps Troubleshooting

Suppose a server suddenly cannot reach an internal service.

A DevOps engineer can inspect:

### Step 1

```bash
ip addr
```

Check the IP address.

### Step 2

```bash
ip route
```

Check the routing table.

### Step 3

```bash
resolvectl status
```

Check DNS.

### Step 4

```bash
nmcli device status
```

Check connection state.

### Step 5

```bash
journalctl -u NetworkManager
```

Check networking events.

### Step 6

```bash
sudo tcpdump -i <interface> -n 'udp port 67 or udp port 68'
```

Inspect DHCP traffic if DHCP is suspected.

---

# 📌 13. DHCP Reservations

A DHCP reservation associates a client with a specific address.

Example:

```text
MAC Address
50:5A:65:B8:91:1D
        ↓
Reserved IP
192.168.1.50
```

The device can then receive the same address when it requests DHCP configuration.

Useful for:

```text
Printers
NAS
Cameras
Network Appliances
Development Devices
```

---

# 🔐 14. Network Security

DHCP itself is not an authentication mechanism.

An attacker on an improperly secured network could potentially attempt to provide false DHCP responses.

This can lead to incorrect:

```text
Gateway
DNS
Network Configuration
```

Enterprise networks can use security controls such as:

```text
DHCP Snooping
Port Security
Network Access Control
VLAN Segmentation
```

The exact controls depend on the network architecture.

---

# 🚨 15. Real-World Failure Scenario

Imagine an office has:

```text
200 employees
```

One morning, many employees report:

> "My laptop is connected to Wi-Fi, but I cannot access the Internet."

The DevOps/networking team investigates.

### Step 1 – Check DHCP

```text
Are clients receiving IP addresses?
```

### Step 2 – Check DHCP Server

```text
Is the DHCP service running?
```

### Step 3 – Check Address Pool

Maybe the pool is exhausted.

Example:

```text
Available:
192.168.1.100 - 192.168.1.200
```

If all addresses are already leased:

```text
New clients
     ↓
No available IP
     ↓
Network connectivity fails
```

### Step 4 – Check DHCP Relay

If clients are in multiple VLANs:

```text
Client
 ↓
VLAN
 ↓
DHCP Relay
 ↓
DHCP Server
```

A relay failure could prevent clients from receiving configuration.

### Step 5 – Capture traffic

```bash
sudo tcpdump -i <interface> -n 'udp port 67 or udp port 68'
```

The team can determine whether DHCP traffic is being exchanged.

---

# 💼 16. DevOps Interview Example

### Scenario

An application server suddenly has no network connectivity.

### Strong response

> First, I would verify whether the network interface is up using `ip link`. Then I would check the assigned IP using `ip addr` and the routing table using `ip route`. I would verify the NetworkManager connection using `nmcli`. If DHCP is involved, I would inspect DHCP-related information and NetworkManager logs. If the problem is still unclear, I would use `tcpdump` to inspect DHCP traffic on UDP ports 67 and 68.

This demonstrates a structured troubleshooting approach instead of randomly restarting services.

---

# 🔥 17. DHCP in a DevOps Workflow

DHCP can be part of the infrastructure beneath DevOps systems.

Example:

```text
Physical / Virtual Network
          ↓
       DHCP
          ↓
      Server IP
          ↓
     Linux Server
          ↓
       Docker
          ↓
     Application
          ↓
       CI/CD
          ↓
       Deployment
```

A basic network problem can therefore affect the entire application delivery process.

---

# 🧠 18. Key Takeaways

### DHCP provides

```text
IP
Subnet
Gateway
DNS
Lease
Other options
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
UDP 67 → Server
UDP 68 → Client
```

### Real-world uses

```text
Home Networks
Enterprise Networks
Office Wi-Fi
VLANs
DHCP Relay
Development Infrastructure
Cloud Infrastructure
CI/CD Runners
```

### Troubleshooting

```text
Interface
   ↓
IP
   ↓
Route
   ↓
DHCP
   ↓
DNS
   ↓
Connectivity
```

---

# 🎯 Final DevOps Lesson

DHCP may look like a simple networking service, but it is an important part of infrastructure.

As a DevOps engineer, you should be able to move from:

```text
"I don't have network connectivity."
```

to:

```text
Interface?
    ↓
IP?
    ↓
Gateway?
    ↓
DHCP?
    ↓
DNS?
    ↓
Packets?
    ↓
Root Cause
```

> **Learn → Practice → Break → Debug → Document → Explain**
