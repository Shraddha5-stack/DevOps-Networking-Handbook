# Chapter 36 — Troubleshooting — Commands

This file contains practical commands for troubleshooting Linux, networking, services, Docker, Kubernetes, and AWS environments.

---

# 1. Basic System Information

## Hostname

```bash
hostname
```

## OS information

```bash
cat /etc/os-release
```

## Kernel information

```bash
uname -a
```

## Current date and time

```bash
date
```

## Current user

```bash
whoami
```

## Current directory

```bash
pwd
```

---

# 2. Network Interface Commands

## Show all interfaces and IP addresses

```bash
ip addr
```

## Short IP information

```bash
ip -brief addr
```

## Show network interfaces

```bash
ip link
```

## Show interface statistics

```bash
ip -s link
```

Useful fields:

```text
RX packets
TX packets
RX errors
TX errors
RX dropped
TX dropped
RX bytes
TX bytes
```

## Continuously monitor interface statistics

```bash
watch -n 2 'ip -s link'
```

---

# 3. Routing Commands

## Show routing table

```bash
ip route
```

## Show default route

```bash
ip route | grep default
```

## Show route to a destination

```bash
ip route get 8.8.8.8
```

This helps determine which interface and route Linux would use.

---

# 4. Socket and Port Troubleshooting

## Show listening TCP/UDP ports

```bash
sudo ss -lntup
```

## Show all TCP connections

```bash
ss -ant
```

## Show listening TCP ports

```bash
sudo ss -lnt
```

## Show socket summary

```bash
ss -s
```

## Search for a specific port

```bash
sudo ss -lntp | grep ':8080'
```

Example:

```bash
sudo ss -lntp | grep ':22'
```

---

# 5. Connectivity Testing

## Ping a host

```bash
ping <host>
```

## Send a fixed number of packets

```bash
ping -c 4 <host>
```

Example:

```bash
ping -c 4 8.8.8.8
```

## Test packet loss

```bash
ping -c 20 <host>
```

Look for:

```text
packet loss
min/avg/max
```

---

# 6. Traceroute

## Trace network path

```bash
traceroute <host>
```

Example:

```bash
traceroute google.com
```

## Alternative

```bash
tracepath <host>
```

Traceroute/tracepath can help investigate:

* Routing
* Network path
* Latency
* Where traffic stops responding

---

# 7. DNS Troubleshooting

## Query DNS

```bash
dig example.com
```

## Get only IP address

```bash
dig +short example.com
```

## Check DNS query time

```bash
dig example.com | grep "Query time"
```

## Use a specific DNS server

```bash
dig @8.8.8.8 example.com
```

## Query another DNS server

```bash
dig @1.1.1.1 example.com
```

## Check resolver configuration

```bash
cat /etc/resolv.conf
```

On systems using systemd-resolved:

```bash
resolvectl status
```

---

# 8. TCP Port Testing

## Test TCP port

```bash
nc -vz <host> <port>
```

Example:

```bash
nc -vz example.com 443
```

Local service:

```bash
nc -vz 127.0.0.1 8080
```

Possible results:

```text
succeeded
connection refused
timed out
```

---

# 9. HTTP Troubleshooting

## Check HTTP headers

```bash
curl -I https://example.com
```

## Verbose HTTP request

```bash
curl -v https://example.com
```

## Follow redirects

```bash
curl -L https://example.com
```

## Show HTTP status code

```bash
curl -s -o /dev/null -w '%{http_code}\n' https://example.com
```

## Measure total response time

```bash
curl -o /dev/null -s -w \
'TIME=%{time_total}\n' \
https://example.com
```

## Detailed timing

```bash
curl -o /dev/null -s -w \
'DNS=%{time_namelookup} CONNECT=%{time_connect} TLS=%{time_appconnect} START=%{time_starttransfer} TOTAL=%{time_total}\n' \
https://example.com
```

---

# 10. HTTPS/TLS Troubleshooting

## Verbose HTTPS request

```bash
curl -v https://example.com
```

Look for:

```text
DNS resolution
TCP connection
TLS handshake
Certificate
HTTP response
```

## Check certificate using OpenSSL

```bash
openssl s_client -connect example.com:443 -servername example.com
```

This can help inspect the TLS handshake and certificate chain.

---

# 11. Packet Capture with tcpdump

## Capture packets

```bash
sudo tcpdump -i any
```

## Capture a specific interface

```bash
sudo tcpdump -i eth0
```

Replace `eth0` with your actual interface.

Find interfaces:

```bash
ip link
```

## Capture DNS

```bash
sudo tcpdump -i any port 53
```

## Capture HTTP

```bash
sudo tcpdump -i any port 80
```

## Capture HTTPS

```bash
sudo tcpdump -i any port 443
```

## Capture TCP traffic

```bash
sudo tcpdump -i any tcp
```

## Capture UDP traffic

```bash
sudo tcpdump -i any udp
```

---

# 12. Save Packet Capture

Capture a fixed number of packets:

```bash
sudo tcpdump -i any -c 100 -w capture.pcap
```

Read the capture:

```bash
sudo tcpdump -r capture.pcap
```

---

# 13. Filter tcpdump by Host

```bash
sudo tcpdump -i any host
```
