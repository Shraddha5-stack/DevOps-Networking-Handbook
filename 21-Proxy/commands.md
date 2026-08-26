# Chapter 21 — Proxy Commands

## Table of Contents

1. Check Proxy Environment Variables
2. Check HTTP Proxy
3. Check HTTPS Proxy
4. Check NO_PROXY
5. Test HTTP Through a Proxy
6. Test HTTPS Through a Proxy
7. Test Proxy Connectivity
8. Check DNS Resolution
9. Check HTTP Headers
10. Test with curl Verbose Mode
11. Test with curl Proxy Option
12. Bypass Proxy with curl
13. Check Nginx Installation
14. Check Nginx Version
15. Check Nginx Configuration
16. Test Nginx Configuration
17. Check Nginx Status
18. Check Nginx Listening Ports
19. Check Listening Services
20. Check Network Connections
21. Check Proxy Process
22. Check Proxy Port
23. Check Environment Variables for a Process
24. Docker Proxy Variables
25. Docker Environment
26. Kubernetes Proxy Variables
27. Check Proxy with wget
28. Proxy Troubleshooting Flow

---

# 1. Check Proxy Environment Variables

Command:

```bash
env | grep -i proxy
```

### Purpose

Displays environment variables related to proxy configuration.

Common variables:

```text
HTTP_PROXY
HTTPS_PROXY
NO_PROXY
http_proxy
https_proxy
no_proxy
```

---

# 2. Check HTTP Proxy

```bash
echo $HTTP_PROXY
```

Lowercase version:

```bash
echo $http_proxy
```

### Purpose

Checks whether an HTTP proxy is configured for the current shell.

---

# 3. Check HTTPS Proxy

```bash
echo $HTTPS_PROXY
```

Lowercase:

```bash
echo $https_proxy
```

### Purpose

Checks the proxy configuration used for HTTPS requests.

---

# 4. Check NO_PROXY

```bash
echo $NO_PROXY
```

Lowercase:

```bash
echo $no_proxy
```

### Purpose

Shows destinations that should bypass the proxy.

Example:

```text
localhost,127.0.0.1,.internal.example.com
```

---

# 5. Test HTTP Through a Proxy

General syntax:

```bash
curl -x http://<proxy-host>:<proxy-port> http://example.com
```

Example:

```bash
curl -x http://192.168.1.10:8080 http://example.com
```

### Purpose

Tests whether an HTTP request can be sent through a proxy.

> Replace the example proxy address with your actual proxy.

---

# 6. Test HTTPS Through a Proxy

```bash
curl -x http://<proxy-host>:<proxy-port> https://example.com
```

### Purpose

Tests HTTPS connectivity through a proxy.

---

# 7. Test Proxy Connectivity

```bash
nc -zv <proxy-host> <proxy-port>
```

Example:

```bash
nc -zv 192.168.1.10 8080
```

### Purpose

Checks whether the proxy host and port are reachable.

Possible result:

```text
succeeded
```

or:

```text
Connection refused
```

---

# 8. Check DNS Resolution

```bash
getent hosts example.com
```

Alternative:

```bash
nslookup example.com
```

If installed:

```bash
dig example.com
```

### Purpose

Checks whether a hostname can be resolved to an IP address.

---

# 9. Check HTTP Headers

```bash
curl -I https://example.com
```

### Purpose

Displays HTTP response headers without downloading the full response body.

Useful for checking:

- HTTP status
- Server
- Redirects
- Cache headers

---

# 10. Test with curl Verbose Mode

```bash
curl -v https://example.com
```

### Purpose

Shows detailed connection information.

Useful for troubleshooting:

- DNS
- TCP connection
- TLS
- HTTP
- Proxy behavior

---

# 11. Test with curl Proxy Option

```bash
curl -v -x http://<proxy-host>:<proxy-port> https://example.com
```

### Explanation

```text
-v
```

Enables verbose output.

```text
-x
```

Specifies the proxy.

---

# 12. Bypass Proxy with curl

```bash
curl --noproxy '*' https://example.com
```

### Purpose

Temporarily bypasses the configured proxy for the request.

Useful for comparing:

```text
Through Proxy
```

versus:

```text
Direct Connection
```

---

# 13. Check Nginx Installation

```bash
nginx -v
```

### Purpose

Checks whether Nginx is installed and displays its version.

---

# 14. Check Nginx Version

```bash
nginx -V
```

### Purpose

Displays detailed Nginx build information.

---

# 15. Check Nginx Configuration

```bash
sudo nginx -T
```

### Purpose

Displays the complete active Nginx configuration.

This is useful when troubleshooting reverse proxy configuration.

---

# 16. Test Nginx Configuration

```bash
sudo nginx -t
```

### Expected result

```text
syntax is ok
test is successful
```

### Purpose

Checks Nginx configuration syntax before reloading or restarting it.

---

# 17. Check Nginx Status

```bash
sudo systemctl status nginx
```

### Purpose

Checks whether Nginx is running.

---

# 18. Check Nginx Listening Ports

```bash
sudo ss -ltnp | grep nginx
```

### Purpose

Checks which TCP ports Nginx is listening on.

Common ports:

```text
80
443
```

---

# 19. Check Listening Services

```bash
ss -tuln
```

### Purpose

Displays listening TCP and UDP ports.

With process information:

```bash
sudo ss -tulnp
```

---

# 20. Check Network Connections

```bash
ss -tun
```

### Purpose

Displays active TCP and UDP connections.

---

# 21. Check Proxy Process

```bash
ps aux | grep -i proxy
```

### Purpose

Searches running processes containing the word `proxy`.

A more specific command can be used when the proxy software is known.

---

# 22. Check Proxy Port

Example:

```bash
sudo ss -ltnp | grep :8080
```

### Purpose

Checks whether something is listening on TCP port `8080`.

---

# 23. Check Environment Variables for a Process

For your current shell:

```bash
printenv | grep -i proxy
```

### Purpose

Displays proxy-related environment variables.

For a known process:

```bash
cat /proc/<PID>/environ | tr '\0' '\n' | grep -i proxy
```

> Access may require appropriate permissions.

---

# 24. Docker Proxy Variables

Check current shell:

```bash
env | grep -i proxy
```

Run a container with proxy variables:

```bash
docker run --rm \
-e HTTP_PROXY="$HTTP_PROXY" \
-e HTTPS_PROXY="$HTTPS_PROXY" \
-e NO_PROXY="$NO_PROXY" \
ubuntu env | grep -i proxy
```

### Purpose

Demonstrates how proxy environment variables can be passed into a container.

---

# 25. Docker Environment

Check a container:

```bash
docker inspect <container-name>
```

To display environment variables:

```bash
docker inspect -f '{{range .Config.Env}}{{println .}}{{end}}' <container-name>
```

Filter proxy variables:

```bash
docker inspect -f '{{range .Config.Env}}{{println .}}{{end}}' <container-name> | grep -i proxy
```

---

# 26. Kubernetes Proxy Variables

Check proxy variables in a running container:

```bash
kubectl exec <pod-name> -- env | grep -i proxy
```

### Purpose

Checks whether proxy environment variables are configured inside a Kubernetes Pod.

---

# 27. Check Proxy with wget

Without proxy:

```bash
wget -S --spider https://example.com
```

Through a proxy:

```bash
wget -e use_proxy=yes \
-e http_proxy=http://<proxy-host>:<proxy-port> \
https://example.com
```

### Purpose

Tests web connectivity using `wget`.

---

# 28. Proxy Troubleshooting Flow

When an application cannot reach an external service, follow this sequence:

```text
1. Check proxy variables
        ↓
2. Check DNS
        ↓
3. Check proxy host
        ↓
4. Check proxy port
        ↓
5. Test proxy connectivity
        ↓
6. Test HTTP/HTTPS request
        ↓
7. Check NO_PROXY
        ↓
8. Check TLS certificates
        ↓
9. Check authentication
        ↓
10. Check application logs
```

Useful commands:

```bash
env | grep -i proxy
```

```bash
getent hosts example.com
```

```bash
nc -zv <proxy-host> <proxy-port>
```

```bash
curl -v https://example.com
```

```bash
curl -v -x http://<proxy-host>:<proxy-port> https://example.com
```

```bash
curl --noproxy '*' https://example.com
```

```bash
echo $NO_PROXY
```

---

# Important Safety Note

Do not paste real proxy usernames, passwords, API tokens, or other credentials into your public GitHub repository.

For example, avoid committing:

```text
http://username:password@proxy.example.com:8080
```

Use environment variables or a secure secrets-management solution instead.

---

# Quick Command Reference

| Command | Purpose |
|---|---|
| `env \| grep -i proxy` | Check proxy variables |
| `echo $HTTP_PROXY` | Check HTTP proxy |
| `echo $HTTPS_PROXY` | Check HTTPS proxy |
| `echo $NO_PROXY` | Check bypass list |
| `curl -I URL` | Check HTTP headers |
| `curl -v URL` | Detailed HTTP/TLS troubleshooting |
| `curl -x PROXY URL` | Use a proxy |
| `curl --noproxy '*' URL` | Bypass proxy |
| `nc -zv HOST PORT` | Test TCP connectivity |
| `getent hosts DOMAIN` | Test DNS |
| `nginx -t` | Test Nginx configuration |
| `systemctl status nginx` | Check Nginx |
| `ss -ltnp` | Check listening TCP ports |
| `docker inspect` | Inspect container configuration |
| `kubectl exec` | Check Pod environment |
| `wget` | Test web connectivity |

---

# Key Commands to Remember

For DevOps interviews and production troubleshooting, remember these first:

```bash
env | grep -i proxy
```

```bash
echo $NO_PROXY
```

```bash
curl -v https://example.com
```

```bash
curl -v -x http://<proxy-host>:<proxy-port> https://example.com
```

```bash
curl --noproxy '*' https://example.com
```

```bash
nc -zv <proxy-host> <proxy-port>
```

```bash
getent hosts example.com
```

```bash
sudo nginx -t
```

```bash
sudo ss -ltnp
```