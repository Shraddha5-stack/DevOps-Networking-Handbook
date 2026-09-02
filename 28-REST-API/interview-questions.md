# REST API – Interview Questions

## 1. What is an API?

**API** stands for **Application Programming Interface**.

It allows different software applications to communicate with each other.

Example:

```text
Frontend → API → Backend → Database
```

---

## 2. What is REST?

REST stands for **Representational State Transfer**.

It is an architectural style used to design network-based applications and APIs.

REST commonly uses:

* HTTP
* URLs
* HTTP methods
* JSON
* HTTP status codes

---

## 3. What is a REST API?

A REST API is an API designed around REST principles.

Example:

```http
GET /api/users/101
```

The API returns information about user `101`.

---

## 4. What are the main HTTP methods used in REST APIs?

| Method | Purpose               |
| ------ | --------------------- |
| GET    | Read data             |
| POST   | Create data           |
| PUT    | Replace/update data   |
| PATCH  | Partially update data |
| DELETE | Delete data           |

---

## 5. What is GET?

GET is used to retrieve data from a server.

Example:

```http
GET /users
```

Specific resource:

```http
GET /users/101
```

---

## 6. What is POST?

POST is generally used to create a new resource.

Example:

```http
POST /users
```

Request:

```json
{
  "name": "Shraddha",
  "role": "DevOps Engineer"
}
```

---

## 7. What is PUT?

PUT is generally used to replace the representation of an existing resource.

Example:

```http
PUT /users/101
```

---

## 8. What is PATCH?

PATCH is used to partially modify an existing resource.

Example:

```http
PATCH /users/101
```

Request:

```json
{
  "role": "Cloud Engineer"
}
```

---

## 9. What is DELETE?

DELETE is used to remove a resource.

Example:

```http
DELETE /users/101
```

---

## 10. PUT vs PATCH

### PUT

Generally replaces the resource representation.

```http
PUT /users/101
```

### PATCH

Changes only specified fields.

```http
PATCH /users/101
```

Interview answer:

> PUT is generally used for replacement, while PATCH is used for partial modification.

---

## 11. What is CRUD?

CRUD means:

```text
C → Create
R → Read
U → Update
D → Delete
```

REST mapping:

```text
Create → POST
Read   → GET
Update → PUT/PATCH
Delete → DELETE
```

---

## 12. What is a REST resource?

A resource is an object or entity exposed through an API.

Examples:

```text
/users
/products
/orders
/customers
```

Specific resources:

```text
/users/101
/products/500
/orders/1001
```

---

## 13. What is a URI/URL in REST?

It identifies the resource or endpoint being accessed.

Example:

```text
https://api.example.com/users/101
```

Here:

```text
https://        → Protocol
api.example.com → Host
/users/101      → Resource path
```

---

## 14. What is a path parameter?

A path parameter identifies a specific resource.

Example:

```text
/users/101
```

Here:

```text
101
```

is the resource identifier.

---

## 15. What is a query parameter?

Query parameters are commonly used for filtering, searching, sorting, and pagination.

Example:

```text
/users?role=devops
```

Multiple parameters:

```text
/users?role=devops&location=pune
```

---

## 16. Path Parameter vs Query Parameter

| Path Parameter                         | Query Parameter       |
| -------------------------------------- | --------------------- |
| Identifies a resource                  | Filters/searches data |
| `/users/101`                           | `/users?role=devops`  |
| Usually important to resource identity | Often optional        |
| Resource-specific                      | Request customization |

---

## 17. What is JSON?

JSON stands for **JavaScript Object Notation**.

It is commonly used to exchange data between clients and REST APIs.

Example:

```json
{
  "id": 101,
  "name": "Shraddha",
  "role": "DevOps Engineer"
}
```

---

## 18. Why is JSON commonly used with REST APIs?

JSON is:

* Lightweight
* Human-readable
* Easy to parse
* Supported by many programming languages
* Easy to send over HTTP

---

## 19. What are HTTP status codes?

HTTP status codes tell the client the result of an HTTP request.

Categories:

```text
1xx → Informational
2xx → Success
3xx → Redirection
4xx → Client errors
5xx → Server errors
```

---

## 20. What does HTTP 200 mean?

`200 OK` means the request was successfully processed.

Example:

```http
GET /users
→ 200 OK
```

---

## 21. What does HTTP 201 mean?

`201 Created` indicates that a new resource was successfully created.

Commonly used with:

```http
POST /users
```

---

## 22. What does HTTP 204 mean?

`204 No Content` means the request succeeded but there is no response body.

Example:

```http
DELETE /users/101
→ 204 No Content
```

---

## 23. What does HTTP 400 mean?

`400 Bad Request` means the server cannot process the request because the request is invalid.

Possible causes:

* Invalid JSON
* Missing required fields
* Invalid parameters
* Incorrect request format

---

## 24. What does HTTP 401 mean?

`401 Unauthorized` means authentication is required or the provided credentials are invalid.

Example:

```text
Missing token
Expired token
Invalid token
```

---

## 25. What does HTTP 403 mean?

`403 Forbidden` means the server understood the request, but the client does not have sufficient permission.

Example:

```text
User authenticated
        ↓
Insufficient permission
        ↓
403 Forbidden
```

---

## 26. 401 vs 403

```text
401 → Authentication problem
403 → Authorization/permission problem
```

Interview answer:

> 401 means the client has not successfully authenticated, while 403 means the client is authenticated or otherwise identified but is not allowed to access the resource.

---

## 27. What does HTTP 404 mean?

`404 Not Found` means the requested resource could not be found.

Example:

```http
GET /users/999999
```

If that user does not exist:

```text
404 Not Found
```

---

## 28. What does HTTP 409 mean?

`409 Conflict` indicates a conflict with the current state of the resource.

Example:

```text
Trying to create a username that already exists
```

---

## 29. What does HTTP 429 mean?

`429 Too Many Requests` means the client has exceeded the server's rate limit.

Example:

```text
100 requests/minute allowed
Client sends 150 requests
        ↓
429 Too Many Requests
```

---

## 30. What does HTTP 500 mean?

`500 Internal Server Error` indicates a general server-side error.

Possible causes:

* Application exception
* Database error
* Unexpected failure
* Application bug

---

## 31. What does HTTP 502 mean?

`502 Bad Gateway` means a gateway or proxy received an invalid response from an upstream server.

Architecture:

```text
Client
  ↓
Nginx
  ↓
Backend API
```

If the backend returns an invalid response:

```text
Nginx → 502 Bad Gateway
```

---

## 32. What does HTTP 503 mean?

`503 Service Unavailable` means the service is temporarily unable to handle the request.

Possible causes:

* Application is down
* Server overloaded
* No healthy backend
* Maintenance

---

## 33. What does HTTP 504 mean?

`504 Gateway Timeout` means a gateway or proxy did not receive a timely response from an upstream server.

Example:

```text
Client
  ↓
Load Balancer
  ↓
API Server
  ↓
Slow/Unavailable Backend
```

The gateway eventually returns:

```text
504 Gateway Timeout
```

---

## 34. What is statelessness in REST?

Statelessness means each request contains the information required to process it.

The server does not depend on remembering the client's previous request.

Example:

```text
Request 1 → Token
Request 2 → Token
Request 3 → Token
```

---

## 35. Why is statelessness useful?

Stateless APIs are easier to:

* Scale horizontally
* Load balance
* Recover
* Deploy
* Operate across multiple servers

Example:

```text
             ┌──→ API Server 1
Client → LB ─┼──→ API Server 2
             └──→ API Server 3
```

Any server can process the request if the required state is carried in the request or stored in an appropriate shared system.

---

## 36. What is authentication?

Authentication verifies the identity of a client or user.

Example:

```text
Who are you?
```

Common mechanisms:

* API keys
* Basic authentication
* Bearer tokens
* OAuth 2.0
* JWT

---

## 37. What is authorization?

Authorization determines what an authenticated client is allowed to do.

Example:

```text
Authentication:
Who are you?

Authorization:
What are you allowed to do?
```

---

## 38. What is a Bearer Token?

A bearer token is commonly sent in the `Authorization` header.

Example:

```http
Authorization: Bearer <TOKEN>
```

The server validates the token before granting access.

---

## 39. What is an API key?

An API key is a credential commonly used to identify or authenticate an API client.

Example:

```http
X-API-Key: <API_KEY>
```

Never commit real API keys to Git repositories.

---

## 40. What is HTTPS and why is it important for REST APIs?

HTTPS is HTTP protected by TLS.

It provides encryption and helps protect data transmitted between client and server.

Example:

```text
Client
  |
  | HTTPS
  ↓
REST API
```

It is especially important when transmitting:

* Passwords
* API keys
* Tokens
* Personal information
* Sensitive application data

---

## 41. What are HTTP headers?

Headers contain metadata about HTTP requests and responses.

Common headers:

```text
Content-Type
Accept
Authorization
User-Agent
Host
Cache-Control
```

Example:

```http
Content-Type: application/json
```

---

## 42. What is Content-Type?

`Content-Type` tells the server what format the request body uses.

Example:

```http
Content-Type: application/json
```

This indicates that the request body contains JSON.

---

## 43. What is the Accept header?

`Accept` tells the server which response media types the client can handle.

Example:

```http
Accept: application/json
```

---

## 44. How do you test a REST API from Linux?

The most common tool is `curl`.

Example:

```bash
curl -i https://example.com
```

Verbose:

```bash
curl -v https://example.com
```

---

## 45. How do you test a GET API using curl?

```bash
curl https://api.example.com/users
```

With headers:

```bash
curl \
-H "Accept: application/json" \
https://api.example.com/users
```

---

## 46. How do you send a POST request using curl?

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{"name":"Shraddha","role":"DevOps Engineer"}' \
https://api.example.com/users
```

---

## 47. How do you check only the HTTP status code?

```bash
curl -o /dev/null -s \
-w "%{http_code}\n" \
https://api.example.com
```

---

## 48. How do you debug an API using curl?

Use verbose mode:

```bash
curl -v https://api.example.com
```

This helps inspect:

* Connection
* TLS
* Request headers
* Response headers
* HTTP status

---

## 49. How do you check API response time?

```bash
curl -o /dev/null -s \
-w "Status: %{http_code}\nTime: %{time_total}s\n" \
https://api.example.com
```

---

## 50. How do you check DNS for an API?

Use:

```bash
dig +short api.example.com
```

or:

```bash
nslookup api.example.com
```

---

## 51. How do you check whether HTTPS port 443 is reachable?

Use:

```bash
nc -vz api.example.com 443
```

---

## 52. How do you troubleshoot an HTTPS connection?

Use:

```bash
curl -v https://api.example.com
```

For TLS certificate details:

```bash
openssl s_client \
-connect api.example.com:443 \
-servername api.example.com
```

---

## 53. How do you check listening ports on Linux?

```bash
ss -tulnp
```

For a specific port:

```bash
ss -tulnp | grep :8080
```

---

## 54. How do you troubleshoot a REST API that returns 502?

Start with:

```text
Client
  ↓
Load Balancer / Reverse Proxy
  ↓
API Server
```

Check:

1. Reverse proxy configuration
2. Backend availability
3. Backend port
4. Service endpoints
5. Application logs
6. Network connectivity

Useful commands:

```bash
curl -v https://api.example.com
```

```bash
docker logs <container>
```

```bash
kubectl logs <pod>
```

---

## 55. How do you troubleshoot a REST API returning 503?

Check:

```text
Application status
Load balancer health
Kubernetes Pods
Kubernetes Services
Endpoints
Application logs
```

Kubernetes commands:

```bash
kubectl get pods
```

```bash
kubectl get svc
```

```bash
kubectl get endpoints
```

```bash
kubectl logs <pod>
```

---

## 56. How do you troubleshoot a REST API returning 404?

Check:

* URL
* HTTP method
* API version
* Resource ID
* Routing
* Ingress configuration
* Reverse proxy configuration

Example:

```text
/api/v1/users
```

may not be the same endpoint as:

```text
/api/v2/users
```

---

## 57. How do you troubleshoot a REST API returning 401?

Check:

```text
Authorization header
Token
API key
Token expiration
Authentication configuration
```

Example:

```bash
curl \
-H "Authorization: Bearer $API_TOKEN" \
https://api.example.com/users
```

---

## 58. How do you troubleshoot a REST API returning 403?

Check:

* User permissions
* IAM policy
* RBAC
* API authorization rules
* Kubernetes RBAC
* Resource permissions

Remember:

```text
401 → Authentication
403 → Authorization
```

---

## 59. What is API rate limiting?

Rate limiting controls the number of requests a client can make during a specific period.

Example:

```text
100 requests/minute
```

If the client exceeds the limit:

```text
429 Too Many Requests
```

---

## 60. Why is rate limiting important?

It helps:

* Protect services
* Control resource usage
* Prevent excessive traffic
* Reduce abuse
* Maintain service availability

---

## 61. What is API pagination?

Pagination divides a large dataset into smaller responses.

Example:

```text
/users?page=1&limit=10
```

Another request:

```text
/users?page=2&limit=10
```

---

## 62. What is API versioning?

API versioning allows an API to evolve while maintaining compatibility for existing clients.

Example:

```text
/api/v1/users
/api/v2/users
```

---

## 63. How does DNS participate in an API request?

Example:

```text
api.example.com
       ↓
      DNS
       ↓
IP Address
       ↓
TCP Connection
       ↓
TLS
       ↓
HTTP Request
```

---

## 64. What is the complete API request flow?

A typical request can look like:

```text
Client
  ↓
DNS
  ↓
Load Balancer
  ↓
Reverse Proxy
  ↓
REST API
  ↓
Authentication
  ↓
Business Logic
  ↓
Database
  ↓
JSON Response
  ↓
Client
```

---

## 65. How are REST APIs used in DevOps?

REST APIs are used for automation and integration.

Examples:

```text
GitHub API
GitLab API
Jira API
Kubernetes API
AWS APIs
Docker Registry APIs
Monitoring APIs
```

DevOps engineers use APIs to:

* Trigger deployments
* Create releases
* Update tickets
* Query infrastructure
* Manage cloud resources
* Retrieve deployment status
* Automate operational tasks

---

## 66. How does Terraform use APIs?

Terraform communicates with infrastructure providers through provider APIs.

Example:

```text
Terraform
    ↓
AWS Provider
    ↓
AWS API
    ↓
AWS Resources
```

---

## 67. How does Kubernetes use APIs?

Kubernetes exposes an API through the **Kubernetes API server**.

For example:

```bash
kubectl get pods
```

Conceptually:

```text
kubectl
   ↓
Kubernetes API Server
   ↓
Kubernetes Resources
```

---

## 68. How can REST APIs be monitored?

Important metrics include:

```text
Request Count
Error Rate
Latency
Response Time
HTTP Status Codes
Throughput
Availability
```

Logs should also be monitored.

---

## 69. What should API logs contain?

Useful fields include:

```text
Timestamp
HTTP Method
Request Path
Status Code
Response Time
Request ID
Client Information
Error Details
```

Avoid logging sensitive credentials or tokens.

---

## 70. What is a health-check endpoint?

A health endpoint is used to determine whether a service is functioning.

Example:

```http
GET /health
```

Possible response:

```json
{
  "status": "healthy"
}
```

DevOps systems can use this endpoint for:

* Monitoring
* Load balancer checks
* Kubernetes probes
* CI/CD verification

---

# DevOps Scenario-Based Questions

## 71. Your API is returning 502. What will you check?

I would troubleshoot from the outside toward the backend:

```text
DNS
 ↓
TCP
 ↓
TLS
 ↓
Load Balancer
 ↓
Reverse Proxy
 ↓
Backend API
```

Then I would check:

```bash
curl -v https://api.example.com
```

Backend logs:

```bash
docker logs <container>
```

or:

```bash
kubectl logs <pod>
```

I would also verify that the backend service and port are reachable.

---

## 72. API is returning 503 in Kubernetes. What will you check?

I would check:

```bash
kubectl get pods
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

Then:

```bash
kubectl describe svc <service>
```

and:

```bash
kubectl logs <pod>
```

I would verify:

* Pods are Running
* Readiness probes are passing
* Service selector matches Pod labels
* Service has endpoints
* Application is listening on the expected port

---

## 73. API is slow. How would you troubleshoot it?

First measure the response time:

```bash
curl -o /dev/null -s \
-w "Time: %{time_total}s\n" \
https://api.example.com
```

Then investigate:

```text
DNS latency
Network latency
TLS handshake
Load balancer
Reverse proxy
Application processing
Database queries
External dependencies
```

I would also check application metrics and logs.

---

## 74. API works locally but not from another machine. What could be wrong?

Possible causes:

```text
Firewall
Security group
Network ACL
Incorrect bind address
Wrong port
DNS
Routing
Load balancer
Reverse proxy
```

For example, an application listening only on:

```text
127.0.0.1:8080
```

cannot normally be reached directly from another machine.

---

## 75. API works by IP but not by hostname. What will you check?

I would check DNS.

Commands:

```bash
dig +short api.example.com
```

```bash
nslookup api.example.com
```

Then compare the resolved IP with the expected server or load balancer address.

---

## 76. API returns 401 even though the token exists. What will you check?

I would check:

```text
Authorization header
Token format
Token expiration
Token issuer
Token audience
API authentication configuration
Clock/time issues
```

Example:

```http
Authorization: Bearer <TOKEN>
```

---

## 77. API returns 403 after successful authentication. What does it mean?

It usually means authentication succeeded but authorization failed.

I would check:

```text
User role
Permissions
IAM policy
RBAC
Resource permissions
API authorization rules
```

---

## 78. Kubernetes Service exists but API is unreachable. What will you check?

I would check:

```bash
kubectl get svc
```

Then:

```bash
kubectl get endpoints
```

If there are no endpoints, I would check the Service selector and Pod labels:

```bash
kubectl get pods --show-labels
```

Then check:

```bash
kubectl get pods -o wide
```

and:

```bash
kubectl logs <pod>
```

---

## 79. How would you test an API inside Kubernetes?

First check Pods:

```bash
kubectl get pods
```

Check Service:

```bash
kubectl get svc
```

Port-forward:

```bash
kubectl port-forward svc/my-api 8080:80
```

Then:

```bash
curl http://localhost:8080/health
```

---

## 80. How would you test API connectivity from one Kubernetes Pod to another?

From a debugging Pod:

```bash
curl http://my-api:80
```

Or:

```bash
kubectl exec -it <pod-name> -- \
curl http://my-api:80
```

If DNS is suspected:

```bash
kubectl exec -it <pod-name> -- \
nslookup my-api
```

---

# Rapid-Fire Revision

## REST Basics

```text
REST
→ Representational State Transfer

API
→ Application Programming Interface

GET
→ Read

POST
→ Create

PUT
→ Replace/update

PATCH
→ Partial update

DELETE
→ Delete
```

## Status Codes

```text
200 → OK
201 → Created
204 → No Content

400 → Bad Request
401 → Authentication problem
403 → Permission problem
404 → Not Found
409 → Conflict
429 → Too Many Requests

500 → Internal Server Error
502 → Bad Gateway
503 → Service Unavailable
504 → Gateway Timeout
```

## Troubleshooting Commands

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

Docker:

```bash
docker ps
docker logs <container>
```

Kubernetes:

```bash
kubectl get pods
kubectl get svc
kubectl get endpoints
kubectl logs <pod>
```

---

# Most Important Interview Answers

### REST API in one sentence

> A REST API is an HTTP-based API that exposes resources through URLs and uses standard HTTP methods to perform operations on those resources.

### 401 vs 403

> 401 is an authentication problem, while 403 is an authorization or permission problem.

### PUT vs PATCH

> PUT generally replaces a resource, while PATCH partially updates it.

### 502 vs 503

> 502 usually indicates an invalid response from an upstream service through a gateway or proxy, while 503 indicates that the service is currently unavailable.

### 404 vs 500

> 404 means the requested resource was not found, while 500 indicates an internal server-side error.

### DevOps API troubleshooting

> I start with DNS, then TCP connectivity, TLS, HTTP status, authentication, application logs, and finally backend or database dependencies.

---

# Final Interview Revision Flow

```text
                    REST API
                       |
          ┌────────────┼────────────┐
          ↓            ↓            ↓
       HTTP          JSON        Resources
          |
    ┌─────┼─────┬─────┬──────┐
    ↓     ↓     ↓     ↓      ↓
   GET   POST   PUT  PATCH  DELETE
          |
          ↓
      Status Codes
          |
     ┌────┼────┐
     ↓    ↓    ↓
    2xx  4xx  5xx
          |
          ↓
    Authentication
          |
          ↓
    Authorization
          |
          ↓
       HTTPS
          |
          ↓
       DevOps
          |
    ┌─────┼─────────────┐
    ↓     ↓             ↓
 Docker Kubernetes    Cloud
```

## Final Goal

By completing this chapter, you should be able to:

* Explain REST APIs clearly
* Understand HTTP methods
* Understand status codes
* Use `curl`
* Work with JSON
* Test API endpoints
* Troubleshoot API failures
* Understand authentication and authorization
* Troubleshoot APIs in Docker
* Troubleshoot APIs in Kubernetes
* Understand REST APIs in CI/CD and cloud environments
* Answer common REST API DevOps interview questions
