# Chapter 37 — Real-World Case Studies — Commands

This file contains practical commands used while investigating real-world DevOps and networking incidents.

> **Golden Rule:** Run read-only diagnostic commands first. Make changes only after understanding the problem.

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

## Kernel

```bash
uname -a
```

## Current user

```bash
whoami
```

## Uptime

```bash
uptime
```

## System load

```bash
cat /proc/loadavg
```

---

# 2. Network Interface Investigation

## Show interfaces

```bash
ip addr
```

Short version:

```bash
ip a
```

## Show interface state

```bash
ip link
```

## Show interface statistics

```bash
ip -s link
```

Look for:

```text
RX packets
TX packets
errors
dropped
```

These can help identify interface-level problems.

---

# 3. Routing Investigation

## Show routing table

```bash
ip route
```

## Show default route

```bash
ip route | grep default
```

## Ask the kernel how it would route to a destination

```bash
ip route get 8.8.8.8
```

This is very useful for troubleshooting routing problems.

---

# 4. Check Listening Ports

## Show listening TCP ports

```bash
ss -lnt
```

## Show listening TCP/UDP ports

```bash
ss -lntup
```

Some systems may require:

```bash
sudo ss -lntup
```

## Show all TCP connections

```bash
ss -ant
```

## Show socket summary

```bash
ss -s
```

---

# 5. Find a Specific Port

Example: check port `8080`.

```bash
ss -lnt | grep :8080
```

Example: check SSH.

```bash
ss -lnt | grep :22
```

---

# 6. Test Basic Connectivity

## Ping an IP

```bash
ping -c 4 8.8.8.8
```

## Ping a domain

```bash
ping -c 4 example.com
```

Remember:

> Ping failure does not always mean the application is down.

ICMP may be blocked while TCP/HTTPS works normally.

---

# 7. Traceroute

```bash
traceroute example.com
```

If unavailable:

```bash
tracepath example.com
```

Traceroute helps investigate the path between source and destination.

A failed hop does not automatically mean that hop is broken because some routers intentionally do not respond to traceroute probes.

---

# 8. DNS Investigation

## Resolve a domain

```bash
dig example.com
```

## Short answer

```bash
dig +short example.com
```

## Query A record

```bash
dig example.com A
```

## Query AAAA record

```bash
dig example.com AAAA
```

## Query MX record

```bash
dig example.com MX
```

## Query NS record

```bash
dig example.com NS
```

---

# 9. Check DNS Resolver

```bash
cat /etc/resolv.conf
```

On systems using systemd-resolved:

```bash
resolvectl status
```

If supported, check DNS for a specific domain:

```bash
resolvectl query example.com
```

---

# 10. DNS Troubleshooting Flow

```text
Domain
  ↓
DNS Resolver
  ↓
DNS Server
  ↓
DNS Record
  ↓
Correct IP?
```

Commands:

```bash
dig example.com
```

```bash
dig +short example.com
```

```bash
cat /etc/resolv.conf
```

---

# 11. Test TCP Connectivity

Using `nc`:

```bash
nc -vz example.com 443
```

Check SSH:

```bash
nc -vz SERVER_IP 22
```

Check HTTP:

```bash
nc -vz SERVER_IP 80
```

Check HTTPS:

```bash
nc -vz SERVER_IP 443
```

A successful TCP connection does not prove that the application itself is healthy.

---

# 12. Test HTTP

## Basic request

```bash
curl http://example.com
```

## Show headers

```bash
curl -I http://example.com
```

## Verbose request

```bash
curl -v http://example.com
```

## Follow redirects

```bash
curl -L http://example.com
```

## Show HTTP status code

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://example.com
```

---

# 13. Measure HTTP Response Time

```bash
curl -s -o /dev/null \
-w "DNS: %{time_namelookup}\nConnect: %{time_connect}\nStart Transfer: %{time_starttransfer}\nTotal: %{time_total}\n" \
https://example.com
```

This can help separate:

```text
DNS delay
TCP connection delay
Server processing delay
Total request time
```

---

# 14. HTTPS Investigation

## Basic HTTPS request

```bash
curl -v https://example.com
```

## Check certificate and TLS handshake

```bash
openssl s_client -connect example.com:443 -servername example.com
```

Look for:

```text
Certificate
TLS version
Cipher
Verification
```

## Show certificate dates

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null | openssl x509 -noout -dates
```

---

# 15. TLS Troubleshooting Flow

```text
DNS
 ↓
TCP 443
 ↓
TLS Handshake
 ↓
Certificate
 ↓
Hostname
 ↓
HTTP
```

Useful commands:

```bash
dig +short example.com
```

```bash
nc -vz example.com 443
```

```bash
openssl s_client -connect example.com:443 -servername example.com
```

```bash
curl -v https://example.com
```

---

# 16. Check Running Processes

```bash
ps aux
```

## Search for a process

```bash
ps aux | grep nginx
```

Better:

```bash
pgrep -a nginx
```

## Interactive process view

```bash
top
```

If installed:

```bash
htop
```

---

# 17. CPU and Memory Investigation

## Memory

```bash
free -h
```

## CPU/load

```bash
uptime
```

```bash
top
```

## Disk

```bash
df -h
```

## Inode usage

```bash
df -i
```

A full disk can cause applications and services to fail.

---

# 18. Service Investigation

## Check service status

```bash
systemctl status nginx
```

Example:

```bash
systemctl status ssh
```

## Check whether service is enabled

```bash
systemctl is-enabled nginx
```

## Check whether service is active

```bash
systemctl is-active nginx
```

---

# 19. Service Logs

For systemd services:

```bash
journalctl -u nginx
```

Recent logs:

```bash
journalctl -u nginx -n 100
```

Follow logs:

```bash
journalctl -u nginx -f
```

SSH logs:

```bash
journalctl -u ssh
```

Some distributions may use a different service name such as `sshd`.

---

# 20. Application Log Investigation

Typical workflow:

```text
Application error
      ↓
Find timestamp
      ↓
Find matching log entry
      ↓
Identify error
      ↓
Correlate with metrics
      ↓
Investigate dependency
```

Useful commands:

```bash
grep -i "error" application.log
```

```bash
grep -i "timeout" application.log
```

```bash
tail -f application.log
```

---

# 21. TCP Packet Capture

Use `tcpdump` to inspect packets.

## List interfaces

```bash
sudo tcpdump -D
```

## Capture traffic on an interface

```bash
sudo tcpdump -i wlo1
```

Replace `wlo1` with your actual interface.

## Capture ICMP

```bash
sudo tcpdump -i wlo1 icmp
```

## Capture TCP port 80

```bash
sudo tcpdump -i wlo1 tcp port 80
```

## Capture TCP port 443

```bash
sudo tcpdump -i wlo1 tcp port 443
```

---

# 22. Save Packet Capture

```bash
sudo tcpdump -i wlo1 -w capture.pcap
```

Stop with:

```text
Ctrl+C
```

Read the capture:

```bash
tcpdump -r capture.pcap
```

Packet captures may contain sensitive information, so handle them carefully.

---

# 23. DNS Packet Capture

```bash
sudo tcpdump -i wlo1 port 53
```

This can help observe DNS traffic.

---

# 24. HTTP Packet Capture

For a local lab:

```bash
sudo tcpdump -i any tcp port 8080
```

This is useful when troubleshooting a local HTTP application.

---

# 25. Create a Simple Test HTTP Server

Create a temporary directory:

```bash
mkdir -p ~/network-test
cd ~/network-test
```

Create a file:

```bash
echo "Hello from troubleshooting lab" > index.html
```

Start server:

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

Test:

```bash
curl http://127.0.0.1:8080
```

---

# 26. Test Listening Address

Check:

```bash
ss -lnt | grep :8080
```

If the server listens on:

```text
127.0.0.1:8080
```

it is accessible through localhost but not generally through the host's other network interfaces.

This is a common real-world application connectivity issue.

---

# 27. Docker Troubleshooting

## List containers

```bash
docker ps
```

All containers:

```bash
docker ps -a
```

## Container logs

```bash
docker logs CONTAINER
```

Follow logs:

```bash
docker logs -f CONTAINER
```

## Inspect container

```bash
docker inspect CONTAINER
```

---

# 28. Docker Network Investigation

List networks:

```bash
docker network ls
```

Inspect network:

```bash
docker network inspect NETWORK
```

Check container network configuration:

```bash
docker inspect CONTAINER
```

---

# 29. Docker Port Mapping

Show published ports:

```bash
docker ps
```

Example:

```text
0.0.0.0:8080->80/tcp
```

Meaning:

```text
Host Port 8080
      ↓
Container Port 80
```

Test from host:

```bash
curl http://127.0.0.1:8080
```

---

# 30. Docker Container-to-Container Troubleshooting

Check networks:

```bash
docker network ls
```

Inspect:

```bash
docker network inspect NETWORK
```

Then test from a suitable container:

```bash
docker exec -it CONTAINER sh
```

Inside the container:

```bash
getent hosts OTHER_CONTAINER
```

If `curl` exists:

```bash
curl http://OTHER_CONTAINER:PORT
```

---

# 31. Kubernetes Basic Investigation

## Cluster information

```bash
kubectl cluster-info
```

## Nodes

```bash
kubectl get nodes
```

## Pods

```bash
kubectl get pods -A
```

## Services

```bash
kubectl get svc -A
```

---

# 32. Kubernetes Detailed Pod Information

```bash
kubectl describe pod POD_NAME -n NAMESPACE
```

This can reveal:

* Events
* Container state
* Image
* Probes
* Volumes
* Scheduling information

---

# 33. Kubernetes Logs

```bash
kubectl logs POD_NAME -n NAMESPACE
```

Follow:

```bash
kubectl logs -f POD_NAME -n NAMESPACE
```

Previous container:

```bash
kubectl logs POD_NAME -n NAMESPACE --previous
```

The `--previous` option is particularly useful for crash-looping containers.

---

# 34. Kubernetes Events

```bash
kubectl get events -A --sort-by=.lastTimestamp
```

Events can reveal:

* Scheduling failures
* Image pull failures
* Probe failures
* Mount failures
* Container restarts

---

# 35. Kubernetes Service Investigation

```bash
kubectl get svc -A
```

Detailed information:

```bash
kubectl describe svc SERVICE_NAME -n NAMESPACE
```

Check EndpointSlices:

```bash
kubectl get endpointslices -n NAMESPACE
```

Also useful:

```bash
kubectl get endpoints SERVICE_NAME -n NAMESPACE
```

---

# 36. Kubernetes Selector Troubleshooting

Check Service:

```bash
kubectl describe svc SERVICE_NAME -n NAMESPACE
```

Look for:

```text
Selector
```

Check Pod labels:

```bash
kubectl get pods -n NAMESPACE --show-labels
```

Then compare:

```text
Service selector
        ↓
Pod labels
```

They must match for Pods to be selected.

---

# 37. Kubernetes NetworkPolicy Investigation

List policies:

```bash
kubectl get networkpolicy -A
```

Detailed information:

```bash
kubectl describe networkpolicy POLICY_NAME -n NAMESPACE
```

Check:

```text
Pod selectors
Namespace selectors
Ingress rules
Egress rules
Ports
```

Remember:

> NetworkPolicy enforcement depends on the cluster's networking implementation/CNI.

---

# 38. Kubernetes DNS Testing

Run a temporary diagnostic Pod:

```bash
kubectl run dns-test \
  --image=busybox:1.36 \
  --restart=Never \
  --rm -it \
  -- nslookup kubernetes.default.svc
```

Check CoreDNS:

```bash
kubectl get pods -n kube-system
```

Look for CoreDNS Pods.

Logs:

```bash
kubectl logs -n kube-system -l k8s-app=kube-dns
```

The exact labels can vary by cluster configuration.

---

# 39. Kubernetes Applicati
