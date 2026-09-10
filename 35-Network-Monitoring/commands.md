# Chapter 35 — Network Monitoring — Commands

This file contains practical commands used by DevOps Engineers to monitor Linux systems, networks, applications, Docker, Kubernetes, and AWS environments.

---

# 1. Check Network Interfaces

## Show all interfaces

```bash
ip link
```

## Show IP addresses

```bash
ip addr
```

Short version:

```bash
ip a
```

## Show a specific interface

```bash
ip addr show eth0
```

## Check interface state

```bash
ip link show eth0
```

Possible states:

```text
UP
DOWN
```

---

# 2. Monitor Interface Statistics

Use:

```bash
ip -s link
```

Example:

```text
RX packets
RX errors
RX dropped
TX packets
TX errors
TX dropped
```

To monitor continuously:

```bash
watch -n 2 'ip -s link'
```

Press:

```text
Ctrl+C
```

to stop.

---

# 3. Check Routing

Show routing table:

```bash
ip route
```

Short version:

```bash
ip r
```

Show the route to a specific destination:

```bash
ip route get 8.8.8.8
```

Example:

```text
8.8.8.8 via 192.168.1.1 dev wlo1
```

This helps identify:

* Gateway
* Interface
* Source IP
* Route

---

# 4. Check Default Gateway

```bash
ip route | grep default
```

Example:

```text
default via 192.168.1.1 dev wlo1
```

Meaning:

```text
default
   ↓
Traffic for unknown networks

via 192.168.1.1
   ↓
Gateway

dev wlo1
   ↓
Network interface
```

---

# 5. Check Network Statistics

Show `/proc` network statistics:

```bash
cat /proc/net/dev
```

This displays interface traffic information.

For a continuously updating view:

```bash
watch -n 1 cat /proc/net/dev
```

---

# 6. Check Network Interfaces Through `/sys`

List interfaces:

```bash
ls /sys/class/net/
```

Check interface state:

```bash
cat /sys/class/net/eth0/operstate
```

Check MAC address:

```bash
cat /sys/class/net/eth0/address
```

---

# 7. Check Socket Statistics

Show socket summary:

```bash
ss -s
```

Show all TCP connections:

```bash
ss -ant
```

Show listening TCP ports:

```bash
ss -lnt
```

Show listening TCP ports with processes:

```bash
sudo ss -lntp
```

Show UDP sockets:

```bash
ss -anu
```

Show listening UDP ports:

```bash
ss -lnup
```

---

# 8. Filter `ss` Output

Find port 22:

```bash
ss -lntp | grep ':22'
```

Find port 80:

```bash
ss -lntp | grep ':80'
```

Find port 443:

```bash
ss -lntp | grep ':443'
```

Find established connections:

```bash
ss -ant state established
```

Count established TCP connections:

```bash
ss -ant state established | tail -n +2 | wc -l
```

---

# 9. Monitor Connections Continuously

```bash
watch -n 2 'ss -s'
```

Monitor listening ports:

```bash
watch -n 2 'ss -lntp'
```

---

# 10. Test Connectivity with `ping`

Basic:

```bash
ping google.com
```

Send four packets:

```bash
ping -c 4 google.com
```

Ping an IP:

```bash
ping -c 4 8.8.8.8
```

Set packet size:

```bash
ping -s 1000 -c 4 8.8.8.8
```

---

# 11. Interpret `ping`

Example:

```text
4 packets transmitted
4 packets received
0% packet loss
```

This indicates that all four ICMP echo requests received replies.

Example latency:

```text
time=25 ms
```

Lower latency generally means faster round-trip communication.

Important:

A failed ping does **not always** mean the destination service is down. ICMP may be blocked.

---

# 12. Test IPv4

```bash
ping -4 google.com
```

Test IPv6:

```bash
ping -6 google.com
```

---

# 13. Trace Network Path

Use:

```bash
traceroute google.com
```

If the command is unavailable, on Debian/Ubuntu you can install it with:

```bash
sudo apt update
sudo apt install traceroute
```

Alternative:

```bash
tracepath google.com
```

---

# 14. DNS Monitoring with `dig`

Basic DNS lookup:

```bash
dig example.com
```

Short answer:

```bash
dig +short example.com
```

Query an A record:

```bash
dig example.com A
```

Query an AAAA record:

```bash
dig example.com AAAA
```

Query MX:

```bash
dig example.com MX
```

Query NS:

```bash
dig example.com NS
```

---

# 15. Use a Specific DNS Server

Query Google's DNS resolver:

```bash
dig @8.8.8.8 example.com
```

Query Cloudflare DNS:

```bash
dig @1.1.1.1 example.com
```

This is useful for comparing DNS resolver behavior.

---

# 16. Check DNS Query Time

```bash
dig example.com | grep 'Query time'
```

Example:

```text
;; Query time: 25 msec
```

High DNS latency can affect application response time.

---

# 17. Reverse DNS Lookup

```bash
dig -x 8.8.8.8
```

---

# 18. Test TCP Ports with `nc`

Check whether TCP port 22 is reachable:

```bash
nc -vz example.com 22
```

Check HTTPS:

```bash
nc -vz example.com 443
```

Check HTTP:

```bash
nc -vz example.com 80
```

Example successful result:

```text
Connection to example.com 443 port [tcp/https] succeeded!
```

---

# 19. Use `curl` for HTTP Monitoring

Check HTTP headers:

```bash
curl -I https://example.com
```

Verbose request:

```bash
curl -v https://example.com
```

Follow redirects:

```bash
curl -IL https://example.com
```

Show only HTTP status code:

```bash
curl -s -o /dev/null -w '%{http_code}\n' https://example.com
```

---

# 20. Monitor HTTP Response Time

```bash
curl -o /dev/null -s -w 'HTTP=%{http_code} TIME=%{time_total}\n' https://example.com
```

Useful timing variables include:

```text
time_namelookup
time_connect
time_appconnect
time_starttransfer
time_total
```

Example:

```bash
curl -o /dev/null -s -w \
'DNS=%{time_namelookup} CONNECT=%{time_connect} TLS=%{time_appconnect} TOTAL=%{time_total}\n' \
https://example.com
```

---

# 21. HTTP Health Check

A simple health check:

```bash
curl -f https://example.com/health
```

If the endpoint returns a successful HTTP response, the command exits successfully.

For a script:

```bash
if curl -fsS https://example.com/health > /dev/null; then
    echo "Application is healthy"
else
    echo "Application is unhealthy"
fi
```

---

# 22. HTTPS/TLS Inspection

Use:

```bash
curl -v https://example.com
```

You can inspect:

* TLS connection
* Certificate information
* HTTP response
* Connection details

For certificate inspection:

```bash
openssl s_client -connect example.com:443 -servername example.com
```

Exit the interactive OpenSSL session with:

```text
Ctrl+C
```

---

# 23. Check Listening Ports

```bash
sudo ss -lntup
```

This can show:

* TCP listeners
* UDP listeners
* Port numbers
* Processes

Example:

```text
LISTEN 0 128 0.0.0.0:22
LISTEN 0 128 0.0.0.0:80
```

---

# 24. Find Unexpected Listening Ports

```bash
sudo ss -lntup
```

Then investigate each unfamiliar port.

For example:

```bash
sudo ss -lntp | grep ':8080'
```

Never expose a service simply because it is listening locally.

---

# 25. `tcpdump` Basics

Capture packets:

```bash
sudo tcpdump
```

Capture from all interfaces:

```bash
sudo tcpdump -i any
```

Capture from a specific interface:

```bash
sudo tcpdump -i eth0
```

---

# 26. Capture Specific Protocol

TCP:

```bash
sudo tcpdump -i any tcp
```

UDP:

```bash
sudo tcpdump -i any udp
```

ICMP:

```bash
sudo tcpdump -i any icmp
```

---

# 27. Capture Specific Port

HTTP:

```bash
sudo tcpdump -i any port 80
```

HTTPS:

```bash
sudo tcpdump -i any port 443
```

SSH:

```bash
sudo tcpdump -i any port 22
```

---

# 28. Capture Specific Host

```bash
sudo tcpdump -i any host 8.8.8.8
```

Source host:

```bash
sudo tcpdump -i any src host 8.8.8.8
```

Destination host:

```bash
sudo tcpdump -i any dst host 8.8.8.8
```

---

# 29. Save Packet Capture

```bash
sudo tcpdump -i any -w capture.pcap
```

Stop with:

```text
Ctrl+C
```

Check the file:

```bash
ls -lh capture.pcap
```

Read the capture:

```bash
sudo tcpdump -r capture.pcap
```

---

# 30. Capture a Limited Number of Packets

Capture 100 packets:

```bash
sudo tcpdump -i any -c 100
```

Save 100 packets:

```bash
sudo tcpdump -i any -c 100 -w capture.pcap
```

---

# 31. Useful `tcpdump` Examples

Capture HTTP traffic:

```bash
sudo tcpdump -i any tcp port 80
```

Capture HTTPS:

```bash
sudo tcpdump -i any tcp port 443
```

Capture DNS:

```bash
sudo tcpdump -i any port 53
```

Capture traffic between a host and a port:

```bash
sudo tcpdump -i any host 192.168.1.10 and port 443
```

---

# 32. Monitor Firewall with UFW

Check status:

```bash
sudo ufw status
```

Detailed status:

```bash
sudo ufw status verbose
```

Numbered rules:

```bash
sudo ufw status numbered
```

Important:

Only change firewall rules when you understand the impact, especially on remote servers.

---

# 33. Check Firewall Service

```bash
sudo systemctl status ufw
```

On systems using other firewall frameworks, inspect the applicable service/configuration instead of assuming UFW is in use.

---

# 34. Monitor System Services

Check a service:

```bash
systemctl status ssh
```

Check whether it is active:

```bash
systemctl is-active ssh
```

Check whether it starts automatically:

```bash
systemctl is-enabled ssh
```

---

# 35. Monitor Service Logs

View recent logs:

```bash
journalctl -u ssh
```

Follow logs:

```bash
journalctl -u ssh -f
```

Show logs from the current boot:

```bash
journalctl -u ssh -b
```

---

# 36. Check Network-Related Processes

Use:

```bash
ps aux
```

Search for a process:

```bash
ps aux | grep nginx
```

Better:

```bash
pgrep -a nginx
```

---

# 37. Monitor System Load

```bash
uptime
```

Interactive:

```bash
top
```

If installed:

```bash
htop
```

High system load can sometimes contribute to application/network symptoms.

---

# 38. Monitor CPU

```bash
top
```

For a quick view:

```bash
uptime
```

If `sysstat` is installed:

```bash
mpstat
```

---

# 39. Monitor Memory

```bash
free -h
```

Continuously:

```bash
watch -n 2 free -h
```

---

# 40. Monitor Disk

```bash
df -h
```

Check inode usage:

```bash
df -i
```

Disk saturation can indirectly cause application performance problems.

---

# 41. Monitor Network Traffic with `sar`

If `sysstat` is installed:

```bash
sar -n DEV
```

Real-time interval:

```bash
sar -n DEV 2 5
```

This collects network interface statistics.

---

# 42. Monitor TCP Statistics

```bash
sar -n TCP,ETCP 2 5
```

This can help investigate TCP activity and errors.

---

# 43. Prometheus — Check Target Health

Prometheus exposes target information through its HTTP API.

Example:

```bash
curl http://localhost:9090/api/v1/targets
```

If authentication or TLS is configured, use the appropriate endpoint and credentials.

---

# 44. Prometheus — Query a Metric

Example:

```bash
curl -G http://localhost:9090/api/v1/query \
  --data-urlencode 'query=up'
```

---

# 45. Prometheus — Check Server Health

```bash
curl http://localhost:9090/-/healthy
```

Readiness:

```bash
curl http://localhost:9090/-/ready
```

---

# 46. PromQL — Target Availability

```promql
up
```

Targets that are down:

```promql
up == 0
```

---

# 47. PromQL — Request Rate

Example:

```promql
rate(http_requests_total[5m])
```

This calculates the per-second average rate of increase over the previous five minutes.

---

# 48. PromQL — Counter Increase

```promql
increase(http_requests_total[1h])
```

This estimates how much the counter increased during the selected time range.

---

# 49. PromQL — Network Receive Bytes

If the relevant Node Exporter metric is available:

```promql
rate(node_network_receive_bytes_total[5m])
```

Transmit:

```promql
rate(node_network_transmit_bytes_total[5m])
```

The exact metric labels depend on the exporter and version.

---

# 50. PromQL — Network Errors

Receive errors:

```promql
rate(node_network_receive_errs_total[5m])
```

Transmit errors:

```promql
rate(node_network_transmit_errs_total[5m])
```

---

# 51. PromQL — Network Drops

Receive drops:

```promql
rate(node_network_receive_drop_total[5m])
```

Transmit drops:

```promql
rate(node_network_transmit_drop_total[5m])
```

Always verify the metric exists in your Prometheus installation before using it in production queries.

---

# 52. Check Exporter Endpoint

For Node Exporter:

```bash
curl http://localhost:9100/metrics
```

Search for network metrics:

```bash
curl -s http://localhost:9100/metrics | grep node_network
```

---

# 53. Grafana Health

If Grafana is running locally:

```bash
curl http://localhost:3000/api/health
```

Typical response indicates whether Grafana is healthy.

---

# 54. Docker Network Monitoring

List Docker networks:

```bash
docker network ls
```

Inspect a network:

```bash
docker network inspect bridge
```

Inspect a custom network:

```bash
docker network inspect <network-name>
```

---

# 55. Docker Container Monitoring

List running containers:

```bash
docker ps
```

List all containers:

```bash
docker ps -a
```

Container resource usage:

```bash
docker stats
```

One container:

```bash
docker stats <container-name>
```

---

# 56. Docker Port Monitoring

Show published ports:

```bash
docker ps --format 'table {{.Names}}\t{{.Ports}}'
```

Inspect a container:

```bash
docker inspect <container-name>
```

---

# 57. Docker Connectivity Test

Enter a running container:

```bash
docker exec -it <container-name> sh
```

Then test:

```bash
ping <destination>
```

or:

```bash
wget -qO- http://<service>:<port>
```

The exact tools available depend on the container image.

---

# 58. Kubernetes Cluster Monitoring

Check nodes:

```bash
kubectl get nodes
```

Detailed nodes:

```bash
kubectl get nodes -o wide
```

Check Pods:

```bash
kubectl get pods -A
```

Check Services:

```bash
kubectl get svc -A
```

Check Endpoints:

```bash
kubectl get endpoints -A
```

---

# 59. Kubernetes Pod Network Information

```bash
kubectl get pods -A -o wide
```

This displays Pod IP addresses and nodes.

---

# 60. Kubernetes DNS Test

Create a temporary debugging Pod:

```bash
kubectl run dns-test \
  --image=busybox:1.36 \
  --rm -it \
  --restart=Never \
  -- nslookup kubernetes.default
```

This tests Kubernetes DNS resolution.

---

# 61. Kubernetes Service Test

List services:

```bash
kubectl get svc -A
```

Inspect a Service:

```bash
kubectl describe svc <service-name> -n <namespace>
```

Check endpoints:

```bash
kubectl get endpoints <service-name> -n <namespace>
```

---

# 62. Kubernetes NetworkPolicy

List NetworkPolicies:

```bash
kubectl get networkpolicy -A
```

Inspect:

```bash
kubectl describe networkpolicy <policy-name> -n <namespace>
```

Important:

NetworkPolicy enforcement depends on the Kubernetes network plugin/CNI.

---

# 63. Kubernetes Pod Logs

```bash
kubectl logs <pod-name>
```

Follow logs:

```bash
kubectl logs -f <pod-name>
```

Previous container:

```bash
kubectl logs <pod-name> --previous
```

---

# 64. Kubernetes Events

```bash
kubectl get events -A
```

Recent events:

```bash
kubectl get events -A --sort-by=.lastTimestamp
```

Events can help identify:

* Pod failures
* Scheduling problems
* Network-related issues
* Configuration changes

---

# 65. Kubernetes Metrics

If Metrics Server is installed:

```bash
kubectl top nodes
```

Pods:

```bash
kubectl top pods -A
```

Remember:

`metrics-server` provides resource metrics for use cases such as HPA. It is not a complete network monitoring solution.

---

# 66. AWS CLI — Check Region

```bash
aws configure get region
```

Set a default region:

```bash
aws configure set region ap-south-1
```

---

# 67. AWS EC2 Network Interfaces

List network interfaces:

```bash
aws ec2 describe-network-interfaces
```

Useful fields can include:

* Interface ID
* Private IP
* Public IP association
* Subnet
* VPC
* Security Groups

---

# 68. AWS VPC Information

List VPCs:

```bash
aws ec2 describe-vpcs
```

List subnets:

```bash
aws ec2 describe-subnets
```

List route tables:

```bash
aws ec2 describe-route-tables
```

---

# 69. AWS Security Groups

List security groups:

```bash
aws ec2 describe-security-groups
```

This helps inspect allowed inbound and outbound traffic.

---

# 70. AWS Network ACLs

List Network ACLs:

```bash
aws ec2 describe-network-acls
```

Inspect:

* Inbound rules
* Outbound rules
* Subnet associations

---

# 71. AWS Load Balancers

List load balancers:

```bash
aws elbv2 describe-load-balancers
```

List target groups:

```bash
aws elbv2 describe-target-groups
```

Check target health:

```bash
aws elbv2 describe-target-health \
  --target-group-arn <target-group-arn>
```

---

# 72. AWS CloudWatch Metrics

List available metrics:

```bash
aws cloudwatch list-metrics
```

Get metric statistics:

```bash
aws cloudwatch get-metric-statistics
```

A real command requires the appropriate:

* Namespace
* Metric name
* Dimensions
* Time range
* Statistic
* Period

---

# 73. AWS VPC Flow Logs

List flow logs:

```bash
aws ec2 describe-flow-logs
```

This helps determine whether VPC Flow Logs are configured.

Remember:

```text
VPC Flow Logs
      ≠
Full packet capture
```

---

# 74. Monitor DNS Resolution Continuously

```bash
while true; do
    date
    dig +short example.com
    sleep 5
done
```

Stop:

```text
Ctrl+C
```

---

# 75. Monitor HTTP Health Continuously

```bash
while true; do
    date
    curl -o /dev/null -s -w 'HTTP=%{http_code} TIME=%{time_total}\n' https://example.com
    sleep 5
done
```

Stop:

```text
Ctrl+C
```

---

# 76. Monitor Ping Continuously

```bash
ping 8.8.8.8
```

Or a limited test:

```bash
while true; do
    ping -c 1 -W 2 8.8.8.8
    sleep 5
done
```

---

# 77. Simple Network Monitoring Script

Create:

```bash
nano network-monitor.sh
```

Add:

```bash
#!/bin/bash

echo "===== Network Monitoring ====="
echo

echo "Hostname:"
hostname

echo
echo "IP Addresses:"
ip -brief addr

echo
echo "Default Route:"
ip route | grep default

echo
echo "Listening Ports:"
ss -lnt

echo
echo "Connectivity:"
ping -c 2 8.8.8.8
```

Make executable:

```bash
chmod +x network-monitor.sh
```

Run:

```bash
./network-monitor.sh
```

---

# 78. HTTP Monitoring Script

Create:

```bash
nano http-check.sh
```

Add:

```bash
#!/bin/bash

URL="https://example.com"

STATUS=$(curl -o /dev/null -s -w "%{http_code}" "$URL")

if [ "$STATUS" = "200" ]; then
    echo "OK: $URL returned HTTP $STATUS"
else
    echo "WARNING: $URL returned HTTP $STATUS"
fi
```

Make executable:

```bash
chmod +x http-check.sh
```

Run:

```bash
./http-check.sh
```

---

# 79. DNS Monitoring Script

Create:

```bash
nano dns-check.sh
```

Add:

```bash
#!/bin/bash

DOMAIN="example.com"

if dig +short "$DOMAIN" | grep -q .; then
    echo "DNS OK: $DOMAIN"
else
    echo "DNS FAILED: $DOMAIN"
fi
```

Make executable:

```bash
chmod +x dns-check.sh
```

Run:

```bash
./dns-check.sh
```

---

# 80. Monitor Open Ports

```bash
sudo ss -lntup
```

Save output:

```bash
sudo ss -lntup > open-ports.txt
```

Compare later:

```bash
diff open-ports-old.txt open-ports.txt
```

This can help identify unexpected listening services.

---

# 81. Monitor Interface Errors

```bash
ip -s link
```

Focus on:

```text
RX errors
RX dropped
TX errors
TX dropped
```

Continuously:

```bash
watch -n 2 'ip -s link'
```

---

# 82. Troubleshooting: Connection Refused

Check:

```bash
ss -lntp
```

Then:

```bash
systemctl status <service>
```

Then:

```bash
journalctl -u <service>
```

Possible cause:

```text
Service is not listening
```

---

# 83. Troubleshooting: Connection Timeout

Check:

```bash
ip route
```

Then:

```bash
ping <destination>
```

Then:

```bash
nc -vz <destination> <port>
```

Then inspect:

* Firewall
* Security Group
* Network ACL
* Routing
* Service availability

---

# 84. Troubleshooting: DNS Failure

Run:

```bash
dig example.com
```

Try a known resolver:

```bash
dig @8.8.8.8 example.com
```

Compare results.

Check local resolver configuration:

```bash
resolvectl status
```

On systems using a different resolver stack, inspect the applicable configuration.

---

# 85. Troubleshooting: High Latency

Check:

```bash
ping -c 10 <destination>
```

Then:

```bash
traceroute <destination>
```

Then:

```bash
ip -s link
```

Then inspect:

* Network utilization
* Packet loss
* Interface errors
* Routing path
* Server load

---

# 86. Troubleshooting: Packet Loss

Start with:

```bash
ping -c 20 <destination>
```

Check interface statistics:

```bash
ip -s link
```

Capture traffic if needed:

```bash
sudo tcpdump -i any
```

Investigate:

* Interface errors
* Drops
* Congestion
* Routing
* Firewall behavior

---

# 87. Monitoring Golden Signals

For services, monitor:

```text
Latency
Traffic
Errors
Saturation
```

Useful commands/tools:

```bash
curl
ss
sar
Prometheus
Grafana
```

---

# 88. RED Monitoring

Monitor:

```text
Rate
Errors
Duration
```

PromQL example:

```promql
rate(http_requests_total[5m])
```

Error metrics depend on the application's metric names.

---

# 89. USE Monitoring

Monitor infrastructure:

```text
Utilization
Saturation
Errors
```

For network interfaces, useful Linux data includes:

```bash
ip -s link
```

and exporter metrics where available.

---

# 90. Important Command Cheat Sheet

| Requirement              | Command                            |
| ------------------------ | ---------------------------------- |
| IP addresses             | `ip addr`                          |
| Interfaces               | `ip link`                          |
| Routes                   | `ip route`                         |
| Interface statistics     | `ip -s link`                       |
| Network statistics       | `cat /proc/net/dev`                |
| Connections              | `ss -ant`                          |
| Listening ports          | `ss -lntp`                         |
| Socket summary           | `ss -s`                            |
| Connectivity             | `ping`                             |
| Network path             | `traceroute`                       |
| Alternative path tool    | `tracepath`                        |
| DNS                      | `dig`                              |
| TCP port test            | `nc -vz`                           |
| HTTP test                | `curl`                             |
| TLS inspection           | `openssl s_client`                 |
| Packet capture           | `tcpdump`                          |
| Firewall                 | `ufw`                              |
| Service status           | `systemctl`                        |
| Service logs             | `journalctl`                       |
| CPU/load                 | `top`, `uptime`                    |
| Memory                   | `free -h`                          |
| Disk                     | `df -h`                            |
| Interface monitoring     | `sar -n DEV`                       |
| Docker networks          | `docker network ls`                |
| Docker stats             | `docker stats`                     |
| Kubernetes nodes         | `kubectl get nodes`                |
| Kubernetes Pods          | `kubectl get pods -A`              |
| Kubernetes Services      | `kubectl get svc -A`               |
| Kubernetes NetworkPolicy | `kubectl get networkpolicy -A`     |
| Kubernetes events        | `kubectl get events -A`            |
| AWS VPCs                 | `aws ec2 describe-vpcs`            |
| AWS subnets              | `aws ec2 describe-subnets`         |
| AWS route tables         | `aws ec2 describe-route-tables`    |
| AWS SGs                  | `aws ec2 describe-security-groups` |
| AWS NACLs                | `aws ec2 describe-network-acls`    |
| AWS Flow Logs            | `aws ec2 describe-flow-logs`       |

---

# 🧠 Final Command Mental Model

When troubleshooting a network problem, remember:

```text
IP
 ↓
Route
 ↓
Ping
 ↓
DNS
 ↓
Port
 ↓
Service
 ↓
HTTP/HTTPS
 ↓
Firewall
 ↓
Packet Capture
 ↓
Metrics
 ↓
Logs
```

The goal is not to run every command.

The goal is to use the **smallest useful set of commands** to isolate the problem.

---

# 🚀 DevOps Monitoring Workflow

```text
1. Observe
      ↓
2. Measure
      ↓
3. Identify abnormal behavior
      ↓
4. Check network
      ↓
5. Check service
      ↓
6. Check application
      ↓
7. Check logs
      ↓
8. Check metrics
      ↓
9. Fix
      ↓
10. Verify
```

This workflow is one of the most important practical skills for a DevOps Engineer.
