# Kubernetes Networking — Interview Questions

This document contains Kubernetes Networking interview questions from beginner to advanced level.

The goal is to understand not only definitions, but also how Kubernetes networking works in real DevOps environments.

---

# 1. Beginner Level

## 1. What is Kubernetes networking?

Kubernetes networking is the system that allows:

* Pod-to-Pod communication
* Pod-to-Service communication
* Service-to-Pod communication
* Node-to-Pod communication
* External-to-Service communication
* DNS-based service discovery
* Network security using NetworkPolicy

The Kubernetes networking model is designed so that Pods can communicate with each other across Nodes without requiring manual NAT between Pods.

---

## 2. What is a Pod IP?

A Pod IP is the IP address assigned to a Pod.

Example:

```text
Pod:
10.244.0.10
```

Every Pod normally receives its own IP address.

Pod IPs are generally temporary because Pods can be recreated.

---

## 3. Why should applications not directly depend on Pod IPs?

Because Pod IPs can change.

For example:

```text
Pod A
10.244.0.10
```

After the Pod is recreated:

```text
Pod A
10.244.0.25
```

Therefore applications should normally communicate through a Kubernetes Service.

---

## 4. What is a Kubernetes Service?

A Service provides a stable network endpoint for a group of Pods.

It provides:

* Stable IP
* Stable DNS name
* Service discovery
* Traffic distribution to selected Pods

Architecture:

```text
Client
  |
  ↓
Service
  |
  +---- Pod
  +---- Pod
  +---- Pod
```

---

## 5. What is ClusterIP?

ClusterIP is the default Kubernetes Service type.

It provides an internal virtual IP that is normally reachable only from inside the cluster.

Example:

```text
Service:
10.96.100.10:80
```

---

## 6. What is NodePort?

NodePort exposes a Service through a port on Kubernetes Nodes.

Example:

```text
Node IP:30080
      |
      ↓
Service
      |
      ↓
Pods
```

Typical NodePort range:

```text
30000-32767
```

---

## 7. What is LoadBalancer?

LoadBalancer exposes a Service through an external load balancer, typically when the Kubernetes environment supports integration with a cloud or external load-balancing system.

Typical architecture:

```text
Internet
   |
   ↓
Load Balancer
   |
   ↓
Service
   |
   ↓
Pods
```

---

## 8. What is Kubernetes DNS?

Kubernetes DNS allows applications to discover Services using names instead of IP addresses.

Example:

```text
backend-service
```

Instead of:

```text
10.96.100.20
```

---

## 9. What is CoreDNS?

CoreDNS is commonly used as the DNS server inside a Kubernetes cluster.

It provides DNS-based service discovery.

For example:

```text
backend-service
```

can resolve to the Service IP.

---

## 10. What is a CNI?

CNI means:

**Container Network Interface**

CNI provides the networking implementation used by Kubernetes.

Examples include:

* Cilium
* Calico
* Flannel
* Weave Net

The CNI is responsible for implementing networking between containers/Pods and can also provide network policy functionality depending on the implementation.

---

# 2. Services

## 11. Why do we need a Service?

Pods are temporary.

A Deployment may create:

```text
Pod 1
Pod 2
Pod 3
```

Pods may be deleted and recreated.

A Service gives applications a stable endpoint:

```text
Application
     |
     ↓
backend-service
     |
     ↓
Backend Pods
```

---

## 12. How does a Service find Pods?

A Service uses label selectors.

Example:

```yaml
selector:
  app: backend
```

Pods with:

```yaml
labels:
  app: backend
```

can become Service endpoints.

---

## 13. What happens if the Service selector is wrong?

The Service may have no endpoints.

Check:

```bash
kubectl get endpoints
```

or:

```bash
kubectl get endpointslices
```

Then compare:

```bash
kubectl get pods --show-labels
```

with:

```bash
kubectl describe svc <service-name>
```

---

## 14. What is an Endpoint?

An Endpoint represents the network destinations associated with a Service.

Example:

```text
backend-service
      |
      +-- 10.244.0.10:80
      +-- 10.244.0.11:80
      +-- 10.244.0.12:80
```

---

## 15. What is an EndpointSlice?

EndpointSlice is the modern Kubernetes API for tracking network endpoints behind Services.

It scales better than maintaining all endpoints in one large Endpoints object.

Check:

```bash
kubectl get endpointslices
```

---

# 3. Kubernetes DNS

## 16. What is a Service DNS name?

A Service can be accessed using its DNS name.

For example:

```text
backend-service
```

From another namespace:

```text
backend-service.networking-lab
```

Full DNS name:

```text
backend-service.networking-lab.svc.cluster.local
```

---

## 17. What is the general Kubernetes Service DNS format?

The common full format is:

```text
<service>.<namespace>.svc.cluster.local
```

Example:

```text
mysql.database.svc.cluster.local
```

---

## 18. How do you test Kubernetes DNS?

Run:

```bash
kubectl exec -it <pod> -- nslookup <service-name>
```

Example:

```bash
kubectl exec -it client -- nslookup backend-service
```

You can also inspect:

```bash
kubectl exec <pod> -- cat /etc/resolv.conf
```

---

## 19. What if `nslookup` fails?

Check:

```bash
kubectl get pods -n kube-system
```

Find CoreDNS:

```bash
kubectl get pods -n kube-system | grep coredns
```

Then check:

```bash
kubectl logs -n kube-system <coredns-pod>
```

Also verify:

```bash
kubectl get svc -n kube-system
```

---

# 4. Pod Networking

## 20. How does Pod-to-Pod communication work?

Kubernetes networking provides each Pod with an IP address.

Example:

```text
Pod A
10.244.0.10
     |
     | Network
     ↓
Pod B
10.244.1.20
```

The CNI implements the underlying network connectivity.

---

## 21. Can Pods on different Nodes communicate?

Yes.

The Kubernetes networking model expects Pods to be able to communicate across Nodes without requiring application-level changes.

The exact implementation depends on the CNI.

---

## 22. What is a Pod network CIDR?

A Pod CIDR is an IP address range used for Pod networking.

Example:

```text
10.244.0.0/16
```

The actual ranges depend on the cluster configuration.

---

## 23. What is a Service CIDR?

Service CIDR is the IP address range used for virtual Service IPs.

Example:

```text
10.96.0.0/12
```

The actual range depends on cluster configuration.

---

# 5. kube-proxy

## 24. What is kube-proxy?

kube-proxy is a Kubernetes component that helps implement Service networking on Nodes.

Depending on configuration, it can use mechanisms such as:

* iptables
* IPVS

Modern Kubernetes networking implementations may also use other approaches depending on the environment and CNI.

---

## 25. What does kube-proxy do?

Conceptually:

```text
Client
  |
  ↓
Service IP
  |
  ↓
Service forwarding/load balancing
  |
  ↓
Pod
```

It helps direct Service traffic toward backend Pods.

---

## 26. How do you check kube-proxy?

In many clusters:

```bash
kubectl get pods -n kube-system
```

Look for:

```text
kube-proxy
```

You can inspect it using:

```bash
kubectl get daemonset -n kube-system
```

---

# 6. NetworkPolicy

## 27. What is NetworkPolicy?

NetworkPolicy controls network traffic between Pods and/or between Pods and other network endpoints, subject to the capabilities of the cluster's networking implementation.

It can control:

* Ingress
* Egress
* Source Pods
* Destination Pods
* Namespaces
* Ports

---

## 28. What is ingress traffic?

Ingress means traffic coming **into** a Pod.

Example:

```text
Client
  |
  ↓
Backend Pod
```

The traffic entering the backend is ingress traffic.

---

## 29. What is egress traffic?

Egress means traffic going **out of** a Pod.

Example:

```text
Backend Pod
    |
    ↓
Database
```

The traffic leaving the backend Pod is egress traffic.

---

## 30. Does creating a NetworkPolicy always block traffic?

No.

NetworkPolicy enforcement depends on the cluster's networking implementation.

The CNI must support NetworkPolicy enforcement.

---

# 7. Port Concepts

## 31. What is `port` in a Kubernetes Service?

`port` is the port exposed by the Service.

Example:

```yaml
ports:
  - port: 80
```

Clients can connect to the Service on port `80`.

---

## 32. What is `targetPort`?

`targetPort` is the port on the backend Pod/container that receives the traffic.

Example:

```yaml
port: 80
targetPort: 8080
```

Traffic flow:

```text
Client
  |
  ↓
Service:80
  |
  ↓
Pod:8080
```

---

## 33. What happens if `targetPort` is wrong?

The Service may exist and have endpoints, but traffic can fail because it is sent to the wrong port.

Example:

```text
Service
80
 ↓
Pod
8080

Application actually listens on:
80
```

Result:

```text
Connection refused
```

or another connectivity failure.

---

# 8. Port Forwarding

## 34. What is `kubectl port-forward`?

`kubectl port-forward` creates a temporary connection from your local machine to a Kubernetes Pod or Service.

Example:

```bash
kubectl port-forward svc/backend-service 8080:80
```

Then:

```bash
curl http://localhost:8080
```

---

## 35. Is port-forward a production load-balancing solution?

No.

Port forwarding is primarily useful for:

* Development
* Debugging
* Testing
* Temporary access

---

# 9. Ingress

## 36. What is Kubernetes Ingress?

Ingress is an API mechanism for routing external HTTP/HTTPS traffic to Services.

Conceptually:

```text
Internet
   |
   ↓
Ingress
   |
   +------ /api ------> API Service
   |
   +------ /web ------> Web Service
```

---

## 37. Does creating an Ingress automatically make it work?

Not necessarily.

You generally need an Ingress controller or another implementation that processes the Ingress configuration.

Examples of controllers include:

* NGINX Ingress Controller
* Traefik
* HAProxy
* cloud-provider-specific controllers

---

## 38. How do you troubleshoot an Ingress?

Check:

```bash
kubectl get ingress
```

Then:

```bash
kubectl describe ingress <name>
```

Check Services:

```bash
kubectl get svc
```

Check endpoints:

```bash
kubectl get endpoints
```

Check Pods:

```bash
kubectl get pods -o wide
```

Then check the Ingress controller's logs.

---

# 10. Docker vs Kubernetes Networking

## 39. What is the difference between Docker bridge networking and Kubernetes networking?

Docker commonly uses networks such as:

```text
bridge
host
none
overlay
```

Kubernetes introduces a cluster-wide networking model involving:

```text
Pods
Services
CNI
DNS
NetworkPolicy
Ingress
```

---

## 40. How does kind networking work?

`kind` runs Kubernetes Nodes as Docker containers.

Conceptually:

```text
Host
  |
  ↓
Docker
  |
  ↓
kind Network
  |
  ↓
Kubernetes Node
  |
  ↓
Pod Network
```

This makes kind especially useful for learning the relationship between Docker and Kubernetes networking.

---

# 11. Troubleshooting Questions

## 41. A Pod cannot reach a Service. What do you check?

Use this order:

```bash
kubectl get pods -o wide
kubectl get svc
kubectl describe svc <service>
kubectl get endpoints <service>
kubectl get endpointslices
kubectl get pods --show-labels
```

Then test DNS:

```bash
kubectl exec <client> -- nslookup <service>
```

Then test connectivity:

```bash
kubectl exec <client> -- wget -qO- http://<service>
```

---

## 42. A Service has no endpoints. What could be wrong?

Possible causes:

* Wrong Service selector
* Wrong Pod labels
* Pods are not Ready
* Pods are not Running
* Service is in the wrong namespace
* Label key/value mismatch

Check:

```bash
kubectl describe svc <service>
kubectl get pods --show-labels
kubectl get endpoints <service>
```

---

## 43. DNS works but HTTP does not. What do you check?

If:

```text
nslookup backend-service
```

works but:

```text
wget http://backend-service
```

fails, DNS may not be the problem.

Check:

* Service port
* targetPort
* EndpointSlices
* Pod readiness
* Application listening port
* NetworkPolicy
* CNI/network connectivity

---

## 44. You get `Connection refused`. What does it mean?

Usually, the destination was reachable, but nothing accepted the connection on that port.

Check:

```text
Service port
targetPort
Container listening port
Application status
```

---

## 45. You get a timeout. What could cause it?

Possible causes include:

* NetworkPolicy blocking traffic
* CNI/network problem
* Firewall
* Routing problem
* Application not responding
* Incorrect destination
* Node networking issue

---

# 12. Real-World DevOps Scenarios

## 46. Your application returns HTTP 503. How do you troubleshoot?

Start:

```bash
kubectl get pods
```

Then:

```bash
kubectl get svc
```

Then:

```bash
kubectl get endpoints
```

Then:

```bash
kubectl get endpointslices
```

Then:

```bash
kubectl describe svc <service>
```

Check Pod readiness:

```bash
kubectl describe pod <pod>
```

Then inspect logs:

```bash
kubectl logs <pod>
```

Common causes:

```text
No healthy backend Pods
Wrong selector
Readiness failure
Wrong targetPort
Ingress configuration
NetworkPolicy
```

---

## 47. Your application returns HTTP 502. What do you check?

Check the path:

```text
Client
 ↓
Ingress
 ↓
Service
 ↓
Pod
 ↓
Application
```

Inspect:

```bash
kubectl get ingress
kubectl describe ingress <name>
kubectl get svc
kubectl get endpoints
kubectl get pods
kubectl logs <pod>
```

A 502 often indicates a problem communicating with the upstream/backend, but the exact cause depends on the proxy/controller.

---

## 48. Your application returns HTTP 504. What do you check?

A 504 generally indicates a gateway/proxy timeout.

Check:

* Backend response time
* Service connectivity
* NetworkPolicy
* Pod health
* Application logs
* Ingress/controller configuration
* DNS
* Network connectivity

---

# 13. Advanced Questions

## 49. What is the Kubernetes networking model?

The core model expects:

1. Every Pod gets its own IP.
2. Pods can communicate with Pods without application-level NAT requirements.
3. Nodes can communicate with Pods.
4. Services provide stable virtual endpoints for applications.

The exact implementation is provided by the cluster's networking stack.

---

## 50. What is a network namespace?

A Linux network namespace provides an isolated networking environment.

It can have its own:

* Interfaces
* IP addresses
* Routes
* Network devices
* Sockets

Containers and Pods use Linux networking isolation mechanisms.

---

## 51. What is a veth pair?

A veth pair is a virtual Ethernet cable with two connected ends.

Conceptually:

```text
Namespace A
   |
 veth
   |
   |
 veth
   |
Namespace B
```

Container and host networking can use veth pairs to connect isolated network namespaces to the host network.

---

## 52. How does Kubernetes connect Pods to the network?

The exact implementation depends on the CNI.

Conceptually:

```text
Pod Network Namespace
        |
        ↓
Virtual Interface
        |
        ↓
CNI
        |
        ↓
Node Network
        |
        ↓
Cluster Network
```

---

## 53. What is service discovery?

Service discovery allows applications to find other applications dynamically.

Instead of hardcoding:

```text
10.96.100.20
```

an application can use:

```text
backend-service
```

This is especially useful in dynamic environments where Pods frequently change.

---

## 54. Why is DNS important in microservices?

Microservices are dynamic.

Pods can:

* Start
* Stop
* Restart
* Move between Nodes
* Scale up
* Scale down

DNS provides a stable naming mechanism.

Example:

```text
frontend
backend
database
redis
```

Applications can communicate using service names.

---

# 14. Security

## 55. How do you secure Kubernetes networking?

Important practices include:

* Use NetworkPolicies
* Restrict unnecessary exposed ports
* Use private Services where possible
* Secure Ingress with TLS
* Avoid exposing databases publicly
* Restrict administrative access
* Use least-privilege network rules
* Monitor network traffic
* Use a CNI with appropriate security features

---

## 56. Should a database be exposed using LoadBalancer?

Normally, a database should not be directly exposed to the public Internet.

A common architecture is:

```text
Internet
   |
   ↓
LoadBalancer
   |
   ↓
Ingress
   |
   ↓
Frontend/API
   |
   ↓
Internal Database Service
   |
   ↓
Database Pods
```

NetworkPolicy can further restrict which workloads can access the database.

---

# 15. Commands Interviewers Expect You to Know

### Pods

```bash
kubectl get pods -o wide
```

```bash
kubectl describe pod <pod>
```

### Services

```bash
kubectl get svc
```

```bash
kubectl describe svc <service>
```

### Endpoints

```bash
kubectl get endpoints
```

### EndpointSlices

```bash
kubectl get endpointslices
```

### DNS

```bash
kubectl exec <pod> -- nslookup <service>
```

### Testing connectivity

```bash
kubectl exec <pod> -- wget -qO- http://<service>
```

### Port forwarding

```bash
kubectl port-forward svc/<service> 8080:80
```

### NetworkPolicy

```bash
kubectl get networkpolicy
```

```bash
kubectl describe networkpolicy <policy>
```

### Ingress

```bash
kubectl get ingress
```

```bash
kubectl describe ingress <ingress>
```

### CoreDNS

```bash
kubectl get pods -n kube-system | grep coredns
```

### Nodes

```bash
kubectl get nodes -o wide
```

---

# 16. Most Important Interview Question

## Explain Kubernetes networking.

### Interview-ready answer

Kubernetes networking allows Pods, Services, Nodes, and external clients to communicate with each other.

Each Pod gets its own IP address, and the CNI provides the underlying Pod network.

Because Pod IPs are dynamic, applications normally communicate through Kubernetes Services, which provide stable IP addresses and DNS names.

Kubernetes DNS, commonly implemented by CoreDNS, provides service discovery.

Services can use types such as ClusterIP, NodePort, and LoadBalancer.

For HTTP and HTTPS traffic, Ingress can route external requests to Services.

NetworkPolicy can control allowed network traffic between workloads when supported by the networking implementation.

---

# 17. Troubleshooting Interview Answer

## Question:

A Pod cannot communicate with another application. How would you troubleshoot it?

### Answer:

I would troubleshoot from the bottom up.

First, I would check whether the Pods are running:

```bash
kubectl get pods -o wide
```

Then I would check the Service:

```bash
kubectl get svc
kubectl describe svc <service>
```

Then I would verify the Service has endpoints:

```bash
kubectl get endpoints <service>
kubectl get endpointslices
```

Next, I would verify that the Service selector matches the Pod labels:

```bash
kubectl get pods --show-labels
```

Then I would test DNS:

```bash
kubectl exec <client> -- nslookup <service>
```

Then I would test HTTP or TCP connectivity.

Finally, I would check:

* NetworkPolicy
* CNI
* Pod readiness
* Application logs
* Ports
* targetPort
* Node networking

---

# 18. Kubernetes Networking Mental Model

Remember this architecture:

```text
                         INTERNET
                            |
                            ↓
                      LoadBalancer
                            |
                            ↓
                         Ingress
                            |
                            ↓
                         Service
                            |
                            ↓
                     EndpointSlice
                            |
              +-------------+-------------+
              |             |             |
              ↓             ↓             ↓
            Pod 1         Pod 2         Pod 3
              |
              ↓
             CNI
              |
              ↓
        Node Networking
              |
              ↓
        Cluster Networking
```

DNS:

```text
Application
    |
    ↓
Service Name
    |
    ↓
CoreDNS
    |
    ↓
Service IP
    |
    ↓
Backend Pods
```

Security:

```text
Frontend
   |
   | allowed
   ↓
Backend
   |
   | allowed
   ↓
Database

Frontend
   |
   X
Database
```

---

# 19. Top 15 Questions to Memorize

Before your interview, make sure you can answer these:

1. What is Kubernetes networking?
2. What is a Pod IP?
3. Why are Pod IPs not normally used directly?
4. What is a Service?
5. What is ClusterIP?
6. What is NodePort?
7. What is LoadBalancer?
8. What is CoreDNS?
9. What is CNI?
10. What is kube-proxy?
11. What is EndpointSlice?
12. What is NetworkPolicy?
13. What is Ingress?
14. How does Pod-to-Pod communication work?
15. How do you troubleshoot a Service that is not reachable?

---

# 20. Final Interview Checklist

Before considering Kubernetes Networking interview-ready, you should be able to explain:

```text
✓ Pod networking
✓ Pod IP
✓ Service
✓ ClusterIP
✓ NodePort
✓ LoadBalancer
✓ Endpoint
✓ EndpointSlice
✓ CoreDNS
✓ Service DNS
✓ CNI
✓ kube-proxy
✓ NetworkPolicy
✓ Ingress
✓ port
✓ targetPort
✓ Port forwarding
✓ Network namespaces
✓ veth
✓ kind networking
✓ Docker + Kubernetes networking
✓ DNS troubleshooting
✓ Service troubleshooting
✓ 502 troubleshooting
✓ 503 troubleshooting
✓ 504 troubleshooting
✓ NetworkPolicy troubleshooting
```

---

# 21. Final Rule to Remember

When troubleshooting Kubernetes networking, think:

```text
DNS
 ↓
Service
 ↓
Selector
 ↓
Endpoints
 ↓
EndpointSlice
 ↓
Pod
 ↓
Port
 ↓
Application
 ↓
NetworkPolicy
 ↓
CNI
 ↓
Node
```

This sequence gives you a systematic approach instead of randomly changing configurations.

---

# 22. Chapter 31 Complete

The Kubernetes Networking chapter should now contain:

```text
31-Kubernetes-Networking/
├── README.md
├── notes.md
├── commands.md
├── practical-lab.md
└── interview-questions.md
```

You have now connected:

```text
Linux Networking
       ↓
Docker Networking
       ↓
Kubernetes Networking
```

This is an important foundation for:

```text
AWS Networking
Kubernetes
DevOps
Cloud
DevSecOps
SRE
Platform Engineering
```
