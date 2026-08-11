# 🛠️ Chapter 15 – Ports & Protocols Troubleshooting

## 🎯 Purpose

When an application is unreachable, don't immediately restart the server.

Troubleshoot systematically:

```text
DNS
 ↓
IP Address
 ↓
Routing
 ↓
Firewall
 ↓
Port
 ↓
Process
 ↓
Application
```

---

# 1. Check Listening Ports

Start with:

```bash
ss -tuln
```

For process information:

```bash
sudo ss -tulpn
```

Look for the expected port.

Example:

```text
LISTEN  0  128  0.0.0.0:8080
```

This indicates that something is listening on TCP port `8080`.

---

# 2. Port Is Not Listening

### Problem

You expect an application on port `8080`, but:

```bash
sudo ss -tulpn | grep :8080
```

returns nothing.

### Possible causes

* Application is stopped.
* Application failed to start.
* Application is configured for another port.
* Configuration is incorrect.
* Application crashed.

### Check the service

```bash
sudo systemctl status <service>
```

Check logs:

```bash
sudo journalctl -u <service>
```

---

# 3. Application Works on localhost but Not Remotely

Test locally:

```bash
curl http://localhost:8080
```

If this works but remote access fails, check the listening address:

```bash
sudo ss -tulpn | grep :8080
```

If you see:

```text
127.0.0.1:8080
```

the service is bound to the loopback interface.

This means remote hosts cannot normally connect directly to that socket.

Check the application's bind/listen configuration.

---

# 4. Port Is Blocked by Firewall

Check UFW:

```bash
sudo ufw status
```

If the required port is blocked, review the firewall rules.

For example:

```bash
sudo ufw status numbered
```

Do not blindly open ports.

Only allow ports that are required.

---

# 5. AWS Security Group Blocking Traffic

In AWS, a service may be listening correctly on the EC2 instance but still be unreachable from the Internet.

Check:

* Security Group inbound rules
* Network ACLs
* Route tables
* Load balancer configuration
* Instance subnet
* Application listening address

Example:

```text
Internet
   ↓
Security Group
   ↓
EC2
   ↓
Application
   ↓
Port 8080
```

A listening port does not automatically mean the port is reachable from the Internet.

---

# 6. Test Local TCP Connectivity

Use:

```bash
nc -zv localhost 8080
```

If successful:

```text
Connection to localhost 8080 port [tcp/*] succeeded!
```

the local TCP connection was accepted.

If it fails, investigate the service or listening socket.

---

# 7. Test Remote TCP Connectivity

From another machine:

```bash
nc -zv <server-ip> 8080
```

Possible outcomes:

### Connection succeeded

The TCP port is reachable.

### Connection refused

The host is reachable, but nothing accepted the connection on that address/port, or an active network device rejected it.

### Connection timed out

Possible causes include:

* Firewall
* Security Group
* Network ACL
* Routing problem
* Network path issue

---

# 8. Ping Works but Port Doesn't

Example:

```bash
ping <server-ip>
```

works.

But:

```bash
nc -zv <server-ip> 443
```

fails.

This is possible because `ping` uses ICMP while HTTPS normally uses TCP port `443`.

Therefore:

```text
ICMP
 ↓
Works

TCP 443
 ↓
Blocked / unavailable
```

Successful ping does **not** prove that a TCP service is reachable.

---

# 9. Port Is Listening but Application Still Fails

Suppose:

```bash
sudo ss -tulpn | grep :443
```

shows a listener.

But:

```bash
curl -v https://example.com
```

fails.

Investigate the application layer.

Check:

* TLS configuration
* Certificate
* Reverse proxy
* Application logs
* Backend connectivity
* HTTP response
* DNS

---

# 10. HTTPS/TLS Troubleshooting

Run:

```bash
curl -v https://example.com
```

Look for:

```text
DNS resolution
TCP connection
TLS handshake
Certificate
HTTP request
HTTP response
```

A failure during TLS indicates a different problem from a TCP connection failure.

---

# 11. Check HTTP Status Code

Run:

```bash
curl -I https://example.com
```

Common responses:

```text
200 → Success
301 → Permanent redirect
302 → Temporary redirect
400 → Bad request
401 → Unauthorized
403 → Forbidden
404 → Not found
500 → Internal server error
502 → Bad gateway
503 → Service unavailable
```

This helps determine whether the network connection succeeded but the application returned an error.

---

# 12. Find Which Process Uses a Port

Use:

```bash
sudo lsof -i :8080
```

You can also use:

```bash
sudo ss -tulpn | grep :8080
```

This is useful when multiple services or containers are running.

---

# 13. Port Already in Use

### Problem

You start an application and receive an error similar to:

```text
Address already in use
```

Check:

```bash
sudo ss -tulpn | grep :8080
```

or:

```bash
sudo lsof -i :8080
```

You may discover another application is already using the port.

### Resolution

Either:

* Stop the existing service if appropriate.
* Change the application's port.
* Correct the configuration.

Do not kill processes blindly in production.

---

# 14. Docker Port Conflict

Example:

```bash
docker run -p 8080:80 nginx
```

If host port `8080` is already occupied, Docker cannot bind that host port.

Check:

```bash
sudo ss -tulpn | grep :8080
```

Also check:

```bash
docker ps
```

Choose another host port if appropriate:

```bash
docker run -p 8081:80 nginx
```

Now:

```text
Host:8081
   ↓
Container:80
```

---

# 15. Docker Application Is Running but Inaccessible

Check:

```bash
docker ps
```

Look at the `PORTS` column.

Example:

```text
0.0.0.0:8080->80/tcp
```

This means:

```text
Host 8080
   ↓
Container 80
```

Then test:

```bash
curl http://localhost:8080
```

If it fails, inspect:

```bash
docker logs <container>
```

and:

```bash
docker inspect <container>
```

---

# 16. Kubernetes Service Not Reachable

Check Services:

```bash
kubectl get svc
```

Then:

```bash
kubectl describe svc <service-name>
```

Check Pods:

```bash
kubectl get pods
```

Verify:

* Service selector
* Endpoints
* `port`
* `targetPort`
* Pod labels
* Pod status

A Service can exist while having no healthy matching endpoints.

---

# 17. DNS Resolves but Application Doesn't Work

First:

```bash
nslookup example.com
```

If DNS resolution works, test the destination:

```bash
nc -zv example.com 443
```

Then:

```bash
curl -v https://example.com
```

This separates:

```text
DNS problem
```

from:

```text
TCP connectivity problem
```

and:

```text
Application/TLS problem
```

---

# 18. Check Routing

Use:

```bash
ip route
```

For a specific destination:

```bash
ip route get 8.8.8.8
```

This can show:

* Selected interface
* Next hop
* Source address
* Route selection

Incorrect routing can prevent access to a service even when the service itself is healthy.

---

# 19. Check the Service Status

For systemd services:

```bash
sudo systemctl status <service>
```

Restart only when appropriate:

```bash
sudo systemctl restart <service>
```

Then verify:

```bash
sudo ss -tulpn
```

and check logs:

```bash
sudo journalctl -u <service>
```

---

# 20. Common Error: Connection Refused

Example:

```text
Connection refused
```

Usually indicates that the destination host was reachable but the connection was not accepted on that port.

Possible causes:

* No service listening
* Wrong port
* Service stopped
* Incorrect bind address
* Active firewall rejection

Check:

```bash
sudo ss -tulpn | grep :<port>
```

---

# 21. Common Error: Connection Timed Out

Example:

```text
Connection timed out
```

Possible causes:

* Firewall silently dropping packets
* AWS Security Group
* Network ACL
* Routing issue
* Network path failure
* Host unavailable

Check network controls and routing.

---

# 22. Common Error: No Route to Host

Example:

```text
No route to host
```

Check:

```bash
ip route
```

Then verify:

```bash
ping <destination>
```

and inspect the network path.

---

# 23. Troubleshooting Decision Tree

```text
Application unreachable
        |
        v
Does DNS resolve?
   |             |
  No            Yes
   |             |
Fix DNS      Can you reach IP?
                 |
             +---+---+
             |       |
            No      Yes
             |       |
        Check route  Is port listening?
                         |
                    +----+----+
                    |         |
                   No        Yes
                    |         |
              Check service   Test TCP
                              |
                         +----+----+
                         |         |
                        Fail      Pass
                         |         |
                    Check firewall  Test app
                                    |
                                    v
                               curl / logs
```

---

# 24. Recommended Troubleshooting Order

Use this sequence:

```text
1. DNS
2. IP
3. Route
4. Firewall
5. Port
6. Process
7. Application
```

Commands:

```bash
nslookup <hostname>
```

```bash
ip route
```

```bash
sudo ss -tulpn
```

```bash
nc -zv <host> <port>
```

```bash
sudo lsof -i :<port>
```

```bash
curl -v <url>
```

```bash
sudo journalctl -u <service>
```

---

# 💼 Real-World DevOps Example

### Problem

A production application is reported as unavailable.

### Investigation

First verify DNS:

```bash
nslookup app.example.com
```

Then verify routing:

```bash
ip route
```

Check the listener:

```bash
sudo ss -tulpn | grep :443
```

Test TCP:

```bash
nc -zv app.example.com 443
```

Test HTTPS:

```bash
curl -v https://app.example.com
```

Check firewall/security controls.

Finally inspect application and proxy logs.

### Goal

Don't just ask:

> "Is the server up?"

Ask:

> **"At which layer is the request failing?"**

---

# ⭐ Interview Answer

### How do you troubleshoot a port connectivity issue?

> I start by verifying DNS and IP connectivity. Then I check the routing table and confirm that the expected service is listening on the required port using `ss -tulpn`. I test TCP connectivity using `nc`. If the port is reachable, I use `curl` to test the application layer. If remote access fails, I check host firewalls, cloud Security Groups, network ACLs, routing, and the application's bind address. Finally, I inspect service and application logs.

---

# 🧠 Quick Troubleshooting Cheat Sheet

| Problem            | First Check            |
| ------------------ | ---------------------- |
| DNS failure        | `nslookup` / `dig`     |
| No route           | `ip route`             |
| Port not listening | `ss -tulpn`            |
| Find process       | `lsof -i :PORT`        |
| TCP test           | `nc -zv`               |
| HTTP test          | `curl -I`              |
| HTTPS/TLS test     | `curl -v`              |
| Firewall           | `ufw status`           |
| Service failure    | `systemctl status`     |
| Service logs       | `journalctl`           |
| Docker ports       | `docker ps`            |
| Docker logs        | `docker logs`          |
| Kubernetes Service | `kubectl get svc`      |
| Kubernetes details | `kubectl describe svc` |

---

# 🏆 Key Principle

> **A service being "running" does not automatically mean it is reachable.**

A successful connection requires the complete path to work:

```text
DNS
 ↓
IP
 ↓
Route
 ↓
Firewall
 ↓
Port
 ↓
Process
 ↓
Application
```

This layered approach is one of the most useful troubleshooting skills for a DevOps engineer.
