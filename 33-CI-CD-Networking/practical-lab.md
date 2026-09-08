# 🔄 CI/CD Networking — Practical Lab

## Chapter 33 — CI/CD Networking

This lab gives hands-on practice with the networking used by CI/CD pipelines.

We will test:

* DNS
* Internet connectivity
* HTTPS
* Git connectivity
* Docker networking
* Container Registry connectivity
* Kubernetes networking
* AWS connectivity
* Network troubleshooting
* CI/CD-style diagnostics

---

# 🎯 Lab Objective

By completing this lab, you should understand how a CI/CD runner communicates with:

```text
Git Repository
      ↓
Package Repository
      ↓
Container Registry
      ↓
Cloud
      ↓
Kubernetes API
      ↓
Application
```

---

# 🧰 Prerequisites

You should have:

* Linux
* Git
* Docker
* kubectl
* AWS CLI
* A Kubernetes cluster such as kind
* Internet access

Check your tools:

```bash
git --version
docker --version
kubectl version --client
aws --version
curl --version
dig -v
```

If a command is missing, install it before continuing.

---

# LAB 1 — Check Your Machine Network

## Step 1 — Check Hostname

```bash
hostname
```

---

## Step 2 — Check IP Address

```bash
ip addr
```

Look for your active network interface.

Example:

```text
eth0
ens33
enp0s3
wlan0
```

---

## Step 3 — Check Routes

```bash
ip route
```

You should normally see a default route similar to:

```text
default via 192.168.1.1 dev wlan0
```

The exact values will be different on your machine.

---

## Step 4 — Check DNS Configuration

```bash
cat /etc/resolv.conf
```

---

# LAB 2 — Test DNS

## Step 1 — Resolve GitHub

```bash
dig github.com
```

---

## Step 2 — Get Only the IP

```bash
dig +short github.com
```

---

## Step 3 — Test DNS Using getent

```bash
getent hosts github.com
```

---

## Step 4 — Test Another Domain

```bash
dig google.com
```

---

## 🎯 Understand the Result

The flow is:

```text
CI Runner
    |
    | DNS Query
    v
DNS Resolver
    |
    v
IP Address
```

If DNS fails, many CI/CD operations will fail.

---

# LAB 3 — Test Internet Connectivity

## Step 1 — Test HTTPS

```bash
curl -I https://github.com
```

---

## Step 2 — Verbose Test

```bash
curl -v https://github.com
```

Observe:

```text
DNS resolution
TCP connection
TLS handshake
HTTP response
```

---

## Step 3 — Test Google

```bash
curl -I https://google.com
```

---

## Step 4 — Test TCP 443

```bash
nc -vz github.com 443
```

Expected result should indicate that the TCP connection succeeded.

---

# LAB 4 — Understand DNS vs Network Failure

Run:

```bash
dig github.com
```

Then:

```bash
curl -v https://github.com
```

Understand the difference:

```text
DNS
 ↓
Domain → IP
```

Then:

```text
Network
 ↓
IP → TCP → TLS → HTTP
```

This distinction is very important when troubleshooting CI/CD.

---

# LAB 5 — Test Git Connectivity

## Step 1 — Check Git

```bash
git --version
```

---

## Step 2 — Test GitHub HTTPS

```bash
git ls-remote https://github.com/git/git.git
```

If successful, Git can communicate with GitHub.

---

## Step 3 — Check SSH

```bash
ssh -T git@github.com
```

If you have not configured GitHub SSH authentication, this may report an authentication-related message.

The important point is that the SSH connection itself can be tested.

---

## Step 4 — Test SSH Port

```bash
nc -vz github.com 22
```

---

# LAB 6 — Analyze GitHub Connection

Run:

```bash
curl -v https://github.com
```

Look for:

```text
Connected
TLS
HTTP status
```

Now run:

```bash
git ls-remote https://github.com/git/git.git
```

Think about the network flow:

```text
Git Command
    |
    v
DNS
    |
    v
IP Address
    |
    v
TCP 443
    |
    v
TLS
    |
    v
GitHub
```

---

# LAB 7 — Docker Network

## Step 1 — Check Docker

```bash
docker version
```

---

## Step 2 — List Docker Networks

```bash
docker network ls
```

You should normally see networks such as:

```text
bridge
host
none
```

---

## Step 3 — Inspect Bridge Network

```bash
docker network inspect bridge
```

Look for:

* Subnet
* Gateway
* Containers
* IP addresses

---

# LAB 8 — Create a CI Network

Create a dedicated Docker network:

```bash
docker network create ci-network
```

Verify:

```bash
docker network ls
```

---

# LAB 9 — Start Application Container

Run nginx:

```bash
docker run -d \
  --name ci-web \
  --network ci-network \
  nginx
```

Check:

```bash
docker ps
```

---

# LAB 10 — Start Diagnostic Container

Run Alpine:

```bash
docker run -d \
  --name ci-client \
  --network ci-network \
  alpine \
  sleep 3600
```

Check:

```bash
docker ps
```

---

# LAB 11 — Test Container DNS

Enter the client:

```bash
docker exec -it ci-client sh
```

Inside the container:

```bash
cat /etc/resolv.conf
```

Docker provides internal DNS functionality for user-defined networks.

Try:

```bash
ping ci-web
```

If `ping` is unavailable, install a diagnostic package or use another diagnostic image.

---

# LAB 12 — Test Container HTTP Connectivity

From the client container, you can use a diagnostic image/tooling environment if the minimal Alpine image does not contain curl.

For example, start a temporary curl container:

```bash
docker run --rm \
  --network ci-network \
  curlimages/curl \
  http://ci-web
```

You should receive an HTTP response from nginx.

The network flow is:

```text
ci-client / curl container
          |
          | Docker DNS
          v
       ci-web
          |
          v
        nginx
```

---

# LAB 13 — Inspect Container Networking

Run:

```bash
docker inspect ci-web
```

Find:

```text
Networks
IP Address
Gateway
Network
```

You can extract the IP with:

```bash
docker inspect -f \
'{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' \
ci-web
```

---

# LAB 14 — Test Published Ports

Remove the previous container:

```bash
docker rm -f ci-web
```

Start nginx with a published port:

```bash
docker run -d \
  --name ci-web \
  --network ci-network \
  -p 8080:80 \
  nginx
```

Check:

```bash
docker ps
```

You should see:

```text
8080 → 80
```

Test:

```bash
curl http://localhost:8080
```

Network flow:

```text
Host:8080
     |
     v
Docker
     |
     v
Container:80
     |
     v
Nginx
```

---

# LAB 15 — Docker CI/CD Simulation

Imagine that a CI runner has built an application.

Run:

```bash
docker build -t myapp:1.0 .
```

If you do not have a Dockerfile, create a simple one:

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
```

Create:

```bash
echo "CI/CD Networking Lab" > index.html
```

Build:

```bash
docker build -t myapp:1.0 .
```

Run:

```bash
docker run -d \
  --name myapp \
  -p 8081:80 \
  myapp:1.0
```

Test:

```bash
curl http://localhost:8081
```

---

# LAB 16 — Container Registry Connectivity

Test Docker Hub connectivity:

```bash
curl -I https://registry-1.docker.io
```

Then:

```bash
docker pull nginx:alpine
```

Observe the network operation:

```text
Docker Client
      |
      | HTTPS
      v
Container Registry
      |
      v
Image
```

---

# LAB 17 — Kubernetes Network Check

Check your Kubernetes cluster:

```bash
kubectl cluster-info
```

---

## Step 1 — Check Nodes

```bash
kubectl get nodes -o wide
```

---

## Step 2 — Check Pods

```bash
kubectl get pods -A -o wide
```

---

## Step 3 — Check Services

```bash
kubectl get svc -A
```

---

# LAB 18 — Create a Kubernetes Test Application

Create a namespace:

```bash
kubectl create namespace cicd-networking
```

Create nginx:

```bash
kubectl create deployment web \
  --image=nginx \
  -n cicd-networking
```

Check:

```bash
kubectl get pods -n cicd-networking -o wide
```

---

# LAB 19 — Expose the Application

Create a ClusterIP Service:

```bash
kubectl expose deployment web \
  --port=80 \
  --target-port=80 \
  --name=web-service \
  -n cicd-networking
```

Check:

```bash
kubectl get svc -n cicd-networking
```

---

# LAB 20 — Check Endpoints

Run:

```bash
kubectl get endpoints -n cicd-networking
```

Also:

```bash
kubectl get endpointslices \
  -n cicd-networking
```

The Service should have an endpoint pointing toward the application Pod.

---

# LAB 21 — Test Kubernetes DNS

Run:

```bash
kubectl run dns-test \
  --image=busybox:1.36 \
  --restart=Never \
  --rm -it \
  -n cicd-networking \
  -- nslookup web-service
```

You should receive a Kubernetes Service IP.

Test the fully qualified name:

```bash
kubectl run dns-test \
  --image=busybox:1.36 \
  --restart=Never \
  --rm -it \
  -n cicd-networking \
  -- nslookup web-service.cicd-networking.svc.cluster.local
```

---

# LAB 22 — Test Kubernetes Service

Start a temporary curl container:

```bash
kubectl run curl-test \
  --image=curlimages/curl \
  --rm -it \
  -n cicd-networking \
  -- sh
```

Inside:

```bash
curl http://web-service
```

Expected:

```text
Nginx HTML response
```

---

# LAB 23 — Test Kubernetes API Connectivity

Run:

```bash
kubectl cluster-info
```

Then:

```bash
kubectl config current-context
```

Check API configuration:

```bash
kubectl config view
```

The CI/CD runner needs network connectivity to the Kubernetes API server.

Typical architecture:

```text
CI Runner
    |
    | HTTPS
    v
Kubernetes API
    |
    v
Cluster
```

---

# LAB 24 — Simulate CI/CD Deployment

Imagine your CI pipeline has created a new image.

Example:

```text
Build
  ↓
Docker Image
  ↓
Registry
  ↓
Kubernetes
```

Create a deployment:

```bash
kubectl create deployment demo \
  --image=nginx \
  -n cicd-networking
```

Check:

```bash
kubectl get deployment -n cicd-networking
```

Check:

```bash
kubectl get pods -n cicd-networking
```

---

# LAB 25 — Check Kubernetes Events

Run:

```bash
kubectl get events \
  -n cicd-networking \
  --sort-by=.lastTimestamp
```

Events can help identify:

* Image pull failures
* Scheduling problems
* Network issues
* Container startup problems

---

# LAB 26 — AWS CLI Connectivity

Check AWS CLI:

```bash
aws --version
```

Check identity:

```bash
aws sts get-caller-identity
```

If successful, your CLI can communicate with AWS and your credentials are being accepted.

---

# LAB 27 — Check AWS Region

```bash
aws configure get region
```

Or:

```bash
aws configure list
```

If your intended region is different, configure it appropriately.

---

# LAB 28 — Inspect AWS VPC Networking

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

List Security Groups:

```bash
aws ec2 describe-security-groups
```

---

# LAB 29 — CI Runner → AWS Mental Model

If a CI runner is outside AWS:

```text
CI Runner
    |
    | HTTPS
    v
AWS API
    |
    v
AWS Resources
```

If a self-hosted runner is inside a private AWS subnet:

```text
Private CI Runner
       |
       v
Route Table
       |
       v
NAT Gateway / VPC Endpoint
       |
       v
AWS Service
```

---

# LAB 30 — Network Troubleshooting Challenge

## Scenario

Your CI pipeline reports:

```text
Connection timed out
```

The pipeline is trying to access:

```text
https://example.com
```

Troubleshoot step-by-step.

---

## Step 1 — DNS

```bash
dig example.com
```

---

## Step 2 — IP

```bash
dig +short example.com
```

---

## Step 3 — Route

```bash
ip route
```

---

## Step 4 — TCP

```bash
nc -vz example.com 443
```

---

## Step 5 — HTTPS

```bash
curl -v https://example.com
```

---

## Step 6 — Proxy

```bash
echo $HTTP_PROXY
echo $HTTPS_PROXY
echo $NO_PROXY
```

---

## Step 7 — Packet Capture

```bash
sudo tcpdump -i any port 443
```

---

# LAB 31 — Troubleshooting Challenge: SSH

Scenario:

```text
CI Runner
   |
   X
   |
Linux Server
```

SSH deployment fails.

Run:

```bash
nc -vz <server-ip> 22
```

Then:

```bash
ssh -vvv user@<server-ip>
```

On the destination server:

```bash
ss -lntp | grep ':22'
```

Check:

```text
Route
Security Group
NACL
Firewall
SSH service
Authentication
```

---

# LAB 32 — Troubleshooting Challenge: Kubernetes

Scenario:

```text
CI Runner
    |
    X
    |
Kubernetes API
```

Check:

```bash
kubectl cluster-info
```

Then:

```bash
kubectl config current-context
```

Then:

```bash
kubectl get nodes
```

If authentication works but application traffic fails, check:

```bash
kubectl get svc -A
kubectl get endpoints -A
kubectl get networkpolicy -A
```

---

# LAB 33 — Troubleshooting Challenge: Docker

Scenario:

```text
Container A
     |
     X
     |
Container B
```

Check:

```bash
docker network ls
```

Then:

```bash
docker network inspect ci-network
```

Check containers:

```bash
docker ps
```

Check container networking:

```bash
docker inspect <container>
```

Test connectivity using a diagnostic container.

---

# LAB 34 — Build a CI/CD Network Flow

Draw this architecture in your notes:

```text
                    Developer
                        |
                        | git push
                        v
                  Git Repository
                        |
                        | Trigger
                        v
                    CI Runner
                        |
            +-----------+-----------+
            |           |           |
            v           v           v
           Git       Registry      AWS
            |           |           |
            |           |           v
            |           |       Kubernetes
            |           |           |
            |           |           v
            +-----------+------> Application
                                  |
                                  v
                               User
```

For every arrow identify:

* Source
* Destination
* Protocol
* Port
* DNS
* Authentication
* Firewall/security control

---

# LAB 35 — Final CI/CD Networking Checklist

## Git

```bash
git --version
git remote -v
git ls-remote <repository>
```

---

## DNS

```bash
dig <domain>
dig +short <domain>
getent hosts <domain>
```

---

## Network

```bash
ip addr
ip route
```

---

## Ports

```bash
ss -lntp
nc -vz <host> <port>
```

---

## HTTP

```bash
curl -v <URL>
```

---

## SSH

```bash
ssh -vvv user@host
```

---

## Docker

```bash
docker network ls
docker network inspect <network>
docker inspect <container>
```

---

## Kubernetes

```bash
kubectl cluster-info
kubectl get pods -A -o wide
kubectl get svc -A
kubectl get endpoints -A
kubectl get networkpolicy -A
```

---

## AWS

```bash
aws sts get-caller-identity
aws ec2 describe-vpcs
aws ec2 describe-subnets
aws ec2 describe-route-tables
aws ec2 describe-security-groups
```

---

# 🧠 Final Troubleshooting Framework

Whenever a CI/CD network problem occurs, follow:

```text
1. SOURCE
      ↓
2. DESTINATION
      ↓
3. DNS
      ↓
4. IP
      ↓
5. ROUTE
      ↓
6. GATEWAY
      ↓
7. PORT
      ↓
8. FIREWALL
      ↓
9. SECURITY GROUP / NACL
      ↓
10. PROXY
      ↓
11. TLS
      ↓
12. AUTHENTICATION
      ↓
13. APPLICATION
```

---

# 🎯 Practical Interview Challenge

### Question

Your CI/CD pipeline successfully builds a Docker image but fails during deployment to Kubernetes.

How would you troubleshoot it?

### Answer Framework

I would divide the problem into stages:

```text
Build
 ↓
Registry
 ↓
Kubernetes API
 ↓
Image Pull
 ↓
Pod
 ↓
Service
 ↓
Application
```

First I would check whether the image was successfully pushed to the registry.

Then I would verify that the CI runner can reach the Kubernetes API.

I would check:

```bash
kubectl cluster-info
kubectl get nodes
```

Then I would inspect the deployment and Pods:

```bash
kubectl get deployment
kubectl get pods -o wide
kubectl describe pod <pod-name>
```

If the Pod cannot pull the image, I would check:

* Registry connectivity
* Image name/tag
* Registry authentication
* ImagePullSecrets

If the Pod is running but the application cannot be reached, I would check:

```bash
kubectl get svc
kubectl get endpoints
kubectl get networkpolicy
```

Finally, I would verify the application port and logs.

---

# 🚀 What You Learned

After completing this lab, you practiced networking across:

```text
Linux
  ↓
Git
  ↓
HTTPS
  ↓
Docker
  ↓
Container Registry
  ↓
Kubernetes
  ↓
AWS
  ↓
CI/CD
```

The most important skill is not memorizing commands.

The important skill is understanding:

```text
WHO
 ↓
CONNECTS TO WHOM
 ↓
USING WHICH PROTOCOL
 ↓
ON WHICH PORT
 ↓
THROUGH WHICH NETWORK PATH
 ↓
WITH WHICH SECURITY CONTROLS
```

That is the core of **CI/CD Networking troubleshooting**.
