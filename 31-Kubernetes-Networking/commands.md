# Kubernetes Networking — Commands

This file contains the most important Kubernetes networking commands for **learning, daily DevOps work, troubleshooting, and interviews**.

---

# 1. Check Kubernetes Cluster

## Check cluster information

```bash
kubectl cluster-info
```

Shows the Kubernetes control-plane and cluster service information.

---

## Check Kubernetes version

```bash
kubectl version
```

Or:

```bash
kubectl version --short
```

Depending on the kubectl version, the `--short` option may not be available.

---

## Check Nodes

```bash
kubectl get nodes
```

Detailed:

```bash
kubectl get nodes -o wide
```

---

# 2. Check Pods

## List Pods

```bash
kubectl get pods
```

All namespaces:

```bash
kubectl get pods -A
```

With networking information:

```bash
kubectl get pods -o wide
```

Specific namespace:

```bash
kubectl get pods -n <namespace>
```

Example:

```bash
kubectl get pods -n default
```

---

# 3. Inspect a Pod

```bash
kubectl describe pod <pod-name>
```

Example:

```bash
kubectl describe pod nginx
```

Useful for checking:

* Pod IP
* Node
* Events
* Containers
* Ports
* Network-related errors

---

# 4. Get Pod IP

```bash
kubectl get pods -o wide
```

Example:

```text
NAME     READY   STATUS    IP            NODE
nginx    1/1     Running   10.244.0.10   node1
```

The `IP` column shows the Pod IP.

---

# 5. Get Pod IP Using JSONPath

```bash
kubectl get pod <pod-name> -o jsonpath='{.status.podIP}'
```

Example:

```bash
kubectl get pod nginx -o jsonpath='{.status.podIP}'
```

---

# 6. Get Pod Node

```bash
kubectl get pod <pod-name> -o wide
```

Or:

```bash
kubectl get pod <pod-name> -o jsonpath='{.spec.nodeName}'
```

---

# 7. Check Pod Labels

```bash
kubectl get pods --show-labels
```

Specific Pod:

```bash
kubectl get pod <pod-name> --show-labels
```

This is extremely useful when troubleshooting Service selectors.

---

# 8. Check Pod Network Namespace

Enter the Pod:

```bash
kubectl exec -it <pod-name> -- sh
```

Then:

```bash
ip addr
```

If `ip` is not installed, use a suitable troubleshooting image/container.

Check routes:

```bash
ip route
```

Check DNS:

```bash
cat /etc/resolv.conf
```

---

# 9. Execute Networking Commands in a Pod

```bash
kubectl exec <pod-name> -- ip addr
```

```bash
kubectl exec <pod-name> -- ip route
```

```bash
kubectl exec <pod-name> -- cat /etc/resolv.conf
```

If the image contains the required commands.

---

# 10. Create a Temporary Network Troubleshooting Pod

A simple BusyBox Pod:

```bash
kubectl run network-test \
  --rm -it \
  --image=busybox \
  --restart=Never \
  -- sh
```

Inside:

```bash
ip addr
```

```bash
ip route
```

```bash
cat /etc/resolv.conf
```

```bash
nslookup kubernetes.default
```

BusyBox is useful for basic network testing, although it does not contain every diagnostic utility.

---

# 11. Create a Curl Testing Pod

```bash
kubectl run curl-test \
  --rm -it \
  --image=curlimages/curl \
  --restart=Never \
  -- sh
```

Test a Service:

```bash
curl http://backend
```

Test a port:

```bash
curl http://backend:8080
```

Test a full DNS name:

```bash
curl http://backend.default.svc.cluster.local
```

---

# 12. Create a Netcat Testing Pod

If you need `nc`:

```bash
kubectl run netcat-test \
  --rm -it \
  --image=busybox \
  --restart=Never \
  -- sh
```

Then:

```bash
nc -vz backend 8080
```

---

# 13. List Services

```bash
kubectl get svc
```

All namespaces:

```bash
kubectl get svc -A
```

Detailed:

```bash
kubectl get svc -o wide
```

Specific namespace:

```bash
kubectl get svc -n <namespace>
```

---

# 14. Describe a Service

```bash
kubectl describe svc <service-name>
```

Example:

```bash
kubectl describe svc backend
```

Check:

* Service type
* ClusterIP
* Ports
* TargetPort
* Selector
* Endpoints

---

# 15. Get Service YAML

```bash
kubectl get svc <service-name> -o yaml
```

Example:

```bash
kubectl get svc backend -o yaml
```

This is useful when you need to inspect the complete configuration.

---

# 16. Get Service ClusterIP

```bash
kubectl get svc <service-name> \
  -o jsonpath='{.spec.clusterIP}'
```

Example:

```bash
kubectl get svc backend \
  -o jsonpath='{.spec.clusterIP}'
```

---

# 17. Get Service Ports

```bash
kubectl get svc <service-name>
```

For detailed information:

```bash
kubectl describe svc <service-name>
```

Look for:

```text
Port
TargetPort
NodePort
```

---

# 18. Check Service Selectors

```bash
kubectl describe svc <service-name>
```

Look for:

```text
Selector: app=backend
```

Then compare with:

```bash
kubectl get pods --show-labels
```

The labels need to match the Service selector appropriately.

---

# 19. Endpoints

List Endpoints:

```bash
kubectl get endpoints
```

Specific Service:

```bash
kubectl get endpoints <service-name>
```

Example:

```bash
kubectl get endpoints backend
```

---

# 20. EndpointSlice

List EndpointSlices:

```bash
kubectl get endpointslices
```

All namespaces:

```bash
kubectl get endpointslices -A
```

Detailed:

```bash
kubectl describe endpointslice <name>
```

---

# 21. Find EndpointSlices for a Service

First:

```bash
kubectl get endpointslices
```

Then inspect:

```bash
kubectl describe endpointslice <name>
```

You can also use labels:

```bash
kubectl get endpointslices \
  -l kubernetes.io/service-name=<service-name>
```

---

# 22. Test Service DNS

Start a temporary Pod:

```bash
kubectl run dns-test \
  --rm -it \
  --image=busybox \
  --restart=Never \
  -- sh
```

Then:

```bash
nslookup backend
```

---

# 23. Test Kubernetes DNS

```bash
kubectl run dns-test \
  --rm -it \
  --image=busybox \
  --restart=Never \
  -- nslookup kubernetes.default
```

A successful result confirms basic Kubernetes DNS resolution.

---

# 24. Test Fully Qualified DNS Name

```bash
kubectl run dns-test \
  --rm -it \
  --image=busybox \
  --restart=Never \
  -- nslookup backend.default.svc.cluster.local
```

---

# 25. Check Pod DNS Configuration

```bash
kubectl exec <pod-name> -- cat /etc/resolv.conf
```

Typical Kubernetes configuration includes a cluster DNS server and search domains.

---

# 26. Check CoreDNS

```bash
kubectl get pods -n kube-system
```

Filter:

```bash
kubectl get pods -n kube-system | grep coredns
```

---

# 27. Check CoreDNS Service

```bash
kubectl get svc -n kube-system
```

Find:

```text
kube-dns
```

or the DNS Service configured by the cluster.

---

# 28. Describe CoreDNS

```bash
kubectl describe deployment coredns -n kube-system
```

Depending on the cluster, the exact resource may differ.

---

# 29. Check CoreDNS Logs

```bash
kubectl logs -n kube-system deployment/coredns
```

If CoreDNS is deployed under a different resource name, find it first:

```bash
kubectl get deployments -n kube-system
```

---

# 30. Check DNS from a Pod

```bash
kubectl exec -it <pod-name> -- nslookup kubernetes.default
```

If `nslookup` is unavailable, use a temporary DNS testing Pod.

---

# 31. Test Service Connectivity

From a temporary curl Pod:

```bash
kubectl run curl-test \
  --rm -it \
  --image=curlimages/curl \
  --restart=Never \
  -- curl http://backend
```

---

# 32. Test Service Port

```bash
kubectl run curl-test \
  --rm -it \
  --image=curlimages/curl \
  --restart=Never \
  -- curl http://backend:8080
```

---

# 33. Test Pod IP Directly

First find the Pod IP:

```bash
kubectl get pods -o wide
```

Then:

```bash
kubectl run curl-test \
  --rm -it \
  --image=curlimages/curl \
  --restart=Never \
  -- curl http://<pod-ip>:8080
```

This helps distinguish:

```text
Service problem
```

from:

```text
Pod/application problem
```

---

# 34. Test Service vs Pod

If:

```text
Pod IP works
```

but:

```text
Service does not work
```

investigate:

* Service selector
* Service port
* targetPort
* EndpointSlice
* kube-proxy/CNI
* NetworkPolicy

---

# 35. Check Nodes

```bash
kubectl get nodes
```

Detailed:

```bash
kubectl get nodes -o wide
```

Describe:

```bash
kubectl describe node <node-name>
```

---

# 36. Check Node Addresses

```bash
kubectl get nodes -o wide
```

You may see:

```text
INTERNAL-IP
EXTERNAL-IP
```

depending on the cluster.

---

# 37. Check Node Conditions

```bash
kubectl describe node <node-name>
```

Look for:

```text
Conditions
```

Important conditions include:

* Ready
* MemoryPressure
* DiskPressure
* PIDPressure
* NetworkUnavailable

---

# 38. Check Ingress

```bash
kubectl get ingress
```

All namespaces:

```bash
kubectl get ingress -A
```

Detailed:

```bash
kubectl describe ingress <ingress-name>
```

---

# 39. Get Ingress YAML

```bash
kubectl get ingress <ingress-name> -o yaml
```

Check:

* Hosts
* Paths
* Backend Services
* TLS
* Rules

---

# 40. Check Ingress Controller

List all Pods:

```bash
kubectl get pods -A
```

Search for controller-related Pods:

```bash
kubectl get pods -A | grep -i ingress
```

The exact namespace and resource names depend on the installed controller.

---

# 41. Check NetworkPolicies

```bash
kubectl get networkpolicy
```

All namespaces:

```bash
kubectl get networkpolicy -A
```

---

# 42. Describe NetworkPolicy

```bash
kubectl describe networkpolicy <policy-name>
```

Check:

* Pod selector
* Ingress rules
* Egress rules
* Ports
* Protocols
* Namespace selectors

---

# 43. Get NetworkPolicy YAML

```bash
kubectl get networkpolicy <policy-name> -o yaml
```

---

# 44. Check All Important Networking Resources

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
kubectl get ingress
```

```bash
kubectl get networkpolicy
```

---

# 45. Get Everything in a Namespace

```bash
kubectl get all
```

Specific namespace:

```bash
kubectl get all -n <namespace>
```

Note: `kubectl get all` is a convenient view but does not literally include every Kubernetes resource type.

---

# 46. Check Events

Events are extremely useful during troubleshooting.

```bash
kubectl get events
```

Newest events:

```bash
kubectl get events --sort-by=.lastTimestamp
```

Namespace:

```bash
kubectl get events -n <namespace> --sort-by=.lastTimestamp
```

---

# 47. Describe Pod Events

```bash
kubectl describe pod <pod-name>
```

Look at:

```text
Events
```

This can reveal:

* Scheduling problems
* Container failures
* Image errors
* Mount problems
* Networking-related events

---

# 48. Check Application Logs

```bash
kubectl logs <pod-name>
```

Follow logs:

```bash
kubectl logs -f <pod-name>
```

Specific container:

```bash
kubectl logs <pod-name> -c <container-name>
```

---

# 49. Check Previous Container Logs

If a container crashed:

```bash
kubectl logs <pod-name> --previous
```

This is useful for CrashLoopBackOff troubleshooting.

---

# 50. Port Forward

Forward local port to a Pod:

```bash
kubectl port-forward pod/<pod-name> 8080:80
```

Example:

```bash
kubectl port-forward pod/nginx 8080:80
```

Then:

```bash
curl http://localhost:8080
```

---

# 51. Port Forward a Service

```bash
kubectl port-forward svc/<service-name> 8080:80
```

Example:

```bash
kubectl port-forward svc/backend 8080:80
```

Then:

```bash
curl http://localhost:8080
```

This is useful for testing a Service without exposing it externally.

---

# 52. Check Port Availability on Linux

On the Kubernetes Node or your Linux host:

```bash
ss -lntp
```

Check a specific port:

```bash
ss -lntp | grep :8080
```

Another useful command:

```bash
sudo lsof -i :8080
```

---

# 53. Check Linux Routes

On a Linux Node:

```bash
ip route
```

Check interfaces:

```bash
ip addr
```

Check links:

```bash
ip link
```

---

# 54. Check Linux Network Connections

```bash
ss -tuln
```

Detailed:

```bash
ss -tulnp
```

This can help identify applications listening on ports.

---

# 55. Check ARP / Neighbor Table

```bash
ip neigh
```

This can help troubleshoot local Layer 2 connectivity.

---

# 56. Check DNS from Linux

```bash
cat /etc/resolv.conf
```

Test:

```bash
getent hosts example.com
```

If available:

```bash
dig example.com
```

---

# 57. Check Kubernetes DNS Configuration

Inside a Pod:

```bash
cat /etc/resolv.conf
```

Important fields:

```text
nameserver
search
options
```

---

# 58. Curl Headers

Test HTTP:

```bash
curl -I http://backend
```

Verbose:

```bash
curl -v http://backend
```

This helps inspect:

* DNS resolution
* Connection
* HTTP status
* Response headers

---

# 59. Curl HTTPS

```bash
curl -v https://example.com
```

Check TLS connection:

```bash
curl -Iv https://example.com
```

---

# 60. Check TCP Port with Netcat

```bash
nc -vz <host> <port>
```

Example:

```bash
nc -vz backend 8080
```

Possible result:

```text
succeeded
```

or:

```text
connection refused
```

---

# 61. Network Troubleshooting Sequence

Use this order:

```text
1. Pod
2. Pod IP
3. Service
4. Service selector
5. EndpointSlice
6. DNS
7. Port
8. Application
9. NetworkPolicy
10. CNI
11. Node
```

Commands:

```bash
kubectl get pods -o wide
```

```bash
kubectl get svc
```

```bash
kubectl describe svc <service>
```

```bash
kubectl get endpoints <service>
```

```bash
kubectl get endpointslices
```

```bash
kubectl get networkpolicy
```

---

# 62. Troubleshooting: Service Has No Endpoints

Run:

```bash
kubectl get endpoints <service>
```

If empty:

```bash
kubectl get pods --show-labels
```

Then:

```bash
kubectl describe svc <service>
```

Check:

```text
Service selector
        ↓
Pod labels
```

They must match appropriately.

---

# 63. Troubleshooting: DNS Failure

Run:

```bash
kubectl get pods -n kube-system
```

Check CoreDNS.

Then:

```bash
kubectl run dns-test \
  --rm -it \
  --image=busybox \
  --restart=Never \
  -- nslookup kubernetes.default
```

Then test your Service:

```bash
kubectl run dns-test \
  --rm -it \
  --image=busybox \
  --restart=Never \
  -- nslookup <service-name>
```

---

# 64. Troubleshooting: Connection Refused

Possible causes:

```text
Wrong port
Wrong targetPort
Application not running
Application listening on another port
Service configuration problem
```

Check:

```bash
kubectl get svc
```

```bash
kubectl describe svc <service>
```

```bash
kubectl get pods -o wide
```

```bash
kubectl logs <pod>
```

---

# 65. Troubleshooting: Connection Timeout

Possible causes:

```text
NetworkPolicy
CNI
Routing
Node networking
Firewall
Application not responding
```

Check:

```bash
kubectl get networkpolicy -A
```

```bash
kubectl get nodes -o wide
```

```bash
kubectl get pods -o wide
```

---

# 66. Troubleshooting: 503 Service Unavailable

Trace:

```text
Ingress
 ↓
Service
 ↓
EndpointSlice
 ↓
Pod
```

Commands:

```bash
kubectl get ingress
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
kubectl get pods -o wide
```

---

# 67. Troubleshooting: 502 Bad Gateway

Check:

```bash
kubectl describe ingress <ingress>
```

Then:

```bash
kubectl describe svc <service>
```

Then:

```bash
kubectl get endpoints <service>
```

Finally test the backend directly:

```bash
curl http://<service>:<port>
```

---

# 68. Check Namespace

A very common mistake is using the wrong namespace.

List namespaces:

```bash
kubectl get namespaces
```

Check Pods:

```bash
kubectl get pods -n <namespace>
```

Check Services:

```bash
kubectl get svc -n <namespace>
```

Remember:

```text
Pod in namespace A
```

and:

```text
Service in namespace B
```

are not automatically the same application environment.

---

# 69. Test Cross-Namespace DNS

Suppose:

```text
Service:
backend

Namespace:
production
```

Use:

```text
backend.production
```

or:

```text
backend.production.svc.cluster.local
```

Test:

```bash
kubectl run dns-test \
  --rm -it \
  --image=busybox \
  --restart=Never \
  -- nslookup backend.production.svc.cluster.local
```

---

# 70. Check Service Account / Pod Configuration

Networking can sometimes be affected by application configuration.

Inspect:

```bash
kubectl describe pod <pod>
```

Get YAML:

```bash
kubectl get pod <pod> -o yaml
```

Check:

* Container ports
* Environment variables
* Readiness probes
* Liveness probes
* DNS policy
* Host networking

---

# 71. Check HostNetwork

Get Pod YAML:

```bash
kubectl get pod <pod> -o yaml
```

Look for:

```yaml
hostNetwork: true
```

A Pod using host networking behaves differently from a normal Pod network namespace.

---

# 72. Check DNS Policy

Get:

```bash
kubectl get pod <pod> -o yaml
```

Look for:

```yaml
dnsPolicy:
```

Common default:

```text
ClusterFirst
```

The actual DNS policy depends on Pod configuration.

---

# 73. Check Pod Network Configuration

```bash
kubectl get pod <pod> -o yaml
```

Useful fields include:

```text
status.podIP
status.podIPs
spec.hostNetwork
spec.dnsPolicy
```

---

# 74. Watch Pod Networking Changes

```bash
kubectl get pods -o wide -w
```

The `-w` option watches for changes.

Useful when Pods are:

* Restarting
* Getting new IP addresses
* Moving through lifecycle states

---

# 75. Watch Services

```bash
kubectl get svc -w
```

Useful while creating or modifying Services.

---

# 76. Watch EndpointSlices

```bash
kubectl get endpointslices -w
```

This can help observe backend endpoint changes.

---

# 77. Check Kubernetes Resources as YAML

Pod:

```bash
kubectl get pod <pod> -o yaml
```

Service:

```bash
kubectl get svc <service> -o yaml
```

Ingress:

```bash
kubectl get ingress <ingress> -o yaml
```

NetworkPolicy:

```bash
kubectl get networkpolicy <policy> -o yaml
```

---

# 78. Kind Networking

If using a `kind` cluster:

```bash
kind get clusters
```

Check:

```bash
docker ps
```

You may see Kubernetes Node containers.

Inspect networks:

```bash
docker network ls
```

Inspect the kind network:

```bash
docker network inspect kind
```

The exact Docker network configuration can vary with the kind setup.

---

# 79. Kind Node Containers

List:

```bash
docker ps
```

Enter a kind Node:

```bash
docker exec -it <kind-node> bash
```

Then inspect:

```bash
ip addr
```

```bash
ip route
```

```bash
ss -lntp
```

This is useful for understanding the relationship between:

```text
Docker Networking
```

and:

```text
Kubernetes Networking
```

---

# 80. Inspect Docker Network

On a kind-based cluster:

```bash
docker network ls
```

Then:

```bash
docker network inspect kind
```

This helps visualize the Docker-level network containing kind Nodes.

---

# 81. Kubernetes + Docker Networking Mental Model

For a kind cluster:

```text
Host
 |
 ↓
Docker Network
 |
 +------------------+
 |                  |
 ↓                  ↓
Kind Node 1       Kind Node 2
 |                  |
 ↓                  ↓
Kubernetes        Kubernetes
Pods              Pods
```

This is especially useful when troubleshooting local Kubernetes networking.

---

# 82. Useful One-Liners

## Pods with IPs

```bash
kubectl get pods -o wide
```

## Services

```bash
kubectl get svc
```

## Endpoints

```bash
kubectl get endpoints
```

## EndpointSlices

```bash
kubectl get endpointslices
```

## Nodes

```bash
kubectl get nodes -o wide
```

## Ingress

```bash
kubectl get ingress
```

## NetworkPolicies

```bash
kubectl get networkpolicy -A
```

## Recent events

```bash
kubectl get events --sort-by=.lastTimestamp
```

---

# 83. Complete Kubernetes Network Health Check

Run:

```bash
kubectl get nodes -o wide
```

```bash
kubectl get pods -A -o wide
```

```bash
kubectl get svc -A
```

```bash
kubectl get endpoints -A
```

```bash
kubectl get endpointslices -A
```

```bash
kubectl get ingress -A
```

```bash
kubectl get networkpolicy -A
```

Then:

```bash
kubectl get pods -n kube-system
```

---

# 84. Quick Service Troubleshooting

When:

```text
Service is not working
```

run:

```bash
kubectl get svc <service>
```

```bash
kubectl describe svc <service>
```

```bash
kubectl get endpoints <service>
```

```bash
kubectl get endpointslices
```

```bash
kubectl get pods --show-labels
```

Then test:

```bash
kubectl run curl-test \
  --rm -it \
  --image=curlimages/curl \
  --restart=Never \
  -- curl http://<service>:<port>
```

---

# 85. Quick DNS Troubleshooting

```bash
kubectl get pods -n kube-system | grep coredns
```

```bash
kubectl get svc -n kube-system
```

```bash
kubectl run dns-test \
  --rm -it \
  --image=busybox \
  --restart=Never \
  -- nslookup kubernetes.default
```

Then:

```bash
kubectl run dns-test \
  --rm -it \
  --image=busybox \
  --restart=Never \
  -- nslookup <service>
```

---

# 86. Quick Ingress Troubleshooting

```bash
kubectl get ingress -A
```

```bash
kubectl describe ingress <ingress>
```

```bash
kubectl get svc
```

```bash
kubectl get endpoints
```

```bash
kubectl get pods -o wide
```

Then test the backend Service directly.

---

# 87. Quick NetworkPolicy Troubleshooting

```bash
kubectl get networkpolicy -A
```

```bash
kubectl describe networkpolicy <policy>
```

Check:

```text
Pod selector
Ingress
Egress
Ports
Namespaces
```

Then test connectivity from an appropriate client Pod.

---

# 88. Most Important Commands to Memorize

If you are preparing for a DevOps interview, memorize these first:

```bash
kubectl get pods -o wide
```

```bash
kubectl get svc
```

```bash
kubectl describe svc <service>
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
kubectl get ingress
```

```bash
kubectl get networkpolicy
```

```bash
kubectl exec -it <pod> -- sh
```

```bash
kubectl logs <pod>
```

```bash
kubectl get events --sort-by=.lastTimestamp
```

```bash
kubectl port-forward svc/<service> 8080:80
```

```bash
kubectl run dns-test --rm -it --image=busybox --restart=Never -- nslookup kubernetes.default
```

---

# 89. DevOps Troubleshooting Flow

Use this mental model:

```text
                    USER REPORTS
                    "Application
                     is not working"
                           |
                           ↓
                    Check Pod Status
                           |
                           ↓
                    Check Pod IP
                           |
                           ↓
                    Check Service
                           |
                           ↓
                  Check Service Selector
                           |
                           ↓
                   Check EndpointSlice
                           |
                           ↓
                      Test DNS
                           |
                           ↓
                    Test TCP / HTTP
                           |
                           ↓
                  Check Application Port
                           |
                           ↓
                  Check NetworkPolicy
                           |
                           ↓
                       Check CNI
                           |
                           ↓
                     Check Node
```

---

# 90. Final Kubernetes Networking Cheat Sheet

| Requirement     | Command                                       |
| --------------- | --------------------------------------------- |
| List Pods       | `kubectl get pods`                            |
| Pod IPs         | `kubectl get pods -o wide`                    |
| Pod details     | `kubectl describe pod <pod>`                  |
| Pod labels      | `kubectl get pods --show-labels`              |
| List Services   | `kubectl get svc`                             |
| Service details | `kubectl describe svc <service>`              |
| Endpoints       | `kubectl get endpoints`                       |
| EndpointSlices  | `kubectl get endpointslices`                  |
| Nodes           | `kubectl get nodes -o wide`                   |
| Ingress         | `kubectl get ingress`                         |
| NetworkPolicy   | `kubectl get networkpolicy`                   |
| DNS Pods        | `kubectl get pods -n kube-system`             |
| Pod shell       | `kubectl exec -it <pod> -- sh`                |
| Logs            | `kubectl logs <pod>`                          |
| Events          | `kubectl get events --sort-by=.lastTimestamp` |
| Port forward    | `kubectl port-forward svc/<svc> 8080:80`      |
| Test DNS        | `nslookup <service>`                          |
| Test HTTP       | `curl http://<service>`                       |
| Linux IPs       | `ip addr`                                     |
| Linux routes    | `ip route`                                    |
| Linux ports     | `ss -lntp`                                    |
| Kind Nodes      | `docker ps`                                   |
| Kind network    | `docker network inspect kind`                 |

---

# 91. Final Command Flow

For any Kubernetes networking problem, start here:

```bash
kubectl get pods -o wide
```

```bash
kubectl get svc
```

```bash
kubectl describe svc <service>
```

```bash
kubectl get endpoints <service>
```

```bash
kubectl get endpointslices
```

```bash
kubectl get pods --show-labels
```

Then test DNS:

```bash
kubectl run dns-test \
  --rm -it \
  --image=busybox \
  --restart=Never \
  -- nslookup <service>
```

Then test HTTP:

```bash
kubectl run curl-test \
  --rm -it \
  --image=curlimages/curl \
  --restart=Never \
  -- curl http://<service>:<port>
```

Then investigate:

```text
NetworkPolicy
      ↓
CNI
      ↓
Node
      ↓
Linux Networking
```

---

# 92. Golden Rule

Never troubleshoot Kubernetes networking by randomly running commands.

Always follow:

```text
POD
 ↓
SERVICE
 ↓
SELECTOR
 ↓
ENDPOINTS
 ↓
DNS
 ↓
PORT
 ↓
APPLICATION
 ↓
NETWORK POLICY
 ↓
CNI
 ↓
NODE
```

This systematic approach is one of the most important skills for a professional DevOps Engineer.
