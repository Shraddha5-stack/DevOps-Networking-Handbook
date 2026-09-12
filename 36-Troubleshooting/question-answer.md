# Chapter 36 — Troubleshooting — Interview Questions

This file contains beginner, intermediate, advanced, and scenario-based troubleshooting interview questions for DevOps and networking roles.

---

# 1. Beginner-Level Questions

## 1. What is troubleshooting?

Troubleshooting is the systematic process of identifying, analyzing, fixing, and verifying a problem.

A good troubleshooting process is:

```text
Identify
   ↓
Collect evidence
   ↓
Isolate
   ↓
Test
   ↓
Fix
   ↓
Verify
   ↓
Document
```

---

## 2. What is the first step when troubleshooting a problem?

First, clearly define the problem.

Ask:

* What is failing?
* Who is affected?
* When did it start?
* Is it consistent or intermittent?
* What changed recently?
* What is the expected behavior?
* What is the actual behavior?

---

## 3. What is the difference between a symptom and a root cause?

A **symptom** is what we observe.

A **root cause** is the underlying reason the problem occurred.

Example:

```text
Symptom:
Website is unavailable.

Root cause:
Web server process crashed because of an invalid configuration.
```

---

## 4. Why should you collect evidence before making changes?

Because changing systems without evidence can:

* Make the problem worse
* Destroy useful information
* Create additional problems
* Make root-cause analysis difficult

A DevOps engineer should investigate first and change carefully.

---

## 5. What is a troubleshooting baseline?

A baseline is a normal reference point for the system.

It can include:

* CPU usage
* Memory usage
* Network traffic
* Latency
* Packet loss
* Connections
* Disk usage
* Application response time

A baseline helps identify abnormal behavior.

---

# 2. Linux Troubleshooting

## 6. How do you check the IP address of a Linux system?

```bash
ip addr
```

Or:

```bash
ip -brief addr
```

---

## 7. How do you check the routing table?

```bash
ip route
```

---

## 8. How do you find the default gateway?

```bash
ip route | grep default
```

---

## 9. How do you check listening ports?

```bash
sudo ss -lntup
```

---

## 10. How do you find which process is using a port?

```bash
sudo ss -lntp
```

For a specific port:

```bash
sudo ss -lntp | grep ':8080'
```

---

## 11. How do you check running processes?

```bash
ps aux
```

Or:

```bash
top
```

---

## 12. How do you identify a CPU-intensive process?

```bash
ps aux --sort=-%cpu | head
```

Or:

```bash
top
```

---

## 13. How do you identify a memory-intensive process?

```bash
ps aux --sort=-%mem | head
```

---

## 14. How do you check memory usage?

```bash
free -h
```

---

## 15. How do you check disk usage?

```bash
df -h
```

---

## 16. How do you check inode usage?

```bash
df -i
```

---

## 17. How do you find large directories?

```bash
du -sh *
```

For the root filesystem:

```bash
sudo du -sh /* 2>/dev/null
```

---

## 18. How do you check a service?

```bash
systemctl status <service>
```

Example:

```bash
systemctl status ssh
```

---

## 19. How do you restart a service?

```bash
sudo systemctl restart <service>
```

However, during troubleshooting, you should understand the problem before restarting a production service.

---

## 20. How do you check service logs?

```bash
journalctl -u <service>
```

Recent logs:

```bash
journalctl -u <service> --since "30 minutes ago"
```

Follow logs:

```bash
journalctl -u <service> -f
```

---

# 3. DNS Troubleshooting

## 21. How do you troubleshoot DNS?

Start with:

```bash
dig example.com
```

Then:

```bash
dig +short example.com
```

Check the configured resolver:

```bash
cat /etc/resolv.conf
```

If applicable:

```bash
resolvectl status
```

Test a specific DNS server:

```bash
dig @8.8.8.8 example.com
```

---

## 22. What happens if DNS fails but IP connectivity works?

Suppose:

```bash
ping 8.8.8.8
```

works, but:

```bash
ping google.com
```

fails.

This suggests that basic IP connectivity may be working while name resolution should be investigated.

Check:

```bash
dig google.com
```

---

## 23. What is DNS troubleshooting?

DNS troubleshooting involves checking:

```text
Client resolver
      ↓
DNS server
      ↓
DNS query
      ↓
DNS response
      ↓
IP address
```

You should investigate:

* Resolver configuration
* DNS server reachability
* Record correctness
* DNS response
* TTL/caching
* Network connectivity

---

# 4. Connectivity Troubleshooting

## 24. How do you test basic connectivity?

Use:

```bash
ping -c 4 <host>
```

But remember that ICMP may be blocked or deprioritized.

For application-level connectivity, use the actual protocol test too.

---

## 25. What does ping test?

`ping` primarily tests IP-layer reachability using ICMP Echo messages.

It can help measure:

* Reachability
* Round-trip latency
* Packet loss

It does not prove that a TCP or HTTP service is healthy.

---

## 26. How do you troubleshoot packet loss?

Start with:

```bash
ping -c 20 <host>
```

Then:

```bash
ip -s link
```

And:

```bash
traceroute <host>
```

Also investigate:

* Interface errors
* Interface drops
* Network congestion
* Routing
* Firewall behavior
* Application-level health

---

## 27. How do you troubleshoot high latency?

Use:

```bash
ping -c 20 <host>
```

Then:

```bash
traceroute <host>
```

For HTTP:

```bash
curl -o /dev/null -s -w '%{time_total}\n' https://example.com
```

Then investigate whether the latency comes from:

* Network
* DNS
* TLS
* Application
* Database
* External dependency
* Resource saturation

---

# 5. Connection Refused vs Timeout

## 28. What does "Connection refused" mean?

It usually means the destination host was reachable enough to actively reject the connection, commonly because no process is listening on that port.

Example:

```bash
nc -vz 127.0.0.1 9999
```

Possible result:

```text
Connection refused
```

Check:

```bash
sudo ss -lntp | grep ':9999'
```

---

## 29. What does "Connection timed out" mean?

A timeout means the expected response did not arrive within the timeout period.

Possible causes include:

* Routing problem
* Firewall
* Security Group
* Network ACL
* Unreachable destination
* Network path issue
* Service path failure

---

## 30. Difference between connection refused and timeout?

| Connection Refused       | Connection Timeout                      |
| ------------------------ | --------------------------------------- |
| Active rejection         | No response received within timeout     |
| Often no listener        | Could be filtering/routing/reachability |
| Usually fails quickly    | Often takes longer                      |
| Investigate service/port | Investigate network path/filtering      |

The exact root cause still requires evidence.

---

# 6. Port Troubleshooting

## 31. How do you test whether a TCP port is reachable?

```bash
nc -vz <host> <port>
```

Example:

```bash
nc -vz example.com 443
```

---

## 32. The application is running but the port is unreachable. What do you check?

Check:

```bash
sudo ss -lntup
```

Then verify:

1. Correct port
2. Correct bind address
3. Firewall
4. Routing
5. Security Group
6. Network ACL
7. Load balancer configuration
8. Application health

---

## 33. What is a bind address?

A bind address determines which local interface/address a service listens on.

For example:

```text
127.0.0.1:8080
```

means the service is listening on loopback.

A service listening on:

```text
0.0.0.0:8080
```

can normally accept connections through the host's IPv4 interfaces, subject to firewall and network controls.

---

# 7. HTTP/HTTPS Troubleshooting

## 34. How do you troubleshoot an HTTP application?

Start with:

```bash
curl -v http://example.com
```

Then investigate:

```text
DNS
 ↓
TCP
 ↓
HTTP
 ↓
Application
 ↓
Dependencies
```

---

## 35. What does HTTP 404 mean?

`404 Not Found` means the server could not find the requested resource.

Possible causes:

* Incorrect URL
* Missing route
* Missing file
* Application routing problem

---

## 36. What does HTTP 500 mean?

`500 Internal Server Error` indicates a server-side application error.

Check:

* Application logs
* Stack traces
* Recent deployments
* Configuration
* Dependencies
* Database connectivity

---

## 37. What does HTTP 502 mean?

`502 Bad Gateway` commonly means a proxy or gateway received an invalid response from an upstream server.

Investigate:

```text
Client
 ↓
Proxy/Load Balancer
 ↓
Upstream
```

Check:

* Upstream health
* Port
* DNS
* Connection
* Application process
* Logs

---

## 38. What does HTTP 503 mean?

`503 Service Unavailable` means the service is currently unavailable.

Possible causes:

* No healthy backend
* Service overloaded
* Maintenance
* Application unavailable
* Load balancer health-check failure

---

## 39. What does HTTP 504 mean?

`504 Gateway Timeout` means a gateway/proxy did not receive a timely response from an upstream service.

Investigate:

* Upstream latency
* Network connectivity
* Application processing
* Database
* External dependencies
* Timeout configuration

---

## 40. How do you troubleshoot HTTPS?

Run:

```bash
curl -v https://example.com
```

Then:

```bash
openssl s_client \
  -connect example.com:443 \
  -servername example.com
```

Check:

* TCP connection
* TLS handshake
* Certificate
* Certificate chain
* Hostname
* Expiration
* Server configuration

---

# 8. Packet Troubleshooting

## 41. What is tcpdump?

`tcpdump` is a command-line packet capture and analysis tool.

Example:

```bash
sudo tcpdump -i any
```

---

## 42. How do you capture HTTPS traffic?

```bash
sudo tcpdump -i any port 443
```

---

## 43. How do you capture DNS traffic?

```bash
sudo tcpdump -i any port 53
```

---

## 44. How do you save packets to a file?

```bash
sudo tcpdump -i any -c 100 -w capture.pcap
```

Read:

```bash
sudo tcpdump -r capture.pcap
```

---

## 45. Why would you use packet capture?

Packet capture provides evidence about what is actually happening on the network.

It can help identify:

* TCP connection attempts
* Retransmissions
* DNS queries
* DNS responses
* Resets
* Unexpected traffic
* Protocol behavior

---

# 9. Docker Troubleshooting

## 46. A Docker container is not working. What do you check?

Start with:

```bash
docker ps -a
```

Then:

```bash
docker logs <container>
```

Then:

```bash
docker inspect <container>
```

Check:

```text
Container state
Ports
Networks
Environment
Mounts
IP address
```

---

## 47. How do you check Docker network configuration?

```bash
docker network ls
```

Then:

```bash
docker network inspect <network>
```

---

## 48. Docker container is running but application is unreachable. What do you check?

Check:

```bash
docker ps
```

Then:

```bash
docker port <container>
```

Then:

```bash
sudo ss -lntup
```

Then:

```bash
curl -v http://127.0.0.1:<published-port>
```

Also inspect:

* Container logs
* Application listening address
* Port mapping
* Docker network
* Host firewall

---

# 10. Kubernetes Troubleshooting

## 49. How do you start troubleshooting a Kubernetes problem?

Start with:

```bash
kubectl get nodes
kubectl get pods -A
```

Then narrow down the affected namespace, workload, Pod, Service, or node.

---

## 50. How do you troubleshoot a Kubernetes Pod?

Use:

```bash
kubectl get pods
```

Then:

```bash
kubectl describe pod <pod>
```

Then:

```bash
kubectl logs <pod>
```

If the container restarted:

```bash
kubectl logs <pod> --previous
```

---

## 51. What does CrashLoopBackOff mean?

It means Kubernetes is repeatedly restarting a container that is failing.

Possible causes:

* Application crash
* Incorrect configuration
* Missing environment variable
* Dependency failure
* Failed health probe
* Resource issue

Investigate:

```bash
kubectl describe pod <pod>
kubectl logs <pod>
kubectl logs <pod> --previous
```

---

## 52. What does ImagePullBackOff mean?

It means Kubernetes is having trouble obtaining the container image.

Possible causes:

* Incorrect image name
* Incorrect tag
* Registry unavailable
* Authentication failure
* Network problem

Check:

```bash
kubectl describe pod <pod>
```

Look at the Events section.

---

## 53. How do you troubleshoot a Kubernetes Service?

Run:

```bash
kubectl get svc
```

Then:

```bash
kubectl describe svc <service>
```

Then:

```bash
kubectl get endpoints <service>
```

And:

```bash
kubectl get endpointslices
```

Check Pod labels:

```bash
kubectl get pods --show-labels
```

The Service selector must match the intended Pod labels.

---

## 54. A Kubernetes Service has no endpoints. What could be wrong?

Possible causes:

* No matching Pods
* Incorrect Service selector
* Pods are not Ready
* Pods are not running
* Namespace mismatch
* EndpointSlice/controller issue

Check:

```bash
kubectl get pods --show-labels
kubectl describe svc <service>
kubectl get endpoints <service>
kubectl get endpointslices
```

---

## 55. How do you troubleshoot Kubernetes DNS?

Check CoreDNS:

```bash
kubectl get pods -n kube-system
```

Run:

```bash
kubectl run dns-test \
  --image=busybox:1.36 \
  --rm -it \
  --restart=Never \
  -- nslookup kubernetes.default
```

Check CoreDNS logs when appropriate:

```bash
kubectl logs -n kube-system -l k8s-app=kube-dns
```

---

## 56. How do you troubleshoot Kubernetes NetworkPolicy?

Check:

```bash
kubectl get networkpolicy -A
```

Then:

```bash
kubectl describe networkpolicy <policy>
```

Verify:

* Pod labels
* Namespace
* Ingress rules
* Egress rules
* Ports
* Selectors
* CNI support

NetworkPolicy enforcement depends on the cluster's networking implementation.

---

# 11. AWS Networking Troubleshooting

## 57. An EC2 instance cannot access the Internet. How do you troubleshoot?

Check:

```text
EC2
 ↓
Subnet
 ↓
Route Table
 ↓
Internet Gateway / NAT Gateway
 ↓
Security Group
 ↓
Network ACL
```

Verify:

* IP configuration
* Subnet
* Route table
* Default route
* Internet Gateway or NAT path
* Security Group
* NACL
* DNS
* Application configuration

---

## 58. What is the difference between Security Group and Network ACL during troubleshooting?

| Security Group                                                   | Network ACL                               |
| ---------------------------------------------------------------- | ----------------------------------------- |
| Instance/ENI level                                               | Subnet level                              |
| Stateful                                                         | Stateless                                 |
| Allow rules                                                      | Allow and deny rules                      |
| Return traffic automatically allowed for established connections | Return traffic must be explicitly allowed |
| No rule numbers                                                  | Rule numbers                              |

---

## 59. An EC2 instance cannot receive traffic on port 80. What do you check?

Check:

```text
1. Application listening?
2. Correct bind address?
3. Security Group allows TCP/80?
4. NACL allows traffic?
5. Route correct?
6. Instance has expected network path?
7. Load balancer configuration correct?
8. Health checks passing?
```

On Linux:

```bash
sudo ss -lntp | grep ':80'
```

---

## 60. What are VPC Flow Logs useful for?

VPC Flow Logs provide records about network flows.

They can help investigate:

* Source/destination
* Ports
* Protocol
* Accepted traffic
* Rejected traffic
* Traffic volume

They are not full packet captures and do not provide packet payloads.

---

# 12. Advanced Troubleshooting

## 61. What is troubleshooting from outside-in?

Start from the client and move toward the application:

```text
Client
 ↓
DNS
 ↓
Network
 ↓
Load Balancer
 ↓
Firewall
 ↓
Server
 ↓
Process
 ↓
Application
 ↓
Database
```

This helps isolate the failing layer.

---

## 62. What is troubleshooting from inside-out?

Start from the server/application and move toward the client.

Example:

```text
Application
 ↓
Process
 ↓
Port
 ↓
Server
 ↓
Network
 ↓
Client
```

The approach depends on where you have evidence and access.

---

## 63. Why is "works on localhost" not enough?

Because localhost only proves that the application is accessible locally.

For example:

```text
127.0.0.1:8080
```

may work while:

```text
server-ip:8080
```

fails.

Possible reasons:

* Bind address
* Firewall
* Security Group
* Routing
* NetworkPolicy
* Load balancer configuration

---

## 64. What is the Five Whys technique?

Five Whys is a root-cause analysis technique.

You repeatedly ask:

> Why did this happen?

until you reach an actionable underlying cause.

Example:

```text
Website failed
   ↓ Why?
Application stopped
   ↓ Why?
Process crashed
   ↓ Why?
Invalid configuration
   ↓ Why?
Bad deployment
   ↓ Why?
Configuration validation was missing
```

---

## 65. What is Root Cause Analysis?

Root Cause Analysis, or RCA, is the process of identifying the underlying reason a failure occurred and determining how to prevent recurrence.

A good RCA contains:

```text
Incident
Impact
Timeline
Symptoms
Evidence
Root cause
Contributing factors
Fix
Prevention
```

---

## 66. What is mitigation?

Mitigation reduces the impact of an incident while the permanent fix is being developed.

Example:

```text
Problem:
One backend is failing.

Mitigation:
Remove the unhealthy backend from traffic.

Permanent fix:
Correct the application bug.
```

---

## 67. What is the difference between mitigation and permanent fix?

**Mitigation** reduces immediate impact.

**Permanent fix** addresses the underlying cause.

Example:

```text
Mitigation:
Restart unhealthy application instance.

Permanent fix:
Fix the memory leak causing the crash.
```

---

# 13. Production Scenarios

## 68. Production website is down. What would you do first?

I would first define the scope and impact.

I would ask:

* Is everyone affected?
* Is it one region?
* Is it one endpoint?
* When did it start?
* What changed recently?

Then I would collect evidence rather than immediately restarting services.

---

## 69. Website works for some users but not others. What would you investigate?

I would compare:

* DNS resolution
* Region
* Network path
* CDN
* Load balancer
* Authentication
* Client/network
* Application routing

I would identify what is common between affected users and unaffected users.

---

## 70. Website returns 502. How would you troubleshoot?

I would investigate the proxy/load-balancer-to-upstream path.

```text
Client
 ↓
Load Balancer / Reverse Proxy
 ↓
Upstream Application
```

Check:

```bash
curl -v <url>
```

Then investigate:

* Backend health
* Backend port
* DNS
* Network connectivity
* Application process
* Application logs
* Load balancer logs/metrics

---

## 71. Website returns 504. What would you investigate?

A 504 commonly points to an upstream response timeout.

I would check:

* Upstream latency
* Network connectivity
* Application processing time
* Database queries
* External APIs
* Proxy timeout settings
* Resource saturation

---

## 72. Server CPU is 100%. What would you do?

First identify the process:

```bash
top
```

or:

```bash
ps aux --sort=-%cpu | head
```

Then determine whether the high CPU is expected.

I would check:

* Recent deployments
* Traffic increase
* Infinite loops
* Background jobs
* Application behavior
* Logs

I would avoid killing processes blindly.

---

## 73. Server memory is exhausted. What would you check?

Run:

```bash
free -h
```

Then:

```bash
ps aux --sort=-%mem | head
```

Investigate:

* Memory leak
* Traffic increase
* Application configuration
* Caching
* Number of processes
* Container limits
* Swap

---

## 74. Disk is 100% full. How would you troubleshoot?

Run:

```bash
df -h
```

Then:

```bash
df -i
```

Find large directories:

```bash
sudo du -sh /* 2>/dev/null
```

Then inspect:

* Logs
* Temporary files
* Application data
* Container images
* Deleted-but-open files

Do not delete files blindly in production.

---

# 14. DevOps Troubleshooting Scenarios

## 75. CI/CD pipeline cannot reach a container registry. What do you check?

Check:

```text
DNS
 ↓
Network connectivity
 ↓
TCP/HTTPS
 ↓
Proxy/firewall
 ↓
Registry authentication
 ↓
Runner configuration
```

Test:

```bash
dig <registry>
```

Then:

```bash
nc -vz <registry> 443
```

Then:

```bash
curl -v https://<registry>
```

---

## 76. Kubernetes application cannot access an external API. What do you check?

Investigate:

```text
Pod
 ↓
DNS
 ↓
NetworkPolicy
 ↓
CNI/network
 ↓
Node
 ↓
NAT/Internet path
 ↓
External API
```

Test DNS from the Pod:

```bash
nslookup <api-domain>
```

Test connectivity:

```bash
wget -qO- https://<api-domain>
```

if the container image provides the required utility.

---

## 77. Kubernetes application cannot access another Pod. What do you check?

Check:

1. Pod status
2. Pod IP
3. Service
4. Service selector
5. EndpointSlices
6. NetworkPolicy
7. CNI
8. Ports
9. Application bind address

Useful commands:

```bash
kubectl get pods -o wide
kubectl get svc
kubectl get endpointslices
kubectl get networkpolicy
```

---

## 78. Deployme
