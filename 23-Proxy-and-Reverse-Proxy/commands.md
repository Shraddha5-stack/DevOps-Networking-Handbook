# 🛠️ Chapter 23 – Proxy and Reverse Proxy Commands

This file contains practical commands for checking, testing, configuring, and troubleshooting proxies and reverse proxies.

---

## 1. Check Proxy Environment Variables

### HTTP Proxy

```bash
echo $HTTP_PROXY
```

### HTTPS Proxy

```bash
echo $HTTPS_PROXY
```

### No Proxy

```bash
echo $NO_PROXY
```

### Check all proxy variables

```bash
env | grep -i proxy
```

You can also check lowercase variables:

```bash
echo $http_proxy
echo $https_proxy
echo $no_proxy
```

### Observation

If the command returns nothing, that particular proxy environment variable is not set in the current shell.

---

# 2. Test Internet Connectivity

```bash
curl -I https://example.com
```

### Observation

A successful request should return an HTTP status such as:

```text
HTTP/2 200
```

This confirms that the request successfully reached the server.

---

# 3. Verbose curl Testing

```bash
curl -v https://example.com
```

Verbose mode shows:

* DNS resolution
* IP addresses
* TCP connection
* TLS handshake
* HTTP protocol
* Request headers
* Response headers

Example flow:

```text
DNS
 ↓
TCP
 ↓
TLS
 ↓
HTTP
 ↓
Response
```

---

# 4. Bypass Proxy

To force `curl` to avoid configured proxy settings:

```bash
curl --noproxy '*' -I https://example.com
```

### Observation

If the request succeeds with `--noproxy` but fails normally, proxy configuration may be involved.

---

# 5. Check DNS Resolution

```bash
getent hosts example.com
```

Alternative:

```bash
nslookup example.com
```

If available:

```bash
dig example.com
```

### Observation

You should receive one or more IP addresses.

---

# 6. Check HTTP Headers

```bash
curl -I http://example.com
```

For HTTPS:

```bash
curl -I https://example.com
```

Headers can reveal:

* HTTP status
* Server information
* Content type
* Cache information
* Redirects

---

# 7. Follow HTTP Redirects

```bash
curl -IL https://example.com
```

The `-L` option follows redirects.

---

# 8. Display Only the HTTP Status Code

```bash
curl -o /dev/null -s -w "%{http_code}\n" https://example.com
```

Example:

```text
200
```

---

# 9. Test a Specific HTTP Host

```bash
curl -v -H "Host: example.com" http://127.0.0.1
```

This is useful when testing reverse-proxy virtual hosts.

---

# 10. Check Listening Ports

```bash
ss -ltn
```

For process information:

```bash
sudo ss -ltnp
```

Example:

```text
LISTEN 0 511 *:80
```

This can indicate that a web server or reverse proxy is listening on port 80.

---

# 11. Check Common Web Ports

```bash
sudo ss -ltnp | grep -E ':80|:443|:8080'
```

Common ports:

```text
80    → HTTP
443   → HTTPS
8080  → Common application/web port
```

---

# 12. Check Nginx Installation

```bash
nginx -v
```

Example:

```text
nginx version: nginx/1.x.x
```

---

# 13. Check Nginx Status

```bash
sudo systemctl status nginx
```

Start Nginx:

```bash
sudo systemctl start nginx
```

Stop Nginx:

```bash
sudo systemctl stop nginx
```

Restart Nginx:

```bash
sudo systemctl restart nginx
```

Reload configuration:

```bash
sudo systemctl reload nginx
```

---

# 14. Test Nginx Configuration

Before reloading Nginx:

```bash
sudo nginx -t
```

Successful output normally indicates:

```text
syntax is ok
test is successful
```

Always validate the configuration before applying changes.

---

# 15. View Nginx Configuration

Main configuration:

```bash
sudo cat /etc/nginx/nginx.conf
```

List configuration files:

```bash
ls -la /etc/nginx/
```

Check available sites:

```bash
ls -la /etc/nginx/sites-available/
```

Check enabled sites:

```bash
ls -la /etc/nginx/sites-enabled/
```

---

# 16. Simple Nginx Reverse Proxy Configuration

A basic reverse proxy can look like:

```nginx
server {
    listen 80;

    location / {
        proxy_pass http://127.0.0.1:8080;
    }
}
```

Traffic flow:

```text
Client
   |
   | HTTP :80
   v
Nginx
   |
   | HTTP :8080
   v
Application
```

---

# 17. Forward Requests to a Backend

Example:

```nginx
location /api/ {
    proxy_pass http://127.0.0.1:8080;
}
```

Requests arriving at:

```text
http://server/api/
```

are forwarded to the configured upstream.

---

# 18. Add Proxy Headers

A common configuration is:

```nginx
location / {
    proxy_pass http://127.0.0.1:8080;

    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

These headers help the backend identify information about the original request.

---

# 19. Nginx Access Logs

View the access log:

```bash
sudo tail -f /var/log/nginx/access.log
```

The access log can show:

* Client IP
* Request method
* Requested path
* HTTP status
* Response size

Stop with:

```text
Ctrl + C
```

---

# 20. Nginx Error Logs

```bash
sudo tail -f /var/log/nginx/error.log
```

Useful for troubleshooting:

* Configuration errors
* Connection failures
* Backend failures
* Permission problems

---

# 21. Test Local Reverse Proxy

If Nginx is listening on port 80:

```bash
curl -v http://127.0.0.1/
```

If it forwards to an application on port 8080, check the backend directly:

```bash
curl -v http://127.0.0.1:8080/
```

Compare both responses.

---

# 22. Check Backend Port

```bash
sudo ss -ltnp | grep ':8080'
```

If nothing is returned, no process is currently listening on TCP port 8080.

---

# 23. Test Backend Connectivity

```bash
curl -v http://127.0.0.1:8080/
```

If the backend is working, you should receive an HTTP response.

If you receive:

```text
Connection refused
```

the backend may not be running or may not be listening on that address/port.

---

# 24. Check Processes

```bash
ps aux | grep nginx
```

For all web-related processes:

```bash
ps aux | grep -E 'nginx|apache|haproxy'
```

---

# 25. Check Which Process Uses a Port

```bash
sudo ss -ltnp | grep ':80'
```

Another useful command:

```bash
sudo lsof -i :80
```

For port 443:

```bash
sudo lsof -i :443
```

---

# 26. Test TCP Connectivity

Using `nc`:

```bash
nc -vz 127.0.0.1 8080
```

Example successful result:

```text
Connection to 127.0.0.1 8080 succeeded
```

---

# 27. Check Routing

```bash
ip route
```

This helps identify the default gateway and routing table.

---

# 28. Check Network Interfaces

```bash
ip addr show
```

This displays:

* Interfaces
* IPv4 addresses
* IPv6 addresses
* Network prefixes
* Interface state

---

# 29. Check DNS Configuration

```bash
cat /etc/resolv.conf
```

On systems using `systemd-resolved`:

```bash
resolvectl status
```

---

# 30. Test DNS + HTTPS Together

```bash
curl -v https://example.com
```

This single command can help identify problems involving:

```text
DNS
 ↓
TCP
 ↓
TLS
 ↓
HTTP
```

---

# 31. Docker – Check Containers

```bash
docker ps
```

All containers:

```bash
docker ps -a
```

---

# 32. Docker – Check Networks

```bash
docker network ls
```

Inspect a network:

```bash
docker network inspect bridge
```

---

# 33. Docker – Check Port Mapping

```bash
docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Ports}}\t{{.Names}}"
```

Example:

```text
0.0.0.0:8080->80/tcp
```

This means:

```text
Host :8080
   ↓
Container :80
```

---

# 34. Docker Reverse Proxy Architecture

Example:

```text
Client
   |
   v
Nginx Container :80
   |
   v
Application Container :8080
```

Check running containers:

```bash
docker ps
```

Check their networks:

```bash
docker inspect <container-name>
```

---

# 35. Kubernetes – Check Services

```bash
kubectl get svc
```

Detailed service information:

```bash
kubectl describe svc <service-name>
```

---

# 36. Kubernetes – Check Endpoints

```bash
kubectl get endpoints
```

EndpointSlices:

```bash
kubectl get endpointslice
```

For a specific service:

```bash
kubectl get endpointslice -l kubernetes.io/service-name=<service-name>
```

This verifies whether the Service has backend endpoints.

---

# 37. Kubernetes – Test Service Internally

Run a temporary curl container:

```bash
kubectl run network-test \
  --rm -it \
  --restart=Never \
  --image=curlimages/curl \
  -- curl -v http://<service-name>:<port>
```

This is useful for testing:

```text
Pod
 ↓
Service
 ↓
Backend Pod
```

---

# 38. Kubernetes – Check Pods

```bash
kubectl get pods -o wide
```

Check pods matching an application label:

```bash
kubectl get pods -l app=<app-name> -o wide
```

---

# 39. Kubernetes – Check Ingress

```bash
kubectl get ingress
```

Detailed information:

```bash
kubectl describe ingress <ingress-name>
```

---

# 40. Troubleshooting Checklist

When a reverse proxy is not working, check in this order:

### 1. Is the backend running?

```bash
ps aux | grep <application>
```

### 2. Is the backend listening?

```bash
sudo ss -ltnp | grep ':8080'
```

### 3. Can the backend be reached directly?

```bash
curl -v http://127.0.0.1:8080/
```

### 4. Is the proxy running?

```bash
sudo systemctl status nginx
```

### 5. Is the proxy listening?

```bash
sudo ss -ltnp | grep ':80'
```

### 6. Is the configuration valid?

```bash
sudo nginx -t
```

### 7. Test through the proxy

```bash
curl -v http://127.0.0.1/
```

### 8. Check logs

```bash
sudo tail -f /var/log/nginx/error.log
```

and:

```bash
sudo tail -f /var/log/nginx/access.log
```

---

# 41. Important Command Summary

| Command                             | Purpose                       |
| ----------------------------------- | ----------------------------- |
| `env \| grep -i proxy`              | Check proxy variables         |
| `curl -I URL`                       | Check HTTP headers            |
| `curl -v URL`                       | Detailed connection debugging |
| `curl --noproxy '*' URL`            | Bypass proxy                  |
| `getent hosts domain`               | DNS lookup                    |
| `ss -ltnp`                          | Listening ports/processes     |
| `nginx -t`                          | Test Nginx configuration      |
| `systemctl status nginx`            | Check Nginx                   |
| `tail -f /var/log/nginx/access.log` | Nginx access logs             |
| `tail -f /var/log/nginx/error.log`  | Nginx error logs              |
| `docker ps`                         | Running containers            |
| `docker network ls`                 | Docker networks               |
| `kubectl get svc`                   | Kubernetes Services           |
| `kubectl get endpointslice`         | Service endpoints             |
| `kubectl get ingress`               | Kubernetes Ingress            |

---

# 42. Practical Observation

During troubleshooting, think about the request path:

```text
Client
  ↓
DNS
  ↓
TCP Connection
  ↓
Reverse Proxy
  ↓
Backend
  ↓
Application Response
  ↓
Reverse Proxy
  ↓
Client
```

If something fails, identify the exact layer.

For example:

```text
DNS failure
    ↓
No IP address

TCP failure
    ↓
Connection refused / timeout

Proxy failure
    ↓
502 Bad Gateway

Backend failure
    ↓
Application unavailable
```

Understanding this request path is one of the most important skills for troubleshooting real-world DevOps infrastructure.
