# Kubernetes Networking — Practical Lab

This lab provides hands-on practice with Kubernetes networking.

You will work with:

* Pods
* Pod IPs
* Services
* ClusterIP
* DNS
* EndpointSlices
* NodePort
* NetworkPolicy
* Ingress concepts
* Port forwarding
* Kubernetes networking troubleshooting
* kind networking

---

# 1. Prerequisites

Make sure these commands work:

```bash
kubectl version --client
```

```bash
kubectl cluster-info
```

```bash
kubectl get nodes
```

If you are using `kind`:

```bash
kind get clusters
```

---

# 2. Create a Lab Namespace

Create:

```bash
kubectl create namespace networking-lab
```

Verify:

```bash
kubectl get namespace networking-lab
```

Set the namespace for easier commands:

```bash
kubectl config set-context --current --namespace=networking-lab
```

Verify:

```bash
kubectl config view --minify --output 'jsonpath={..namespace}'; echo
```

Expected:

```text
networking-lab
```

---

# 3. Create a Backend Pod

Create a simple NGINX Pod:

```bash
kubectl run backend \
  --image=nginx \
  --port=80
```

Check:

```bash
kubectl get pods
```

Wait until:

```text
STATUS
Running
```

---

# 4. Check Pod IP

Run:

```bash
kubectl get pods -o wide
```

Example:

```text
NAME      READY   STATUS    IP            NODE
backend   1/1     Running   10.244.0.10   node1
```

The IP is the Pod IP.

---

# 5. Describe the Pod

```bash
kubectl describe pod backend
```

Look for:

```text
IP
Node
Containers
Ports
Events
```

---

# 6. Check Pod Network Configuration

Enter the Pod:

```bash
kubectl exec -it backend -- sh
```

Inside the container:

```bash
cat /etc/resolv.conf
```

Then exit:

```bash
exit
```

If the NGINX image does not contain `ip`, do not worry. Minimal production images often contain only the tools needed to run the application.

---

# 7. Create a Service

Expose the backend Pod:

```bash
kubectl expose pod backend \
  --name=backend-service \
  --port=80 \
  --target-port=80
```

Check:

```bash
kubectl get svc
```

You should see:

```text
backend-service
```

---

# 8. Inspect the Service

```bash
kubectl describe svc backend-service
```

Look for:

```text
Type
ClusterIP
Port
TargetPort
Selector
Endpoints
```

---

# 9. Check Service Selector

Run:

```bash
kubectl get svc backend-service -o yaml
```

Find:

```yaml
selector:
  run: backend
```

Now check the Pod labels:

```bash
kubectl get pods --show-labels
```

The Service selector should match the Pod labels.

---

# 10. Check Service IP

```bash
kubectl get svc backend-service
```

Example:

```text
NAME              TYPE        CLUSTER-IP      PORT(S)
backend-service   ClusterIP   10.96.100.10    80/TCP
```

The ClusterIP is the Service's virtual IP.

---

# 11. Check Endpoints

Run:

```bash
kubectl get endpoints backend-service
```

You should see the backend Pod IP and port.

Example:

```text
NAME              ENDPOINTS
backend-service   10.244.0.10:80
```

---

# 12. Check EndpointSlices

Run:

```bash
kubectl get endpointslices
```

You can filter by Service:

```bash
kubectl get endpointslices \
  -l kubernetes.io/service-name=backend-service
```

Describe one:

```bash
kubectl describe endpointslice <name>
```

---

# 13. Create a Client Pod

Create a temporary BusyBox client:

```bash
kubectl run client \
  --image=busybox \
  --restart=Never \
  --command -- sleep 3600
```

Check:

```bash
kubectl get pods -o wide
```

You should now have:

```text
backend
client
```

---

# 14. Test DNS

Enter the client:

```bash
kubectl exec -it client -- sh
```

Run:

```bash
nslookup backend-service
```

You should receive a DNS response.

---

# 15. Test Kubernetes Service DNS

Inside the client:

```bash
nslookup backend-service.networking-lab
```

Then:

```bash
nslookup backend-service.networking-lab.svc.cluster.local
```

These demonstrate Kubernetes Service DNS naming.

Exit:

```bash
exit
```

---

# 16. Test Service Connectivity

Run:

```bash
kubectl exec client -- wget -qO- http://backend-service
```

Expected result:

```text
NGINX HTML response
```

You have now demonstrated:

```text
Client Pod
    |
    ↓
Kubernetes DNS
    |
    ↓
Service
    |
    ↓
Backend Pod
    |
    ↓
NGINX
```

---

# 17. Test Using Service Port

```bash
kubectl exec client -- wget -qO- http://backend-service:80
```

Port `80` is the Service port.

---

# 18. Test Using Full DNS Name

```bash
kubectl exec client -- wget -qO- \
  http://backend-service.networking-lab.svc.cluster.local
```

---

# 19. Test Pod IP Directly

First find the Pod IP:

```bash
kubectl get pod backend -o wide
```

Suppose the IP is:

```text
10.244.0.10
```

Test:

```bash
kubectl exec client -- wget -qO- http://10.244.0.10
```

This demonstrates direct Pod-to-Pod communication.

---

# 20. Compare Pod IP and Service

You have now tested:

### Direct Pod access

```text
Client
  |
  ↓
Pod IP
  |
  ↓
Backend Pod
```

### Service access

```text
Client
  |
  ↓
Service DNS
  |
  ↓
Service
  |
  ↓
Backend Pod
```

The Service approach is preferred for stable application communication.

---

# 21. Scale the Backend

Convert the Pod into a Deployment:

First remove the standalone Pod:

```bash
kubectl delete pod backend
```

Create a Deployment:

```bash
kubectl create deployment backend \
  --image=nginx \
  --replicas=3
```

Check:

```bash
kubectl get pods -o wide
```

You should see three backend Pods.

---

# 22. Check the Service

The Service still exists:

```bash
kubectl get svc
```

Check endpoints:

```bash
kubectl get endpoints backend-service
```

You should see multiple backend endpoints.

Example:

```text
10.244.0.11:80
10.244.0.12:80
10.244.0.13:80
```

---

# 23. Test Load Distribution

Run:

```bash
kubectl get endpoints backend-service
```

The Service now has multiple backend Pods.

Architecture:

```text
                 Service
                    |
          +---------+---------+
          |         |         |
          ↓         ↓         ↓
        Pod 1     Pod 2     Pod 3
```

---

# 24. Check Deployment

```bash
kubectl get deployment
```

Detailed:

```bash
kubectl describe deployment backend
```

---

# 25. Check Backend Pods

```bash
kubectl get pods \
  -l app=backend \
  -o wide
```

Depending on the Deployment labels, verify the correct selector with:

```bash
kubectl get pods --show-labels
```

---

# 26. Test DNS Again

```bash
kubectl exec client -- nslookup backend-service
```

Then:

```bash
kubectl exec client -- wget -qO- http://backend-service
```

The Service continues to provide a stable endpoint even though the backend now has multiple Pods.

---

# 27. Delete One Backend Pod

Find a backend Pod:

```bash
kubectl get pods
```

Delete one:

```bash
kubectl delete pod <backend-pod-name>
```

Watch:

```bash
kubectl get pods -w
```

The Deployment creates a replacement Pod.

---

# 28. Observe Endpoint Changes

Before deletion:

```bash
kubectl get endpoints backend-service
```

After deletion:

```bash
kubectl get endpoints backend-service
```

Also:

```bash
kubectl get endpointslices
```

The backend endpoint list changes as Pods are created and removed.

This demonstrates why Services are useful.

---

# 29. Test NodePort

Create a new NodePort Service:

```bash
kubectl expose deployment backend \
  --name=backend-nodeport \
  --type=NodePort \
  --port=80 \
  --target-port=80
```

Check:

```bash
kubectl get svc
```

You should see a NodePort.

Example:

```text
backend-nodeport   NodePort   10.96.x.x   80:30xxx/TCP
```

---

# 30. Find the NodePort

Run:

```bash
kubectl get svc backend-nodeport
```

Or:

```bash
kubectl describe svc backend-nodeport
```

Look for:

```text
NodePort
```

---

# 31. NodePort with kind

If you are using `kind`, do not assume that the NodePort is directly reachable from your host exactly like a cloud or bare-metal Kubernetes Node.

Check your kind configuration and Node container networking.

Inspect:

```bash
kind get clusters
```

Then:

```bash
docker ps
```

And:

```bash
docker network inspect kind
```

For local testing, `kubectl port-forward` is often simpler.

---

# 32. Port Forward the Service

Run:

```bash
kubectl port-forward svc/backend-service 8080:80
```

Keep this terminal running.

Open another terminal:

```bash
curl http://localhost:8080
```

You should receive the NGINX response.

---

# 33. Port Forward Architecture

```text
Your Computer
     |
localhost:8080
     |
     ↓
kubectl port-forward
     |
     ↓
Kubernetes Service
     |
     ↓
Backend Pod
```

---

# 34. Troubleshoot Port Conflict

If you see:

```text
address already in use
```

check:

```bash
ss -lntp | grep :8080
```

Or:

```bash
sudo lsof -i :8080
```

Use another port:

```bash
kubectl port-forward svc/backend-service 8081:80
```

Then:

```bash
curl http://localhost:8081
```

---

# 35. Test Service From Inside the Cluster

Run:

```bash
kubectl exec client -- wget -qO- http://backend-service
```

If this works but:

```bash
curl http://localhost:8080
```

does not work, the problem may be related to port forwarding or the local host port rather than Kubernetes Service networking.

---

# 36. Test DNS Failure Scenario

Try resolving a fake Service:

```bash
kubectl exec client -- nslookup does-not-exist
```

You should receive a DNS failure.

This demonstrates:

```text
DNS name
    ↓
Service does not exist
    ↓
DNS lookup fails
```

---

# 37. Test Wrong Service Port

Try:

```bash
kubectl exec client -- wget -qO- http://backend-service:9999
```

This should fail because NGINX is not exposed through Service port `9999`.

This demonstrates the importance of correct port configuration.

---

# 38. Inspect Service Configuration

```bash
kubectl get svc backend-service -o yaml
```

Study:

```yaml
ports:
```

and:

```yaml
selector:
```

---

# 39. Test Service Selector

Get labels:

```bash
kubectl get pods --show-labels
```

Get selector:

```bash
kubectl describe svc backend-service
```

Compare:

```text
Service selector
       ↓
Pod labels
```

---

# 40. Create a Second Namespace

```bash
kubectl create namespace test-network
```

Create a client there:

```bash
kubectl run client \
  -n test-network \
  --image=busybox \
  --restart=Never \
  --command -- sleep 3600
```

Check:

```bash
kubectl get pods -n test-network
```

---

# 41. Cross-Namespace DNS

From the `test-network` client:

```bash
kubectl exec -n test-network client -- \
  nslookup backend-service.networking-lab.svc.cluster.local
```

This demonstrates cross-namespace Service discovery.

---

# 42. Cross-Namespace HTTP Test

```bash
kubectl exec -n test-network client -- \
  wget -qO- http://backend-service.networking-lab.svc.cluster.local
```

If networking and DNS are working, the request should reach the backend Service.

---

# 43. NetworkPolicy Lab

First check whether NetworkPolicies already exist:

```bash
kubectl get networkpolicy -A
```

For a clean learning environment, create policies carefully and remove them after testing.

---

# 44. Create a Deny-All Ingress Policy

Create:

```bash
cat > deny-all.yaml <<'EOF'
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all-backend
  namespace: networking-lab
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
    - Ingress
EOF
```

Apply:

```bash
kubectl apply -f deny-all.yaml
```

Check:

```bash
kubectl get networkpolicy
```

---

# 45. Test NetworkPolicy

Try:

```bash
kubectl exec client -- wget -T 5 -qO- http://backend-service
```

Depending on whether your cluster's networking implementation enforces NetworkPolicy, the request may now be blocked.

This is an important point:

**NetworkPolicy requires an implementation that supports enforcement.**

The Kubernetes API object existing does not by itself guarantee that traffic is blocked.

---

# 46. Allow Client to Backend

Create:

```bash
cat > allow-client.yaml <<'EOF'
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-client-to-backend
  namespace: networking-lab
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
    - Ingress
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: networking-lab
          podSelector:
            matchLabels:
              run: client
      ports:
        - protocol: TCP
          port: 80
EOF
```

Apply:

```bash
kubectl apply -f allow-client.yaml
```

Check:

```bash
kubectl get networkpolicy
```

---

# 47. Test the Allow Rule

```bash
kubectl exec client -- wget -T 5 -qO- http://backend-service
```

If your CNI supports NetworkPolicy enforcement, traffic from the selected client Pod to backend port `80` should be allowed.

---

# 48. Check NetworkPolicy

```bash
kubectl describe networkpolicy deny-all-backend
```

Then:

```bash
kubectl describe networkpolicy allow-client-to-backend
```

Understand:

```text
Pod selector
     ↓
Source selector
     ↓
Allowed port
```

---

# 49. Test the Cross-Namespace Client

The client in `test-network` should not match the namespace selector from the previous allow rule.

Test:

```bash
kubectl exec -n test-network client -- \
  wget -T 5 -qO- \
  http://backend-service.networking-lab.svc.cluster.local
```

If NetworkPolicy is enforced, this traffic should be denied.

This demonstrates namespace-based network segmentation.

---

# 50. Inspect CoreDNS

```bash
kubectl get pods -n kube-system
```

Find CoreDNS:

```bash
kubectl get pods -n kube-system | grep coredns
```

Check its Service:

```bash
kubectl get svc -n kube-system
```

---

# 51. Test Kubernetes DNS

```bash
kubectl exec client -- nslookup kubernetes.default
```

Expected:

```text
Name:
kubernetes.default
```

This confirms basic Kubernetes DNS functionality.

---

# 52. Inspect Pod DNS Configuration

```bash
kubectl exec client -- cat /etc/resolv.conf
```

Study:

```text
nameserver
search
options
```

The search domains explain why shorter names such as:

```text
backend-service
```

can resolve.

---

# 53. Check All Networking Resources

Run:

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
kubectl get networkpolicy
```

---

# 54. Complete Service Troubleshooting Lab

Pretend the user reports:

> "The backend application is not reachable."

Start with:

```bash
kubectl get pods -o wide
```

Then:

```bash
kubectl get svc
```

Then:

```bash
kubectl describe svc backend-service
```

Then:

```bash
kubectl get endpoints backend-service
```

Then:

```bash
kubectl get endpointslices
```

Then:

```bash
kubectl get pods --show-labels
```

Then test DNS:

```bash
kubectl exec client -- nslookup backend-service
```

Then test HTTP:

```bash
kubectl exec client -- wget -qO- http://backend-service
```

---

# 55. Complete DNS Troubleshooting Lab

Start:

```bash
kubectl exec client -- cat /etc/resolv.conf
```

Then:

```bash
kubectl exec client -- nslookup kubernetes.default
```

Then:

```bash
kubectl exec client -- nslookup backend-service
```

Then:

```bash
kubectl get pods -n kube-system | grep coredns
```

Then:

```bash
kubectl get svc -n kube-system
```

---

# 56. Complete NetworkPolicy Troubleshooting Lab

Check:

```bash
kubectl get networkpolicy -A
```

Then:

```bash
kubectl describe networkpolicy -n networking-lab
```

Check:

```text
Pod selector
Ingress
Egress
Ports
Namespace selectors
Pod selectors
```

Then test from:

```text
Client Pod
```

and:

```text
Cross-Namespace Client
```

---

# 57. Kind Networking Investigation

If your cluster is a kind cluster:

```bash
kind get clusters
```

Check Docker containers:

```bash
docker ps
```

Find the kind Node containers.

Then:

```bash
docker network ls
```

Inspect:

```bash
docker network inspect kind
```

---

# 58. Enter a Kind Node

Find a Node:

```bash
docker ps --format 'table {{.Names}}\t{{.Image}}'
```

Then:

```bash
docker exec -it <kind-node> bash
```

Inside:

```bash
ip addr
```

Check routes:

```bash
ip route
```

Check listening ports:

```bash
ss -lntp
```

Exit:

```bash
exit
```

---

# 59. Observe Docker + Kubernetes Networking

For kind:

```text
Host
 |
 ↓
Docker
 |
 ↓
kind Docker Network
 |
 +-------------+-------------+
 |                           |
 ↓                           ↓
Kubernetes Node          Kubernetes Node
 |                           |
 ↓                           ↓
Pods                        Pods
```

This connects your knowledge from:

```text
Chapter 29 → Linux Networking
Chapter 30 → Docker Networking
Chapter 31 → Kubernetes Networking
```

---

# 60. Troubleshooting Scenario 1 — DNS Failure

### Problem

```text
curl: Could not resolve host
```

### Investigation

```bash
kubectl exec client -- nslookup backend-service
```

Then:

```bash
kubectl get pods -n kube-system | grep coredns
```

Then:

```bash
kubectl get svc -n kube-system
```

### Possible causes

* CoreDNS problem
* Wrong Service name
* Wrong namespace
* DNS configuration issue

---

# 61. Troubleshooting Scenario 2 — Service Has No Endpoints

### Problem

```text
Service exists but traffic does not reach Pods.
```

Check:

```bash
kubectl get endpoints backend-service
```

Then:

```bash
kubectl describe svc backend-service
```

Then:

```bash
kubectl get pods --show-labels
```

### Possible causes

```text
Wrong selector
Wrong labels
Pod not Ready
Pod not Running
Wrong namespace
```

---

# 62. Troubleshooting Scenario 3 — Wrong targetPort

Suppose:

```yaml
port: 80
targetPort: 8080
```

but the application listens on:

```text
80
```

Traffic becomes:

```text
Client
 ↓
Service:80
 ↓
Pod:8080
 ↓
Nothing listening
```

Result:

```text
Connection refused / timeout
```

Fix the Service or application port configuration.

---

# 63. Troubleshooting Scenario 4 — NetworkPolicy

### Problem

The Service works before applying a NetworkPolicy but fails afterward.

Check:

```bash
kubectl get networkpolicy
```

Then:

```bash
kubectl describe networkpolicy <policy>
```

Verify:

```text
Source
Destination
Port
Protocol
Namespace
Pod selector
```

---

# 64. Troubleshooting Scenario 5 — Ingress

If using an Ingress, trace:

```text
Client
 ↓
DNS
 ↓
LoadBalancer
 ↓
Ingress Controller
 ↓
Ingress Rule
 ↓
Service
 ↓
EndpointSlice
 ↓
Pod
 ↓
Application
```

Commands:

```bash
kubectl get ingress
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

---

# 65. Final Practical Challenge

Build this architecture:

```text
                     Client
                       |
                       ↓
                  Client Pod
                       |
                       ↓
                backend-service
                       |
             +---------+---------+
             |         |         |
             ↓         ↓         ↓
          Backend1  Backend2  Backend3
             |
             ↓
         NetworkPolicy
```

Requirements:

* Create a namespace.
* Create a backend Deployment.
* Use 3 replicas.
* Create a ClusterIP Service.
* Verify Pod IPs.
* Verify Service IP.
* Verify EndpointSlices.
* Verify DNS.
* Create a client Pod.
* Access the backend through DNS.
* Access the backend through Service IP.
* Scale the Deployment.
* Delete one Pod.
* Observe endpoint changes.
* Create a NetworkPolicy.
* Test allowed traffic.
* Test denied traffic.
* Troubleshoot deliberately broken configuration.

---

# 66. Challenge Commands

Check:

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
kubectl get networkpolicy
```

DNS:

```bash
kubectl exec client -- nslookup backend-service
```

HTTP:

```bash
kubectl exec client -- wget -qO- http://backend-service
```

Scale:

```bash
kubectl scale deployment backend --replicas=5
```

Verify:

```bash
kubectl get pods -o wide
```

Verify endpoints:

```bash
kubectl get endpoints backend-service
```

---

# 67. Cleanup

Delete the NetworkPolicies:

```bash
kubectl delete networkpolicy deny-all-backend allow-client-to-backend
```

Delete the NodePort:

```bash
kubectl delete svc backend-nodeport
```

Delete the Deployment:

```bash
kubectl delete deployment backend
```

Delete the Services:

```bash
kubectl delete svc backend-service
```

Delete the client:

```bash
kubectl delete pod client
```

Delete the second namespace:

```bash
kubectl delete namespace test-network
```

Delete the lab namespace:

```bash
kubectl delete namespace networking-lab
```

Restore your original namespace if needed:

```bash
kubectl config set-context --current --namespace=default
```

---

# 68. Final Verification

Check:

```bash
kubectl get namespaces
```

Check all Pods:

```bash
kubectl get pods -A
```

Check Services:

```bash
kubectl get svc -A
```

Make sure your temporary lab resources are removed.

---

# 69. What You Practiced

You have practiced:

```text
✓ Pod IP
✓ Pod networking
✓ Service
✓ ClusterIP
✓ NodePort
✓ Service selectors
✓ Endpoints
✓ EndpointSlices
✓ Kubernetes DNS
✓ CoreDNS
✓ Cross-namespace DNS
✓ Service connectivity
✓ Port forwarding
✓ NetworkPolicy
✓ Network isolation
✓ Deployment scaling
✓ Pod replacement
✓ kind networking
✓ Docker + Kubernetes networking
✓ Troubleshooting
```

---

# 70. Final Architecture

You have now connected the major networking concepts:

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
             +--------------+--------------+
             |              |              |
             ↓              ↓              ↓
           Pod 1          Pod 2          Pod 3
             |
             ↓
            CNI
             |
             ↓
       Node Networking
             |
             ↓
       Cluster Networking
             |
             ↓
           DNS
             |
          CoreDNS
```

And security:

```text
Frontend
   |
   ↓
Backend
   |
   ↓
Database

NetworkPolicy:
Frontend → Backend ✓
Backend → Database ✓
Frontend → Database ✗
```

---

# 71. Interview Practice

After completing this lab, answer these without looking at your notes:

### Question 1

How does a Pod communicate with another Pod?

### Question 2

Why should you not normally use Pod IPs directly?

### Question 3

What problem does a Service solve?

### Question 4

What is the difference between ClusterIP and NodePort?

### Question 5

How does Kubernetes DNS help applications?

### Question 6

What is CoreDNS?

### Question 7

What is CNI?

### Question 8

What is kube-proxy?

### Question 9

What is an EndpointSlice?

### Question 10

How would you troubleshoot a Service with no endpoints?

### Question 11

How would you troubleshoot a DNS failure?

### Question 12

How would you troubleshoot a 503 from an Ingress?

### Question 13

What is NetworkPolicy?

### Question 14

What is the difference between ingress and egress traffic?

### Question 15

How does networking in kind involve Docker networking?

---

# 72. Final Troubleshooting Mental Model

Memorize this:

```text
User
 ↓
DNS
 ↓
LoadBalancer
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

For internal communication:

```text
Pod A
 ↓
Service DNS
 ↓
Service
 ↓
EndpointSlice
 ↓
Pod B
```

When something fails:

```text
DNS
 ↓
Service
 ↓
Selector
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

This is the Kubernetes networking troubleshooting workflow you should remember for real DevOps work and interviews.
