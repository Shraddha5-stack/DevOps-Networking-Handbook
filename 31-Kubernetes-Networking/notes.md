# Kubernetes Networking — Notes

## 1. What Is Kubernetes Networking?

Kubernetes networking is the system that allows:

* Pods to communicate with Pods
* Pods to communicate with Services
* Pods to communicate with external systems
* Users to access applications
* Nodes to communicate with each other
* Applications to discover each other through DNS

A simplified architecture is:

```text
User
 |
 ↓
Ingress / LoadBalancer
 |
 ↓
Service
 |
 ↓
Pods
 |
 ↓
Containers
```

---

# 2. Why Kubernetes Networking Is Important

A Kubernetes application is rarely a single container.

A typical application may contain:

```text
Frontend
Backend
Database
Cache
Message Queue
Monitoring
```

These components must communicate reliably.

For example:

```text
Frontend
   |
   ↓
Backend
   |
   ↓
Database
```

Kubernetes networking provides the communication infrastructure required for this architecture.

---

# 3. Kubernetes Networking Model

Kubernetes follows an important networking model.

Each Pod gets an IP address.

Pods should be able to communicate with other Pods according to the cluster networking implementation.

For example:

```text
Pod A
10.244.1.10
     |
     ↓
Cluster Network
     |
     ↓
Pod B
10.244.2.20
```

The actual implementation is provided by the cluster's networking solution, usually through CNI.

---

# 4. What Is a Pod?

A Pod is the smallest deployable unit in Kubernetes.

A Pod can contain one or more containers.

Example:

```text
Pod
+-----------------------+
|                       |
| Container A           |
|                       |
| Container B           |
|                       |
+-----------------------+
```

Containers inside the same Pod share the Pod's network namespace.

---

# 5. Pod Network Namespace

Each Pod has a network namespace.

The network namespace provides an isolated networking environment containing things such as:

* Network interfaces
* IP addresses
* Routing table
* Ports
* Network configuration

Example:

```text
Pod Network Namespace
|
+-- eth0
+-- IP Address
+-- Routes
+-- Ports
```

---

# 6. Containers Inside a Pod

Containers in the same Pod share the network namespace.

Therefore they can communicate through:

```text
localhost
```

Example:

```text
Pod
|
+-- Frontend container → localhost:8080
|
+-- Sidecar container  → localhost:9090
```

The containers share the same Pod IP.

---

# 7. Pod IP Address

A Pod normally receives an IP address from the cluster's Pod network.

Example:

```text
Pod A → 10.244.0.10
Pod B → 10.244.0.11
Pod C → 10.244.0.12
```

You can view Pod IP addresses with:

```bash
kubectl get pods -o wide
```

Example:

```text
NAME       READY   STATUS    IP            NODE
frontend   1/1     Running   10.244.0.10   node1
backend    1/1     Running   10.244.0.11   node2
```

---

# 8. Pod IPs Are Ephemeral

Pod IP addresses should not normally be treated as permanent addresses.

Suppose:

```text
backend Pod
10.244.0.10
```

The Pod is deleted.

A new Pod might receive:

```text
backend Pod
10.244.0.25
```

Therefore, applications should not normally depend directly on Pod IPs.

Use a Service instead.

---

# 9. Kubernetes Service

A Service provides a stable network endpoint for a group of Pods.

Example:

```text
              backend-service
                     |
          +----------+----------+
          |          |          |
          ↓          ↓          ↓
       Pod A       Pod B       Pod C
```

The Pods may change, but the Service provides a stable access point.

---

# 10. Why Services Are Needed

Without a Service:

```text
Frontend
   |
   ↓
Pod IP
```

If the Pod is recreated, its IP may change.

With a Service:

```text
Frontend
   |
   ↓
backend-service
   |
   ↓
Backend Pods
```

The Service remains the stable endpoint.

---

# 11. Service Selector

A Service usually selects Pods using labels.

Pod:

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

The Service finds Pods whose labels match the selector.

---

# 12. Service Traffic

Suppose there are three backend Pods:

```text
backend-1
backend-2
backend-3
```

A Service can distribute traffic across the selected Pods.

```text
                  Service
                     |
          +----------+----------+
          |          |          |
          ↓          ↓          ↓
       backend-1  backend-2  backend-3
```

The exact traffic implementation depends on the Kubernetes networking setup.

---

# 13. ClusterIP

ClusterIP is the default Service type.

It provides an internal virtual IP.

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
backend:80
     |
     ↓
Backend Pod:8080
```

---

# 14. ClusterIP Is Usually Internal

A ClusterIP is intended for communication within the cluster.

Example:

```text
Frontend Pod
     |
     ↓
backend-service
     |
     ↓
Backend Pods
```

An external user normally does not connect directly to a ClusterIP.

---

# 15. NodePort

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
Node IP:NodePort
      |
      ↓
Service
      |
      ↓
Pod
```

Example:

```text
192.168.1.20:30080
```

---

# 16. LoadBalancer

LoadBalancer exposes a Service using an external load-balancing mechanism when supported by the environment.

Example:

```yaml
spec:
  type: LoadBalancer
```

Typical cloud architecture:

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

The exact behavior depends on the cloud provider and cluster implementation.

---

# 17. ExternalName

ExternalName maps a Kubernetes Service name to an external DNS name.

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

Applications can use the Kubernetes Service name instead of directly using the external hostname.

---

# 18. Service Types Summary

| Service Type | Main Purpose             |
| ------------ | ------------------------ |
| ClusterIP    | Internal cluster access  |
| NodePort     | Expose through Node port |
| LoadBalancer | External load balancer   |
| ExternalName | Map to external DNS name |

Remember:

```text
ClusterIP
   ↓
Internal

NodePort
   ↓
Node-level external access

LoadBalancer
   ↓
External load balancer

ExternalName
   ↓
External DNS name
```

---

# 19. Kubernetes DNS

Kubernetes provides DNS-based service discovery.

Instead of connecting to:

```text
10.96.20.10
```

an application can use:

```text
backend
```

or a fully qualified DNS name such as:

```text
backend.default.svc.cluster.local
```

---

# 20. DNS Structure

A typical Service DNS name is:

```text
<service>.<namespace>.svc.<cluster-domain>
```

Example:

```text
backend.production.svc.cluster.local
```

Breakdown:

```text
backend
   ↓
Service name

production
   ↓
Namespace

svc
   ↓
Service DNS zone

cluster.local
   ↓
Cluster domain
```

---

# 21. CoreDNS

CoreDNS is commonly used as the DNS server for Kubernetes clusters.

It provides service discovery for applications inside the cluster.

Check CoreDNS:

```bash
kubectl get pods -n kube-system
```

You may see:

```text
coredns-xxxxx
coredns-yyyyy
```

---

# 22. DNS Search Domains

Inside a Pod, `/etc/resolv.conf` usually contains Kubernetes DNS configuration.

Check:

```bash
kubectl exec <pod-name> -- cat /etc/resolv.conf
```

You may see search domains similar to:

```text
search default.svc.cluster.local svc.cluster.local cluster.local
```

This allows short names such as:

```text
backend
```

to resolve without typing the complete DNS name.

---

# 23. DNS Example

Suppose:

```text
Service:
backend

Namespace:
production
```

Full DNS:

```text
backend.production.svc.cluster.local
```

From another Pod:

```bash
curl http://backend.production.svc.cluster.local
```

---

# 24. DNS Troubleshooting

If a Pod cannot resolve a Service:

Check CoreDNS:

```bash
kubectl get pods -n kube-system
```

Check the Service:

```bash
kubectl get svc
```

Test DNS:

```bash
kubectl run dns-test \
  --rm -it \
  --image=busybox \
  --restart=Never \
  -- nslookup kubernetes.default
```

---

# 25. EndpointSlice

A Service needs to know which Pods are available as backends.

Kubernetes uses EndpointSlices to represent network endpoints associated with Services.

Check:

```bash
kubectl get endpointslices
```

Example:

```text
NAME              ADDRESSES
backend-xxxxx     10.244.0.10
                  10.244.0.11
                  10.244.0.12
```

---

# 26. Endpoints

You can also inspect traditional Endpoints objects:

```bash
kubectl get endpoints
```

For a specific Service:

```bash
kubectl get endpoints backend
```

If a Service has no endpoints, investigate:

* Pod labels
* Service selector
* Pod readiness
* Namespace
* Pod status

---

# 27. Service Selector Failure

Suppose the Service has:

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

Result:

```text
Service
   |
   X
   |
No backend Pods
```

Check:

```bash
kubectl get pods --show-labels
```

and:

```bash
kubectl describe svc backend
```

---

# 28. Port vs TargetPort

Consider:

```yaml
ports:
  - port: 80
    targetPort: 8080
```

This means:

```text
Service port:
80

Pod/application port:
8080
```

Traffic:

```text
Client
  |
  ↓
Service:80
  |
  ↓
Pod:8080
```

This distinction is extremely important during troubleshooting.

---

# 29. NodePort Traffic

Example:

```text
External Client
       |
       ↓
NodeIP:30080
       |
       ↓
Service
       |
       ↓
Pod:8080
```

The NodePort provides an externally reachable entry point through a Node.

---

# 30. Ingress

Ingress provides HTTP/HTTPS routing into Kubernetes.

Example:

```text
Internet
   |
   ↓
Ingress
   |
   +-------------+
   |             |
   ↓             ↓
Frontend       Backend
Service        Service
```

Ingress can route based on:

* Host
* Path

---

# 31. Host-Based Routing

Example:

```text
app.example.com
        |
        ↓
Frontend Service
```

and:

```text
api.example.com
        |
        ↓
Backend Service
```

Architecture:

```text
                  Ingress
                     |
            +--------+--------+
            |                 |
            ↓                 ↓
     app.example.com    api.example.com
            |                 |
            ↓                 ↓
       Frontend           Backend
```

---

# 32. Path-Based Routing

Example:

```text
example.com/
     ↓
frontend

example.com/api
     ↓
backend
```

This allows multiple applications to share an HTTP/HTTPS entry point.

---

# 33. Ingress Controller

An Ingress resource defines desired routing.

An Ingress Controller implements the actual routing.

Architecture:

```text
Client
  |
  ↓
Ingress Controller
  |
  ↓
Ingress Rules
  |
  +----------+
  |          |
  ↓          ↓
Service A  Service B
```

---

# 34. CNI

CNI means:

**Container Network Interface**

CNI provides the networking implementation used for containers and Pods.

Examples include:

* Cilium
* Calico
* Flannel
* Antrea

CNI implementations can provide functionality such as:

* Pod IP allocation
* Pod connectivity
* Routing
* Network interfaces
* Network policy support

The exact capabilities depend on the CNI.

---

# 35. Why Kubernetes Needs CNI

Kubernetes itself defines the networking model but relies on networking implementations to provide the underlying connectivity.

Simplified:

```text
Kubernetes
    |
    ↓
CNI
    |
    ↓
Linux Networking
    |
    ↓
Node / Cluster Network
```

---

# 36. CNI and Pod Creation

When a Pod requiring networking is created, the networking system must provide the Pod with network connectivity.

Conceptually:

```text
Pod Created
     |
     ↓
CNI Called
     |
     ↓
Network Interface Created
     |
     ↓
IP Assigned
     |
     ↓
Routes / Connectivity Configured
```

The exact implementation varies between CNI plugins.

---

# 37. kube-proxy

`kube-proxy` is a Kubernetes component involved in Service networking.

It runs on Nodes and can configure networking rules that help direct Service traffic to backend Pods.

Possible implementations include:

```text
iptables
IPVS
nftables
```

The actual mode depends on Kubernetes version and cluster configuration.

---

# 38. Service Traffic Flow

A simplified Service flow is:

```text
Client Pod
    |
    ↓
Service IP
    |
    ↓
Service routing
    |
    ↓
Backend Pod
```

The actual packet path can involve:

* kube-proxy
* CNI
* routing
* NAT
* Linux networking

---

# 39. Pod-to-Pod Communication

Example:

```text
Pod A
10.244.1.10
    |
    ↓
CNI Network
    |
    ↓
Pod B
10.244.2.20
```

If the Pods are on different Nodes, the CNI must provide the required cross-node connectivity.

---

# 40. Cross-Node Networking

Example:

```text
Node 1                         Node 2
+-----------+                  +-----------+
|           |                  |           |
| Pod A     |                  | Pod B     |
|10.244.1.10|                  |10.244.2.20|
|           |                  |           |
+-----+-----+                  +-----+-----+
      |                              |
      +--------- CNI Network --------+
```

The exact packet path depends on the CNI implementation.

---

# 41. Node Networking

Each Node has its own network interfaces.

On a Linux Node:

```bash
ip addr
```

shows interfaces and addresses.

Routing:

```bash
ip route
```

Listening ports:

```bash
ss -lntp
```

Kubernetes view:

```bash
kubectl get nodes -o wide
```

---

# 42. Pod CIDR

A cluster may allocate Pod IPs from a Pod network range.

Example:

```text
10.244.0.0/16
```

This is only an example.

The actual range depends on the cluster and CNI configuration.

---

# 43. Service CIDR

Services normally receive virtual IP addresses from a Service CIDR.

Example:

```text
10.96.0.0/12
```

Again, this is an example.

Actual configuration varies between clusters.

---

# 44. Pod CIDR vs Service CIDR

Important distinction:

```text
Pod CIDR
    ↓
Pod IP addresses
```

```text
Service CIDR
    ↓
Service ClusterIP addresses
```

Example:

```text
Pod:
10.244.0.10

Service:
10.96.0.10
```

They represent different networking concepts.

---

# 45. NetworkPolicy

NetworkPolicy controls network traffic involving selected Pods.

Example:

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

This can help implement network segmentation.

---

# 46. Ingress and Egress

NetworkPolicy can control:

### Ingress

Traffic coming **into** a Pod.

```text
Client
  |
  ↓
Pod
```

### Egress

Traffic going **out of** a Pod.

```text
Pod
 |
 ↓
Database / External Service
```

Policies may control either or both directions.

---

# 47. NetworkPolicy Example

Conceptual policy:

```text
Allow:
frontend → backend

Allow:
backend → database

Deny:
frontend → database
```

This creates a more secure architecture.

---

# 48. NetworkPolicy Selectors

Policies can select Pods using labels.

Example:

```yaml
podSelector:
  matchLabels:
    app: backend
```

This means the policy applies to Pods matching:

```text
app=backend
```

---

# 49. Namespace-Based Isolation

Applications can be separated using namespaces.

Example:

```text
development
staging
production
```

NetworkPolicies can further restrict communication between namespaces.

Example:

```text
production frontend
       |
       ↓
production backend
```

while preventing unnecessary access from development workloads.

---

# 50. Kubernetes Networking Security

A production environment should follow least-privilege networking.

Avoid:

```text
Everything → Everything
```

Prefer:

```text
Frontend → Backend
Backend → Database
Monitoring → Metrics
```

Only required traffic should be allowed.

---

# 51. Docker Networking vs Kubernetes Networking

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

Kubernetes networking operates across multiple Nodes and integrates with Services, DNS, Ingress, and NetworkPolicy.

---

# 52. Kubernetes Networking Traffic Flows

### Internal Service

```text
Pod A
 |
 ↓
Service
 |
 ↓
Pod B
```

### External HTTP

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
Service
 |
 ↓
Pod
```

### NodePort

```text
Internet
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

# 53. Kubernetes Networking Troubleshooting

When an application cannot connect, do not immediately assume the problem is Kubernetes.

Check layer by layer.

```text
DNS
 ↓
Service
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

---

# 54. Step 1 — Check Pods

```bash
kubectl get pods -o wide
```

Check:

* STATUS
* READY
* Pod IP
* Node

If the Pod is not Running or Ready, investigate it first.

---

# 55. Step 2 — Check Service

```bash
kubectl get svc
```

Then:

```bash
kubectl describe svc <service-name>
```

Check:

* Service type
* ClusterIP
* Port
* TargetPort
* Selector

---

# 56. Step 3 — Check Endpoints

```bash
kubectl get endpoints <service-name>
```

and:

```bash
kubectl get endpointslices
```

If there are no endpoints, the Service may not be selecting the intended Pods.

---

# 57. Step 4 — Check Labels

```bash
kubectl get pods --show-labels
```

Compare the Pod labels with the Service selector.

Example:

```text
Pod:
app=backend

Service:
selector:
  app=backend
```

They must match appropriately.

---

# 58. Step 5 — Test DNS

From a Pod:

```bash
kubectl exec -it <pod-name> -- nslookup backend
```

If the command does not exist in the image, use a temporary diagnostic Pod.

Example:

```bash
kubectl run dns-test \
  --rm -it \
  --image=busybox \
  --restart=Never \
  -- nslookup backend
```

---

# 59. Step 6 — Test Connectivity

If curl exists:

```bash
kubectl exec -it <pod-name> -- curl http://backend
```

Or test a specific port:

```bash
kubectl exec -it <pod-name> -- curl http://backend:8080
```

If the image does not contain curl, use a suitable diagnostic image.

---

# 60. Step 7 — Check Application Port

Check the application's listening port.

Inside a suitable diagnostic container:

```bash
ss -lnt
```

Or inspect the application configuration.

Make sure:

```text
Service port
      ↓
targetPort
      ↓
Application listening port
```

are configured correctly.

---

# 61. Step 8 — Check NetworkPolicy

```bash
kubectl get networkpolicy
```

Inspect:

```bash
kubectl describe networkpolicy <policy-name>
```

Look for:

* Ingress rules
* Egress rules
* Pod selectors
* Namespace selectors
* Ports

---

# 62. Step 9 — Check CoreDNS

```bash
kubectl get pods -n kube-system
```

Look for CoreDNS.

Check logs:

```bash
kubectl logs -n kube-system deployment/coredns
```

The exact resource name may vary.

---

# 63. Step 10 — Check CNI

Identify the networking components:

```bash
kubectl get pods -n kube-system
```

Depending on the cluster, you may see CNI-related components.

Investigate CNI logs when Pod networking itself is failing.

---

# 64. Common Error: Connection Refused

Example:

```text
curl: (7) Failed to connect
```

Possible causes:

* Application not running
* Wrong port
* Wrong targetPort
* Application listening only on an unexpected address
* Service configuration problem

Check:

```bash
kubectl get pods
kubectl get svc
kubectl describe svc <service>
```

---

# 65. Common Error: Timeout

A timeout may indicate:

* NetworkPolicy blocking traffic
* Routing problem
* CNI problem
* Node networking problem
* Firewall
* Application not responding

Do not assume every timeout is a DNS problem.

---

# 66. Common Error: DNS Failure

Symptoms:

```text
Could not resolve host
```

Check:

```bash
kubectl get pods -n kube-system
```

Then test:

```bash
nslookup backend
```

Also verify:

```bash
kubectl get svc
```

and the namespace.

---

# 67. Common Error: Service Has No Endpoints

Check:

```bash
kubectl get endpoints <service>
```

If empty, check:

```bash
kubectl get pods --show-labels
```

Compare with:

```bash
kubectl describe svc <service>
```

Typical causes:

```text
Wrong selector
Wrong namespace
Pods not Ready
Pods not running
```

---

# 68. Common Error: 502 / 503

A reverse proxy or Ingress may return:

```text
502 Bad Gateway
503 Service Unavailable
```

Possible causes:

* Service has no endpoints
* Wrong Service port
* Wrong targetPort
* Backend Pod unavailable
* Ingress configuration issue
* NetworkPolicy
* Application failure

Trace:

```text
Ingress
 ↓
Service
 ↓
EndpointSlice
 ↓
Pod
 ↓
Application
```

---

# 69. Kind Kubernetes Networking

For a local `kind` cluster, Kubernetes Nodes run as containers.

Conceptually:

```text
Host
 |
 +-------------------+
 | Docker            |
 |                   |
 | kind node         |
 | kind node         |
 | kind node         |
 +-------------------+
```

Therefore, troubleshooting may involve both:

```text
Docker Networking
```

and:

```text
Kubernetes Networking
```

This is an important connection between Chapter 30 and Chapter 31.

---

# 70. Kubernetes Networking Mental Model

Remember these layers:

```text
Application
    ↓
Container
    ↓
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

For Service access:

```text
Application
    ↓
Service DNS
    ↓
ClusterIP
    ↓
EndpointSlice
    ↓
Pod
```

For external HTTP access:

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

# 71. Most Important Commands

### Pods

```bash
kubectl get pods -o wide
```

### Services

```bash
kubectl get svc
```

### Service details

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

### Nodes

```bash
kubectl get nodes -o wide
```

### Ingress

```bash
kubectl get ingress
```

### NetworkPolicy

```bash
kubectl get networkpolicy
```

### DNS test

```bash
kubectl run dns-test \
  --rm -it \
  --image=busybox \
  --restart=Never \
  -- nslookup kubernetes.default
```

### Pod shell

```bash
kubectl exec -it <pod> -- sh
```

---

# 72. Interview Mental Model

If an interviewer asks:

**"How does a request reach a Kubernetes application?"**

A good answer is:

```text
Client
 ↓
LoadBalancer / Ingress
 ↓
Service
 ↓
EndpointSlice
 ↓
Selected Pod
 ↓
Container
 ↓
Application
```

For internal communication:

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
```

---

# 73. Important Kubernetes Networking Terms

| Term          | Meaning                                  |
| ------------- | ---------------------------------------- |
| Pod IP        | IP assigned to a Pod                     |
| Service       | Stable access point for Pods             |
| ClusterIP     | Internal virtual Service IP              |
| NodePort      | Node-level Service port                  |
| LoadBalancer  | External load-balancing Service          |
| CoreDNS       | Kubernetes DNS                           |
| CNI           | Container networking interface           |
| kube-proxy    | Component involved in Service networking |
| Ingress       | HTTP/HTTPS routing                       |
| EndpointSlice | Backend endpoint representation          |
| NetworkPolicy | Network traffic control                  |
| Pod CIDR      | Address range for Pods                   |
| Service CIDR  | Address range for Services               |

---

# 74. Kubernetes Networking vs Traditional Networking

Traditional networking often focuses on:

```text
Servers
Switches
Routers
Firewalls
IP addresses
Ports
```

Kubernetes adds abstractions:

```text
Pods
Services
Ingress
CNI
CoreDNS
EndpointSlices
NetworkPolicies
```

A DevOps Engineer needs to understand both worlds.

---

# 75. Real-World Example

Imagine an e-commerce application:

```text
                    INTERNET
                       |
                       ↓
                Load Balancer
                       |
                       ↓
                  Ingress
                       |
             +---------+---------+
             |                   |
             ↓                   ↓
       Frontend Service    Backend Service
             |                   |
          +--+--+             +--+--+
          |     |             |     |
          ↓     ↓             ↓     ↓
        Pod   Pod           Pod   Pod
                                |
                                ↓
                         Database Service
                                |
                                ↓
                           Database
```

Possible NetworkPolicy:

```text
Internet → Frontend ✓
Frontend → Backend ✓
Backend → Database ✓
Frontend → Database ✗
Internet → Database ✗
```

This is a common production security pattern.

---

# 76. Kubernetes Networking Checklist

Before considering yourself comfortable with Kubernetes networking, you should understand:

* [ ] Pod IP
* [ ] Pod network
* [ ] Network namespace
* [ ] Service
* [ ] ClusterIP
* [ ] NodePort
* [ ] LoadBalancer
* [ ] ExternalName
* [ ] Service selectors
* [ ] EndpointSlices
* [ ] Kubernetes DNS
* [ ] CoreDNS
* [ ] CNI
* [ ] kube-proxy
* [ ] Ingress
* [ ] Ingress Controller
* [ ] NetworkPolicy
* [ ] Pod CIDR
* [ ] Service CIDR
* [ ] Cross-node networking
* [ ] DNS troubleshooting
* [ ] Service troubleshooting
* [ ] Ingress troubleshooting
* [ ] NetworkPolicy troubleshooting

---

# 77. Final Mental Model

The most important thing to remember:

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
                      EndpointSlice
                            |
                  +---------+---------+
                  |         |         |
                  ↓         ↓         ↓
                 Pod       Pod       Pod
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

Internal application communication:

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
EndpointSlice
     |
     ↓
Backend Pod
     |
     ↓
Application
```

When troubleshooting, always think:

```text
DNS
 ↓
Service
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

That mental model will make Kubernetes networking troubleshooting much easier.
