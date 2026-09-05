# Kubernetes Networking

Kubernetes Networking explains how Pods, Services, Nodes, and external clients communicate inside and outside a Kubernetes cluster.

Kubernetes networking is one of the most important topics for a **DevOps / Cloud / Kubernetes Engineer** because many real-world issues involve:

* Pod-to-Pod communication
* Service discovery
* DNS
* Services
* ClusterIP
* NodePort
* LoadBalancer
* Ingress
* Network Policies
* CNI
* kube-proxy
* CoreDNS
* Troubleshooting

---

# 1. Learning Objectives

By completing this chapter, you will understand:

* Kubernetes networking fundamentals
* Pod networking
* Pod IP addresses
* Pod-to-Pod communication
* Node networking
* Services
* ClusterIP
* NodePort
* LoadBalancer
* ExternalName
* Kubernetes DNS
* CoreDNS
* kube-proxy
* CNI
* Network namespaces
* Network policies
* Ingress networking
* Internal and external traffic
* Kubernetes networking troubleshooting

---

# 2. Why Kubernetes Networking Is Important

A Kubernetes application normally contains multiple components.

Example:

```text
User
 |
 ↓
Ingress
 |
 ↓
Frontend Service
 |
 ↓
Frontend Pods
 |
 ↓
Backend Service
 |
 ↓
Backend Pods
 |
 ↓
Database Service
 |
 ↓
Database Pod
```

Every component needs reliable networking.

---

# 3. Kubernetes Networking Model

Kubernetes follows several important networking principles.

A simplified model is:

```text
Pod A
  |
  | Pod IP
  ↓
Pod B
```

Pods should generally be able to communicate with other Pods without requiring NAT between Pods.

Services provide a stable virtual endpoint in front of changing Pods.

```text
Client
  |
  ↓
Service
  |
  +------ Pod
  |
  +------ Pod
  |
  +------ Pod
```

---

# 4. Kubernetes Networking Architecture

A simplified architecture:

```text
                         INTERNET
                            |
                            ↓
                    LoadBalancer / Ingress
                            |
                            ↓
                         Service
                            |
                  +---------+---------+
                  |         |         |
                  ↓         ↓         ↓
                Pod       Pod       Pod
                  |
                Node
                  |
                  ↓
                CNI
                  |
                  ↓
              Node Network
```

---

# 5. Main Kubernetes Networking Components

Important components include:

| Component     | Purpose                             |
| ------------- | ----------------------------------- |
| Pod           | Application networking unit         |
| Service       | Stable access to Pods               |
| CoreDNS       | DNS/service discovery               |
| kube-proxy    | Service traffic handling            |
| CNI           | Pod network implementation          |
| Ingress       | HTTP/HTTPS entry point              |
| NetworkPolicy | Traffic control                     |
| Node          | Runs Pods and networking components |

---

# 6. Pod Networking

Every Pod normally receives its own IP address.

Example:

```text
Pod 1 → 10.244.0.10
Pod 2 → 10.244.0.11
Pod 3 → 10.244.0.12
```

Pods can communicate using their Pod IPs according to the cluster's networking implementation.

---

# 7. Pod-to-Pod Communication

Example:

```text
Pod A
10.244.0.10
    |
    ↓
Kubernetes Network
    |
    ↓
Pod B
10.244.0.11
```

The exact implementation depends on the cluster's CNI.

---

# 8. Pod IPs Are Not Stable

Pod IP addresses can change when Pods are recreated.

For example:

```text
Before:
backend → 10.244.0.10
```

After recreation:

```text
backend → 10.244.0.25
```

Therefore, applications should normally communicate through a **Service** rather than hardcoding Pod IPs.

---

# 9. Kubernetes Service

A Service provides a stable network endpoint for a group of Pods.

Example:

```text
                 backend-service
                       |
             +---------+---------+
             |         |         |
             ↓         ↓         ↓
          Pod 1      Pod 2      Pod 3
```

Pods can be replaced while the Service remains available.

---

# 10. Service Discovery

Instead of using:

```text
10.244.0.10
```

an application can use:

```text
backend-service
```

Kubernetes DNS resolves the Service name.

Example:

```text
frontend
   |
   ↓
backend-service
   |
   ↓
Backend Pods
```

---

# 11. Kubernetes Service Types

Common Service types:

```text
ClusterIP
NodePort
LoadBalancer
ExternalName
```

---

# 12. ClusterIP

ClusterIP is the default Service type.

It provides internal access within the cluster.

Example:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: backend
spec:
  type: ClusterIP
  selector:
    app: backend
  ports:
    - port: 80
      targetPort: 8080
```

Architecture:

```text
Frontend Pod
     |
     ↓
backend Service
     |
     ↓
Backend Pods
```

---

# 13. NodePort

NodePort exposes a Service through a port on Kubernetes Nodes.

Example:

```yaml
spec:
  type: NodePort
```

Architecture:

```text
External Client
      |
      ↓
NodeIP:NodePort
      |
      ↓
Service
      |
      ↓
Pod
```

---

# 14. LoadBalancer

LoadBalancer exposes a Service through an external load balancer when supported by the cluster/cloud environment.

Example:

```yaml
spec:
  type: LoadBalancer
```

Architecture:

```text
Internet
   |
   ↓
Cloud Load Balancer
   |
   ↓
Service
   |
   ↓
Pods
```

---

# 15. ExternalName

ExternalName maps a Service name to an external DNS name.

Example:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: external-db
spec:
  type: ExternalName
  externalName: database.example.com
```

This does not create a normal Pod-backed Service.

---

# 16. Kubernetes DNS

Kubernetes provides DNS-based service discovery.

For example:

```text
backend
```

can resolve to the backend Service.

A fully qualified Service DNS name can look like:

```text
backend.default.svc.cluster.local
```

The exact namespace and cluster domain depend on cluster configuration.

---

# 17. CoreDNS

CoreDNS is commonly used to provide DNS services inside Kubernetes clusters.

It helps applications discover:

* Services
* Service IPs
* Cluster DNS records

Check CoreDNS:

```bash
kubectl get pods -n kube-system
```

Look for CoreDNS Pods.

---

# 18. kube-proxy

`kube-proxy` is a Kubernetes component involved in implementing Service networking.

It can configure node-level networking rules so traffic sent to a Service can reach the appropriate backend Pods.

Depending on the Kubernetes environment and configuration, implementations can use mechanisms such as:

```text
iptables
IPVS
nftables
```

Do not assume every modern Kubernetes cluster uses exactly the same mechanism.

---

# 19. CNI

CNI stands for:

**Container Network Interface**

CNI provides the networking implementation used by Kubernetes.

Examples of CNI implementations include:

* Cilium
* Calico
* Flannel
* Antrea

CNI is responsible for implementing networking behavior such as:

* Pod connectivity
* IP assignment
* Network interfaces
* Routing
* Network policies, depending on the implementation

---

# 20. Kubernetes Network Namespace

Pods use Linux network namespaces.

Containers in the same Pod share the Pod's network namespace.

This means containers inside the same Pod can communicate using:

```text
localhost
```

Example:

```text
Pod
 |
 +-- Container A
 |
 +-- Container B
```

Container A can communicate with Container B using:

```text
localhost:<port>
```

if the application is listening on the appropriate port.

---

# 21. Containers Inside the Same Pod

Example:

```text
Pod
+-----------------------+
|                       |
| Container A           |
| localhost:8080        |
|                       |
| Container B           |
| localhost:9090        |
|                       |
+-----------------------+
```

Both containers share:

* Network namespace
* Pod IP
* Network interfaces

---

# 22. Pod-to-Service Communication

Typical application flow:

```text
Frontend Pod
     |
     ↓
backend.default.svc.cluster.local
     |
     ↓
Backend Service
     |
     ↓
Backend Pod
```

This is much more reliable than using Pod IP addresses directly.

---

# 23. Service Selectors

A Service normally selects Pods using labels.

Example Pod:

```yaml
metadata:
  labels:
    app: backend
```

Service:

```yaml
spec:
  selector:
    app: backend
```

The Service can then route traffic to matching Pods.

---

# 24. Endpoints and EndpointSlices

Kubernetes needs to know which backend Pods are associated with a Service.

Modern Kubernetes commonly uses **EndpointSlices** for this purpose.

Check:

```bash
kubectl get endpoints
```

And:

```bash
kubectl get endpointslices
```

These objects represent backend endpoints associated with Services.

---

# 25. Service Traffic Flow

A simplified flow:

```text
Client Pod
    |
    ↓
Service
    |
    ↓
Service routing
    |
    ↓
Selected Pod
```

The exact packet path depends on:

* CNI
* kube-proxy implementation
* Node placement
* Cluster configuration

---

# 26. Ingress

Ingress provides HTTP/HTTPS routing into a Kubernetes cluster.

Example:

```text
Internet
   |
   ↓
Ingress Controller
   |
   +--------+
   |        |
   ↓        ↓
Frontend  Backend
Service   Service
```

Ingress can route based on:

* Hostname
* URL path

Example:

```text
example.com/
        ↓
frontend

example.com/api
        ↓
backend
```

---

# 27. Ingress Controller

An Ingress resource by itself does not normally implement the actual proxying.

An **Ingress Controller** watches Ingress resources and implements the routing behavior.

Examples include controllers based on:

* NGINX
* Traefik
* HAProxy
* cloud-provider implementations

---

# 28. NetworkPolicy

NetworkPolicy controls which traffic is allowed between Pods and other network endpoints.

Example concept:

```text
Frontend
   |
   ↓ allowed
Backend
   |
   ↓ allowed
Database
```

But:

```text
Frontend
   X
   ↓ denied
Database
```

NetworkPolicy support depends on the networking implementation.

---

# 29. Kubernetes Networking Security

A secure architecture may look like:

```text
Internet
   |
   ↓
Ingress
   |
   ↓
Frontend
   |
   ↓
Backend
   |
   ↓
Database
```

Network policies can restrict unnecessary communication.

For example:

```text
Frontend → Backend ✓
Backend → Database ✓
Frontend → Database ✗
```

---

# 30. Kubernetes Networking vs Docker Networking

Docker:

```text
Container
    |
Docker Network
    |
Host
```

Kubernetes:

```text
Pod
    |
CNI
    |
Node Network
    |
Cluster Network
```

Kubernetes networking is designed for a distributed cluster containing multiple Nodes.

---

# 31. Kubernetes Networking Across Nodes

Example:

```text
Node 1                         Node 2

Pod A                          Pod B
10.244.1.10                    10.244.2.10
   |                               |
   +---------- CNI Network --------+
```

The CNI is responsible for providing the required connectivity.

---

# 32. Node Network

Each Kubernetes Node has its own network interfaces and IP address.

Check:

```bash
kubectl get nodes -o wide
```

This shows Node information including IP addresses.

On the Linux Node:

```bash
ip addr
```

and:

```bash
ip route
```

can be used to inspect networking.

---

# 33. Pod Network CIDR

A Kubernetes cluster generally uses a Pod CIDR or equivalent address allocation mechanism.

Example:

```text
Pod Network:
10.244.0.0/16
```

Individual Pods may receive addresses from this range.

The exact CIDR depends on the cluster configuration.

---

# 34. Service CIDR

Kubernetes Services also use a virtual IP range.

Example:

```text
Service CIDR:
10.96.0.0/12
```

This is only an example; the actual Service CIDR depends on cluster configuration.

---

# 35. Pod Network vs Service Network

Important distinction:

```text
Pod Network
    ↓
Pod IPs
```

versus:

```text
Service Network
    ↓
Service ClusterIPs
```

Example:

```text
Pod:
10.244.0.10

Service:
10.96.0.10
```

These are different logical address spaces in a typical cluster.

---

# 36. ClusterIP Is Virtual

A ClusterIP is a stable virtual IP associated with a Service.

Example:

```text
backend
ClusterIP: 10.96.20.15
```

Applications use the Service rather than individual Pod IPs.

---

# 37. NodePort Architecture

Example:

```text
External Client
       |
       ↓
Node IP:30080
       |
       ↓
Node networking
       |
       ↓
Service
       |
       ↓
Backend Pod
```

NodePort normally uses a port from the Kubernetes NodePort range.

---

# 38. LoadBalancer Architecture

Cloud example:

```text
Internet
   |
   ↓
Cloud Load Balancer
   |
   ↓
Kubernetes Service
   |
   ↓
Pods
```

The actual implementation depends on the cloud provider and cluster setup.

---

# 39. Kubernetes DNS Example

Suppose:

```text
Service:
backend

Namespace:
production
```

A DNS name can be:

```text
backend.production.svc.cluster.local
```

From another Pod:

```bash
curl http://backend.production.svc.cluster.local
```

Shorter forms may also work depending on DNS search configuration:

```bash
curl http://backend
```

---

# 40. Kubernetes Networking Commands

Useful commands:

```bash
kubectl get pods -o wide
```

```bash
kubectl get svc
```

```bash
kubectl get endpoints
```

```bash
kubectl get endpointslices
```

```bash
kubectl get nodes -o wide
```

```bash
kubectl get networkpolicy
```

```bash
kubectl describe svc <service>
```

```bash
kubectl describe pod <pod>
```

---

# 41. Basic Networking Troubleshooting Flow

When a Pod cannot connect to another application:

```text
Pod
 ↓
Pod IP
 ↓
Network
 ↓
DNS
 ↓
Service
 ↓
EndpointSlice
 ↓
Target Pod
 ↓
Application Port
```

Check each layer.

---

# 42. Common Kubernetes Networking Problems

Common problems include:

* Service selector mismatch
* Wrong Service port
* Wrong targetPort
* Pod not Ready
* DNS failure
* NetworkPolicy blocking traffic
* CNI problem
* Incorrect Ingress configuration
* Application not listening
* Wrong namespace
* Incorrect hostname
* Node networking issue

---

# 43. Service Selector Problem

Suppose:

```yaml
selector:
  app: backend
```

But the Pod has:

```yaml
labels:
  app: api
```

The Service will not select that Pod.

Check:

```bash
kubectl get pods --show-labels
```

Then:

```bash
kubectl describe svc backend
```

---

# 44. Service Port vs TargetPort

Example:

```yaml
ports:
  - port: 80
    targetPort: 8080
```

Meaning:

```text
Service port:
80

Container application port:
8080
```

Flow:

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

# 45. DNS Troubleshooting

Check CoreDNS:

```bash
kubectl get pods -n kube-system
```

Check DNS Service:

```bash
kubectl get svc -n kube-system
```

Test from a temporary Pod:

```bash
kubectl run dns-test \
  --rm -it \
  --image=busybox \
  --restart=Never \
  -- nslookup kubernetes.default
```

---

# 46. Service Troubleshooting

Run:

```bash
kubectl get svc
```

Then:

```bash
kubectl describe svc <service-name>
```

Check endpoints:

```bash
kubectl get endpoints <service-name>
```

Also check:

```bash
kubectl get endpointslices
```

If the Service has no endpoints, investigate:

* Pod labels
* Service selector
* Pod readiness
* Namespace

---

# 47. Pod Connectivity Troubleshooting

Check:

```bash
kubectl get pods -o wide
```

Look at:

* Pod IP
* Node
* Ready status
* Status

Then inspect:

```bash
kubectl describe pod <pod-name>
```

---

# 48. Test Application Connectivity

From a client Pod:

```bash
kubectl exec -it <client-pod> -- curl http://backend
```

If curl is not available, use another diagnostic image/tool.

For DNS:

```bash
kubectl exec -it <client-pod> -- nslookup backend
```

---

# 49. NetworkPolicy Troubleshooting

Check:

```bash
kubectl get networkpolicy
```

Inspect:

```bash
kubectl describe networkpolicy <policy-name>
```

If traffic suddenly stops after applying a NetworkPolicy, verify:

* Pod selectors
* Namespace selectors
* Ingress rules
* Egress rules
* Ports
* Protocols

---

# 50. Ingress Troubleshooting

Check:

```bash
kubectl get ingress
```

Then:

```bash
kubectl describe ingress <ingress-name>
```

Check the controller:

```bash
kubectl get pods -A
```

Verify:

```text
Ingress
   ↓
Ingress Controller
   ↓
Service
   ↓
Pods
```

---

# 51. Real-World Kubernetes Architecture

A production-style application can look like:

```text
                         INTERNET
                            |
                            ↓
                    Load Balancer
                            |
                            ↓
                   Ingress Controller
                            |
                 +----------+----------+
                 |                     |
                 ↓                     ↓
          Frontend Service       Backend Service
                 |                     |
             +---+---+             +---+---+
             |       |             |       |
             ↓       ↓             ↓       ↓
           Pod     Pod            Pod     Pod
                                   |
                                   ↓
                            Database Service
                                   |
                                   ↓
                              Database Pods
```

---

# 52. DevOps Networking Responsibilities

A DevOps Engineer should be able to:

* Expose applications
* Configure Services
* Configure Ingress
* Understand DNS
* Debug Service connectivity
* Understand Pod networking
* Configure NetworkPolicies
* Troubleshoot CNI issues
* Investigate Node networking
* Analyze application ports
* Understand traffic flow

---

# 53. Kubernetes Networking Mental Model

Remember:

```text
Pod
 ↓
Pod IP
 ↓
CNI
 ↓
Node Network
 ↓
Cluster Network
```

For stable application access:

```text
Client
 ↓
Service
 ↓
EndpointSlice
 ↓
Pod
```

For HTTP/HTTPS external access:

```text
Internet
 ↓
LoadBalancer
 ↓
Ingress
 ↓
Service
 ↓
Pod
```

---

# 54. Docker → Kubernetes Networking Progression

You have now learned:

```text
Linux Networking
       ↓
Docker Networking
       ↓
Kubernetes Networking
```

Linux taught you:

```text
IP
Route
DNS
Port
Bridge
veth
Network Namespace
```

Docker applied these concepts to:

```text
Containers
Docker Networks
Docker DNS
Port Publishing
```

Kubernetes builds on them with:

```text
Pods
Services
CNI
CoreDNS
Ingress
NetworkPolicy
```

---

# 55. Important Commands Cheat Sheet

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

```bash
kubectl get endpointslices
```

### Nodes

```bash
kubectl get nodes -o wide
```

### DNS

```bash
kubectl get pods -n kube-system
```

### NetworkPolicy

```bash
kubectl get networkpolicy
```

### Ingress

```bash
kubectl get ingress
```

---

# 56. Interview Preparation

You should be able to explain:

1. What is Kubernetes networking?
2. How do Pods communicate?
3. What is a Service?
4. What is ClusterIP?
5. What is NodePort?
6. What is LoadBalancer?
7. What is Ingress?
8. What is CoreDNS?
9. What is kube-proxy?
10. What is CNI?
11. What is a Pod network?
12. What is a Service CIDR?
13. What is NetworkPolicy?
14. How does Service discovery work?
15. How do you troubleshoot a Service with no endpoints?
16. How do you troubleshoot DNS?
17. How do you troubleshoot an Ingress?
18. How do Pods communicate across Nodes?

---

# 57. Final Goal

By the end of this chapter, you should be able to look at a Kubernetes networking problem and trace the traffic:

```text
User
 ↓
DNS
 ↓
Load Balancer
 ↓
Ingress
 ↓
Service
 ↓
EndpointSlice
 ↓
Pod
 ↓
Container
 ↓
Application
```

For internal traffic:

```text
Pod A
 ↓
DNS
 ↓
Service
 ↓
EndpointSlice
 ↓
Pod B
 ↓
Application
```

And when something fails, troubleshoot from:

```text
DNS
 ↓
Service
 ↓
Endpoints
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

---

# 58. Chapter Structure

The chapter will contain:

```text
31-Kubernetes-Networking/
│
├── README.md
├── notes.md
├── commands.md
├── practical-lab.md
└── interview-questions.md
```

Each file will progressively build your Kubernetes networking knowledge.

---

# 59. Final Summary

Kubernetes networking connects:

```text
Pods
Services
Nodes
Ingress
External Clients
```

The most important concepts are:

```text
Pod IP
Service
ClusterIP
NodePort
LoadBalancer
DNS
CoreDNS
CNI
kube-proxy
Ingress
NetworkPolicy
EndpointSlice
```

The most important DevOps skill is not just knowing these terms.

It is being able to **trace traffic and troubleshoot where the connection is failing**.

```text
                    KUBERNETES NETWORKING

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
                       EndpointSlice
                       /      |      \
                      ↓       ↓       ↓
                    Pod     Pod      Pod
                      |
                     CNI
                      |
                 Node Network
                      |
                   Cluster
```

This is the foundation for advanced Kubernetes networking, service mesh, cloud networking, and production troubleshooting.
