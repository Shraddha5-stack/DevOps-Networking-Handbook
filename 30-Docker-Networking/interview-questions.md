# Docker Networking — Interview Questions

This file contains Docker Networking interview questions from **beginner to advanced level**, including practical commands, troubleshooting scenarios, and DevOps interview answers.

---

# 1. Beginner-Level Questions

## 1. What is Docker networking?

Docker networking provides communication between:

* Containers
* Containers and the Docker host
* Containers and external networks
* Containers and the internet

Docker uses Linux networking technologies such as:

* Network namespaces
* veth pairs
* Linux bridges
* Routing
* NAT
* Firewall rules

---

## 2. Why do Docker containers need networking?

Containers are isolated environments.

Networking allows containers to communicate with:

```text
Container
    ↓
Other containers
    ↓
Host
    ↓
External services
    ↓
Internet
```

For example:

```text
Frontend
   ↓
Backend
   ↓
Database
```

All three components need networking to communicate.

---

## 3. What are the default Docker networks?

Common default networks are:

```text
bridge
host
none
```

Check them:

```bash
docker network ls
```

---

## 4. What is the bridge network?

The bridge network is commonly used for containers running on the same Docker host.

Conceptually:

```text
Container A
     |
     ↓
 Docker Bridge
     |
     ↓
Container B
```

The default bridge is commonly associated with the Linux interface:

```text
docker0
```

---

## 5. What is a user-defined bridge network?

A user-defined bridge is a custom Docker network created by the user.

Example:

```bash
docker network create app-network
```

Run a container:

```bash
docker run -d \
  --name web \
  --network app-network \
  nginx
```

User-defined networks provide better application-level isolation and Docker DNS-based service discovery.

---

# 6. What is the difference between default bridge and user-defined bridge?

| Feature                      | Default bridge          | User-defined bridge |
| ---------------------------- | ----------------------- | ------------------- |
| Network name                 | `bridge`                | Custom name         |
| DNS/service discovery        | Limited/legacy behavior | Built-in DNS        |
| Isolation                    | Basic                   | Better              |
| Configuration                | Limited                 | Flexible            |
| Recommended for applications | No                      | Yes                 |

For application stacks, user-defined networks are generally preferred.

---

# 7. How do you create a Docker network?

```bash
docker network create app-network
```

Verify:

```bash
docker network ls
```

---

# 8. How do you inspect a Docker network?

```bash
docker network inspect app-network
```

This can show:

* Driver
* Subnet
* Gateway
* Connected containers
* Container IP addresses

---

# 9. How do you remove a Docker network?

```bash
docker network rm app-network
```

The network normally must not have containers attached to it.

---

# 10. How do you remove unused Docker networks?

```bash
docker network prune
```

Be careful because this removes unused networks.

---

# 11. How do you connect a running container to a network?

```bash
docker network connect app-network container-name
```

Verify:

```bash
docker network inspect app-network
```

---

# 12. How do you disconnect a container from a network?

```bash
docker network disconnect app-network container-name
```

---

# 13. What is a network namespace?

A network namespace provides an isolated networking environment.

A container normally has its own network namespace.

It can contain:

```text
eth0
lo
Routing table
Network interfaces
Ports
Neighbour information
```

This provides network isolation between containers and the host.

---

# 14. What is a veth pair?

A veth pair is a pair of connected virtual Ethernet interfaces.

Think of it as a virtual network cable:

```text
Container Namespace
       |
      eth0
       |
       |  veth pair
       |
Docker Host
       |
Docker Network
```

One end is associated with the container namespace and the other with the host-side networking.

---

# 15. What is `docker0`?

`docker0` is commonly the default Linux bridge created by Docker on Linux hosts.

Check:

```bash
ip addr show docker0
```

Check:

```bash
ip link show docker0
```

---

# 16. How do you find a container's IP address?

One option:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container
```

Or:

```bash
docker inspect container
```

Look under:

```text
NetworkSettings
```

---

# 17. Why should you avoid hardcoding container IP addresses?

Container IP addresses can change when containers are recreated.

Example:

```text
Old container:
mysql → 172.18.0.4
```

After recreation:

```text
New container:
mysql → 172.18.0.7
```

Therefore, use:

```text
mysql
```

instead of:

```text
172.18.0.4
```

Docker DNS can resolve the name.

---

# 18. What is Docker's embedded DNS?

Docker provides DNS-based service discovery for user-defined networks.

For example:

```text
client
   |
   ↓
Docker DNS
   |
   ↓
web
```

The client can use:

```text
http://web
```

instead of knowing the web container's IP address.

---

# 19. How do you test Docker DNS?

Example:

```bash
docker exec client getent hosts web
```

If the containers are on the same user-defined network, `web` should resolve.

---

# 20. How do containers communicate with each other?

If containers are attached to the same compatible Docker network, they can communicate through that network.

Example:

```text
client
   |
   ↓
app-network
   |
   ↓
web
```

Test:

```bash
docker exec client wget -qO- http://web
```

---

# 21. What is port publishing?

Port publishing maps a host port to a container port.

Example:

```bash
docker run -d \
  --name web \
  -p 8080:80 \
  nginx
```

Meaning:

```text
Host:8080
    ↓
Container:80
```

---

# 22. Explain `-p 8080:80`.

The syntax is:

```text
-p HOST_PORT:CONTAINER_PORT
```

Therefore:

```text
-p 8080:80
```

means:

```text
Host port 8080
       ↓
Container port 80
```

---

# 23. Does `EXPOSE 80` publish port 80?

No.

`EXPOSE` documents the port used by the application.

Example:

```dockerfile
EXPOSE 80
```

Actual host publishing requires something like:

```bash
docker run -p 8080:80 nginx
```

---

# 24. What is the difference between EXPOSE and -p?

| `EXPOSE`                              | `-p`                              |
| ------------------------------------- | --------------------------------- |
| Documents a port                      | Publishes a port                  |
| Dockerfile instruction                | `docker run` option               |
| Does not create host access by itself | Creates host-to-container mapping |

---

# 25. How do you check published ports?

```bash
docker port web
```

Or:

```bash
docker ps
```

Example:

```text
0.0.0.0:8080->80/tcp
```

---

# 26. How do you publish a port only on localhost?

```bash
docker run -d \
  -p 127.0.0.1:8080:80 \
  nginx
```

This restricts the host binding to localhost.

---

# 27. What is host networking?

Host networking allows the container to use the host's network namespace rather than normal isolated container networking.

Example:

```bash
docker run --network host nginx
```

Advantages:

* Less networking overhead
* Direct access to host networking

Disadvantages:

* Less network isolation
* Possible port conflicts
* Additional security considerations

---

# 28. What is the `none` network?

The `none` network disables normal container networking.

Example:

```bash
docker run --rm \
  --network none \
  alpine \
  ip addr
```

The container normally only has loopback networking.

---

# 29. What are Docker network drivers?

Common drivers include:

```text
bridge
host
none
overlay
macvlan
ipvlan
```

---

# 30. What is an overlay network?

An overlay network allows workloads on different Docker hosts to communicate over a logical network.

Conceptually:

```text
Docker Host 1                 Docker Host 2

Container A                  Container B
      |                            |
      +---------- Overlay ---------+
```

Overlay networking is commonly associated with Docker Swarm.

---

# 31. What is macvlan?

macvlan can allow containers to appear directly connected to a physical network and have their own MAC addresses.

Example architecture:

```text
Physical Network
       |
       +---- Host
       |
       +---- Container
```

It is an advanced networking option.

---

# 32. What is ipvlan?

ipvlan is an advanced Linux networking mechanism that Docker can use as a network driver.

It provides different networking behavior from macvlan and can be useful for specialized L2/L3 network designs.

---

# 33. What is NAT in Docker networking?

NAT means Network Address Translation.

Docker can use NAT when containers communicate with external networks.

Conceptually:

```text
Container
172.x.x.x
    |
    ↓
Docker NAT
    |
    ↓
Host Interface
    |
    ↓
Internet
```

The external network generally sees traffic through the host's network identity.

---

# 34. How does a container access the internet?

A typical flow is:

```text
Container
   ↓
Container Network
   ↓
Docker Bridge
   ↓
NAT
   ↓
Host Interface
   ↓
Router
   ↓
Internet
```

---

# 35. What are iptables and nftables doing in Docker networking?

Docker networking may interact with Linux packet filtering and NAT mechanisms.

Depending on the system, you may encounter:

```text
iptables
```

or:

```text
nftables
```

They can be involved in:

* NAT
* Forwarding
* Filtering
* Port publishing

Inspect carefully:

```bash
sudo iptables -L -n
```

or:

```bash
sudo nft list ruleset
```

Do not blindly modify firewall rules on production systems.

---

# 36. How do you check Docker network configuration?

Use:

```bash
docker network inspect <network>
```

Look for:

```text
Driver
Subnet
Gateway
Containers
```

---

# 37. How do you check container network configuration?

Use:

```bash
docker inspect <container>
```

Look under:

```text
NetworkSettings
```

You can also enter the container:

```bash
docker exec -it <container> sh
```

Then:

```bash
ip addr
ip route
```

---

# 38. How do you check container DNS configuration?

```bash
docker exec <container> cat /etc/resolv.conf
```

Test resolution:

```bash
docker exec <container> getent hosts google.com
```

---

# 39. How do you check the container routing table?

```bash
docker exec <container> ip route
```

You may see something similar to:

```text
default via 172.18.0.1 dev eth0
```

---

# 40. How do you check the host's Docker bridge?

```bash
ip addr show docker0
```

And:

```bash
ip link show docker0
```

---

# 41. How do you check listening ports on the host?

```bash
ss -ltnp
```

For port 8080:

```bash
ss -ltnp | grep :8080
```

Another option:

```bash
sudo lsof -i :8080
```

---

# 42. How do you check listening ports inside a container?

```bash
docker exec <container> ss -lnt
```

If the image does not contain `ss`, use another appropriate diagnostic method.

---

# 43. What is the difference between connection refused and timeout?

### Connection refused

Usually means the destination was reachable, but no service accepted the connection on that port, or the connection was actively rejected.

Check:

```bash
docker exec <container> ss -lnt
```

### Connection timeout

Usually indicates that traffic is not reaching the destination or responses are being blocked/dropped.

Investigate:

* Routing
* Firewall
* Network path
* Security rules
* Application availability

---

# 44. Scenario: Container cannot connect to another container. What do you check?

Use this order:

```text
1. Are both containers running?
2. Are both attached to the same network?
3. Does the target name resolve?
4. Does the target have the expected IP?
5. Is the target application listening?
6. Is the correct port being used?
7. Is a firewall/network rule blocking traffic?
```

Commands:

```bash
docker ps
```

```bash
docker network inspect app-network
```

```bash
docker exec client getent hosts server
```

```bash
docker exec server ss -lnt
```

---

# 45. Scenario: DNS does not work between containers.

Suppose:

```bash
docker exec client getent hosts web
```

fails.

Check:

```bash
docker network inspect app-network
```

Make sure both containers are attached to the same user-defined network.

Then:

```bash
docker exec client cat /etc/resolv.conf
```

Test again:

```bash
docker exec client getent hosts web
```

---

# 46. Scenario: Container has no internet access.

Check the container:

```bash
docker exec client ip addr
```

Check route:

```bash
docker exec client ip route
```

Check DNS:

```bash
docker exec client getent hosts google.com
```

Test IP connectivity if the image has the necessary tools:

```bash
docker exec client ping -c 3 8.8.8.8
```

Possible causes:

* Missing route
* DNS failure
* Docker networking issue
* Host firewall
* External firewall
* Proxy configuration
* Host connectivity issue

---

# 47. Scenario: Docker says "address already in use".

Example:

```text
bind: address already in use
```

Check:

```bash
ss -ltnp | grep :8080
```

or:

```bash
sudo lsof -i :8080
```

Then either:

* Stop the process using the port, if appropriate.
* Choose another host port.

Example:

```bash
docker run -d \
  -p 8081:80 \
  nginx
```

---

# 48. Scenario: Application is running but cannot be accessed.

Check the application:

```bash
docker exec web ss -lnt
```

Check port mapping:

```bash
docker port web
```

Check container:

```bash
docker ps
```

Check network:

```bash
docker network inspect app-network
```

Test locally:

```bash
curl http://localhost:8080
```

If still failing, investigate:

* Application binding address
* Host firewall
* Docker port mapping
* Network configuration

---

# 49. Why is binding to `127.0.0.1` different from `0.0.0.0`?

Example:

```bash
-p 127.0.0.1:8080:80
```

The host port is bound to localhost.

Example:

```bash
-p 0.0.0.0:8080:80
```

The port is bound on all IPv4 host interfaces.

This affects which network interfaces can receive traffic.

---

# 50. Should you publish a MySQL port?

Not necessarily.

If only the backend needs MySQL:

```text
Backend
   |
   ↓
MySQL
```

both can remain on an internal Docker network.

There is usually no need to publish:

```bash
-p 3306:3306
```

unless external access is specifically required.

---

# 51. How would you design a secure Docker application network?

A common architecture is:

```text
                    Internet
                       |
                       ↓
                     Nginx
                       |
                 frontend-net
                       |
                    Backend
                       |
                 backend-net
                   /       \
                  ↓         ↓
               MySQL      Redis
```

Only Nginx is publicly exposed.

Backend, MySQL, and Redis remain internal where possible.

---

# 52. Can a container belong to multiple networks?

Yes.

Example:

```bash
docker network connect frontend-net backend
```

The container can then communicate through both networks.

Example:

```text
frontend-net
      |
    backend
      |
backend-net
```

This is useful for controlled communication between application tiers.

---

# 53. How does Docker Compose handle networking?

Docker Compose normally creates a project-specific network for services.

Example:

```yaml
services:
  web:
    image: nginx

  backend:
    image: nginx
```

The services can communicate using their service names.

For example:

```text
http://backend
```

---

# 54. Why are service names important in Docker Compose?

Because container IPs can change.

Instead of:

```text
DB_HOST=172.18.0.5
```

use:

```text
DB_HOST=database
```

Compose/Docker DNS resolves the service name.

---

# 55. How do you test Compose service discovery?

Example:

```bash
docker compose exec client getent hosts web
```

Then:

```bash
docker compose exec client wget -qO- http://web
```

---

# 56. Docker Networking vs Kubernetes Networking

Docker:

```text
Container
   ↓
Docker Network
   ↓
Host
```

Kubernetes:

```text
Pod
   ↓
CNI
   ↓
Node Network
   ↓
Cluster Network
```

Docker networking concepts help build the foundation for understanding Kubernetes networking.

---

# 57. What is network isolation?

Network isolation means restricting communication between different network segments.

Example:

```text
frontend-net
    |
 frontend


backend-net
    |
 backend
    |
 database
```

The frontend does not automatically have access to the backend network.

---

# 58. How would you troubleshoot a Docker 502 error?

A 502 often means a proxy such as Nginx cannot successfully communicate with the upstream backend.

Check:

### Step 1

Is backend running?

```bash
docker ps
```

### Step 2

Is backend on the expected network?

```bash
docker network inspect app-network
```

### Step 3

Does backend DNS resolve?

```bash
docker exec nginx getent hosts backend
```

### Step 4

Is backend listening?

```bash
docker exec backend ss -lnt
```

### Step 5

Test directly:

```bash
docker exec nginx wget -qO- http://backend:<PORT>
```

Then check:

* Backend logs
* Network configuration
* Port configuration
* Application health

---

# 59. How would you troubleshoot a Docker 504 error?

A 504 generally indicates a timeout while waiting for an upstream response.

Check:

```text
Nginx
  ↓
DNS
  ↓
Backend network
  ↓
Backend port
  ↓
Backend application
  ↓
Database/external dependencies
```

Commands:

```bash
docker logs nginx
```

```bash
docker exec nginx getent hosts backend
```

```bash
docker exec nginx nc -zv backend <PORT>
```

```bash
docker logs backend
```

---

# 60. What commands do you use most for Docker networking troubleshooting?

Important commands:

```bash
docker network ls
docker network inspect <network>
docker inspect <container>
docker port <container>
docker exec <container> ip addr
docker exec <container> ip route
docker exec <container> cat /etc/resolv.conf
docker exec <container> getent hosts <target>
docker exec <container> ss -lnt
ss -ltnp
ip addr
ip route
curl
nc
```

---

# 61. Explain Docker networking in an interview.

A strong answer:

> Docker networking allows containers to communicate with each other, the host, and external networks. On Linux, Docker uses network namespaces, veth pairs, bridges, routing, NAT, and firewall mechanisms. For single-host applications, bridge networks are commonly used. User-defined bridge networks provide better isolation and DNS-based service discovery. Port publishing maps host ports to container ports, while containers on the same Docker network can communicate internally without publishing their ports.

---

# 62. Explain Docker networking architecture.

A good explanation:

```text
Container
    ↓
Network Namespace
    ↓
eth0
    ↓
veth Pair
    ↓
Docker Bridge
    ↓
Routing / NAT
    ↓
Host Interface
    ↓
External Network
```

The container has an isolated network namespace.

A veth pair connects the container networking to the host-side Docker network.

---

# 63. Explain container-to-container communication.

Example:

```text
client
   |
   ↓
app-network
   |
   ↓
web
```

Docker DNS resolves:

```text
web → container IP
```

The client can then access:

```text
http://web
```

without knowing the IP address.

---

# 64. Explain host-to-container communication.

Example:

```text
Browser
   |
   ↓
Host:8080
   |
   ↓
Docker port mapping
   |
   ↓
Container:80
```

Command:

```bash
docker run -d -p 8080:80 nginx
```

---

# 65. What happens when you run `docker run -p 8080:80 nginx`?

Conceptually:

```text
1. Docker creates the container.
2. Container receives a network namespace.
3. Container gets a network interface.
4. Container connects to the Docker network.
5. Nginx listens on port 80.
6. Docker creates host-to-container port mapping.
7. Traffic to host port 8080 is forwarded to container port 80.
```

Flow:

```text
Host:8080
    ↓
Docker networking/NAT
    ↓
Container:80
    ↓
Nginx
```

---

# 66. What happens when a container is recreated?

Its IP may change.

Example:

```text
Before:
web → 172.18.0.2
```

After recreation:

```text
web → 172.18.0.5
```

Applications should therefore use:

```text
web
```

rather than:

```text
172.18.0.2
```

---

# 67. Real-World Scenario: Three-Tier Application

You have:

```text
Nginx
Backend
MySQL
```

How would you network them?

Answer:

```text
Internet
   |
   ↓
Nginx
   |
frontend/backend network
   |
Backend
   |
backend network
   |
MySQL
```

Only Nginx should normally have a public published port.

The backend and database should communicate over private Docker networks.

---

# 68. Real-World Scenario: Database Is Unreachable

Application reports:

```text
connection refused
```

Check:

```bash
docker ps
```

Then:

```bash
docker network inspect backend-net
```

Check DNS:

```bash
docker exec backend getent hosts database
```

Check database port:

```bash
docker exec database ss -lnt
```

Check application configuration:

```text
DB_HOST=database
DB_PORT=3306
```

Do not immediately assume that the database IP is the problem.

---

# 69. Real-World Scenario: Website Works Inside Container but Not From Host

Check:

```bash
docker exec web ss -lnt
```

Then:

```bash
docker port web
```

Then:

```bash
ss -ltnp | grep :8080
```

Possible issue:

```text
Application works inside container
        ↓
But host port is not published
```

Fix:

```bash
docker run -p 8080:80 nginx
```

---

# 70. Real-World Scenario: Port 8080 Is Busy

Run:

```bash
ss -ltnp | grep :8080
```

Find the process.

Then:

```bash
sudo lsof -i :8080
```

Possible solutions:

```text
Stop the conflicting service
```

or:

```text
Use another host port
```

Example:

```bash
docker run -p 8081:80 nginx
```

---

# 71. Real-World Scenario: Container DNS Works but Internet DNS Fails

Suppose:

```bash
docker exec client getent hosts web
```

works.

But:

```bash
docker exec client getent hosts google.com
```

fails.

This suggests:

```text
Docker internal service discovery
        ↓
Working

External DNS resolution
        ↓
Potential problem
```

Investigate:

* `/etc/resolv.conf`
* Docker DNS behavior
* Host DNS
* Network connectivity
* VPN/proxy configuration
* Firewall

---

# 72. Real-World Scenario: DNS Works but Application Fails

Suppose:

```bash
docker exec client getent hosts backend
```

works.

But:

```bash
docker exec client wget -qO- http://backend:8080
```

fails.

Then DNS is probably not the main issue.

Check:

```bash
docker exec backend ss -lnt
```

Verify:

* Application is running
* Correct port
* Correct bind address
* Application logs

---

# 73. Real-World Scenario: Connection Times Out

Use:

```bash
docker exec client ip route
```

Then:

```bash
docker exec client getent hosts backend
```

Then:

```bash
docker exec client nc -zv backend 8080
```

Check:

```bash
docker network inspect app-network
```

Investigate:

* Routing
* Firewall
* Network membership
* Application
* External connectivity

---

# 74. Security Interview Question: Should Every Container Have a Public Port?

No.

Only services that require external access should normally be published.

Example:

```text
Public
  |
  ↓
Nginx
  |
  ↓
Backend
  |
  ↓
Database
```

Only Nginx needs public exposure in this simple architecture.

---

# 75. Security Interview Question: Why avoid exposing databases?

Public database ports increase attack surface.

Instead of:

```text
Internet
   |
   ↓
MySQL:3306
```

prefer:

```text
Backend
   |
   ↓
Private Docker Network
   |
   ↓
MySQL
```

---

# 76. What is the most important Docker networking concept for DevOps?

Understand the difference between:

```text
Internal communication
```

and:

```text
External access
```

Internal:

```text
container → Docker network → container
```

External:

```text
client → host port → Docker → container
```

This distinction solves many Docker networking problems.

---

# 77. Docker Networking Troubleshooting Framework

Use:

```text
1. Container
       ↓
2. Network
       ↓
3. IP
       ↓
4. Route
       ↓
5. DNS
       ↓
6. Port
       ↓
7. Application
       ↓
8. Firewall
       ↓
9. External network
```

Corresponding commands:

```bash
docker ps
docker network inspect
docker inspect
docker exec ip addr
docker exec ip route
docker exec getent hosts
docker port
docker exec ss -lnt
ss -ltnp
curl
nc
```

---

# 78. Top 10 Docker Networking Interview Questions

Before an interview, make sure you can answer these:

### 1.

What is Docker networking?

### 2.

What is a bridge network?

### 3.

Default bridge vs user-defined bridge?

### 4.

What is Docker DNS?

### 5.

What is `-p 8080:80`?

### 6.

EXPOSE vs publish?

### 7.

What is host networking?

### 8.

What is an overlay network?

### 9.

How do containers communicate with each other?

### 10.

How do you troubleshoot Docker connectivity?

---

# 79. Commands to Memorize for Interviews

```bash
docker network ls
```

```bash
docker network inspect <network>
```

```bash
docker network create <network>
```

```bash
docker network connect <network> <container>
```

```bash
docker network disconnect <network> <container>
```

```bash
docker inspect <container>
```

```bash
docker port <container>
```

```bash
docker exec <container> ip addr
```

```bash
docker exec <container> ip route
```

```bash
docker exec <container> getent hosts <target>
```

```bash
docker exec <container> ss -lnt
```

```bash
ss -ltnp
```

```bash
ip addr
```

```bash
ip route
```

```bash
curl
```

```bash
nc
```

---

# 80. Final Interview Answer

If an interviewer asks:

**"Explain Docker networking from start to finish."**

Answer:

> Docker networking provides connectivity between containers, the host, and external networks. On Linux, Docker uses network namespaces to isolate container networking, veth pairs to connect namespaces to the host, and bridge networks to connect containers. Containers on user-defined networks can communicate using Docker's embedded DNS and service names. When external access is required, Docker can publish a container port to a host port using `-p`, and networking/NAT and firewall mechanisms handle the traffic path. For troubleshooting, I check the container status, network membership, IP address, route, DNS resolution, application listening port, published port, and firewall rules in that order.

---

# 81. Final Mental Model

Remember:

```text
                  INTERNET
                     |
                     ↓
                Host Network
                     |
                    NAT
                     |
              Docker Network
                     |
              +------+------+
              |             |
              ↓             ↓
          Container A   Container B
              |             |
             eth0          eth0
              |             |
        Network Namespace
              |
            veth pair
              |
        Docker Bridge
```

For applications:

```text
                    Internet
                       |
                    :80/:443
                       |
                     Nginx
                       |
                  Docker DNS
                       |
                    Backend
                       |
                  Docker DNS
                       |
                    MySQL
```

The key principles are:

```text
1. Containers are isolated.
2. Networks provide connectivity.
3. veth connects container networking to the host.
4. Bridges connect containers on the same Docker host.
5. User-defined networks provide Docker DNS.
6. Use names instead of container IPs.
7. -p publishes ports.
8. EXPOSE does not publish ports.
9. Keep internal services private.
10. Troubleshoot layer by layer.
```

---

# 82. Chapter 30 — Final Checklist

After completing this chapter, you should understand:

```text
[ ] Docker networking basics
[ ] Network namespaces
[ ] veth pairs
[ ] docker0
[ ] Bridge networks
[ ] User-defined networks
[ ] Container IP addresses
[ ] Docker DNS
[ ] Container-to-container communication
[ ] Port publishing
[ ] EXPOSE vs -p
[ ] Host networking
[ ] None networking
[ ] Overlay networking
[ ] macvlan
[ ] ipvlan
[ ] NAT
[ ] iptables/nftables
[ ] Docker Compose networking
[ ] Network isolation
[ ] Network security
[ ] Docker troubleshooting
[ ] Real-world three-tier architecture
```

---

# 83. Chapter 30 Complete

The complete chapter now contains:

```text
30-Docker-Networking/
│
├── README.md
├── notes.md
├── commands.md
├── practical-lab.md
└── interview-questions.md
```

Docker networking is now connected to the Linux networking concepts you learned in Chapter 29.

The next major topic in the handbook is:

```text
31-Kubernetes-Networking
```

which will build on:

```text
Linux Networking
       ↓
Docker Networking
       ↓
Kubernetes Networking
```
