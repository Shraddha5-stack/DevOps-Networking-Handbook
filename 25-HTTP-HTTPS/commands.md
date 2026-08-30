# 🌐 Chapter 25 — HTTP & HTTPS Commands

## 🎯 Objective

This file contains practical HTTP/HTTPS commands used by DevOps engineers for:

* Testing web servers
* Checking HTTP status codes
* Inspecting headers
* Testing APIs
* Troubleshooting connectivity
* Checking redirects
* Inspecting TLS certificates
* Testing ports
* Debugging DNS and HTTP problems

---

# 1. Check HTTP Website

```bash
curl http://example.com
```

### Observation

The command sends an HTTP GET request and displays the response body.

---

# 2. Check HTTPS Website

```bash
curl https://example.com
```

### Observation

The request is sent over HTTPS using TLS.

---

# 3. Display HTTP Response Headers

```bash
curl -I https://example.com
```

Example:

```text
HTTP/2 200
content-type: text/html
```

### Useful for

* Status code
* Content-Type
* Server information
* Cache headers
* Redirects

---

# 4. Verbose HTTP Request

```bash
curl -v https://example.com
```

This displays detailed connection information.

### Useful for troubleshooting

* DNS
* TCP connection
* TLS handshake
* HTTP request
* HTTP response

---

# 5. Show Only HTTP Status Code

```bash
curl -o /dev/null -s -w "%{http_code}\n" https://example.com
```

Example:

```text
200
```

### Observation

This is useful in monitoring scripts and health checks.

---

# 6. Check Response Time

```bash
curl -o /dev/null -s -w "HTTP: %{http_code}\nTime: %{time_total}s\n" https://example.com
```

Example:

```text
HTTP: 200
Time: 0.245s
```

---

# 7. Follow HTTP Redirects

```bash
curl -L http://example.com
```

Check redirect chain:

```bash
curl -IL http://example.com
```

### Observation

`-L` tells curl to follow redirects.

---

# 8. Display Headers and Body

```bash
curl -i https://example.com
```

Difference:

```text
-I → Headers only
-i → Headers + response body
```

---

# 9. Send a GET Request

```bash
curl -X GET https://example.com
```

Normally `curl` already uses GET when no other method is specified:

```bash
curl https://example.com
```

---

# 10. Send a POST Request

```bash
curl -X POST https://example.com/api/users
```

### Observation

The request uses the HTTP POST method.

---

# 11. POST JSON Data

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"name":"Shraddha"}' \
  https://example.com/api/users
```

### Important

```text
-H → Header
-d → Request body
```

---

# 12. Send PUT Request

```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"name":"Shraddha"}' \
  https://example.com/api/users/1
```

---

# 13. Send PATCH Request

```bash
curl -X PATCH \
  -H "Content-Type: application/json" \
  -d '{"name":"Shraddha Updated"}' \
  https://example.com/api/users/1
```

---

# 14. Send DELETE Request

```bash
curl -X DELETE https://example.com/api/users/1
```

---

# 15. Send Custom HTTP Header

```bash
curl -H "X-Test: DevOps" https://example.com
```

Multiple headers:

```bash
curl \
  -H "Accept: application/json" \
  -H "X-Environment: development" \
  https://example.com
```

---

# 16. Send Authorization Header

Example using a bearer token:

```bash
curl \
  -H "Authorization: Bearer <TOKEN>" \
  https://example.com/api
```

### Security

Never put real production tokens in documentation, Git repositories, screenshots, or public posts.

---

# 17. Display Request Headers

```bash
curl -v https://example.com
```

Look for:

```text
> GET / HTTP/...
> Host:
> User-Agent:
> Accept:
```

---

# 18. Display Response Headers

```bash
curl -I https://example.com
```

Look for:

```text
< HTTP/...
< Content-Type:
< Content-Length:
< Server:
< Cache-Control:
```

---

# 19. Test HTTP Port 80

```bash
nc -vz example.com 80
```

Possible result:

```text
Connection to example.com 80 port [tcp/http] succeeded!
```

---

# 20. Test HTTPS Port 443

```bash
nc -vz example.com 443
```

### Observation

This checks TCP connectivity to port 443.

It does not by itself validate the HTTPS application or certificate.

---

# 21. Check Listening HTTP Ports

```bash
sudo ss -ltnp
```

Look for:

```text
:80
:443
:8080
```

### Observation

This shows TCP ports on which local processes are listening.

---

# 22. Check a Specific Port

```bash
sudo ss -ltnp | grep :80
```

For HTTPS:

```bash
sudo ss -ltnp | grep :443
```

---

# 23. Check DNS Before HTTP

```bash
getent hosts example.com
```

Or:

```bash
dig example.com
```

### Observation

If DNS does not resolve, investigate DNS before troubleshooting HTTP.

---

# 24. Check HTTP Using IP Address

```bash
curl -v http://<IP>
```

Example:

```bash
curl -v http://192.168.1.100
```

This can help separate DNS problems from HTTP connectivity problems.

---

# 25. Test a Specific Host Header

Useful when multiple websites share the same server/IP:

```bash
curl -v -H "Host: example.com" http://192.168.1.100
```

### DevOps Use

This is useful for troubleshooting:

* Virtual hosts
* Reverse proxies
* Load balancers
* Ingress

---

# 26. Test HTTPS with a Specific Host

For testing an HTTPS service by IP while keeping the hostname for TLS/SNI:

```bash
curl -vk --resolve example.com:443:<IP> https://example.com/
```

Example:

```bash
curl -vk --resolve example.com:443:192.168.1.100 https://example.com/
```

### Observation

`--resolve` maps the hostname to a specified IP for that curl request.

---

# 27. Inspect TLS Certificate

```bash
openssl s_client -connect example.com:443
```

This can display:

* Certificate
* TLS version
* Cipher
* Certificate chain
* Handshake information

Exit with:

```text
Ctrl + C
```

---

# 28. Inspect Certificate Dates

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates
```

Example:

```text
notBefore=...
notAfter=...
```

### Observation

This helps identify expired or soon-to-expire certificates.

---

# 29. Display Certificate Subject

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -subject
```

---

# 30. Display Certificate Issuer

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -issuer
```

---

# 31. Check TLS Version

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | grep "Protocol"
```

---

# 32. Test a Specific TLS Version

TLS 1.2:

```bash
openssl s_client -connect example.com:443 -tls1_2
```

TLS 1.3:

```bash
openssl s_client -connect example.com:443 -tls1_3
```

### Observation

Useful for troubleshooting TLS compatibility.

---

# 33. Check HTTP/2

```bash
curl -I --http2 https://example.com
```

If supported by your curl build and the server, the response will use HTTP/2.

---

# 34. Check HTTP/1.1

```bash
curl -I --http1.1 https://example.com
```

---

# 35. Check HTTP/3

If your curl build supports HTTP/3:

```bash
curl -I --http3 https://example.com
```

### Observation

HTTP/3 uses QUIC over UDP.

Support depends on the local curl build and the server.

---

# 36. Download a File

```bash
curl -O https://example.com/file.txt
```

---

# 37. Save Response to a File

```bash
curl https://example.com -o response.html
```

Check:

```bash
ls -lh response.html
```

---

# 38. Use wget

Download a page:

```bash
wget https://example.com
```

Download a file:

```bash
wget https://example.com/file.txt
```

---

# 39. Check HTTP Compression

```bash
curl -I -H "Accept-Encoding: gzip, br" https://example.com
```

Look for:

```text
Content-Encoding:
```

---

# 40. Check Cache Headers

```bash
curl -I https://example.com
```

Look for:

```text
Cache-Control:
ETag:
Last-Modified:
Expires:
```

---

# 41. Test Cookies

Save cookies:

```bash
curl -c cookies.txt https://example.com
```

Send cookies:

```bash
curl -b cookies.txt https://example.com
```

### Observation

`-c` stores cookies.

`-b` sends cookies.

---

# 42. Check HTTP Authentication

Example Basic Authentication:

```bash
curl -u username:password https://example.com
```

### Security Warning

Do not use real production passwords in shell history or documentation.

For production systems, prefer safer credential handling.

---

# 43. Check API Response as JSON

```bash
curl -s https://api.example.com/data
```

If `jq` is installed:

```bash
curl -s https://api.example.com/data | jq
```

---

# 44. Health Check

A simple HTTP health check:

```bash
curl -f https://example.com/health
```

### Observation

`-f` causes curl to return a failure status for many HTTP 4xx/5xx responses.

This can be useful in scripts and CI/CD health checks.

---

# 45. Kubernetes HTTP Service Test

List services:

```bash
kubectl get svc
```

Example:

```text
NAME          TYPE        CLUSTER-IP      PORT(S)
web-app       ClusterIP   10.96.10.20     80/TCP
```

Test from inside the cluster:

```bash
kubectl run curl-test \
  --rm -it \
  --restart=Never \
  --image=curlimages/curl \
  -- curl -v http://10.96.10.20:80
```

### Observation

This tests communication from a pod to a Kubernetes Service.

---

# 46. Kubernetes Service DNS Test

Example:

```bash
kubectl run curl-test \
  --rm -it \
  --restart=Never \
  --image=curlimages/curl \
  -- curl -v http://web-app.default.svc.cluster.local
```

This tests Kubernetes DNS + Service + HTTP.

---

# 47. Test Nginx Locally

If Nginx is installed:

```bash
sudo systemctl status nginx
```

Check listening ports:

```bash
sudo ss -ltnp | grep nginx
```

Test:

```bash
curl -I http://localhost
```

---

# 48. Docker HTTP Test

Run Nginx:

```bash
docker run -d --name web-test -p 8080:80 nginx
```

Check container:

```bash
docker ps
```

Test:

```bash
curl -I http://localhost:8080
```

Clean up:

```bash
docker rm -f web-test
```

---

# 49. Check HTTP Redirect

```bash
curl -I http://example.com
```

Look for:

```text
HTTP/1.1 301
Location: https://example.com/
```

Follow it:

```bash
curl -IL http://example.com
```

---

# 50. Troubleshooting 404

Run:

```bash
curl -v https://example.com/nonexistent
```

Expected type of response:

```text
404 Not Found
```

Check:

* URL
* Application routes
* Reverse proxy configuration
* Backend service

---

# 51. Troubleshooting 502

Run:

```bash
curl -v https://example.com
```

If you receive:

```text
502 Bad Gateway
```

check the reverse proxy and upstream application.

Useful commands:

```bash
sudo ss -ltnp
```

```bash
curl -v http://<UPSTREAM-IP>:<PORT>
```

---

# 52. Troubleshooting 503

If:

```text
503 Service Unavailable
```

check:

* Backend health
* Application status
* Load balancer
* Kubernetes endpoints
* Service availability

Kubernetes:

```bash
kubectl get pods
kubectl get svc
kubectl get endpointslice
```

---

# 53. Troubleshooting 504

If:

```text
504 Gateway Timeout
```

investigate:

* Network connectivity
* Backend response time
* Application performance
* Proxy timeout
* Load balancer timeout

Test backend directly:

```bash
curl -v http://<UPSTREAM-IP>:<PORT>
```

---

# 54. Trace Network Path

```bash
tracepath example.com
```

If unavailable:

```bash
traceroute example.com
```

### Observation

This helps investigate the network path toward the destination.

---

# 55. Capture HTTP Traffic

For HTTP traffic:

```bash
sudo tcpdump -i any port 80
```

For HTTPS:

```bash
sudo tcpdump -i any port 443
```

### Important

HTTPS payload is encrypted, so packet capture normally does not expose the HTTP contents.

---

# 56. Check Network Interface Statistics

```bash
ip -s link
```

Useful for identifying:

* RX packets
* TX packets
* Errors
* Dropped packets

---

# 57. Complete HTTP Troubleshooting Workflow

Use this sequence when a website or API is not working:

```text
1. DNS
   ↓
2. IP connectivity
   ↓
3. TCP port
   ↓
4. TLS
   ↓
5. HTTP response
   ↓
6. Reverse proxy
   ↓
7. Application
   ↓
8. Database
```

Commands:

```bash
getent hosts example.com
```

```bash
ping -c 4 example.com
```

```bash
nc -vz example.com 443
```

```bash
curl -v https://example.com
```

```bash
openssl s_client -connect example.com:443
```

---

# 📊 Command Quick Reference

| Command            | Purpose                   |
| ------------------ | ------------------------- |
| `curl URL`         | Send HTTP request         |
| `curl -I URL`      | Show headers              |
| `curl -v URL`      | Verbose troubleshooting   |
| `curl -i URL`      | Headers + body            |
| `curl -L URL`      | Follow redirects          |
| `curl -X POST`     | POST request              |
| `curl -H`          | Add header                |
| `curl -d`          | Send request body         |
| `curl -o`          | Save response             |
| `curl -f`          | Fail on HTTP errors       |
| `nc -vz`           | Test TCP port             |
| `ss -ltnp`         | Check listening TCP ports |
| `openssl s_client` | Inspect TLS               |
| `dig`              | DNS troubleshooting       |
| `getent hosts`     | DNS resolution            |
| `tcpdump`          | Packet capture            |
| `tracepath`        | Network path              |
| `wget`             | Download resources        |

---

# 🎯 Key DevOps Commands to Remember

If you remember only these commands from this chapter:

```bash
curl -I https://example.com
```

```bash
curl -v https://example.com
```

```bash
curl -IL https://example.com
```

```bash
nc -vz example.com 443
```

```bash
openssl s_client -connect example.com:443
```

```bash
ss -ltnp
```

```bash
dig example.com
```

These commands cover a large part of day-to-day HTTP/HTTPS troubleshooting.
