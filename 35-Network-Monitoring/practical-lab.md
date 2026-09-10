# Chapter 35 — Network Monitoring — Practical Lab

This practical lab provides hands-on exercises for learning network monitoring as a DevOps Engineer.

The labs progress from:

```text
Linux Networking
      ↓
Connectivity
      ↓
DNS
      ↓
Ports
      ↓
HTTP/HTTPS
      ↓
Packet Capture
      ↓
Service Monitoring
      ↓
Docker
      ↓
Kubernetes
      ↓
Prometheus
      ↓
Grafana
      ↓
AWS
      ↓
Troubleshooting
```

---

# 🧪 Lab 1 — Network Inventory

## Objective

Understand the current network configuration of your Linux machine.

### Step 1 — Check hostname

```bash
hostname
```

### Step 2 — Check IP addresses

```bash
ip addr
```

### Step 3 — Use the shorter output

```bash
ip -brief addr
```

### Step 4 — Check interfaces

```bash
ip link
```

### Step 5 — Check routing

```bash
ip route
```

### Step 6 — Check default gateway

```bash
ip route | grep default
```

### Step 7 — Check network statistics

```bash
ip -s link
```

### Task

Record:

* Hostname
* Active interface
* Private IP
* Default gateway
* Interface state
* RX packets
* TX packets
* RX errors
* TX errors
* RX drops
* TX drops

---

# 🧪 Lab 2 — Monitor Network Statistics

## Objective

Observe network statistics changing in real time.

Run:

```bash
watch -n 2 'ip -s link'
```

Generate some traffic in another terminal:

```bash
curl https://example.com
```

Then:

```bash
ping -c 5 8.8.8.8
```

Observe whether packet counters change.

Stop `watch` with:

```text
Ctrl+C
```

### Task

Answer:

1. Which interface transmitted packets?
2. Which interface received packets?
3. Did RX/TX counters increase?
4. Were there any errors?
5. Were there any dropped packets?

---

# 🧪 Lab 3 — Monitor `/proc/net/dev`

## Objective

Understand Linux network statistics through `/proc`.

Run:

```bash
cat /proc/net/dev
```

Then:

```bash
watch -n 1 cat /proc/net/dev
```

Generate traffic:

```bash
curl https://example.com
```

Observe the receive and transmit counters.

### Task

Identify:

```text
Interface
Receive bytes
Receive packets
Receive errors
Receive drops
Transmit bytes
Transmit packets
Transmit errors
Transmit drops
```

---

# 🧪 Lab 4 — Inspect `/sys/class/net`

## Objective

Understand network interface information exposed through `/sys`.

List interfaces:

```bash
ls /sys/class/net/
```

Check the state of your interface:

```bash
cat /sys/class/net/<interface>/operstate
```

Check MAC address:

```bash
cat /sys/class/net/<interface>/address
```

Replace:

```text
<interface>
```

with your actual interface, such as `wlo1` or `eth0`.

### Expected result

You may see:

```text
up
```

and a MAC address.

---

# 🧪 Lab 5 — Socket Monitoring

## Objective

Understand active connections and listening ports.

Run:

```bash
ss -s
```

Then:

```bash
ss -ant
```

Then:

```bash
sudo ss -lntp
```

### Task

Find:

* Number of TCP connections
* Listening ports
* Processes using listening ports
* Established connections

### Investigation

Pick one listening port and investigate its process.

Example:

```bash
sudo ss -lntp | grep ':22'
```

---

# 🧪 Lab 6 — Continuous Connection Monitoring

## Objective

Monitor socket activity continuously.

Run:

```bash
watch -n 2 'ss -s'
```

In another terminal, generate traffic:

```bash
curl https://example.com
```

Then:

```bash
ping -c 5 8.8.8.8
```

Observe the socket statistics.

Stop:

```text
Ctrl+C
```

---

# 🧪 Lab 7 — Connectivity Monitoring

## Objective

Test network reachability.

### Test your gateway

First identify it:

```bash
ip route | grep default
```

Then:

```bash
ping -c 4 <gateway-ip>
```

### Test an Internet IP

```bash
ping -c 4 8.8.8.8
```

### Test a domain

```bash
ping -c 4 google.com
```

### Compare

Record:

```text
Destination
Packet loss
Minimum latency
Average latency
Maximum latency
```

### Important

A failed ping does not necessarily mean that the application is unavailable. ICMP can be blocked.

---

# 🧪 Lab 8 — Network Path Monitoring

## Objective

Understand the path traffic takes to a destination.

Run:

```bash
traceroute google.com
```

If unavailable:

```bash
tracepath google.com
```

### Task

Observe:

* Number of hops
* Hop IP addresses
* Response times
* Any timeouts

### Questions

1. What is the first hop?
2. Is it your local gateway?
3. Which hop has the highest latency?
4. Are any hops not responding?

Remember that a non-responding hop does not automatically mean that the network is broken.

---

# 🧪 Lab 9 — DNS Monitoring

## Objective

Monitor DNS resolution.

Run:

```bash
dig example.com
```

Short output:

```bash
dig +short example.com
```

Check query time:

```bash
dig example.com | grep 'Query time'
```

Use another DNS resolver:

```bash
dig @8.8.8.8 example.com
```

Try:

```bash
dig @1.1.1.1 example.com
```

### Task

Compare:

```text
DNS server
Response
Query time
Returned IP
```

---

# 🧪 Lab 10 — DNS Failure Simulation

## Objective

Understand how DNS problems can affect applications.

Run:

```bash
dig example.com
```

Then:

```bash
dig @8.8.8.8 example.com
```

Compare the results.

### Questions

If the default resolver fails but a known public resolver responds:

* What component should you investigate?
* Is Internet connectivity necessarily broken?
* Could the local resolver configuration be the problem?

Check:

```bash
resolvectl status
```

---

# 🧪 Lab 11 — TCP Port Monitoring

## Objective

Check whether a TCP port is reachable.

Test HTTPS:

```bash
nc -vz example.com 443
```

Test HTTP:

```bash
nc -vz example.com 80
```

Test SSH:

```bash
nc -vz <server-ip> 22
```

### Understand the result

Possible outcomes:

```text
succeeded
```

or:

```text
connection refused
```

or:

```text
timed out
```

These outcomes suggest different troubleshooting paths.

---

# 🧪 Lab 12 — Local Listening Port Investigation

## Objective

Find services listening on your machine.

Run:

```bash
sudo ss -lntup
```

Create a table:

| Port | Protocol | Process | Expected? |
| ---- | -------- | ------- | --------- |
| 22   | TCP      | sshd    | Yes/No    |
| ...  | ...      | ...     | ...       |

Do not terminate services simply because you do not recognize them.

First identify what they are used for.

---

# 🧪 Lab 13 — HTTP Monitoring

## Objective

Monitor application-level availability.

Run:

```bash
curl -I https://example.com
```

Then:

```bash
curl -v https://example.com
```

Check the HTTP status:

```bash
curl -s -o /dev/null -w '%{http_code}\n' https://example.com
```

### Expected

A successful website commonly returns:

```text
200
```

But redirects such as `301` or `302` can also be valid depending on the endpoint.

---

# 🧪 Lab 14 — Measure HTTP Response Time

## Objective

Measure application response time.

Run:

```bash
curl -o /dev/null -s -w \
'HTTP=%{http_code} TOTAL=%{time_total}\n' \
https://example.com
```

More detailed:

```bash
curl -o /dev/null -s -w \
'DNS=%{time_namelookup} CONNECT=%{time_connect} TLS=%{time_appconnect} START=%{time_starttransfer} TOTAL=%{time_total}\n' \
https://example.com
```

### Understand

```text
DNS
 ↓
TCP connection
 ↓
TLS handshake
 ↓
Server processing
 ↓
Response
```

---

# 🧪 Lab 15 — Continuous HTTP Health Monitoring

## Objective

Create a simple synthetic monitoring check.

Run:

```bash
while true; do
    date
    curl -o /dev/null -s -w \
    'HTTP=%{http_code} TIME=%{time_total}\n' \
    https://example.com
    sleep 5
done
```

Stop:

```text
Ctrl+C
```

### Task

Observe:

* HTTP status
* Response time
* Changes over time

---

# 🧪 Lab 16 — Create an HTTP Health-Check Script

Create:

```bash
nano http-check.sh
```

Paste:

```bash
#!/bin/bash

URL="https://example.com"

STATUS=$(curl -o /dev/null -s -w "%{http_code}" "$URL")

if [ "$STATUS" = "200" ]; then
    echo "$(date): OK - HTTP $STATUS"
else
    echo "$(date): WARNING - HTTP $STATUS"
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

### Task

Modify the script to also display:

```text
Response time
```

---

# 🧪 Lab 17 — DNS Health-Check Script

Create:

```bash
nano dns-check.sh
```

Paste:

```bash
#!/bin/bash

DOMAIN="example.com"

IP=$(dig +short "$DOMAIN" | head -n 1)

if [ -n "$IP" ]; then
    echo "$(date): DNS OK - $DOMAIN -> $IP"
else
    echo "$(date): DNS FAILED - $DOMAIN"
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

# 🧪 Lab 18 — Packet Capture with tcpdump

## Objective

Observe actual network packets.

Start:

```bash
sudo tcpdump -i any
```

In another terminal:

```bash
ping -c 4 8.8.8.8
```

Return to tcpdump and press:

```text
Ctrl+C
```

You should see ICMP traffic.

---

# 🧪 Lab 19 — Capture DNS Traffic

Run:

```bash
sudo tcpdump -i any port 53
```

In another terminal:

```bash
dig example.com
```

Stop:

```text
Ctrl+C
```

### Task

Observe:

* Source IP
* Destination IP
* UDP/TCP
* Port 53

---

# 🧪 Lab 20 — Capture HTTPS Traffic

Run:

```bash
sudo tcpdump -i any port 443
```

In another terminal:

```bash
curl https://example.com
```

Stop capture:

```text
Ctrl+C
```

You can observe connection metadata, but HTTPS encrypts application payloads.

---

# 🧪 Lab 21 — Save a Packet Capture

Run:

```bash
sudo tcpdump -i any -c 100 -w network-monitoring.pcap
```

Generate some traffic while it runs:

```bash
curl https://example.com
```

After 100 packets, inspect the file:

```bash
ls -lh network-monitoring.pcap
```

Read it:

```bash
sudo tcpdump -r network-monitoring.pcap
```

---

# 🧪 Lab 22 — Capture Only HTTP

Run:

```bash
sudo tcpdump -i any tcp port 80
```

If your test website redirects to HTTPS, use a local HTTP server for a predictable test.

---

# 🧪 Lab 23 — Create a Local HTTP Service

## Objective

Create a controlled local service for monitoring.

Create a directory:

```bash
mkdir -p ~/network-monitoring-lab/web
cd ~/network-monitoring-lab/web
```

Create a page:

```bash
echo "Network Monitoring Lab" > index.html
```

Start Python HTTP server:

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

Keep this terminal running.

---

# 🧪 Lab 24 — Monitor the Local HTTP Service

Open another terminal.

Check the port:

```bash
ss -lntp | grep ':8080'
```

Test the service:

```bash
curl http://127.0.0.1:8080
```

Check headers:

```bash
curl -I http://127.0.0.1:8080
```

Check timing:

```bash
curl -o /dev/null -s -w \
'HTTP=%{http_code} TIME=%{time_total}\n' \
http://127.0.0.1:8080
```

Stop the Python server with:

```text
Ctrl+C
```

---

# 🧪 Lab 25 — Observe Service Failure

Start the service:

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

In another terminal:

```bash
curl http://127.0.0.1:8080
```

Stop the server:

```text
Ctrl+C
```

Try again:

```bash
curl http://127.0.0.1:8080
```

You should now observe a connection failure.

### Lesson

Monitoring detects the symptom.

Troubleshooting determines the cause.

---

# 🧪 Lab 26 — Monitor the Local Service with `watch`

Start the server again:

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

In another terminal:

```bash
watch -n 2 'curl -s -o /dev/null -w "HTTP=%{http_code} TIME=%{time_total}\n" http://127.0.0.1:8080'
```

Stop with:

```text
Ctrl+C
```

---

# 🧪 Lab 27 — Monitor Service Logs

If you are running a systemd service, inspect its status:

```bash
systemctl status <service>
```

View logs:

```bash
journalctl -u <service>
```

Follow logs:

```bash
journalctl -u <service> -f
```

### Task

Identify:

* Service state
* Recent events
* Errors
* Restart information

---

# 🧪 Lab 28 — Monitor System Load

Run:

```bash
uptime
```

Then:

```bash
top
```

If available:

```bash
htop
```

Check memory:

```bash
free -h
```

Check disk:

```bash
df -h
```

### Why?

Network problems can sometimes be symptoms of overloaded systems.

---

# 🧪 Lab 29 — Monitor Network Traffic with `sar`

Check whether `sar` is available:

```bash
sar -n DEV
```

If it is not installed on Ubuntu:

```bash
sudo apt update
sudo apt install sysstat
```

Then:

```bash
sar -n DEV 2 5
```

This collects network device statistics every two seconds for five reports.

---

# 🧪 Lab 30 — Monitor TCP Statistics

Run:

```bash
sar -n TCP,ETCP 2 5
```

Observe TCP-related statistics.

### Task

Record any counters related to:

* TCP connections
* Retransmissions
* Errors

---

# 🧪 Lab 31 — Docker Network Inventory

## Objective

Monitor Docker networking.

Check Docker:

```bash
docker version
```

List networks:

```bash
docker network ls
```

Inspect the default bridge:

```bash
docker network inspect bridge
```

### Task

Record:

* Network name
* Driver
* Subnet
* Gateway
* Connected containers

---

# 🧪 Lab 32 — Docker Container Monitoring

List containers:

```bash
docker ps
```

List all containers:

```bash
docker ps -a
```

Monitor resource usage:

```bash
docker stats
```

Stop with:

```text
Ctrl+C
```

---

# 🧪 Lab 33 — Docker Port Monitoring

Run:

```bash
docker ps --format 'table {{.Names}}\t{{.Ports}}'
```

Inspect a container:

```bash
docker inspect <container-name>
```

### Task

Identify:

* Published ports
* Container ports
* IP address
* Network name

---

# 🧪 Lab 34 — Docker Connectivity Test

If you have two containers on the same user-defined network, test connectivity between them.

List networks:

```bash
docker network ls
```

Inspect:

```bash
docker network inspect <network-name>
```

Enter a container:

```bash
docker exec -it <container-name> sh
```

From inside the container, test the destination using whatever networking tools the image provides.

Remember that minimal images may not contain `ping`, `curl`, or `wget`.

---

# 🧪 Lab 35 — Kubernetes Network Monitoring

## Objective

Monitor Kubernetes network objects.

Check cluster:

```bash
kubectl cluster-info
```

Check nodes:

```bash
kubectl get nodes -o wide
```

Check Pods:

```bash
kubectl get pods -A -o wide
```

Check Services:

```bash
kubectl get svc -A
```

Check endpoints:

```bash
kubectl get endpoints -A
```

---

# 🧪 Lab 36 — Kubernetes DNS Monitoring

Run a temporary DNS test Pod:

```bash
kubectl run dns-test \
  --image=busybox:1.36 \
  --rm -it \
  --restart=Never \
  -- nslookup kubernetes.default
```

### Expected

You should receive an address for the Kubernetes DNS service.

### Task

If DNS fails, investigate:

```bash
kubectl get pods -n kube-system
```

Look for CoreDNS Pods.

---

# 🧪 Lab 37 — Kubernetes Service Monitoring

List Services:

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

### Important

A Service without healthy endpoints may not be able to send traffic to the intended application.

---

# 🧪 Lab 38 — Kubernetes Pod Network Information

Run:

```bash
kubectl get pods -A -o wide
```

Record:

```text
Pod
Pod IP
Node
Status
```

### Task

Pick two Pods and determine:

1. Are they on the same node?
2. What are their IP addresses?
3. Which Service selects them, if applicable?

---

# 🧪 Lab 39 — Kubernetes NetworkPolicy Monitoring

List policies:

```bash
kubectl get networkpolicy -A
```

Inspect:

```bash
kubectl describe networkpolicy <policy-name> -n <namespace>
```

### Important

NetworkPolicy enforcement depends on the CNI/network plugin.

Creating a NetworkPolicy object does not guarantee enforcement if the installed networking implementation does not support it.

---

# 🧪 Lab 40 — Kubernetes Resource Monitoring

If Metrics Server is installed:

```bash
kubectl top nodes
```

Pods:

```bash
kubectl top pods -A
```

### Understand

Metrics Server is useful for resource metrics and autoscaling-related use cases.

It is not a complete network observability platform.

---

# 🧪 Lab 41 — Prometheus Health Check

If Prometheus is running locally:

```bash
curl http://localhost:9090/-/healthy
```

Check readiness:

```bash
curl http://localhost:9090/-/ready
```

### Expected

A healthy Prometheus instance should respond successfully.

---

# 🧪 Lab 42 — Prometheus Target Monitoring

Open:

```text
http://localhost:9090/targets
```

Or use:

```bash
curl http://localhost:9090/api/v1/targets
```

### Task

Record:

* Target
* Job
* Health
* Last scrape
* Error, if any

---

# 🧪 Lab 43 — Prometheus `up` Metric

Query:

```bash
curl -G http://localhost:9090/api/v1/query \
  --data-urlencode 'query=up'
```

Or use the Prometheus UI and query:

```promql
up
```

Then:

```promql
up == 0
```

### Understand

`up` is commonly:

```text
1 → target is reachable
0 → scrape failed
```

---

# 🧪 Lab 44 — Node Exporter

If Node Exporter is running:

```bash
curl http://localhost:9100/metrics
```

Search network metrics:

```bash
curl -s http://localhost:9100/metrics | grep node_network
```

### Task

Find metrics related to:

* Receive bytes
* Transmit bytes
* Receive errors
* Transmit errors
* Receive drops
* Transmit drops

Metric availability depends on the exporter version and configuration.

---

# 🧪 Lab 45 — PromQL Network Monitoring

If Node Exporter exposes the relevant metrics, try:

```promql
rate(node_network_receive_bytes_total[5m])
```

Transmit:

```promql
rate(node_network_transmit_bytes_total[5m])
```

Receive errors:

```promql
rate(node_network_receive_errs_total[5m])
```

Transmit errors:

```promql
rate(node_network_transmit_errs_total[5m])
```

### Task

Create a Grafana panel for network traffic.

---

# 🧪 Lab 46 — Grafana Monitoring Dashboard

If Grafana is installed:

```bash
curl http://localhost:3000/api/health
```

Open Grafana in your browser.

Create a dashboard containing:

```text
Network Traffic
Network Errors
Network Drops
CPU
Memory
Disk
Target Availability
```

### Suggested dashboard structure

```text
+----------------------------------+
| Target Availability              |
+----------------------------------+
| Network Receive | Network TX    |
+----------------------------------+
| Network Errors  | Network Drops |
+----------------------------------+
| CPU             | Memory        |
+----------------------------------+
```

---

# 🧪 Lab 47 — Create a Monitoring Baseline

For your Linux machine, record:

```text
Hostname:
Interface:
IP:
Gateway:

Average ping:
Packet loss:

DNS query time:

HTTP response time:

Listening ports:

RX errors:
TX errors:

RX drops:
TX drops:
```

Run these commands:

```bash
hostname
ip -brief addr
ip route
ping -c 10 8.8.8.8
dig example.com | grep 'Query time'
curl -o /dev/null -s -w 'HTTP=%{http_code} TIME=%{time_total}\n' https://example.com
sudo ss -lntup
ip -s link
```

Save the results as your initial baseline.

---

# 🧪 Lab 48 — Monitor for Changes

After some normal system activity, run the same commands again.

Compare:

```text
Baseline
   vs
Current
```

Look for:

* New ports
* Increased errors
* Increased drops
* Higher latency
* DNS changes
* Higher traffic

---

# 🧪 Lab 49 — Network Troubleshooting Scenario

## Scenario

Users report:

> "The application is slow."

Do not immediately restart anything.

Follow:

```text
User complaint
      ↓
Availability
      ↓
Latency
      ↓
Packet loss
      ↓
DNS
      ↓
Ports
      ↓
Service
      ↓
Network
      ↓
Application
      ↓
Logs
      ↓
Metrics
```

Commands:

```bash
ping -c 10 <destination>
```

```bash
dig <domain>
```

```bash
nc -vz <host> <port>
```

```bash
curl -v <url>
```

```bash
ss -s
```

```bash
ip -s link
```

---

# 🧪 Lab 50 — Troubleshooting Scenario: Connection Refused

## Scenario

You run:

```bash
curl http://127.0.0.1:8080
```

and receive:

```text
Connection refused
```

Investigate:

### Step 1

```bash
ss -lntp | grep ':8080'
```

### Step 2

If nothing is listening, check the service.

### Step 3

If it is a systemd service:

```bash
systemctl status <service>
```

### Step 4

Check logs:

```bash
journalctl -u <service>
```

### Lesson

Connection refused commonly means the destination was reachable but no process was accepting the connection on that port, or an active reject occurred.

---

# 🧪 Lab 51 — Troubleshooting Scenario: Timeout

## Scenario

A remote service does not respond.

Test:

```bash
ping -c 4 <server-ip>
```

Then:

```bash
nc -vz <server-ip> <port>
```

Then:

```bash
ip route
```

Investigate:

* Routing
* Firewall
* Security Group
* Network ACL
* Service
* Network path

### Lesson

A timeout often suggests traffic is being dropped or the destination is unreachable, but the exact cause requires investigation.

---

# 🧪 Lab 52 — Troubleshooting Scenario: DNS

## Scenario

The application cannot resolve a hostname.

Run:

```bash
dig example.com
```

Then:

```bash
dig @8.8.8.8 example.com
```

Then:

```bash
resolvectl status
```

Compare the results.

### Investigation

Check:

```text
Resolver
DNS server
Network connectivity
DNS response
Application configuration
```

---

# 🧪 Lab 53 — Troubleshooting Scenario: HTTPS

## Scenario

HTTPS is failing.

Run:

```bash
curl -v https://example.com
```

Then:

```bash
openssl s_client -connect example.com:443 -servername example.com
```

Investigate:

* DNS
* TCP 443
* TLS handshake
* Certificate
* HTTP response

---

# 🧪 Lab 54 — Troubleshooting Scenario: High Packet Loss

Run:

```bash
ping -c 50 <destination>
```

Then:

```bash
ip -s link
```

Then:

```bash
traceroute <destination>
```

Investigate:

```text
Packet loss
Interface errors
Interface drops
Network path
Congestion
Firewall behavior
```

---

# 🧪 Lab 55 — Troubleshooting Scenario: High Network Traffic

Check:

```bash
ip -s link
```

Then:

```bash
sar -n DEV 2 5
```

Check active connections:

```bash
ss -s
```

Capture traffic if necessary:

```bash
sudo tcpdump -i any
```

Investigate:

* Which interface is busy?
* Is traffic inbound or outbound?
* Which hosts are communicating?
* Is the traffic expected?
* Is there a recent deployment or backup?

---

# 🧪 Lab 56 — Build a Simple Monitoring Dashboard

Create a monitoring checklist:

```text
+----------------------------------+
| Network Monitoring Dashboard     |
+----------------------------------+
| Availability                     |
| Latency                          |
| Packet Loss                      |
| Throughput                       |
| Errors                           |
| Drops                            |
| Connections                      |
| DNS                              |
| HTTP Status                      |
| HTTP Response Time               |
+----------------------------------+
```

For each item, define:

```text
Metric
Normal value
Warning threshold
Critical threshold
Action
```

Example:

| Metric       | Normal | Warning | Critical |
| ------------ | -----: | ------: | -------: |
| Packet Loss  |    <1% |     >2% |      >5% |
| Latency      | <50 ms | >100 ms |  >500 ms |
| Availability | >99.9% |  <99.9% |     <99% |

These are **example thresholds for practice**, not universal production thresholds.

---

# 🧪 Lab 57 — Alert Design Exercise

For each metric, create an alert idea.

Example:

```text
Metric:
HTTP availability

Condition:
Health check fails repeatedly

Action:
Notify DevOps Engineer
```

Create alerts for:

* High latency
* Packet loss
* Service down
* DNS failure
* High network utilization
* Interface errors
* Unexpected traffic

---

# 🧪 Lab 58 — Monitoring Security

Review what is exposed on your machine.

Run:

```bash
sudo ss -lntup
```

Identify:

```text
Expected ports
Unexpected ports
```

Check firewall:

```bash
sudo ufw status verbose
```

If using another firewall framework, inspect that configuration instead.

### Goal

Reduce unnecessary exposure.

Golden rule:

> **Do not expose what you do not need.**

---

# 🧪 Lab 59 — Final Network Monitoring Audit

Perform a complete audit.

## Network

```bash
ip addr
ip route
ip -s link
```

## Connections

```bash
ss -s
ss -lntup
```

## DNS

```bash
dig example.com
```

## Connectivity

```bash
ping -c 10 8.8.8.8
```

## Path

```bash
tracepath 8.8.8.8
```

## HTTP

```bash
curl -I https://example.com
```

## Packet Capture

```bash
sudo tcpdump -i any -c 20
```

## Services

```bash
systemctl --type=service --state=running
```

---

# 🏆 Final Challenge

Complete the following without looking at previous commands.

## Challenge 1

Find your:

```text
IP
Interface
Gateway
```

## Challenge 2

Find all listening ports.

## Challenge 3

Identify which process owns port 22 if SSH is running.

## Challenge 4

Measure packet loss to:

```text
8.8.8.8
```

## Challenge 5

Measure DNS query time.

## Challenge 6

Measure HTTPS response time.

## Challenge 7

Capture 50 packets.

## Challenge 8

Identify network interface errors and drops.

## Challenge 9

Check Docker networks.

## Challenge 10

Check Kubernetes Services and endpoints.

## Challenge 11

Check Prometheus target health if Prometheus is available.

## Challenge 12

Explain how you would investigate:

```text
High latency
Packet loss
Connection refused
Connection timeout
DNS failure
HTTP 500
```

---

# 🧠 Final Troubleshooting Framework

Remember:

```text
1. What is failing?
        ↓
2. Is it reachable?
        ↓
3. Is DNS working?
        ↓
4. Is routing correct?
        ↓
5. Is the port reachable?
        ↓
6. Is the service listening?
        ↓
7. Is the firewall allowing traffic?
        ↓
8. Is the network healthy?
        ↓
9. Is the application healthy?
        ↓
10. What do metrics and logs show?
        ↓
11. Fix
        ↓
12. Verify
```

---

# 📋 Lab Completion Checklist

* [ ] Network inventory
* [ ] Interface monitoring
* [ ] `/proc/net/dev`
* [ ] `/sys/class/net`
* [ ] Socket monitoring
* [ ] Connectivity testing
* [ ] Network path analysis
* [ ] DNS monitoring
* [ ] TCP port monitoring
* [ ] HTTP monitoring
* [ ] Response-time monitoring
* [ ] Health-check scripts
* [ ] tcpdump
* [ ] Packet capture
* [ ] Local HTTP service
* [ ] Service monitoring
* [ ] Linux resource monitoring
* [ ] `sar`
* [ ] Docker networking
* [ ] Docker monitoring
* [ ] Kubernetes networking
* [ ] Kubernetes DNS
* [ ] Kubernetes Services
* [ ] Kubernetes NetworkPolicy
* [ ] Prometheus
* [ ] PromQL
* [ ] Node Exporter
* [ ] Grafana
* [ ] Baseline creation
* [ ] Alert design
* [ ] Security audit
* [ ] Troubleshooting scenarios
* [ ] Final challenge

---

# 🎯 What You Should Be Able to Do After This Lab

After completing this practical lab, you should be able to:

1. Inspect Linux network configuration.
2. Monitor interfaces and socket connections.
3. Test connectivity.
4. Troubleshoot DNS.
5. Test TCP ports.
6. Monitor HTTP/HTTPS.
7. Measure network and application latency.
8. Capture packets with tcpdump.
9. Monitor Linux services.
10. Monitor Docker networking.
11. Inspect Kubernetes networking.
12. Understand Prometheus monitoring.
13. Query metrics with PromQL.
14. Build basic Grafana dashboards.
15. Understand AWS network monitoring concepts.
16. Establish a network baseline.
17. Design useful alerts.
18. Troubleshoot common network failures.

---

# 🏁 Final Mental Model

```text
                 NETWORK MONITORING
                         |
        +----------------+----------------+
        |                |                |
     Network          Services        Application
        |                |                |
     Metrics           Health           Metrics
        |                |                |
        +----------------+----------------+
                         |
                    Prometheus
                         |
                      PromQL
                         |
                      Grafana
                         |
                      Alerts
                         |
                  DevOps / SRE
                         |
                  Troubleshooting
                         |
                       Fix
                         |
                      Verify
```

**Monitor → Detect → Investigate → Fix → Verify → Improve**
