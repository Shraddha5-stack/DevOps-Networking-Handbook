# REST API – Notes

## 1. What is an API?

**API** stands for **Application Programming Interface**.

An API allows two or more software applications to communicate with each other.

### Simple Example

A frontend application needs user information.

Instead of directly accessing the database:

```text
Frontend → API → Backend → Database
```

The API acts as a communication layer between applications.

---

# 2. What is REST?

**REST** stands for **Representational State Transfer**.

REST is an architectural style used to design web APIs.

REST APIs commonly use:

* HTTP
* JSON
* URLs
* HTTP methods
* HTTP status codes

Example:

```text
GET /users/101
```

This means:

> Get information about user 101.

---

# 3. REST API Architecture

A typical REST API architecture looks like:

```text
Client
  |
  | HTTP Request
  ↓
REST API
  |
  ↓
Backend Application
  |
  ↓
Database
```

Response:

```text
Database
   |
   ↓
Backend
   |
   ↓
REST API
   |
   | HTTP Response
   ↓
Client
```

---

# 4. Client

The **client** is the application that sends a request to the API.

Examples:

* Web browser
* Mobile application
* Frontend application
* Postman
* curl
* Python program
* CI/CD pipeline

Example:

```text
Browser → API
```

---

# 5. Server

The **server** receives the API request, processes it, and sends a response.

Example:

```text
Client
  |
  | GET /users
  ↓
API Server
  |
  ↓
Database
  |
  ↓
API Server
  |
  | JSON Response
  ↓
Client
```

---

# 6. REST Resources

In REST, everything is represented as a **resource**.

Examples:

```text
/users
/products
/orders
/customers
/servers
/projects
```

A specific resource can be identified using an ID.

Example:

```text
/users/101
/products/500
/orders/2001
```

---

# 7. HTTP Methods

REST APIs use HTTP methods to perform operations.

| Method | Purpose               |
| ------ | --------------------- |
| GET    | Read data             |
| POST   | Create data           |
| PUT    | Replace/update data   |
| PATCH  | Partially update data |
| DELETE | Delete data           |

---

# 8. GET

`GET` is used to retrieve information.

Example:

```http
GET /users
```

Get all users.

Specific user:

```http
GET /users/101
```

Get user with ID `101`.

Example response:

```json
{
  "id": 101,
  "name": "Shraddha",
  "role": "DevOps Engineer"
}
```

---

# 9. POST

`POST` is used to create a new resource.

Example:

```http
POST /users
```

Request body:

```json
{
  "name": "Shraddha",
  "role": "DevOps Engineer"
}
```

The server may return:

```http
201 Created
```

---

# 10. PUT

`PUT` is generally used to replace an existing resource.

Example:

```http
PUT /users/101
```

Request:

```json
{
  "name": "Shraddha",
  "role": "Cloud Engineer"
}
```

---

# 11. PATCH

`PATCH` is used for a partial update.

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

Only the specified field is changed.

---

# 12. DELETE

`DELETE` removes a resource.

Example:

```http
DELETE /users/101
```

Possible response:

```http
204 No Content
```

---

# 13. CRUD Operations

CRUD stands for:

```text
C → Create
R → Read
U → Update
D → Delete
```

REST mapping:

| CRUD   | HTTP Method |
| ------ | ----------- |
| Create | POST        |
| Read   | GET         |
| Update | PUT / PATCH |
| Delete | DELETE      |

Example:

```text
POST   /users
GET    /users
GET    /users/101
PUT    /users/101
PATCH  /users/101
DELETE /users/101
```

---

# 14. HTTP Request

An HTTP request generally contains:

```text
Method
URL
Headers
Body
```

Example:

```http
POST /users HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
  "name": "Shraddha"
}
```

---

# 15. HTTP Response

An HTTP response contains:

```text
Status Code
Headers
Body
```

Example:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 101,
  "name": "Shraddha"
}
```

---

# 16. HTTP Status Codes

Status codes tell the client what happened with the request.

## 2xx – Success

### 200 OK

Request completed successfully.

```text
GET /users
→ 200 OK
```

### 201 Created

A new resource was created.

```text
POST /users
→ 201 Created
```

### 204 No Content

Request succeeded but there is no response body.

Common example:

```text
DELETE /users/101
→ 204 No Content
```

---

# 17. 4xx – Client Errors

## 400 Bad Request

The request is invalid.

```text
400 Bad Request
```

## 401 Unauthorized

Authentication is required or credentials are invalid.

```text
401 Unauthorized
```

## 403 Forbidden

The client is authenticated but does not have permission.

```text
403 Forbidden
```

## 404 Not Found

The requested resource does not exist.

```text
404 Not Found
```

## 409 Conflict

The request conflicts with the current resource state.

```text
409 Conflict
```

---

# 18. 5xx – Server Errors

## 500 Internal Server Error

A general server-side error.

```text
500 Internal Server Error
```

## 502 Bad Gateway

A gateway or proxy received an invalid response from an upstream server.

```text
502 Bad Gateway
```

## 503 Service Unavailable

The server is temporarily unavailable.

```text
503 Service Unavailable
```

## 504 Gateway Timeout

The gateway did not receive a response from the upstream server in time.

```text
504 Gateway Timeout
```

---

# 19. Path Parameters

A path parameter identifies a specific resource.

Example:

```text
/users/101
```

Here:

```text
101
```

is the user ID.

Another example:

```text
/products/500
```

---

# 20. Query Parameters

Query parameters are used to filter, search, sort, or paginate data.

Example:

```text
/users?role=devops
```

Multiple parameters:

```text
/users?role=devops&location=pune
```

Pagination:

```text
/users?page=2&limit=10
```

---

# 21. Path Parameter vs Query Parameter

| Path Parameter        | Query Parameter              |
| --------------------- | ---------------------------- |
| Identifies a resource | Filters/modifies the request |
| Usually required      | Often optional               |
| `/users/101`          | `/users?role=devops`         |
| Resource identity     | Search/filter/pagination     |

Example:

```text
/users/101
```

means:

> User 101.

While:

```text
/users?role=devops
```

means:

> Users whose role is DevOps.

---

# 22. JSON

REST APIs commonly use **JSON** for data exchange.

JSON stands for:

**JavaScript Object Notation**

Example:

```json
{
  "id": 101,
  "name": "Shraddha",
  "skills": [
    "Linux",
    "Docker",
    "Kubernetes",
    "AWS"
  ]
}
```

JSON is:

* Lightweight
* Human-readable
* Easy to parse
* Widely supported

---

# 23. HTTP Headers

Headers provide additional information about a request or response.

Example:

```http
Content-Type: application/json
```

Common headers:

```text
Content-Type
Accept
Authorization
User-Agent
Host
Cache-Control
```

---

# 24. Content-Type

`Content-Type` tells the server what type of data is being sent.

Example:

```http
Content-Type: application/json
```

This means the request body contains JSON.

---

# 25. Accept Header

The `Accept` header tells the server what response format the client expects.

Example:

```http
Accept: application/json
```

---

# 26. Authentication

Authentication verifies **who the user or client is**.

Common API authentication methods include:

* API keys
* Basic authentication
* Bearer tokens
* OAuth 2.0
* JWT

Example:

```http
Authorization: Bearer <token>
```

---

# 27. Authorization

Authorization determines **what an authenticated user is allowed to do**.

Example:

```text
Authentication:
Who are you?

Authorization:
What are you allowed to access?
```

Example:

```text
Developer → Read application logs
Admin     → Read + Delete application logs
```

---

# 28. API Key

An API key is a value used to identify or authenticate an API client.

Example:

```http
X-API-Key: <API_KEY>
```

API keys should never be hard-coded into public repositories.

Bad:

```python
API_KEY = "my-secret-key"
```

Better:

```python
API_KEY = os.getenv("API_KEY")
```

---

# 29. Bearer Token

A bearer token is commonly sent using the `Authorization` header.

Example:

```http
Authorization: Bearer eyJ...
```

The server validates the token before allowing access.

---

# 30. HTTPS and REST APIs

REST APIs should use **HTTPS** to protect data while it travels over the network.

Architecture:

```text
Client
  |
  | HTTPS
  ↓
Load Balancer
  |
  ↓
REST API
  |
  ↓
Database
```

HTTPS provides encryption and helps protect credentials, tokens, and sensitive data.

---

# 31. REST Statelessness

One important REST principle is **statelessness**.

Each request should contain the information necessary for the server to process it.

Example:

```text
Request 1 → Authentication Token
Request 2 → Authentication Token
Request 3 → Authentication Token
```

The server should not depend on remembering the previous request.

---

# 32. Stateless vs Stateful

### Stateless

```text
Client → Request → Server
Client → Request → Server
Client → Request → Server
```

Each request contains required information.

### Stateful

```text
Client → Request → Server
             |
             ↓
          Session
```

The server maintains client state between requests.

---

# 33. REST API Versioning

APIs may change over time.

Versioning helps maintain compatibility.

Example:

```text
/api/v1/users
/api/v2/users
```

Example:

```text
GET /api/v1/users
```

and:

```text
GET /api/v2/users
```

---

# 34. API Pagination

Returning thousands of records at once can be inefficient.

Pagination divides results into smaller pages.

Example:

```text
/users?page=1&limit=10
```

Meaning:

```text
Page = 1
Limit = 10 users
```

Another request:

```text
/users?page=2&limit=10
```

---

# 35. API Rate Limiting

Rate limiting controls how many requests a client can make within a period.

Example:

```text
100 requests / minute
```

If the client exceeds the limit, the API may return:

```text
429 Too Many Requests
```

Rate limiting helps prevent:

* Abuse
* Excessive traffic
* Resource exhaustion
* Some types of denial-of-service activity

---

# 36. REST API Example

Suppose we have a user management API.

### Get users

```http
GET /api/v1/users
```

### Get one user

```http
GET /api/v1/users/101
```

### Create user

```http
POST /api/v1/users
```

### Update user

```http
PUT /api/v1/users/101
```

### Partially update user

```http
PATCH /api/v1/users/101
```

### Delete user

```http
DELETE /api/v1/users/101
```

---

# 37. REST API with curl

GET request:

```bash
curl https://api.example.com/users
```

Verbose request:

```bash
curl -v https://api.example.com/users
```

Show headers:

```bash
curl -i https://api.example.com/users
```

POST request:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"name":"Shraddha"}' \
  https://api.example.com/users
```

GET a specific resource:

```bash
curl https://api.example.com/users/101
```

DELETE:

```bash
curl -X DELETE https://api.example.com/users/101
```

---

# 38. REST API Testing Tools

Common tools:

```text
curl
Postman
Insomnia
HTTPie
Python requests
Browser
```

In DevOps, `curl` is especially useful for troubleshooting APIs from Linux servers.

---

# 39. REST API and DNS

Before a client connects to an API hostname, DNS may resolve the hostname to an IP address.

Example:

```text
api.example.com
       |
       ↓
      DNS
       |
       ↓
192.0.2.10
```

Then:

```text
Client
  |
  | TCP connection
  ↓
API Server
```

For HTTPS:

```text
DNS
 ↓
TCP
 ↓
TLS
 ↓
HTTP
 ↓
REST API
```

---

# 40. REST API and Load Balancer

Production APIs often run behind a load balancer.

```text
                ┌──→ API Server 1
                |
Client → Load Balancer
                |
                ├──→ API Server 2
                |
                └──→ API Server 3
```

Benefits:

* High availability
* Load distribution
* Scalability
* Health checks
* TLS termination

---

# 41. REST API and Reverse Proxy

A reverse proxy can sit in front of an API.

```text
Client
  |
  ↓
Nginx
  |
  ↓
REST API
```

The reverse proxy can provide:

* TLS termination
* Routing
* Load balancing
* Rate limiting
* Caching
* Access logging

---

# 42. REST API in Docker

A REST API can run inside a Docker container.

Example:

```text
Client
  |
  ↓
Docker Host
  |
  ↓
API Container
```

Check running containers:

```bash
docker ps
```

Check container logs:

```bash
docker logs <container>
```

Test an API:

```bash
curl http://localhost:8080
```

---

# 43. REST API in Kubernetes

In Kubernetes, an API application may run as Pods behind a Service.

```text
Client
  |
  ↓
Ingress
  |
  ↓
Service
  |
  ↓
Pods
```

Example:

```bash
kubectl get pods
```

```bash
kubectl get svc
```

```bash
kubectl get ingress
```

Test an application:

```bash
kubectl port-forward svc/my-api 8080:80
```

Then:

```bash
curl http://localhost:8080
```

---

# 44. REST API and CI/CD

REST APIs are heavily used in CI/CD.

Examples:

```text
GitHub API
GitLab API
Jira API
Docker Registry API
Kubernetes API
AWS APIs
```

A CI/CD pipeline can use APIs to:

* Trigger deployments
* Create releases
* Update tickets
* Retrieve artifacts
* Query deployment status
* Send notifications

Example:

```text
Git Push
   ↓
CI Pipeline
   ↓
Build
   ↓
Test
   ↓
REST API
   ↓
Deployment
```

---

# 45. Kubernetes API Server

Kubernetes itself exposes an API.

Architecture:

```text
kubectl
   |
   ↓
Kubernetes API Server
   |
   ├──→ etcd
   ├──→ Scheduler
   └──→ Controllers
```

Example:

```bash
kubectl get pods
```

Behind the scenes, `kubectl` communicates with the Kubernetes API server.

---

# 46. Cloud APIs

Cloud providers expose APIs for managing infrastructure.

Examples:

```text
Create EC2 instance
Create S3 bucket
Create VPC
Create Load Balancer
Create IAM resources
```

Terraform and other automation tools use cloud APIs to create and manage infrastructure.

Example:

```text
Terraform
   |
   ↓
Cloud API
   |
   ↓
AWS Resources
```

---

# 47. REST API Monitoring

APIs should be monitored in production.

Important metrics:

```text
Request count
Response time
Error rate
HTTP status codes
Throughput
Availability
Latency
```

Example:

```text
API Requests
     |
     ↓
Monitoring
     |
     ├──→ Metrics
     ├──→ Logs
     └──→ Alerts
```

---

# 48. API Logging

API logs help troubleshoot problems.

Example:

```text
2026-09-02 10:30:01
GET /users/101
200
120ms
```

Important log fields:

```text
Timestamp
HTTP Method
URL
Status Code
Response Time
Client IP
Request ID
```

---

# 49. Common REST API Problems

### 404 Not Found

Possible causes:

```text
Wrong URL
Wrong endpoint
Wrong resource ID
Incorrect API version
```

### 401 Unauthorized

Possible causes:

```text
Missing token
Expired token
Invalid credentials
```

### 403 Forbidden

Possible causes:

```text
Insufficient permissions
Incorrect role
Access policy restriction
```

### 429 Too Many Requests

Possible cause:

```text
Rate limit exceeded
```

### 500 Internal Server Error

Possible causes:

```text
Application error
Database error
Unexpected exception
```

### 502 Bad Gateway

Possible causes:

```text
Backend unavailable
Reverse proxy problem
Invalid upstream response
```

### 503 Service Unavailable

Possible causes:

```text
Server overloaded
Application down
No healthy backend
```

---

# 50. REST API Troubleshooting Flow

When an API is not working:

```text
1. Check DNS
      ↓
2. Check network connectivity
      ↓
3. Check TCP connection
      ↓
4. Check TLS/HTTPS
      ↓
5. Check HTTP status code
      ↓
6. Check API logs
      ↓
7. Check backend
      ↓
8. Check database
```

Useful commands:

```bash
nslookup api.example.com
```

```bash
dig api.example.com
```

```bash
ping api.example.com
```

```bash
curl -v https://api.example.com
```

```bash
curl -I https://api.example.com
```

```bash
ss -tulnp
```

---

# 51. REST Principles

Important REST principles include:

1. Client-server architecture
2. Statelessness
3. Cacheability
4. Uniform interface
5. Layered system
6. Code-on-demand (optional)

The most commonly discussed REST characteristics are:

```text
Client-Server
Stateless
Cacheable
Uniform Interface
Layered System
```

---

# 52. REST API Request Flow

A complete request may look like:

```text
User
 |
 ↓
Browser / Application
 |
 ↓
DNS
 |
 ↓
Load Balancer
 |
 ↓
Reverse Proxy
 |
 ↓
REST API
 |
 ↓
Authentication
 |
 ↓
Business Logic
 |
 ↓
Database
 |
 ↓
REST API
 |
 ↓
JSON Response
 |
 ↓
Client
```

---

# 53. DevOps Engineer Responsibilities with REST APIs

A DevOps engineer may need to:

* Deploy APIs
* Configure DNS
* Configure HTTPS
* Configure reverse proxies
* Configure load balancers
* Monitor API performance
* Troubleshoot HTTP errors
* Configure Kubernetes Ingress
* Manage API secrets
* Automate API calls
* Test endpoints
* Monitor logs
* Configure alerts
* Integrate APIs with CI/CD

---

# 54. Important Commands

Check API response:

```bash
curl -i https://example.com
```

Verbose debugging:

```bash
curl -v https://example.com
```

Only headers:

```bash
curl -I https://example.com
```

DNS:

```bash
dig example.com
```

Network connections:

```bash
ss -tulnp
```

Test HTTPS:

```bash
curl -v https://example.com
```

---

# 55. Interview Quick Revision

### What is REST?

REST is an architectural style for designing networked applications using resources and standard HTTP operations.

### What is REST API?

A REST API is an API that follows REST principles and commonly uses HTTP and JSON for communication.

### What is GET?

Used to retrieve resources.

### What is POST?

Used to create a resource.

### What is PUT?

Generally used to replace/update a resource.

### What is PATCH?

Used for partial updates.

### What is DELETE?

Used to delete a resource.

### What is JSON?

A lightweight data-interchange format commonly used by REST APIs.

### What is statelessness?

Each request contains the information needed to process it, without relying on stored client state between requests.

### Difference between 401 and 403?

```text
401 → Authentication problem
403 → Permission problem
```

### Difference between PUT and PATCH?

```text
PUT   → Generally replaces the resource
PATCH → Partially updates the resource
```

### What is 404?

The requested resource was not found.

### What is 500?

A server-side application error.

### What is 502?

A gateway or proxy received an invalid response from an upstream service.

### What is 503?

The service is temporarily unavailable.

### What is 429?

The client has sent too many requests.

---

# 56. Final REST API Architecture

```text
                         Internet
                            |
                            ↓
                         DNS
                            |
                            ↓
                      Load Balancer
                            |
                            ↓
                      Reverse Proxy
                            |
                            ↓
                       REST API
                            |
             ┌──────────────┼──────────────┐
             ↓              ↓              ↓
       Authentication   Business Logic   Logging
                            |
                            ↓
                         Database
                            |
                            ↓
                      JSON Response
                            |
                            ↓
                          Client
```

---

# 57. Key Takeaways

Remember these points:

```text
REST = Representational State Transfer

API = Application Programming Interface

GET    → Read
POST   → Create
PUT    → Replace/Update
PATCH  → Partial Update
DELETE → Delete

2xx → Success
4xx → Client Error
5xx → Server Error

401 → Unauthorized
403 → Forbidden
404 → Not Found
429 → Too Many Requests
500 → Internal Server Error
502 → Bad Gateway
503 → Service Unavailable
504 → Gateway Timeout
```

For a DevOps engineer, understanding REST APIs is important because **Kubernetes, cloud platforms, CI/CD systems, monitoring tools, Git platforms, and automation tools heavily rely on APIs**.
