# REST API – Commands

## 1. Introduction

This file contains practical commands for working with and troubleshooting REST APIs.

Main tools covered:

* `curl`
* `wget`
* `http`
* `jq`
* `dig`
* `nslookup`
* `ss`
* `openssl`
* Docker
* Kubernetes
* HTTP debugging

---

# 2. Check curl Installation

Check whether `curl` is installed:

```bash
curl --version
```

Install on Ubuntu/Debian:

```bash
sudo apt update
sudo apt install curl -y
```

---

# 3. Basic GET Request

Send a GET request:

```bash
curl https://example.com
```

Example:

```bash
curl https://api.example.com/users
```

---

# 4. Show HTTP Response Headers

Use:

```bash
curl -i https://example.com
```

Example output:

```text
HTTP/1.1 200 OK
Content-Type: text/html
```

---

# 5. Show Only Response Headers

Use:

```bash
curl -I https://example.com
```

This sends a HEAD request.

---

# 6. Verbose curl

For detailed debugging:

```bash
curl -v https://example.com
```

This can show:

* DNS connection
* TCP connection
* TLS handshake details
* Request headers
* Response headers

---

# 7. Very Detailed curl

Use:

```bash
curl -vv https://example.com
```

or:

```bash
curl -vvv https://example.com
```

Useful when troubleshooting connection problems.

---

# 8. GET Request with Headers

Example:

```bash
curl \
  -H "Accept: application/json" \
  https://api.example.com/users
```

Multiple headers:

```bash
curl \
  -H "Accept: application/json" \
  -H "User-Agent: DevOps-Test" \
  https://api.example.com/users
```

---

# 9. GET Request with Query Parameters

Example:

```bash
curl "https://api.example.com/users?role=devops"
```

Multiple parameters:

```bash
curl "https://api.example.com/users?role=devops&location=pune"
```

---

# 10. GET Specific Resource

Example:

```bash
curl https://api.example.com/users/101
```

---

# 11. POST Request

Basic POST:

```bash
curl -X POST https://api.example.com/users
```

POST with JSON:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"name":"Shraddha","role":"DevOps Engineer"}' \
  https://api.example.com/users
```

---

# 12. POST Using a JSON File

Create a JSON file:

```bash
nano user.json
```

Example:

```json
{
  "name": "Shraddha",
  "role": "DevOps Engineer"
}
```

Send it:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d @user.json \
  https://api.example.com/users
```

---

# 13. PUT Request

Example:

```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"name":"Shraddha","role":"Cloud Engineer"}' \
  https://api.example.com/users/101
```

---

# 14. PATCH Request

Example:

```bash
curl -X PATCH \
  -H "Content-Type: application/json" \
  -d '{"role":"Platform Engineer"}' \
  https://api.example.com/users/101
```

---

# 15. DELETE Request

Example:

```bash
curl -X DELETE \
  https://api.example.com/users/101
```

---

# 16. Authentication with Bearer Token

Example:

```bash
curl \
  -H "Authorization: Bearer <TOKEN>" \
  https://api.example.com/users
```

For real secrets, avoid putting tokens directly into shell history.

Better:

```bash
export API_TOKEN="<TOKEN>"
```

Then:

```bash
curl \
  -H "Authorization: Bearer $API_TOKEN" \
  https://api.example.com/users
```

---

# 17. API Key Authentication

Example:

```bash
curl \
  -H "X-API-Key: <API_KEY>" \
  https://api.example.com/users
```

Using an environment variable:

```bash
export API_KEY="<API_KEY>"
```

Then:

```bash
curl \
  -H "X-API-Key: $API_KEY" \
  https://api.example.com/users
```

---

# 18. Basic Authentication

Example:

```bash
curl -u username:password https://api.example.com/users
```

Safer interactive approach:

```bash
curl -u username https://api.example.com/users
```

curl will prompt for the password.

---

# 19. Follow Redirects

Use:

```bash
curl -L https://example.com
```

Useful when the server returns:

```text
301
302
307
308
```

---

# 20. Save Response to a File

Use:

```bash
curl https://api.example.com/users -o users.json
```

Check:

```bash
cat users.json
```

---

# 21. Download Using curl

```bash
curl -O https://example.com/file.txt
```

Specify output filename:

```bash
curl -o output.txt https://example.com/file.txt
```

---

# 22. Download Using wget

Check installation:

```bash
wget --version
```

Download:

```bash
wget https://example.com/file.txt
```

Specify filename:

```bash
wget -O output.txt https://example.com/file.txt
```

---

# 23. Pretty Print JSON with jq

Check installation:

```bash
jq --version
```

Install:

```bash
sudo apt update
sudo apt install jq -y
```

Use:

```bash
curl https://api.example.com/users | jq
```

---

# 24. Extract a JSON Field

Example response:

```json
{
  "id": 101,
  "name": "Shraddha",
  "role": "DevOps Engineer"
}
```

Extract name:

```bash
curl https://api.example.com/users/101 | jq '.name'
```

Output:

```text
"Shraddha"
```

Extract ID:

```bash
curl https://api.example.com/users/101 | jq '.id'
```

---

# 25. Extract Multiple Fields

```bash
curl https://api.example.com/users/101 | jq '.name, .role'
```

---

# 26. Check HTTP Status Code

Use:

```bash
curl -o /dev/null -s -w "%{http_code}\n" https://example.com
```

Example output:

```text
200
```

This is very useful in scripts and CI/CD pipelines.

---

# 27. Check Response Time

Use:

```bash
curl -o /dev/null -s \
-w "Time: %{time_total}s\n" \
https://example.com
```

---

# 28. Check Multiple curl Metrics

```bash
curl -o /dev/null -s \
-w "HTTP: %{http_code}\nDNS: %{time_namelookup}s\nConnect: %{time_connect}s\nTLS: %{time_appconnect}s\nStart Transfer: %{time_starttransfer}s\nTotal: %{time_total}s\n" \
https://example.com
```

Useful for API performance troubleshooting.

---

# 29. Test API Availability

Simple health check:

```bash
curl -f https://api.example.com/health
```

`-f` makes curl fail for HTTP errors such as 4xx and 5xx.

Useful in scripts:

```bash
if curl -fsS https://api.example.com/health > /dev/null; then
    echo "API is healthy"
else
    echo "API is unhealthy"
fi
```

---

# 30. curl Timeout

Set connection timeout:

```bash
curl --connect-timeout 5 https://api.example.com
```

Set maximum total time:

```bash
curl --max-time 10 https://api.example.com
```

Both:

```bash
curl \
  --connect-timeout 5 \
  --max-time 10 \
  https://api.example.com
```

---

# 31. HTTP Method Explicitly

GET:

```bash
curl -X GET https://api.example.com/users
```

POST:

```bash
curl -X POST https://api.example.com/users
```

PUT:

```bash
curl -X PUT https://api.example.com/users/101
```

PATCH:

```bash
curl -X PATCH https://api.example.com/users/101
```

DELETE:

```bash
curl -X DELETE https://api.example.com/users/101
```

---

# 32. Send Custom User-Agent

```bash
curl \
  -A "DevOps-Test" \
  https://example.com
```

---

# 33. Send Form Data

Example:

```bash
curl \
  -X POST \
  -d "username=shraddha&role=devops" \
  https://api.example.com/users
```

For modern JSON APIs, prefer JSON when the API expects it.

---

# 34. Check DNS

Using `nslookup`:

```bash
nslookup api.example.com
```

Using `dig`:

```bash
dig api.example.com
```

Short answer:

```bash
dig +short api.example.com
```

---

# 35. Check DNS Records

A record:

```bash
dig A example.com
```

AAAA record:

```bash
dig AAAA example.com
```

CNAME:

```bash
dig CNAME www.example.com
```

MX:

```bash
dig MX example.com
```

---

# 36. Check DNS and API Connection

First:

```bash
dig +short api.example.com
```

Then:

```bash
curl -v https://api.example.com
```

This helps determine whether the problem is related to DNS or the HTTP connection.

---

# 37. Check Network Connectivity

Ping:

```bash
ping -c 4 api.example.com
```

Important:

**Ping failure does not always mean the API is unavailable.**

ICMP may be blocked while HTTPS works normally.

---

# 38. Check TCP Port

For HTTPS:

```bash
nc -vz api.example.com 443
```

For HTTP:

```bash
nc -vz api.example.com 80
```

Alternative:

```bash
telnet api.example.com 443
```

---

# 39. Check Listening Ports

Use:

```bash
ss -tuln
```

Show processes:

```bash
sudo ss -tulnp
```

Check port 8080:

```bash
sudo ss -tulnp | grep :8080
```

---

# 40. Test Local REST API

If an application runs on port 8080:

```bash
curl http://localhost:8080
```

Health endpoint:

```bash
curl http://localhost:8080/health
```

API endpoint:

```bash
curl http://localhost:8080/api/users
```

---

# 41. Test Localhost with Headers

```bash
curl -i http://localhost:8080/health
```

Verbose:

```bash
curl -v http://localhost:8080/health
```

---

# 42. Test HTTPS Certificate

Use:

```bash
openssl s_client -connect example.com:443
```

Show certificate information:

```bash
openssl s_client \
  -connect example.com:443 \
  -servername example.com
```

---

# 43. Check Certificate Expiration

```bash
echo | openssl s_client \
  -connect example.com:443 \
  -servername example.com 2>/dev/null |
  openssl x509 -noout -dates
```

Example:

```text
notBefore=...
notAfter=...
```

---

# 44. Docker – Check Running Containers

```bash
docker ps
```

All containers:

```bash
docker ps -a
```

---

# 45. Docker – Check API Container Logs

```bash
docker logs <container_name>
```

Follow logs:

```bash
docker logs -f <container_name>
```

Last 100 lines:

```bash
docker logs --tail 100 <container_name>
```

---

# 46. Docker – Check Container Ports

```bash
docker ps
```

Detailed information:

```bash
docker inspect <container_name>
```

Port mapping:

```bash
docker port <container_name>
```

---

# 47. Docker – Test API from Host

If container publishes port 8080:

```bash
curl http://localhost:8080
```

Health endpoint:

```bash
curl http://localhost:8080/health
```

---

# 48. Kubernetes – Check Pods

```bash
kubectl get pods
```

All namespaces:

```bash
kubectl get pods -A
```

Detailed information:

```bash
kubectl get pods -o wide
```

---

# 49. Kubernetes – Check Service

```bash
kubectl get svc
```

Detailed service information:

```bash
kubectl describe svc <service-name>
```

---

# 50. Kubernetes – Check Endpoints

```bash
kubectl get endpoints
```

Modern Kubernetes:

```bash
kubectl get endpointslices
```

This is useful when a Service exists but traffic is not reaching Pods.

---

# 51. Kubernetes – Check Ingress

```bash
kubectl get ingress
```

Detailed:

```bash
kubectl describe ingress <ingress-name>
```

---

# 52. Kubernetes – Check API Application Logs

```bash
kubectl logs <pod-name>
```

Follow logs:

```bash
kubectl logs -f <pod-name>
```

Previous container:

```bash
kubectl logs <pod-name> --previous
```

---

# 53. Kubernetes – Port Forward

Forward local port 8080 to a Service:

```bash
kubectl port-forward svc/my-api 8080:80
```

Then test:

```bash
curl http://localhost:8080
```

Health check:

```bash
curl http://localhost:8080/health
```

---

# 54. Kubernetes – Execute curl from a Pod

If a debugging container has curl:

```bash
kubectl exec -it <pod-name> -- curl http://my-api
```

Test a specific endpoint:

```bash
kubectl exec -it <pod-name> -- \
curl http://my-api/health
```

---

# 55. Kubernetes – Check DNS

From a debugging Pod:

```bash
kubectl exec -it <pod-name> -- \
nslookup my-api
```

You can also inspect DNS configuration:

```bash
kubectl exec -it <pod-name> -- cat /etc/resolv.conf
```

---

# 56. Kubernetes – Check Service Connectivity

```bash
kubectl exec -it <pod-name> -- \
curl http://my-api:80
```

If the Service uses a different port, replace `80`.

---

# 57. Kubernetes – Check Pod IP

```bash
kubectl get pods -o wide
```

This shows:

* Pod IP
* Node
* Status

---

# 58. Kubernetes – Check Events

```bash
kubectl get events
```

Sort by creation time:

```bash
kubectl get events --sort-by=.metadata.creationTimestamp
```

Events are useful for troubleshooting:

* Scheduling
* Networking
* Image problems
* Readiness
* Configuration

---

# 59. HTTP Status Code Testing

Check status:

```bash
curl -o /dev/null -s -w "%{http_code}\n" https://example.com
```

Possible results:

```text
200 → Success
201 → Created
204 → No Content
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
429 → Too Many Requests
500 → Internal Server Error
502 → Bad Gateway
503 → Service Unavailable
504 → Gateway Timeout
```

---

# 60. API Health Check Script

Create:

```bash
nano api-health.sh
```

Example:

```bash
#!/bin/bash

URL="https://api.example.com/health"

STATUS=$(curl -o /dev/null -s -w "%{http_code}" "$URL")

if [ "$STATUS" -eq 200 ]; then
    echo "API is healthy: HTTP $STATUS"
else
    echo "API is unhealthy: HTTP $STATUS"
fi
```

Make executable:

```bash
chmod +x api-health.sh
```

Run:

```bash
./api-health.sh
```

---

# 61. API Response Time Script

```bash
#!/bin/bash

URL="https://api.example.com/health"

curl -o /dev/null -s \
-w "HTTP Status: %{http_code}\nResponse Time: %{time_total}s\n" \
"$URL"
```

---

# 62. Test API from CI/CD

A simple CI/CD check:

```bash
STATUS=$(curl -o /dev/null -s -w "%{http_code}" \
https://api.example.com/health)

if [ "$STATUS" -ne 200 ]; then
    echo "API health check failed"
    exit 1
fi

echo "API health check passed"
```

If the API is unhealthy, the pipeline exits with:

```text
exit 1
```

---

# 63. Useful curl Options

| Option              | Purpose                    |
| ------------------- | -------------------------- |
| `-X`                | Specify HTTP method        |
| `-H`                | Add HTTP header            |
| `-d`                | Send request data          |
| `-i`                | Show response headers      |
| `-I`                | HEAD request               |
| `-v`                | Verbose output             |
| `-L`                | Follow redirects           |
| `-o`                | Save output to file        |
| `-O`                | Save using remote filename |
| `-u`                | Basic authentication       |
| `-A`                | Set User-Agent             |
| `-s`                | Silent mode                |
| `-f`                | Fail on HTTP errors        |
| `-w`                | Custom output format       |
| `--connect-timeout` | Connection timeout         |
| `--max-time`        | Maximum request time       |

---

# 64. REST API Troubleshooting Command Flow

When an API is not working, follow this sequence:

```text
1. DNS
   ↓
2. TCP
   ↓
3. TLS
   ↓
4. HTTP
   ↓
5. Authentication
   ↓
6. Application
   ↓
7. Database
```

Commands:

### Step 1 – DNS

```bash
dig +short api.example.com
```

### Step 2 – TCP

```bash
nc -vz api.example.com 443
```

### Step 3 – TLS

```bash
openssl s_client \
  -connect api.example.com:443 \
  -servername api.example.com
```

### Step 4 – HTTP

```bash
curl -v https://api.example.com
```

### Step 5 – Status code

```bash
curl -o /dev/null -s -w "%{http_code}\n" \
https://api.example.com
```

### Step 6 – Logs

Docker:

```bash
docker logs <container>
```

Kubernetes:

```bash
kubectl logs <pod>
```

---

# 65. Most Important Commands to Remember

For DevOps interviews and real-world troubleshooting, remember these first:

```bash
curl -i https://example.com
```

```bash
curl -v https://example.com
```

```bash
curl -I https://example.com
```

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"name":"Shraddha"}' \
  https://api.example.com/users
```

```bash
curl -o /dev/null -s -w "%{http_code}\n" https://example.com
```

```bash
dig +short example.com
```

```bash
nc -vz example.com 443
```

```bash
ss -tulnp
```

```bash
openssl s_client -connect example.com:443
```

```bash
docker logs <container>
```

```bash
kubectl logs <pod>
```

```bash
kubectl get svc
```

```bash
kubectl get endpoints
```

```bash
kubectl get ingress
```

---

# 66. Quick Revision

```text
curl -i       → Headers + body
curl -I       → Headers only
curl -v       → Detailed HTTP debugging
curl -X       → Specify HTTP method
curl -H       → Add header
curl -d       → Send data
curl -L       → Follow redirects
curl -u       → Basic authentication
curl -w       → Custom output
curl -o       → Save response

dig           → DNS troubleshooting
nslookup      → DNS lookup
nc            → TCP connectivity
ss            → Socket/port information
openssl       → TLS/certificate troubleshooting

docker ps     → Running containers
docker logs   → Container logs

kubectl get pods
kubectl get svc
kubectl get endpoints
kubectl get ingress
kubectl logs
```

## Final DevOps API Troubleshooting Formula

```text
DNS
 ↓
TCP
 ↓
TLS
 ↓
HTTP
 ↓
Authentication
 ↓
Application
 ↓
Database
```

This sequence is one of the most useful troubleshooting patterns for a DevOps engineer.
