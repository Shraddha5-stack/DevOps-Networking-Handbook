# Chapter 35 — Network Monitoring

## 📌 Introduction

Network Monitoring is the process of continuously observing network infrastructure, traffic, systems, services, and applications to understand their **health, performance, availability, and security**.

For a DevOps Engineer, network monitoring is important because many production problems are related to:

* High latency
* Packet loss
* Network congestion
* DNS failures
* Connection failures
* Port availability
* Service downtime
* Interface errors
* Kubernetes networking
* Docker networking
* Cloud networking
* Security incidents

A good monitoring system helps us **detect problems early, troubleshoot faster, and maintain reliable infrastructure**.

---

# 🎯 Learning Objectives

By completing this chapter, you will understand:

* What network monitoring is
* Why network monitoring is important
* Monitoring vs observability
* Metrics, logs, events, and traces
* Network availability
* Uptime
* Latency
* Packet loss
* Jitter
* Bandwidth
* Throughput
* Network errors and drops
* Active and passive monitoring
* ICMP monitoring
* TCP monitoring
* HTTP/HTTPS monitoring
* DNS monitoring
* Port monitoring
* Service monitoring
* Network interface monitoring
* Linux network monitoring
* `ip` command
* `ss` command
* `ping`
* `traceroute`
* `tracepath`
* `tcpdump`
* `curl`
* Prometheus
* Exporters
* PromQL
* Grafana
* Dashboards
* Alerting
* Alertmanager
* SLI, SLO, and SLA
* Golden Signals
* RED method
* USE method
* Kubernetes monitoring
* Docker monitoring
* AWS CloudWatch
* VPC Flow Logs
* Load Balancer monitoring
* NAT Gateway monitoring
* Security monitoring
* Capacity planning
* Incident response
* Network troubleshooting

---

# 🧠 What Is Network Monitoring?

Network monitoring means continuously collecting and analyzing information about a network.

We monitor things such as:

```text
Servers
   ↓
Network Interfaces
   ↓
Routers / Switches
   ↓
Firewalls
   ↓
Load Balancers
   ↓
Applications
   ↓
Containers
   ↓
Kubernetes
   ↓
Cloud Infrastructure
```

The objective is to answer questions such as:

* Is the service available?
* Is the network slow?
* Are packets being dropped?
* Which interface has errors?
* Which ports are open?
* Are connections increasing?
* Is DNS working?
* Is HTTPS working?
* Is a server overloaded?
* Is the application reachable?
* Is the Kubernetes service healthy?

---

# 🔍 What Should We Monitor?

## 1. Infrastructure

Monitor:

* Servers
* Routers
* Switches
* Firewalls
* Load balancers
* Network interfaces

## 2. Network

Monitor:

* Latency
* Packet loss
* Throughput
* Bandwidth
* Jitter
* Errors
* Drops
* Connections

## 3. Applications

Monitor:

* HTTP response time
* HTTP status codes
* API availability
* Application errors
* Request rate

## 4. Kubernetes

Monitor:

* Pods
* Services
* Endpoints
* Nodes
* Network traffic
* DNS
* Container metrics

## 5. Cloud

Monitor:

* VPC
* Subnets
* Load Balancers
* NAT Gateways
* Network interfaces
* Flow Logs
* Security Groups
* Network ACLs

---

# 📊 Important Network Metrics

| Metric       | Meaning                                                |
| ------------ | ------------------------------------------------------ |
| Availability | Whether a service is reachable                         |
| Uptime       | How long a service remains available                   |
| Latency      | Time required for communication                        |
| Packet Loss  | Percentage of packets that don't reach the destination |
| Jitter       | Variation in packet delay                              |
| Bandwidth    | Maximum data-carrying capacity                         |
| Throughput   | Actual amount of data transferred                      |
| Errors       | Failed transmissions                                   |
| Drops        | Packets discarded by the network                       |
| Connections  | Number of active network connections                   |

---

# ⚡ Latency

Latency is the time required for data to travel from one point to another.

Example:

```text
Client
  |
  | Request
  ↓
Server
  |
  | Response
  ↓
Client
```

If the round-trip time is:

```text
20 ms
```

the network is generally faster than one with:

```text
500 ms
```

High latency can affect:

* APIs
* Websites
* Databases
* Kubernetes applications
* Distributed systems

---

# 📦 Packet Loss

Packet loss occurs when packets fail to reach their destination.

Example:

```text
100 packets sent
5 packets lost

Packet Loss = 5%
```

Packet loss can cause:

* Slow applications
* Retransmissions
* Connection failures
* Poor voice/video quality
* TCP performance problems

---

# 📶 Bandwidth vs Throughput

### Bandwidth

The maximum capacity of a network connection.

Example:

```text
Network bandwidth = 1 Gbps
```

### Throughput

The actual amount of data transferred.

Example:

```text
Bandwidth = 1 Gbps
Throughput = 700 Mbps
```

Bandwidth is capacity.

Throughput is actual performance.

---

# 📡 Jitter

Jitter is the variation in packet arrival time.

Example:

```text
Packet 1 → 20 ms
Packet 2 → 21 ms
Packet 3 → 80 ms
Packet 4 → 25 ms
```

The large variation indicates jitter.

Jitter is especially important for:

* Voice
* Video
* Real-time applications

---

# 🔄 Active vs Passive Monitoring

## Active Monitoring

The monitoring system actively sends traffic to test the network.

Examples:

```bash
ping
curl
traceroute
```

Example:

```bash
ping google.com
```

## Passive Monitoring

The monitoring system observes existing network traffic.

Examples:

```bash
tcpdump
VPC Flow Logs
Network traffic monitoring
```

### Difference

| Active                 | Passive                   |
| ---------------------- | ------------------------- |
| Generates test traffic | Observes existing traffic |
| Tests availability     | Observes real traffic     |
| `ping`                 | `tcpdump`                 |
| `curl`                 | Flow Logs                 |

---

# 🧾 Metrics, Logs, Events and Traces

Modern monitoring commonly uses four types of telemetry.

### Metrics

Numerical measurements.

Example:

```text
CPU = 70%
Latency = 120 ms
Packet Loss = 2%
```

### Logs

Detailed records of events.

Example:

```text
Connection refused
DNS lookup failed
HTTP 500
```

### Events

Something important happened.

Example:

```text
Server restarted
Pod deleted
Network interface changed
```

### Traces

Track a request across multiple services.

Example:

```text
Client
 ↓
API Gateway
 ↓
Service A
 ↓
Service B
 ↓
Database
```

---

# 🛠️ Linux Network Monitoring Commands

## Check IP addresses

```bash
ip addr
```

## Check routing table

```bash
ip route
```

## Check interface statistics

```bash
ip -s link
```

## Check listening ports

```bash
ss -lntp
```

## Check active connections

```bash
ss -ant
```

## Check socket statistics

```bash
ss -s
```

## Test connectivity

```bash
ping google.com
```

## Trace network path

```bash
traceroute google.com
```

or:

```bash
tracepath google.com
```

## Capture packets

```bash
sudo tcpdump
```

## Test HTTP/HTTPS

```bash
curl -I https://example.com
```

---

# 📈 Prometheus

Prometheus is a popular open-source monitoring and alerting system.

A simplified architecture:

```text
Applications
     ↓
Exporters
     ↓
Prometheus
     ↓
PromQL
     ↓
Grafana
     ↓
Dashboards
```

Prometheus normally uses a **pull/scrape model**.

It periodically collects metrics from targets.

Example:

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

# 📤 Exporters

Exporters expose metrics in a format that Prometheus can collect.

Common examples include:

* Node Exporter
* Blackbox Exporter
* Application-specific exporters

For Linux infrastructure, Node Exporter can expose system and network-related metrics.

---

# 🔎 PromQL

PromQL means **Prometheus Query Language**.

It is used to query Prometheus metrics.

Example:

```promql
up
```

This can be used to determine whether monitored targets are up.

---

# 📊 Grafana

Grafana is commonly used to visualize monitoring data.

Architecture:

```text
Infrastructure
      ↓
Prometheus
      ↓
Grafana
      ↓
Dashboard
```

A dashboard can display:

* CPU
* Memory
* Network traffic
* Latency
* Packet loss
* Requests
* Errors
* Availability

---

# 🚨 Alerting

Monitoring tells us what is happening.

Alerting tells us when something requires attention.

Example:

```text
Network latency > 500 ms
        ↓
Alert
        ↓
DevOps Engineer
```

Good alerts should be:

* Actionable
* Relevant
* Clear
* Based on meaningful thresholds

Avoid creating too many alerts because this can cause **alert fatigue**.

---

# 🔔 Alertmanager

Prometheus can detect alert conditions, while Alertmanager is commonly used to manage alerts.

Alertmanager can handle:

* Alert grouping
* Deduplication
* Routing
* Silencing
* Notification integration

Example:

```text
Prometheus
    ↓
Alert
    ↓
Alertmanager
    ↓
Email / Slack / Other notification systems
```

---

# 🎯 SLI, SLO and SLA

## SLI

Service Level Indicator.

A measurable value representing service performance.

Example:

```text
API Availability = 99.95%
```

## SLO

Service Level Objective.

The target for the SLI.

Example:

```text
API Availability SLO = 99.9%
```

## SLA

Service Level Agreement.

A formal agreement between a service provider and customer.

---

# ⭐ Golden Signals

The four Golden Signals are:

```text
1. Latency
2. Traffic
3. Errors
4. Saturation
```

### Latency

How long requests take.

### Traffic

How much demand the system receives.

### Errors

How many requests fail.

### Saturation

How much of a resource is being utilized.

---

# 🔴 RED Method

RED is commonly used for monitoring services.

```text
R → Rate
E → Errors
D → Duration
```

### Rate

Number of requests.

### Errors

Number of failed requests.

### Duration

Time required to process requests.

---

# 🟢 USE Method

USE is commonly applied to infrastructure resources.

```text
U → Utilization
S → Saturation
E → Errors
```

Example:

```text
Network Interface
 ├── Utilization
 ├── Saturation
 └── Errors
```

---

# ☸️ Kubernetes Network Monitoring

Kubernetes monitoring should include:

* Nodes
* Pods
* Services
* Endpoints
* DNS
* Network traffic
* Container metrics
* Network policies

Example:

```text
User
 ↓
Load Balancer
 ↓
Kubernetes Service
 ↓
Pods
 ↓
Application
```

Important components may include:

* kubelet
* cAdvisor/container metrics
* Node Exporter
* kube-state-metrics
* Prometheus
* Grafana

`metrics-server` is primarily used for resource metrics and features such as HPA; it is not a complete monitoring/observability platform.

---

# 🐳 Docker Network Monitoring

For Docker, monitor:

* Containers
* Networks
* Published ports
* Container connectivity
* Network traffic
* DNS
* Errors

Useful commands:

```bash
docker network ls
```

```bash
docker network inspect bridge
```

```bash
docker ps
```

```bash
docker stats
```

---

# ☁️ AWS Network Monitoring

AWS provides several monitoring capabilities.

Important services/features include:

* Amazon CloudWatch
* VPC Flow Logs
* Elastic Load Balancing metrics
* NAT Gateway metrics
* Network interfaces
* Route monitoring

A simplified architecture:

```text
AWS VPC
   |
   +-- EC2
   |
   +-- Load Balancer
   |
   +-- NAT Gateway
   |
   +-- Network Interfaces
   |
   +-- VPC Flow Logs
            ↓
        CloudWatch
```

---

# 📝 VPC Flow Logs

VPC Flow Logs capture information about network traffic flows for supported AWS resources.

They can help investigate:

* Accepted traffic
* Rejected traffic
* Source/destination information
* Network troubleshooting
* Security investigations

Flow Logs are **flow records**, not a replacement for full packet capture.

---

# 🔐 Security Monitoring

Network monitoring also supports security.

Monitor for:

* Unexpected open ports
* Unusual connections
* Traffic spikes
* Repeated connection attempts
* Suspicious DNS activity
* Unexpected outbound traffic
* Firewall denies
* Network policy violations

---

# 📉 Anomaly Detection

Anomaly detection means identifying behavior that differs significantly from the normal baseline.

Example:

Normal:

```text
Network traffic:
100 Mbps
120 Mbps
110 Mbps
115 Mbps
```

Suddenly:

```text
950 Mbps
```

This may require investigation.

---

# 📊 Network Baseline

Before identifying abnormal behavior, understand normal behavior.

Example baseline:

```text
Normal latency: 20–50 ms
Normal packet loss: <1%
Normal traffic: 100–300 Mbps
Normal connections: 500–1000
```

Then compare current behavior with the baseline.

---

# 🏗️ Capacity Planning

Monitoring helps predict when infrastructure needs more capacity.

Example:

```text
Current traffic → 60%
      ↓
      ↓
70%
      ↓
80%
      ↓
90%
      ↓
Scale infrastructure
```

Capacity planning helps prevent:

* Network saturation
* Performance degradation
* Service outages

---

# 🔧 Network Troubleshooting Flow

When a network problem occurs:

```text
1. Identify the problem
        ↓
2. Check availability
        ↓
3. Check IP configuration
        ↓
4. Check routing
        ↓
5. Check DNS
        ↓
6. Check ports
        ↓
7. Check firewall
        ↓
8. Check latency / packet loss
        ↓
9. Check service
        ↓
10. Check application
        ↓
11. Check logs and metrics
        ↓
12. Fix and verify
```

Useful commands:

```bash
ip addr
ip route
ss -lntp
ping
traceroute
dig
curl
tcpdump
```

---

# 🧩 Common Network Monitoring Problems

## Problem 1: High Latency

Possible causes:

* Network congestion
* Long network path
* Server overload
* DNS delay
* Cloud routing issues

## Problem 2: Packet Loss

Possible causes:

* Network congestion
* Interface errors
* Faulty hardware
* Firewall behavior
* Unstable connection

## Problem 3: Service Down

Check:

```bash
ss -lntp
```

Then:

```bash
curl
```

Then inspect:

```bash
systemctl status <service>
```

and:

```bash
journalctl -u <service>
```

## Problem 4: DNS Failure

Check:

```bash
dig example.com
```

Then investigate:

* DNS configuration
* Resolver
* Network connectivity
* Firewall
* DNS server availability

---

# 🏆 DevOps Network Monitoring Architecture

A practical monitoring architecture can look like:

```text
                  Users
                    |
                    v
             Load Balancer
                    |
                    v
              Application
                    |
          +---------+---------+
          |                   |
          v                   v
       Metrics              Logs
          |                   |
          v                   v
     Prometheus          Log System
          |
          v
       Grafana
          |
          v
      Alerting
          |
          v
     DevOps / SRE
```

For infrastructure:

```text
Servers
Containers
Kubernetes
AWS
Network Devices
      |
      v
Metrics / Logs / Flow Data
      |
      v
Monitoring Platform
      |
      v
Dashboards + Alerts
      |
      v
Troubleshooting + Incident Response
```

---

# ✅ Network Monitoring Checklist

Before considering a network healthy, check:

* [ ] IP configuration
* [ ] Routing
* [ ] DNS
* [ ] Connectivity
* [ ] Latency
* [ ] Packet loss
* [ ] Bandwidth
* [ ] Throughput
* [ ] Network errors
* [ ] Network drops
* [ ] Open ports
* [ ] Active connections
* [ ] Service availability
* [ ] HTTP/HTTPS health
* [ ] Monitoring metrics
* [ ] Logs
* [ ] Alerts
* [ ] Kubernetes networking
* [ ] Docker networking
* [ ] AWS networking
* [ ] Security events
* [ ] Capacity
* [ ] Baseline

---

# 🧠 Interview Mental Model

When an interviewer asks:

> "How do you monitor a network?"

Think:

```text
Availability
    ↓
Latency
    ↓
Packet Loss
    ↓
Throughput
    ↓
Errors / Drops
    ↓
Connections
    ↓
DNS
    ↓
Ports
    ↓
Services
    ↓
Metrics + Logs
    ↓
Prometheus
    ↓
Grafana
    ↓
Alerts
    ↓
Troubleshooting
```

---

# 🏁 Final Mental Model

Remember:

```text
Observe
   ↓
Measure
   ↓
Visualize
   ↓
Alert
   ↓
Investigate
   ↓
Troubleshoot
   ↓
Fix
   ↓
Verify
   ↓
Improve
```

Network monitoring is not only about checking whether a server is **up or down**.

A strong DevOps Engineer monitors:

```text
Network
+
Infrastructure
+
Applications
+
Containers
+
Kubernetes
+
Cloud
+
Security
```

The ultimate goal is:

> **Detect problems early, understand what is happening, troubleshoot quickly, and keep systems reliable.**

---

## 📚 Chapter 35 Files

This chapter contains:

* `README.md` → Introduction and complete roadmap
* `notes.md` → Detailed Network Monitoring theory
* `commands.md` → Practical monitoring commands
* `practical-lab.md` → Hands-on monitoring labs
* `interview-questions.md` → Interview preparation

---

## 🚀 Next Step

After completing this README, continue with:

```text
notes.md
```

Then move to:

```text
commands.md
        ↓
practical-lab.md
        ↓
interview-questions.md
```
