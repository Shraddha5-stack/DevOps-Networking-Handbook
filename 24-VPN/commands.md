# 🔐 Chapter 24 — VPN Commands & Hands-On Practice

This chapter contains Linux networking commands useful for understanding, testing, and troubleshooting VPN connectivity.

> **Note:** The commands below are mostly safe diagnostic commands. VPN configuration commands can change network connectivity, so run configuration commands only when you understand the environment.

---

# 1. Check Network Interfaces

### Command

```bash
ip addr
```

### Short form

```bash
ip a
```

### Purpose

Displays network interfaces and their IP addresses.

### Example

```text
lo
wlo1
docker0
```

A VPN may create an additional interface such as:

```text
tun0
```

or:

```text
wg0
```

### Observation

```text
VPN connection active → VPN interface may appear
VPN disconnected → VPN interface may disappear
```

---

# 2. Check Network Routes

### Command

```bash
ip route
```

### Purpose

Displays the system routing table.

### Example

```text
default via 192.168.1.1 dev wlo1
10.10.0.0/16 dev tun0
```

### Observation

The route:

```text
10.10.0.0/16 dev tun0
```

indicates that traffic destined for the `10.10.0.0/16` network can be routed through the VPN interface.

---

# 3. Identify the Default Route

### Command

```bash
ip route | grep default
```

### Example

```text
default via 192.168.1.1 dev wlo1
```

### Observation

The default route determines where traffic goes when no more specific route exists.

---

# 4. Check a Specific Route

### Command

```bash
ip route get 10.10.0.10
```

### Purpose

Shows how Linux would route traffic to a particular destination.

### Example

```text
10.10.0.10 dev tun0 src 10.8.0.2
```

### Observation

This is useful for determining whether traffic is actually going through the VPN.

---

# 5. Check VPN Interfaces

### Command

```bash
ip link show
```

### Purpose

Lists network interfaces.

Look for interfaces such as:

```text
tun0
wg0
```

depending on the VPN technology.

### Observation

* `tun0` → commonly associated with TUN-based VPNs
* `wg0` → commonly associated with WireGuard

The exact interface name depends on the VPN configuration.

---

# 6. Check Interface Details

### Command

```bash
ip addr show tun0
```

### Purpose

Displays the IP configuration of a TUN interface.

If using WireGuard:

```bash
ip addr show wg0
```

### Observation

Record:

* Interface state
* IP address
* Prefix
* MTU

---

# 7. Check Interface State

### Command

```bash
ip link show tun0
```

### Example

```text
tun0: <POINTOPOINT,UP,LOWER_UP>
```

### Observation

`UP` generally indicates that the interface is administratively active.

---

# 8. Test Basic Connectivity

### Command

```bash
ping -c 4 8.8.8.8
```

### Purpose

Tests basic IP connectivity without depending on DNS.

### Observation

If this works but hostname resolution does not, DNS may be the problem.

---

# 9. Test DNS Resolution

### Command

```bash
getent hosts example.com
```

### Purpose

Tests hostname resolution using the system's configured name-resolution mechanisms.

### Observation

If an IP address is returned, DNS/name resolution is working for that hostname.

---

# 10. Check DNS Configuration

### Command

```bash
cat /etc/resolv.conf
```

### Purpose

Shows DNS resolver configuration.

### Observation

When using a VPN, DNS configuration may change depending on the VPN client and operating system.

---

# 11. Check DNS with `nslookup`

If installed:

```bash
nslookup example.com
```

### Purpose

Tests DNS resolution directly.

### Observation

Check:

* DNS server
* Resolved IP address
* Response status

---

# 12. Check DNS with `dig`

If installed:

```bash
dig example.com
```

### Short version

```bash
dig +short example.com
```

### Purpose

Provides detailed DNS query information.

---

# 13. Test a Private IP

If your VPN provides access to a private network, test a known private IP.

Example:

```bash
ping -c 4 10.10.0.10
```

### Observation

If the destination responds, basic network connectivity exists.

If it does not respond, investigate:

* Routing
* Firewall
* VPN tunnel
* Destination availability

---

# 14. Test a Private Service

Use `curl` when the private service exposes HTTP/HTTPS.

Example:

```bash
curl -v http://10.10.0.10
```

### HTTPS

```bash
curl -vk https://10.10.0.10
```

### Observation

Look for:

```text
Connected
HTTP/1.1 200 OK
```

or another valid HTTP response.

---

# 15. Test a TCP Port

Use `nc` if available.

```bash
nc -vz 10.10.0.10 443
```

### Example

```text
Connection to 10.10.0.10 443 port [tcp/https] succeeded!
```

### Observation

This helps determine whether a specific TCP service is reachable.

---

# 16. Check Listening Ports

### Command

```bash
sudo ss -ltnup
```

### Purpose

Displays listening TCP and UDP sockets.

### Useful filters

```bash
sudo ss -ltnp
```

```bash
sudo ss -lunp
```

### Observation

Use this to identify services listening on the local system.

---

# 17. Check Established Connections

### Command

```bash
ss -tun
```

### Purpose

Displays TCP and UDP connections.

### Observation

Useful for checking whether connections to private services are established.

---

# 18. Check the Network Path

### Command

```bash
tracepath 10.10.0.10
```

If `tracepath` is unavailable:

```bash
traceroute 10.10.0.10
```

### Purpose

Shows the network path toward a destination.

### Observation

This can help identify where connectivity stops.

---

# 19. Check MTU

### Command

```bash
ip link show
```

Look for:

```text
mtu 1500
```

or another value.

### Check a specific interface

```bash
ip link show tun0
```

### Observation

VPN tunnels can have a lower effective MTU because of encapsulation overhead.

---

# 20. Check Routing Table for Private Networks

### Command

```bash
ip route | grep -E '10\.|172\.|192\.168\.'
```

### Purpose

Looks for common private IPv4 network routes.

### Observation

This can help identify routes added for private infrastructure.

---

# 21. Check Network Statistics

### Command

```bash
ip -s link
```

### Purpose

Displays interface statistics.

Look for:

```text
RX
TX
errors
dropped
```

### Observation

Large numbers of errors or dropped packets can indicate network problems.

---

# 22. Check VPN-Related Processes

### Command

```bash
ps aux | grep -Ei 'openvpn|wireguard|wg-quick'
```

### Purpose

Looks for common VPN-related processes.

### Observation

The result depends on which VPN implementation is installed.

---

# 23. Check WireGuard Status

If WireGuard is installed:

```bash
sudo wg show
```

### Purpose

Displays WireGuard interface and peer information.

### Useful information

* Interface
* Public key
* Peer
* Latest handshake
* Transfer statistics

### Observation

A recent handshake generally indicates recent communication with the peer.

---

# 24. Check WireGuard Interface

```bash
sudo wg show wg0
```

### Purpose

Displays information specifically for `wg0`.

---

# 25. Check WireGuard Configuration

```bash
sudo wg showconf wg0
```

### Important

Be careful when sharing configuration output because VPN configurations can contain sensitive information.

Do not publish private keys.

---

# 26. Check OpenVPN Process

### Command

```bash
ps aux | grep openvpn
```

### Purpose

Checks whether an OpenVPN process is running.

---

# 27. Check OpenVPN Service

On systems using systemd:

```bash
systemctl status openvpn
```

Depending on the installation, the service may have a different name.

You can search for related units:

```bash
systemctl list-units --type=service | grep -i openvpn
```

---

# 28. Check NetworkManager VPN Connections

If NetworkManager is being used:

```bash
nmcli connection show
```

### Purpose

Lists configured network connections.

### Look for

VPN connections and their status.

---

# 29. Show Active Network Connections

```bash
nmcli connection show --active
```

### Observation

This helps identify which network and VPN connections are currently active.

---

# 30. Inspect a NetworkManager VPN Connection

```bash
nmcli connection show "<VPN-NAME>"
```

### Purpose

Displays configuration information for the selected connection.

Be careful when sharing output because it may contain sensitive configuration information.

---

# 31. Test the VPN Gateway

If you know the VPN gateway address:

```bash
ping -c 4 <VPN-GATEWAY-IP>
```

Example:

```bash
ping -c 4 10.8.0.1
```

### Observation

A successful response indicates basic IP connectivity to the gateway.

---

# 32. Test Private Network Routing

Suppose your organization uses:

```text
10.20.0.0/16
```

Check:

```bash
ip route get 10.20.0.10
```

### Observation

Confirm that Linux selects the expected VPN interface.

---

# 33. Compare Before and After VPN Connection

Before connecting:

```bash
ip addr
ip route
```

Save the output.

Connect to the VPN.

Then run:

```bash
ip addr
ip route
```

### Observation

Compare:

* New interface
* New IP address
* New routes
* Changed DNS configuration

This is one of the best ways to understand what a VPN changes on a Linux system.

---

# 34. Check Public IP

You can use:

```bash
curl -4 https://ifconfig.me
```

### Purpose

Shows the public IPv4 address observed by the external service.

### Observation

With some VPN configurations, the public IP may change when the VPN is connected.

> This depends on whether the VPN is configured as a full tunnel or split tunnel.

---

# 35. Check IPv4 and IPv6 Addresses

### IPv4

```bash
ip -4 addr
```

### IPv6

```bash
ip -6 addr
```

### Observation

VPN behavior can differ between IPv4 and IPv6.

---

# 36. Check Firewall Status

If using UFW:

```bash
sudo ufw status verbose
```

### Purpose

Checks firewall rules that could affect VPN traffic.

---

# 37. Check Firewall Rules with nftables

On systems using nftables:

```bash
sudo nft list ruleset
```

### Observation

Look for rules affecting:

* VPN interface
* Private subnets
* TCP/UDP traffic
* Forwarding

---

# 38. Check IP Forwarding

### Command

```bash
sysctl net.ipv4.ip_forward
```

### Example

```text
net.ipv4.ip_forward = 1
```

### Purpose

IP forwarding is important when a Linux system is routing traffic between networks.

---

# 39. Check Kernel Network Parameters

```bash
sysctl -a 2>/dev/null | grep net.ipv4
```

### Purpose

Useful for advanced network troubleshooting.

---

# 40. Capture VPN Traffic with tcpdump

If `tcpdump` is installed:

```bash
sudo tcpdump -i tun0
```

For WireGuard:

```bash
sudo tcpdump -i wg0
```

### Purpose

Captures packets on the VPN interface.

### Stop

Press:

```text
Ctrl + C
```

### Observation

Packet capture can help determine whether traffic is entering or leaving the VPN interface.

> Do not share packet captures publicly if they contain sensitive information.

---

# 41. Capture Traffic on a Specific Port

Example:

```bash
sudo tcpdump -i tun0 port 443
```

### Purpose

Captures HTTPS-related TCP traffic on the VPN interface.

---

# 42. Check ARP/Neighbor Information

### Command

```bash
ip neigh
```

### Purpose

Displays IPv4 neighbor information.

### Observation

Useful when troubleshooting local network connectivity.

---

# 43. Check Network Connectivity Step by Step

A useful troubleshooting sequence is:

```bash
ip addr
```

Then:

```bash
ip route
```

Then:

```bash
ip route get <private-ip>
```

Then:

```bash
ping -c 4 <private-ip>
```

Then:

```bash
nc -vz <private-ip> <port>
```

Then:

```bash
curl -v http://<private-ip>:<port>
```

### Troubleshooting flow

```text
Interface
   ↓
Route
   ↓
Reachability
   ↓
Port
   ↓
Application
```

---

# 44. Hands-On Lab — Observe VPN Networking

## Objective

Understand how network interfaces and routes change when a VPN is connected.

### Step 1 — Check interfaces

```bash
ip addr
```

Record the output.

### Step 2 — Check routes

```bash
ip route
```

Record the output.

### Step 3 — Check DNS

```bash
cat /etc/resolv.conf
```

### Step 4 — Connect to your VPN

Use your organization's or lab's approved VPN client.

### Step 5 — Check interfaces again

```bash
ip addr
```

### Step 6 — Check routes again

```bash
ip route
```

### Step 7 — Compare the results

Look for:

* New VPN interface
* VPN IP address
* New routes
* DNS changes
* MTU changes

---

# 45. Hands-On Lab — Test a Private Service

Assume the private service is:

```text
10.10.0.10:443
```

Run:

```bash
ip route get 10.10.0.10
```

Then:

```bash
ping -c 4 10.10.0.10
```

Then:

```bash
nc -vz 10.10.0.10 443
```

Finally:

```bash
curl -vk https://10.10.0.10
```

### Observation

Record whether each step succeeds.

| Test         | Result    |
| ------------ | --------- |
| Route exists | Pass/Fail |
| Ping         | Pass/Fail |
| TCP 443      | Pass/Fail |
| HTTPS        | Pass/Fail |

---

# 46. Hands-On Lab — Full Tunnel vs Split Tunnel

Before VPN:

```bash
ip route
```

Check public IP:

```bash
curl -4 https://ifconfig.me
```

Connect to the VPN.

Run:

```bash
ip route
```

Then:

```bash
curl -4 https://ifconfig.me
```

### Observation

If the default route changes through the VPN, it may indicate a full-tunnel configuration.

If only private-network routes are added, it may indicate split tunneling.

---

# 47. Hands-On Lab — DNS Troubleshooting

Test:

```bash
getent hosts example.com
```

Then test an internal hostname if your VPN provides one:

```bash
getent hosts <internal-hostname>
```

Check:

```bash
cat /etc/resolv.conf
```

### Observation

If public DNS works but the internal hostname does not resolve, investigate the VPN's DNS configuration.

---

# 48. Hands-On Lab — Route Troubleshooting

Suppose the private network is:

```text
10.20.0.0/16
```

Run:

```bash
ip route | grep 10.20
```

Then:

```bash
ip route get 10.20.0.10
```

### Observation

Confirm:

```text
Destination
Interface
Source IP
Gateway
```

---

# 49. Useful Command Cheat Sheet

| Task                       | Command                       |
| -------------------------- | ----------------------------- |
| Show interfaces            | `ip addr`                     |
| Show interface state       | `ip link`                     |
| Show routes                | `ip route`                    |
| Find route                 | `ip route get <IP>`           |
| Test connectivity          | `ping <IP>`                   |
| Test DNS                   | `getent hosts <HOST>`         |
| DNS configuration          | `cat /etc/resolv.conf`        |
| DNS lookup                 | `nslookup <HOST>`             |
| Detailed DNS               | `dig <HOST>`                  |
| Check TCP port             | `nc -vz <IP> <PORT>`          |
| HTTP test                  | `curl -v <URL>`               |
| Listening ports            | `sudo ss -ltnup`              |
| Connections                | `ss -tun`                     |
| Trace path                 | `tracepath <IP>`              |
| Interface statistics       | `ip -s link`                  |
| Neighbor table             | `ip neigh`                    |
| WireGuard status           | `sudo wg show`                |
| NetworkManager connections | `nmcli connection show`       |
| Firewall status            | `sudo ufw status verbose`     |
| nftables rules             | `sudo nft list ruleset`       |
| Packet capture             | `sudo tcpdump -i <interface>` |

---

# 50. Troubleshooting Checklist

When VPN connectivity fails:

```text
☐ VPN client running
☐ VPN authentication successful
☐ VPN interface exists
☐ VPN interface is UP
☐ VPN IP address assigned
☐ Private route exists
☐ Correct route selected
☐ Gateway reachable
☐ Private IP reachable
☐ Required TCP/UDP port reachable
☐ DNS resolution works
☐ Firewall allows required traffic
☐ MTU is appropriate
☐ VPN logs checked
```

---

# 🎯 Chapter 24 Practical Summary

The most important commands to remember are:

```bash
ip addr
ip route
ip route get <IP>
ip link
ping <IP>
getent hosts <HOST>
cat /etc/resolv.conf
ss -ltnup
nc -vz <IP> <PORT>
curl -v <URL>
tracepath <IP>
sudo wg show
nmcli connection show
```

The core VPN troubleshooting approach is:

```text
VPN
 ↓
Interface
 ↓
IP Address
 ↓
Route
 ↓
Connectivity
 ↓
Port
 ↓
DNS
 ↓
Application
```

A DevOps engineer should be able to identify **where the connection fails** instead of simply assuming that the VPN itself is broken.
