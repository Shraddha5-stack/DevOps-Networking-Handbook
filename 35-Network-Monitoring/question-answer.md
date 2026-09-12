# Chapter 35 — Network Monitoring Interview Questions

This document contains beginner-to-advanced and scenario-based interview questions for **Network Monitoring** from a DevOps Engineer perspective.

---

# 🟢 Beginner Level

## 1. What is network monitoring?

Network monitoring is the continuous observation of network infrastructure, traffic, devices, services, and performance to detect failures, degradation, security issues, and abnormal behavior.

---

## 2. Why is network monitoring important?

Network monitoring helps us:

* Detect outages
* Identify high latency
* Detect packet loss
* Monitor bandwidth
* Monitor network errors
* Detect unavailable services
* Troubleshoot connectivity problems
* Identify abnormal traffic
* Maintain application availability

---

## 3. What are the main things you monitor in a network?

Common network monitoring metrics include:

* Availability
* Latency
* Packet loss
* Bandwidth
* Throughput
* Jitter
* Network errors
* Network drops
* Connections
* DNS response time
* HTTP response time
* Interface utilization
* Service health

---

## 4. What is network availability?

Network availability measures whether a network, service, or endpoint is reachable and operational.

Example:

```text
100% availability
→ Service was available during the monitoring period
```

---

## 5. What is latency?

Latency is the time required for data to travel between two points.

Example:

```text
Client → Server
       20 ms
```

Lower latency generally means faster communication.

---

## 6. What is packet loss?

Packet loss occurs when packets sent across a network do not reach their destination.

Example:

```text
100 packets sent
95 received

Packet loss = 5%
```

Packet loss can cause:

* Slow applications
* Retransmissions
* Connection problems
* Poor VoIP/video quality

---

## 7. What is bandwidth?

Bandwidth is the maximum amount of data that a network connection can theoretically transfer over a period of time.

Example:

```text
Network link = 1 Gbps
```

---

## 8. What is throughput?

Throughput is the actual amount of data successfully transferred over a network during a given period.

Bandwidth is capacity.

Throughput is actual achieved transfer.

---

## 9. What is jitter?

Jitter is the variation in packet arrival time.

It is particularly important for:

* VoIP
* Video conferencing
* Real-time applications

---

# 🟢 Linux Network Monitoring

## 10. How do you check IP addresses in Linux?

```bash
ip addr
```

or:

```bash
ip -brief addr
```

---

## 11. How do you check network interfaces?

```bash
ip link
```

---

## 12. How do you check routing information?

```bash
ip route
```

---

## 13. How do you find the default gateway?

```bash
ip route | grep default
```

---

## 14. How do you monitor interface statistics?

```bash
ip -s link
```

This can show:

* RX packets
* TX packets
* RX errors
* TX errors
* RX drops
* TX drops
* Bytes

---

## 15. How do you monitor listening ports?

```bash
sudo ss -lntup
```

---

## 16. How do you see TCP connections?

```bash
ss -ant
```

---

## 17. What does `ss -s` show?

```bash
ss -s
```

provides a summary of socket statistics, including TCP and other socket states.

---

## 18. How do you monitor network traffic continuously?

One simple approach is:

```bash
watch -n 2 'ip -s link'
```

---

## 19. What is `/proc/net/dev`?

`/proc/net/dev` provides Linux network interface statistics.

Example:

```bash
cat /proc/net/dev
```

It can provide information about received and transmitted traffic, errors, and drops.

---

## 20. What is `/sys/class/net`?

`/sys/class/net` exposes information about network interfaces through the Linux sysfs filesystem.

Example:

```bash
ls /sys/class/net/
```

---

# 🟢 Connectivity Monitoring

## 21. How do you test basic connectivity?

Use:

```bash
ping <destination>
```

Example:

```bash
ping -c 4 8.8.8.8
```

---

## 22. What does ping tell you?

Ping can help determine:

* Reachability
* Approximate round-trip latency
* Packet loss

However, a failed ping does not always mean the application is unavailable because ICMP may be blocked.

---

## 23. How do you trace the network path?

Use:

```bash
traceroute <destination>
```

or:

```bash
tracepath <destination>
```

---

## 24. What is traceroute useful for?

Traceroute helps identify the network hops between a source and destination.

It can help investigate:

* Routing problems
* High latency
* Unexpected network paths
* Where traffic stops responding

---

# 🟢 DNS Monitoring

## 25. How do you test DNS resolution?

```bash
dig example.com
```

---

## 26. How do you get only the resolved IP?

```bash
dig +short example.com
```

---

## 27. How do you check DNS query time?

```bash
dig example.com | grep "Query time"
```

---

## 28. How can you test a specific DNS server?

```bash
dig @8.8.8.8 example.com
```

Another example:

```bash
dig @1.1.1.1 example.com
```

---

## 29. How would you troubleshoot a DNS failure?

I would check:

```text
1. Is network connectivity working?
2. Can I reach the DNS server?
3. What resolver is configured?
4. Does dig return a response?
5. Does another DNS server work?
6. Is the domain correctly configured?
7. Is the application using the expected resolver?
```

---

# 🟢 Port and Service Monitoring

## 30. How do you test whether a TCP port is reachable?

```bash
nc -vz <host> <port>
```

Example:

```bash
nc -vz example.com 443
```

---

## 31. What is the difference between connection refused and timeout?

### Connection refused

The destination was reachable, but the connection was actively rejected.

A common reason is that no process is listening on that port.

### Timeout

No response was received within the expected time.

Possible causes include:

* Firewall
* Security Group
* Network ACL
* Routing problem
* Service unavailable
* Packet filtering

---

## 32. How do you check whether a service is listening on a port?

```bash
sudo ss -lntp
```

Example:

```bash
sudo ss -lntp | grep ':8080'
```

---

# 🟢 HTTP/HTTPS Monitoring

## 33. How do you check HTTP headers?

```bash
curl -I https://example.com
```

---

## 34. How do you test HTTP connectivity in detail?

```bash
curl -v https://example.com
```

---

## 35. How do you check HTTP status code?

```bash
curl -s -o /dev/null -w '%{http_code}\n' https://example.com
```

---

## 36. How do you measure HTTP response time?

```bash
curl -o /dev/null -s -w \
'HTTP=%{http_code} TIME=%{time_total}\n' \
https://example.com
```

---

## 37. How do you break down HTTP request timing?

```bash
curl -o /dev/null -s -w \
'DNS=%{time_namelookup} CONNECT=%{time_connect} TLS=%{time_appconnect} START=%{time_starttransfer} TOTAL=%{time_total}\n' \
https://example.com
```

This helps separate:

```text
DNS
 ↓
TCP connection
 ↓
TLS
 ↓
Server response
```

---

# 🟡 Packet Monitoring

## 38. What is tcpdump?

`tcpdump` is a command-line packet capture and analysis tool.

Example:

```bash
sudo tcpdump -i any
```

---

## 39. How do you capture DNS traffic?

```bash
sudo tcpdump -i any port 53
```

---

## 40. How do you capture HTTPS traffic?

```bash
sudo tcpdump -i any port 443
```

---

## 41. How do you save packets to a file?

```bash
sudo tcpdump -i any -c 100 -w capture.pcap
```

---

## 42. How do you read a packet capture?

```bash
sudo tcpdump -r capture.pcap
```

---

## 43. Can tcpdump decrypt HTTPS traffic?

Normally, no.

You can observe network metadata such as:

* Source/destination
* Ports
* Packet timing
* TCP behavior

But HTTPS application data is encrypted.

---

# 🟡 Monitoring Concepts

## 44. What is active monitoring?

Active monitoring generates traffic to test availability or performance.

Examples:

```text
ping
HTTP health check
TCP connection check
DNS query
```

---

## 45. What is passive monitoring?

Passive monitoring observes existing traffic or system activity without generating synthetic test traffic.

Examples:

```text
tcpdump
VPC Flow Logs
Interface counters
Network telemetry
```

---

## 46. What is the difference between monitoring and observability?

Monitoring tells us:

> "Something is wrong."

Observability helps us understand:

> "Why is it wrong?"

Monitoring commonly focuses on known metrics and conditions.

Observability combines signals such as:

* Metrics
* Logs
* Traces
* Events

to understand system behavior.

---

## 47. What are metrics, logs, and events?

### Metrics

Numerical measurements over time.

Example:

```text
CPU = 75%
Latency = 100 ms
```

### Logs

Detailed records of system or application events.

### Events

Discrete occurrences such as:

```text
Pod restarted
Instance terminated
Deployment created
```

---

# 🟡 Prometheus

## 48. What is Prometheus?

Prometheus is an open-source monitoring and time-series database system commonly used for infrastructure and application monitoring.

---

## 49. How does Prometheus collect metrics?

Prometheus normally uses a **pull/scrape model**.

Conceptually:

```text
Prometheus
     |
     | scrape
     ↓
Target
     |
     ↓
Metrics
```

---

## 50. What is an exporter?

An exporter exposes metrics in a format that Prometheus can scrape.

Examples:

```text
Node Exporter
Blackbox Exporter
Application exporters
```

---

## 51. What is Node Exporter?

Node Exporter exposes Linux host metrics for Prometheus.

It can expose metrics related to:

* CPU
* Memory
* Disk
* Network interfaces
* Filesystems
* System statistics

---

## 52. What is PromQL?

PromQL is the query language used by Prometheus.

Example:

```promql
up
```

---

## 53. What does the Prometheus `up` metric mean?

Typically:

```text
up = 1
```

means the target scrape succeeded.

```text
up = 0
```

means the scrape failed.

---

## 54. How can you monitor network receive traffic using PromQL?

If Node Exporter provides the metric:

```promql
rate(node_network_receive_bytes_total[5m])
```

---

## 55. How can you monitor transmit traffic?

```promql
rate(node_network_transmit_bytes_total[5m])
```

---

## 56. What are the main Prometheus metric types?

The four commonly discussed metric types are:

```text
Counter
Gauge
Histogram
Summary
```

### Counter

Only increases, except when reset.

Example:

```text
HTTP requests
```

### Gauge

Can increase or decrease.

Example:

```text
CPU temperature
Active connections
```

### Histogram

Measures observations across buckets.

Useful for:

```text
Latency distributions
Request durations
```

### Summary

Calculates quantile-related summaries on the client side.

---

# 🟡 Grafana

## 57. What is Grafana?

Grafana is a visualization and dashboarding platform commonly used to display metrics from monitoring systems such as Prometheus.

---

## 58. What can you show in a network monitoring dashboard?

Examples:

```text
Network traffic
Packet loss
Latency
Errors
Drops
Connections
Interface utilization
HTTP availability
DNS latency
```

---

## 59. What makes a good monitoring dashboard?

A good dashboard should:

* Focus on important signals
* Avoid unnecessary metrics
* Show trends
* Highlight abnormal conditions
* Use understandable labels
* Provide useful context
* Help troubleshooting

---

# 🟡 Alerting

## 60. What is an alert?

An alert is a notification generated when a monitored condition crosses a defined threshold or condition.

Example:

```text
HTTP availability < expected level
```

---

## 61. What is alert fatigue?

Alert fatigue occurs when engineers receive too many alerts, especially noisy or low-value alerts.

This can cause important alerts to be ignored.

---

## 62. How do you reduce alert fatigue?

Use:

* Meaningful thresholds
* Proper severity levels
* Alert grouping
* Deduplication
* Suppression
* Maintenance windows
* Actionable alerts
* Good runbooks

---

## 63. What is Alertmanager?

Alertmanager is a component commonly used with Prometheus to handle alerts.

It can provide:

* Grouping
* Deduplication
* Routing
* Silencing
* Notification management

---

# 🟡 Golden Signals

## 64. What are the four Golden Signals?

The four Golden Signals are:

```text
Latency
Traffic
Errors
Saturation
```

---

## 65. Explain the Golden Signals.

### Latency

How long requests take.

### Traffic

How much demand the system receives.

### Errors

How many requests or operations fail.

### Saturation

How full or constrained a resource is.

---

# 🟡 RED and USE

## 66. What is the RED method?

RED stands for:

```text
Rate
Errors
Duration
```

It is commonly applied to request-driven services.

---

## 67. What is the USE method?

USE stands for:

```text
Utilization
Saturation
Errors
```

It is commonly useful for infrastructure resources.

---

# 🟡 Kubernetes Monitoring

## 68. How do you monitor Kubernetes nodes?

```bash
kubectl get nodes -o wide
```

If Metrics Server is available:

```bash
kubectl top nodes
```

---

## 69. How do you monitor Kubernetes Pods?

```bash
kubectl get pods -A -o wide
```

If Metrics Server is available:

```bash
kubectl top pods -A
```

---

## 70. How do you inspect Kubernetes Services?

```bash
kubectl get svc -A
```

---

## 71. How do you inspect Service endpoints?

```bash
kubectl get endpoints -A
```

Depending on Kubernetes version, EndpointSlices are also important:

```bash
kubectl get endpointslices -A
```

---

## 72. How do you monitor Kubernetes DNS?

Check CoreDNS:

```bash
kubectl get pods -n kube-system
```

Test DNS:

```bash
kubectl run dns-test \
  --image=busybox:1.36 \
  --rm -it \
  --restart=Never \
  -- nslookup kubernetes.default
```

---

## 73. Is Metrics Server a complete monitoring solution?

No.

Metrics Server primarily provides resource metrics used for purposes such as autoscaling.

A complete observability platform may also use:

```text
Prometheus
Grafana
Node Exporter
kube-state-metrics
Logs
Tracing
```

---

# 🟡 Docker Monitoring

## 74. How do you monitor Docker containers?

```bash
docker ps
```

and:

```bash
docker stats
```

---

## 75. How do you monitor Docker networks?

```bash
docker network ls
```

and:

```bash
docker network inspect <network>
```

---

## 76. How do you identify published Docker ports?

```bash
docker ps --format 'table {{.Names}}\t{{.Ports}}'
```

---

# 🟠 AWS Network Monitoring

## 77. What AWS service is commonly used for monitoring?

Amazon CloudWatch is commonly used for AWS monitoring.

---

## 78. What can you monitor in AWS networking?

Examples include:

* EC2 network metrics
* Load balancers
* NAT Gateways
* Network interfaces
* VPC-related metrics
* Application metrics
* Infrastructure metrics

---

## 79. What are VPC Flow Logs?

VPC Flow Logs capture information about network traffic flows associated with supported VPC resources.

They are useful for investigating:

* Allowed traffic
* Rejected traffic
* Source/destination information
* Ports
* Protocols
* Traffic patterns

They are flow records, not full packet-payload captures.

---

## 80. Can VPC Flow Logs replace tcpdump?

No.

They serve different purposes.

```text
tcpdump
→ packet-level local capture

VPC Flow Logs
→ cloud network flow telemetry
```

---

## 81. How would you monitor a Load Balancer?

I would monitor metrics such as:

* Request count
* Latency
* HTTP errors
* Target health
* Connection behavior
* Backend response status

The exact metrics depend on the AWS load balancer type.

---

# 🔴 Advanced Scenario Questions

## 82. A production application is slow. How do you troubleshoot it?

I would follow a layered approach.

```text
Availability
 ↓
Latency
 ↓
Packet loss
 ↓
DNS
 ↓
Routing
 ↓
TCP connectivity
 ↓
Load balancer
 ↓
Application
 ↓
Database
 ↓
Logs and metrics
```

I would compare the current metrics against the normal baseline before making changes.

---

## 83. Users report intermittent packet loss. What would you check?

I would investigate:

```text
1. Ping and packet loss
2. Interface errors
3. Interface drops
4. Network utilization
5. Network path
6. Retransmissions
7. Firewall behavior
8. Cloud network metrics
9. Recent infrastructure changes
```

Useful commands include:

```bash
ping
ip -s link
ss -s
traceroute
tcpdump
sar
```

---

## 84. DNS works from one machine but not another. What would you check?

I would compare:

* DNS resolver configuration
* DNS server
* Network connectivity
* Search domains
* `/etc/resolv.conf`
* `resolvectl status`
* Firewall rules
* Local caching
* Application-specific DNS configuration

Then compare:

```bash
dig example.com
```

and:

```bash
dig @<dns-server> example.com
```

---

## 85. A service is running but users cannot connect. What do you check?

I would check:

```text
1. Is the process running?
2. Is it listening?
3. Which address is it bound to?
4. Is the port reachable?
5. Is the firewall blocking traffic?
6. Are cloud security controls allowing it?
7. Is routing correct?
8. Is the load balancer healthy?
9. Is the application itself healthy?
```

Commands:

```bash
systemctl status <service>
sudo ss -lntp
nc -vz <host> <port>
curl -v <url>
ip route
```

---

## 86. The application works locally but not remotely. What could be wrong?

A common cause is that the application is listening only on localhost.

For example:

```text
127.0.0.1:8080
```

is reachable locally but not through the machine's external interface.

I would check:

```bash
ss -lntp
```

Then investigate:

* Bind address
* Firewall
* Security Group
* Network ACL
* Routing
* Load balancer configuration

---

## 87. Prometheus shows a target as DOWN. How do you troubleshoot it?

I would check:

```text
1. Is the target running?
2. Is the endpoint reachable?
3. Is the port correct?
4. Is the metrics endpoint working?
5. Is DNS resolving?
6. Is a firewall blocking the connection?
7. Is Prometheus configuration correct?
8. What scrape error is reported?
```

Test manually:

```bash
curl http://<target>:<port>/metrics
```

---

## 88. Prometheus is healthy but metrics are missing. What would you investigate?

I would check:

* Target configuration
* Target health
* Scrape errors
* Exporter availability
* Metric name
* Labels
* PromQL query
* Scrape interval
* Time range
* Permissions/network connectivity

---

## 89. Grafana dashboard shows no data. What would you check?

I would check:

```text
Grafana
 ↓
Data source
 ↓
Prometheus
 ↓
Prometheus query
 ↓
Metric availability
 ↓
Labels
 ↓
Time range
```

I would first test the same query directly in Prometheus.

---

## 90. Network utilization suddenly reaches 100%. What do you do?

I would not immediately restart the server.

I would investigate:

```text
1. Which interface?
2. RX or TX?
3. Which process generates traffic?
4. Which destination is involved?
5. Is this expected traffic?
6. Did a deployment happen?
7. Is there a backup or data transfer?
8. Is there suspicious traffic?
9. Is the network link saturated?
```

Tools:

```bash
ip -s link
ss -s
sar -n DEV
tcpdump
```

---

# 🔴 Production Architecture

## 91. Design a network monitoring architecture for a production environment.

A simple architecture could be:

```text
             Applications
                  |
             Infrastructure
                  |
          +-------+-------+
          |               |
       Metrics           Logs
          |               |
          ↓               ↓
     Prometheus        Log System
          |
       PromQL
          |
       Grafana
          |
       Alerts
          |
     Alertmanager
          |
    DevOps / SRE Team
```

---

## 92. What should you monitor in a production Kubernetes cluster?

I would monitor:

### Cluster

* Node health
* API server health
* Control-plane components

### Workloads

* Pod health
* Restarts
* CPU
* Memory
* Replica availability

### Networking

* DNS
* Services
* Endpoints
* Network errors
* Network traffic
* Network policies where applicable

### Applications

* Request rate
* Error rate
* Latency
* Availability

---

## 93. How would you monitor a production web application?

I would use multiple layers:

```text
Internet
   ↓
DNS monitoring
   ↓
HTTP synthetic monitoring
   ↓
Load balancer metrics
   ↓
Application metrics
   ↓
Infrastructure metrics
   ↓
Logs
   ↓
Alerts
```

This provides visibility from the user to the infrastructure.

---

# 🔴 Troubleshooting Interview Scenarios

## 94. Scenario: Ping works but HTTP does not. What could be wrong?

Ping tests ICMP.

HTTP requires TCP and an application service.

Possible problems:

* Port 80/443 blocked
* Web server stopped
* Reverse proxy issue
* TLS problem
* Application issue
* Firewall
* Security Group

I would test:

```bash
nc -vz <host> 80
nc -vz <host> 443
curl -v http://<host>
curl -v https://<host>
```

---

## 95. Scenario: TCP connection works but HTTP returns 500. What does this indicate?

TCP connectivity is working.

The problem is likely at the application/server layer.

HTTP 500 generally indicates an internal server-side error.

I would investigate:

```text
Application logs
Web server logs
Dependencies
Database
Recent deployments
Application metrics
```

---

## 96. Scenario: DNS works, but TCP connection times out. What do you check?

DNS resolving only proves that name resolution works.

I would investigate:

```text
Routing
Firewall
Security Group
Network ACL
Server availability
Port listening state
Network path
```

---

## 97. Scenario: Port is listening locally but unreachable remotely. Why?

Possible reasons:

* Service bound to localhost
* Host firewall
* Cloud Security Group
* Network ACL
* Incorrect routing
* Load balancer configuration
* Container port not published

---

## 98. Scenario: Kubernetes Service exists but application is unreachable. What do you check?

I would check:

```bash
kubectl get svc
kubectl describe svc <service>
kubectl get endpoints <service>
kubectl get endpointslices
kubectl get pods -o wide
```

Then verify:

* Service selector
* Pod labels
* Endpoint health
* Target port
* Container port
* NetworkPolicy
* CNI behavior

---

## 99. Scenario: Kubernetes DNS suddenly stops working. What do you check?

I would investigate:

```bash
kubectl get pods -n kube-system
```

Then inspect CoreDNS:

```bash
kubectl get pods -n kube-system -l k8s-app=kube-dns
```

Check logs:

```bash
kubectl logs -n kube-system -l k8s-app=kube-dns
```

Then test DNS from a temporary Pod.

---

## 100. Scenario: Network monitoring reports high latency after deployment. What would you do?

I would compare:

```text
Before deployment
        vs
After deployment
```

Then check:

* Application metrics
* Network latency
* CPU/memory
* Network traffic
* Database latency
* Load balancer metrics
* Pod placement
* DNS
* Recent configuration changes

If the deployment is confirmed as the cause, I would follow the organization's rollback or mitigation procedure.

---

# 🏆 Senior-Level Questions

## 101. How do you create a network monitoring baseline?

I would collect normal values for:

```text
Latency
Packet loss
Throughput
Bandwidth
Connections
Errors
Drops
DNS latency
HTTP latency
Service availability
```

Then compare future observations against that baseline.

---

## 102. Why is baseline monitoring important?

Without a baseline, it is difficult to determine whether a value is abnormal.

Example:

```text
Normal latency = 20 ms
Current latency = 200 ms
```

The deviation is immediately meaningful.

---

## 103. What is saturation?

Saturation means a resource is approaching or reaching its capacity.

Examples:

```text
Network link = saturated
CPU = saturated
Disk I/O = saturated
Connection pool = exhausted
```

---

## 104. What is SLI?

SLI means **Service Level Indicator**.

It is a measured indicator of service performance.

Example:

```text
Successful request percentage
```

---

## 105. What is SLO?

SLO means **Service Level Objective**.

It defines the target for an SLI.

Example:

```text
99.9% successful requests
```

---

## 106. What is SLA?

SLA means **Service Level Agreement**.

It is a formal agreement describing expected service levels and potentially consequences when those commitments are not met.

---

## 107. What is the difference between SLI, SLO, and SLA?

```text
SLI
→ What we measure

SLO
→ What target we aim for

SLA
→ What we formally promise/agreed upon
```

---

# 🎯 Rapid-Fire Interview Questions

## 108. Command to check IP?

```bash
ip addr
```

## 109. Command to check routes?

```bash
ip route
```

## 110. Command to check listening ports?

```bash
sudo ss -lntup
```

## 111. Command to test connectivity?

```bash
ping <destination>
```

## 112. Command to test DNS?

```bash
dig <domain>
```

## 113. Command to test TCP port?

```bash
nc -vz <host> <port>
```

## 114. Command to test HTTP?

```bash
curl -I <url>
```

## 115. Command to capture packets?

```bash
sudo tcpdump -i any
```

## 116. Command to monitor Docker resources?

```bash
docker stats
```

## 117. Command to list Kubernetes Services?

```bash
kubectl get svc -A
```

## 118. Command to check Kubernetes Pod IPs?

```bash
kubectl get pods -A -o wide
```

## 119. Prometheus default model?

```text
Pull / Scrape
```

## 120. Prometheus query language?

```text
PromQL
```

## 121. Common visualization tool?

```text
Grafana
```

## 122. Four Golden Signals?

```text
Latency
Traffic
Errors
Saturation
```

## 123. RED?

```text
Rate
Errors
Duration
```

## 124. USE?

```text
Utilization
Saturation
Errors
```

---

# 🧠 Interview Mental Model

When an interviewer asks:

> "How do you troubleshoot a network problem?"

Think:

```text
                    USER REPORT
                         |
                         ↓
                    Availability
                         |
                         ↓
                       DNS
                         |
                         ↓
                      Routing
                         |
                         ↓
                     TCP / Port
                         |
                         ↓
                    Firewall
                         |
                         ↓
                  Network Metrics
                         |
                         ↓
                    Application
                         |
                         ↓
                  Logs + Traces
                         |
                         ↓
                       Fix
                         |
                         ↓
                     Verify
```

---

# ⭐ Best Interview Answer

If asked:

> **"How do you monitor and troubleshoot network issues as a DevOps Engineer?"**

A strong answer is:

> "I use a layered monitoring approach. First, I monitor availability, latency, packet loss, throughput, errors, and network utilization. On Linux, I use tools such as `ip`, `ss`, `ping`, `traceroute`, `dig`, `curl`, `nc`, and `tcpdump`. For centralized monitoring, I can use Prometheus and Grafana to collect and visualize infrastructure and application metrics. In Kubernetes, I monitor nodes, Pods, Services, endpoints, DNS, and workload health. In AWS, I use CloudWatch and VPC Flow Logs along with service-specific metrics. During troubleshooting, I move from DNS and connectivity to routing, ports, firewalls, network health, and finally the application and its logs. After making a change, I always verify that the issue is resolved and monitor the system for recurrence."

---

# 🏁 Final Interview Preparation Checklist

Before considering Network Monitoring interview-ready, make sure you can explain:

* [ ] Network monitoring
* [ ] Availability
* [ ] Latency
* [ ] Packet loss
* [ ] Bandwidth
* [ ] Throughput
* [ ] Jitter
* [ ] Errors
* [ ] Drops
* [ ] Active monitoring
* [ ] Passive monitoring
* [ ] Metrics
* [ ] Logs
* [ ] Events
* [ ] Observability
* [ ] Linux monitoring
* [ ] `ip`
* [ ] `ss`
* [ ] `ping`
* [ ] `traceroute`
* [ ] `dig`
* [ ] `nc`
* [ ] `curl`
* [ ] `tcpdump`
* [ ] Prometheus
* [ ] PromQL
* [ ] Exporters
* [ ] Node Exporter
* [ ] Grafana
* [ ] Alertmanager
* [ ] Alert fatigue
* [ ] Golden Signals
* [ ] RED
* [ ] USE
* [ ] Kubernetes monitoring
* [ ] Kubernetes DNS
* [ ] Kubernetes Services
* [ ] Docker monitoring
* [ ] AWS CloudWatch
* [ ] VPC Flow Logs
* [ ] Baselines
* [ ] SLI
* [ ] SLO
* [ ] SLA
* [ ] Troubleshooting methodology

---

# 🚀 Final Mental Model

```text
MONITOR
   ↓
MEASURE
   ↓
DETECT
   ↓
ALERT
   ↓
INVESTIGATE
   ↓
TROUBLESHOOT
   ↓
FIX
   ↓
VERIFY
   ↓
IMPROVE
```

**A good DevOps Engineer does not just monitor whether a system is UP.**

They understand:

```text
Is it available?
      ↓
Is it fast?
      ↓
Is traffic normal?
      ↓
Are errors increasing?
      ↓
Is the network saturated?
      ↓
What changed?
      ↓
Why did it happen?
      ↓
How do we prevent it?
```

That is the mindset required for production monitoring.
