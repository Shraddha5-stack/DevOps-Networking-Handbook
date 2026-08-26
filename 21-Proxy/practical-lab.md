# Chapter 21 — Proxy Practical Lab

## Objective

In this practical lab, I will understand Proxy configuration and troubleshoot network connectivity using Linux commands.

I will practice:

- Checking Proxy environment variables
- Checking DNS
- Testing Internet connectivity
- Testing HTTP/HTTPS with `curl`
- Checking `NO_PROXY`
- Checking listening ports
- Understanding Nginx as a Reverse Proxy
- Understanding Proxy troubleshooting

---

# Lab 1 — Check Proxy Environment Variables

## Command

```bash
env | grep -i proxy
```

## Purpose

This command checks whether Proxy-related environment variables are configured.

Common variables:

```text
HTTP_PROXY
HTTPS_PROXY
NO_PROXY
```

## Observation

If the command returns nothing, no Proxy environment variables are currently configured in the shell.

If variables are configured, they will be displayed.

---

# Lab 2 — Check Individual Proxy Variables

Run:

```bash
echo $HTTP_PROXY
```

```bash
echo $HTTPS_PROXY
```

```bash
echo $NO_PROXY
```

## Purpose

These commands check individual Proxy environment variables.

### My Actual Result

I checked the Proxy environment variables:

```bash
echo $HTTP_PROXY
echo $HTTPS_PROXY
echo $NO_PROXY


---

# Lab 3 — Check DNS Resolution

Run:

```bash
getent hosts example.com
```

## Purpose

This verifies that the system can resolve a domain name to an IP address.

## Expected Result

You should receive an IP address associated with `example.com`.

Example:

```text
<IP-address> example.com
```

### My Actual Result

I ran:

```bash
getent hosts example.com


## Observation

DNS resolution is working if an IP address is returned.

---

# Lab 4 — Test Internet Connectivity with curl

Run:

```bash
curl -I https://example.com
```

## Purpose

This sends an HTTP HEAD request and displays response headers.

Possible output includes:

```text
HTTP/2 200
```

or another valid HTTP status.



### My Actual Result

I ran:

```bash
curl -I https://example.com



## Observation

A successful response confirms that the system can reach the website using HTTPS.

---

# Lab 5 — Test HTTPS with Verbose Mode

Run:

```bash
curl -v https://example.com
```

## Purpose

The `-v` option provides detailed information about:

- DNS
- TCP connection
- TLS
- HTTP
- Server response

### My Actual Result

I ran:

```bash
curl -v https://example.com



## Observation

Look for messages related to:

```text
Connected
TLS
SSL
HTTP
```

---

# Lab 6 — Check NO_PROXY

Run:

```bash
echo $NO_PROXY
```

Also try:

```bash
echo $no_proxy
```

## Purpose

This shows destinations that should bypass the Proxy.


### My Actual Result

I checked both uppercase and lowercase `NO_PROXY` variables:

```bash
echo $NO_PROXY
echo $no_proxy


## Observation

If empty, there is no `NO_PROXY` value configured in the current shell.

---

# Lab 7 — Test Direct Connection

Run:

```bash
curl --noproxy '*' -v https://example.com
```

## Purpose

This forces `curl` to bypass Proxy settings.

This is useful when troubleshooting:

```text
Proxy connection
vs
Direct connection
```

### My Actual Result

I ran:

```bash
curl --noproxy '*' -I https://example.com



## Observation

Compare this result with:

```bash
curl -v https://example.com
```

---

# Lab 8 — Check Listening Ports

Run:

```bash
ss -ltnp
```

## Purpose

Displays TCP ports that are currently listening.

Example:

```text
LISTEN
0.0.0.0:80
0.0.0.0:443
```

### My Actual Result

I ran:

```bash
ss -ltnp


## Observation

Look for services listening on common web ports:

```text
80
443
8080
8443
```

---

# Lab 9 — Check Network Connections

Run:

```bash
ss -tun
```

## Purpose

Displays active TCP and UDP connections.

This helps understand current network communication.



### My Actual Result

I ran:

```bash
sudo ss -ltnp


---

# Lab 10 — Check Nginx

First check whether Nginx is installed:

```bash
nginx -v
```

If Nginx is installed, check its status:

```bash
sudo systemctl status nginx
```

## Purpose

Nginx is commonly used as:

- Web server
- Reverse Proxy
- Load balancer
- TLS termination point


### Important Docker Observation

My Docker CLI is currently using the:

```text
desktop-linux



---

# Lab 11 — Test Nginx Configuration

If Nginx is installed, run:

```bash
sudo nginx -t
```

## Expected Result

A valid configuration normally produces output similar to:

```text
syntax is ok
test is successful
```

## Important

This command checks configuration syntax before reloading Nginx.

---

# Lab 12 — Check Nginx Listening Ports

Run:

```bash
sudo ss -ltnp | grep nginx
```

## Purpose

Checks which TCP ports Nginx is listening on.

Common ports:

```text
80
443
```

## Lab 12 — Check Docker Networks

### Command

```bash
docker network ls



---

# Lab 13 — Check Nginx Configuration

Run:

```bash
sudo nginx -T
```

## Purpose

Displays the complete active Nginx configuration.

Look for:

```nginx
server {
```

and:

```nginx
location
```

and:

```nginx
proxy_pass
```

## Lab 13 — Identify Docker and Kubernetes Processes

### Command

```bash
ps aux | grep -E 'docker|kube' | grep -v grep


---

# Lab 14 — Identify Reverse Proxy Configuration

If Nginx is configured as a Reverse Proxy, look for:

```nginx
proxy_pass
```

Example:

```nginx
location / {
    proxy_pass http://127.0.0.1:8080;
}
```

This means:

```text
Client
   |
   ↓
Nginx :80
   |
   ↓
Application :8080
```

---

# Lab 15 — Check Proxy Processes

Run:

```bash
ps aux | grep -i proxy
```

## Purpose

Searches running processes containing the word `proxy`.

Remember that this may also return the `grep` command itself.

## Lab 15 — Verify Kubernetes Cluster Networking

### Commands

```bash
kubectl cluster-info



---

# Lab 16 — Test a Proxy Port

If you have a known Proxy host and port, run:

```bash
nc -zv <proxy-host> <proxy-port>
```

Example:

```bash
nc -zv 192.168.1.10 8080
```

## Purpose

Checks TCP connectivity to the Proxy.

Do not use a random IP as evidence of a real Proxy. Use an actual Proxy address only if one exists in your environment.


## Lab 16 — Inspect Kubernetes Services

### Command

```bash
kubectl get svc -A



---

# Lab 17 — Test HTTP Through a Proxy

If you have an actual Proxy:

```bash
curl -v -x http://<proxy-host>:<proxy-port> http://example.com
```

## Purpose

Tests HTTP traffic through a Proxy.

## Lab 17 — Inspect NodePort Service Configuration

### Commands

```bash
kubectl get svc web-app-nodeport -o yaml



---

# Lab 18 — Test HTTPS Through a Proxy

Run:

```bash
curl -v -x http://<proxy-host>:<proxy-port> https://example.com
```

## Purpose

Tests HTTPS connectivity through a Proxy.

## Lab 18 — Find Pods Behind a Kubernetes Service

### Command

```bash
kubectl get pods -l app=web-app -o wide


---

# Lab 19 — Check Docker Proxy Variables

Check your current environment:

```bash
env | grep -i proxy
```

If you have a running Docker container:

```bash
docker ps
```

Then inspect its environment:

```bash
docker inspect -f '{{range .Config.Env}}{{println .}}{{end}}' <container-name> | grep -i proxy
```

## Purpose

Checks whether Proxy variables have been passed into a container.


## Lab 19 — Inspect Kubernetes EndpointSlice

### Command

```bash
kubectl get endpointslice -l kubernetes.io/service-name=web-app-nodeport



---

# Lab 20 — Check Kubernetes Proxy Variables

If Kubernetes is available:

```bash
kubectl get pods
```

Then:

```bash
kubectl exec <pod-name> -- env | grep -i proxy
```

## Purpose

Checks whether Proxy variables exist inside a Pod.

## Lab 20 — Test Kubernetes Service Connectivity

### Test 1 — Host NodePort

Command:

```bash
curl http://127.0.0.1:30080


---

# Lab 21 — Proxy Troubleshooting

Suppose an application cannot access:

```text
https://example.com
```

Follow this process:

### Step 1 — Check IP

```bash
ip addr
```

### Step 2 — Check routing

```bash
ip route
```

### Step 3 — Check DNS

```bash
getent hosts example.com
```

### Step 4 — Check Proxy variables

```bash
env | grep -i proxy
```

### Step 5 — Check connectivity

```bash
curl -v https://example.com
```

### Step 6 — Test without Proxy

```bash
curl --noproxy '*' -v https://example.com
```

### Step 7 — Check Proxy port

```bash
nc -zv <proxy-host> <proxy-port>
```

### Step 8 — Check TLS

Look at:

```text
certificate
TLS handshake
SSL errors
```

### Step 9 — Check logs

Check:

```text
Proxy logs
Application logs
Nginx logs
System logs
```


## Lab 21 — Access Application Through Kubernetes NodePort

### Command

```bash
curl -v http://172.23.0.2:30080


---

# Lab 22 — Compare Proxy and Direct Connections

The goal is to understand whether a Proxy is causing a connectivity problem.

### Through configured Proxy

```bash
curl -v https://example.com
```

### Bypass Proxy

```bash
curl --noproxy '*' -v https://example.com
```

Compare:

```text
DNS
Connection
TLS
HTTP response
```
## Lab 22 — Verify NodePort Service Configuration

### Command 1

```bash
kubectl describe svc web-app-nodeport


If the direct connection works but the Proxy connection fails, the Proxy configuration becomes an important troubleshooting area.

---

# Lab 23 — Real-World Reverse Proxy Architecture

A common DevOps architecture is:

```text
                    Internet
                       |
                       ↓
                    DNS
                       |
                       ↓
                Reverse Proxy
                   (Nginx)
                       |
          +------------+------------+
          |            |            |
          ↓            ↓            ↓
       App 1        App 2        App 3
```

The Reverse Proxy can handle:

```text
TLS
Routing
Load balancing
Access control
Logging
```

---

# Lab Results

## My Environment

### Proxy Variables

Command:

```bash
env | grep -i proxy
```

My output:

```text
Paste your actual output here
```

### DNS

Command:

```bash
getent hosts example.com
```

My output:

```text
Paste your actual output here
```

### HTTPS Test

Command:

```bash
curl -I https://example.com
```

My output:

```text
Paste your actual output here
```

### Listening Ports

Command:

```bash
ss -ltnp
```

My relevant output:

```text
Paste your actual output here
```

### Nginx

Command:

```bash
nginx -v
```

My output:

```text
Paste your actual output here
```

---

# Final Observation

In this lab, I learned how to investigate Proxy configuration and connectivity using Linux tools.

Important commands practiced:

```bash
env | grep -i proxy
```

```bash
getent hosts example.com
```

```bash
curl -I https://example.com
```

```bash
curl -v https://example.com
```

```bash
curl --noproxy '*' https://example.com
```

```bash
ss -ltnp
```

```bash
sudo nginx -t
```

```bash
nc -zv <proxy-host> <proxy-port>
```

I also learned that a Proxy is different from a Gateway and NAT, and that Reverse Proxies such as Nginx are commonly used in DevOps architectures.



### My Actual Result

I ran:

```bash
env | grep -i proxy


