# Docker Networking — Notes

## 1. What Is Docker Networking?

Docker networking allows containers to communicate with:

* Other containers
* The Docker host
* External networks
* The internet
* Services running on other networks

A Docker container is isolated from the host by default. Networking provides the communication path between these isolated environments.

Basic flow:

```text
Container
    ↓
Network Namespace
    ↓
Virtual Ethernet (veth)
    ↓
Docker Network
    ↓
Host Network
    ↓
Internet / External Services
```

---

# 2. Why Do Containers Need Networking?

Consider a typical application:

```text
                    Internet
                       |
                    Nginx
                       |
                    Backend
                       |
                    MySQL
```

These components may run in separate containers.

For example:

```text
nginx-container
       |
       ↓
api-container
       |
       ↓
mysql-container
```

They need networking to communicate.

Without networking:

* Nginx cannot reach the backend.
* Backend cannot reach MySQL.
* Users cannot reach the application.

---

# 3. Docker Networking Architecture

Docker creates networking components using Linux networking features.

Important components include:

```text
Docker Container
      |
      ↓
Network Namespace
      |
      ↓
veth Pair
      |
      ↓
Docker Bridge
      |
      ↓
Host Network Interface
      |
      ↓
Router
      |
      ↓
Internet
```

Docker uses Linux networking technologies such as:

* Network namespaces
* veth pairs
* Linux bridges
* Routing
* NAT
* iptables/nftables

---

# 4. Network Namespace

A network namespace provides an isolated networking environment.

Each container normally gets its own network namespace.

Inside a container, you can have:

```text
eth0
lo
routing table
ARP/neighbour table
ports
```

The container sees its own networking environment.

Example:

```bash
docker exec -it <container-name> ip addr
```

You may see:

```text
lo
eth0
```

The container's `eth0` is different from the host's physical interface.

---

# 5. veth Pair

A veth pair is a virtual Ethernet cable.

It has two connected endpoints.

Conceptually:

```text
Container Namespace
       |
      eth0
       |
       |
     veth
       |
       |
Docker Host
```

One end is inside the container.

The other end is connected to the Docker network on the host.

Think of it as:

```text
Container ===== Virtual Cable ===== Host
```

This allows packets to travel between the container and the Docker network.

---

# 6. Docker Bridge Network

The default Docker networking mode on Linux is generally based on a bridge network.

Docker commonly creates a bridge called:

```text
docker0
```

Check it with:

```bash
ip link show docker0
```

or:

```bash
ip addr show docker0
```

You can also run:

```bash
docker network ls
```

Example:

```text
NETWORK ID     NAME      DRIVER    SCOPE
xxxx           bridge    bridge    local
xxxx           host      host      local
xxxx           none      null      local
```

---

# 7. Default Bridge Network

Docker creates a default network named:

```text
bridge
```

Containers can attach to it.

Example:

```bash
docker run -d --name web nginx
```

The container normally receives a private IP address.

Check:

```bash
docker inspect web
```

Look for:

```text
IPAddress
```

You can also use:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web
```

---

# 8. User-Defined Bridge Network

It is better to create your own bridge network for applications.

Create one:

```bash
docker network create mynetwork
```

Check:

```bash
docker network ls
```

Run containers on it:

```bash
docker run -d --name web --network mynetwork nginx
```

Run another container:

```bash
docker run -d --name test --network mynetwork alpine sleep 3600
```

Now both containers belong to:

```text
mynetwork
```

---

# 9. User-Defined Bridge vs Default Bridge

| Feature                   | Default bridge          | User-defined bridge |
| ------------------------- | ----------------------- | ------------------- |
| Name                      | `bridge`                | Custom              |
| Container DNS             | Limited/legacy behavior | Built-in DNS        |
| Isolation                 | Basic                   | Better              |
| Recommended               | Simple testing          | Applications        |
| Container name resolution | Limited                 | Supported           |
| Configuration             | Less flexible           | More flexible       |

For real applications, prefer user-defined networks.

---

# 10. Container IP Address

Containers normally receive private IP addresses.

Example:

```text
Container 1 → 172.18.0.2
Container 2 → 172.18.0.3
Container 3 → 172.18.0.4
```

Check container IP:

```bash
docker inspect <container>
```

Or:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container>
```

However, application code should generally avoid depending on container IP addresses.

Why?

Because container IPs can change when containers are recreated.

Use Docker DNS and service/container names instead.

---

# 11. Container-to-Container Communication

Suppose we have:

```text
web
 |
 ↓
api
 |
 ↓
db
```

All containers are connected to:

```text
app-network
```

Create:

```bash
docker network create app-network
```

Run API:

```bash
docker run -d \
  --name api \
  --network app-network \
  nginx
```

Run another container:

```bash
docker run -d \
  --name client \
  --network app-network \
  alpine \
  sleep 3600
```

The containers can communicate through the Docker network.

---

# 12. Docker Embedded DNS

Docker provides an internal DNS service for user-defined networks.

For example:

```text
client
   |
   | DNS lookup
   ↓
api
   |
   ↓
172.18.0.x
```

Instead of using:

```text
172.18.0.2
```

the client can use:

```text
api
```

This is extremely useful in DevOps.

Example:

```text
DATABASE_HOST=mysql
```

instead of:

```text
DATABASE_HOST=172.18.0.5
```

The IP can change.

The service/container name remains stable.

---

# 13. Docker Network DNS Example

Create network:

```bash
docker network create app-network
```

Start a server:

```bash
docker run -d \
  --name web \
  --network app-network \
  nginx
```

Start a client:

```bash
docker run --rm \
  --network app-network \
  alpine \
  ping -c 3 web
```

The name:

```text
web
```

is resolved by Docker's internal DNS.

---

# 14. Port Publishing

Containers have their own networking environment.

A service inside a container may listen on:

```text
80
```

But this does not automatically mean that the host can access it through port 80.

We can publish the port:

```bash
docker run -d \
  --name web \
  -p 8080:80 \
  nginx
```

Meaning:

```text
Host Port       Container Port
   8080    →        80
```

Flow:

```text
Browser
   |
   ↓
Host:8080
   |
   ↓
Docker NAT / Port Mapping
   |
   ↓
Container:80
   |
   ↓
Nginx
```

Access:

```text
http://localhost:8080
```

---

# 15. Understanding `-p`

General syntax:

```bash
-p HOST_PORT:CONTAINER_PORT
```

Example:

```bash
-p 8080:80
```

Means:

```text
Host 8080 → Container 80
```

Another example:

```bash
-p 5000:5000
```

Means:

```text
Host 5000 → Container 5000
```

Another:

```bash
-p 3000:80
```

Means:

```text
Host 3000 → Container 80
```

---

# 16. Publishing Does Not Change the Container Port

If Nginx listens on:

```text
80
```

and we run:

```bash
-p 8080:80
```

Nginx still listens on:

```text
80
```

Only the host-facing port is:

```text
8080
```

So:

```text
Host:8080
     ↓
Container:80
```

---

# 17. Bind to Localhost Only

You can restrict a published port to localhost:

```bash
docker run -d \
  --name web \
  -p 127.0.0.1:8080:80 \
  nginx
```

Now the service is accessible from the host itself through:

```text
127.0.0.1:8080
```

This is useful for local development when you don't want the port exposed on all host interfaces.

---

# 18. Bind to All Interfaces

Example:

```bash
docker run -d \
  --name web \
  -p 0.0.0.0:8080:80 \
  nginx
```

This can expose the published port on the host's network interfaces.

Be careful with production systems.

Always consider:

* Firewall rules
* Security groups
* Authentication
* TLS
* Network exposure

---

# 19. Exposing vs Publishing Ports

These two concepts are different.

## EXPOSE

Dockerfile:

```dockerfile
EXPOSE 80
```

This documents that the application uses port 80.

It does not automatically make the port accessible from the host.

## PUBLISH

```bash
docker run -p 8080:80 nginx
```

This creates host-to-container port mapping.

Simple difference:

```text
EXPOSE
   ↓
Documentation / metadata

-p
   ↓
Actual port publishing
```

---

# 20. Docker Host Network

With host networking:

```bash
docker run --network host nginx
```

The container shares the host's network namespace.

Conceptually:

```text
Host Network
     |
     +---- Container
```

There is no normal isolated container network namespace in the same way as bridge mode.

Advantages:

* Less networking overhead
* Direct access to host networking
* Useful for some high-performance workloads

Disadvantages:

* Less isolation
* Possible port conflicts
* Reduced portability
* More security considerations

---

# 21. Docker None Network

The `none` network disables normal networking.

Example:

```bash
docker run --network none alpine
```

The container has very limited networking.

Typically it only has:

```text
lo
```

This can be useful when a container does not require network access.

---

# 22. Docker Network Drivers

Docker supports different network drivers.

| Driver  | Purpose                                           |
| ------- | ------------------------------------------------- |
| bridge  | Containers on the same Docker host                |
| host    | Use host networking                               |
| none    | Disable networking                                |
| overlay | Networking across Docker hosts                    |
| macvlan | Give containers MAC addresses on physical network |
| ipvlan  | Advanced L2/L3 networking                         |

---

# 23. Overlay Networking

Overlay networks allow containers on different Docker hosts to communicate as if they are on the same logical network.

Conceptually:

```text
Docker Host 1                 Docker Host 2

Container A                   Container B
     |                             |
     ↓                             ↓
Overlay Network
     |=============================|
```

Overlay networking is commonly associated with Docker Swarm.

For a single Docker host, bridge networking is usually sufficient.

---

# 24. macvlan

macvlan can make a container appear directly connected to the physical network.

Conceptually:

```text
Physical Network
       |
       +---- Host
       |
       +---- Container
```

The container can have its own MAC address.

Use cases may include:

* Network appliances
* Legacy applications
* Special network requirements

It is more advanced than normal bridge networking.

---

# 25. ipvlan

ipvlan is another advanced networking driver.

It allows multiple network endpoints while using a shared MAC address model.

It can be useful in environments where administrators need more control over L2/L3 networking.

For most beginners:

```text
bridge → learn first
host → understand
none → understand
overlay → understand
macvlan/ipvlan → advanced
```

---

# 26. Docker Network Commands

List networks:

```bash
docker network ls
```

Inspect network:

```bash
docker network inspect bridge
```

Create network:

```bash
docker network create app-network
```

Remove network:

```bash
docker network rm app-network
```

Connect container:

```bash
docker network connect app-network container1
```

Disconnect container:

```bash
docker network disconnect app-network container1
```

Remove unused networks:

```bash
docker network prune
```

Be careful with `prune`.

---

# 27. Inspecting a Container's Network

Use:

```bash
docker inspect container-name
```

Look for:

```text
NetworkSettings
```

Useful information includes:

* Network name
* IP address
* Gateway
* MAC address
* Published ports

A formatted command:

```bash
docker inspect -f '{{json .NetworkSettings.Networks}}' container-name
```

---

# 28. Inspecting Network Interfaces

On the host:

```bash
ip addr
```

List interfaces:

```bash
ip link
```

Look for Docker bridge:

```bash
ip addr show docker0
```

You may also see virtual interfaces associated with containers.

---

# 29. Docker NAT

When a container accesses the internet, Docker commonly uses NAT.

Example:

```text
Container
172.17.0.2
    |
    ↓
Docker Bridge
    |
    ↓
NAT
    |
    ↓
Host Wi-Fi/Ethernet
    |
    ↓
Router
    |
    ↓
Internet
```

The outside world generally sees traffic as originating from the host's network address rather than directly from the private container IP.

---

# 30. iptables and nftables

Docker networking may interact with Linux firewall/network packet-filtering systems.

Depending on the Linux distribution and Docker configuration, you may encounter:

```text
iptables
```

or:

```text
nftables
```

These mechanisms can participate in:

* NAT
* Forwarding
* Filtering
* Port publishing

You can inspect firewall rules using commands appropriate to your system.

For example:

```bash
sudo iptables -L -n
```

or:

```bash
sudo nft list ruleset
```

Do not modify firewall rules blindly on a production machine.

---

# 31. Docker Compose Networking

Docker Compose makes multi-container networking easier.

Example:

```yaml
services:

  frontend:
    image: nginx
    ports:
      - "8080:80"

  backend:
    image: nginx

  database:
    image: mysql
```

Compose automatically creates a project network.

Conceptually:

```text
              app-network
                  |
       +----------+----------+
       |          |          |
   frontend    backend    database
```

---

# 32. Compose Service Names

Compose services can communicate using their service names.

Example:

```yaml
services:

  backend:
    image: nginx

  database:
    image: mysql
```

The backend can use:

```text
database
```

as the database hostname.

Example application configuration:

```text
DB_HOST=database
```

Not:

```text
DB_HOST=172.18.0.5
```

This is one of the most important concepts in container networking.

---

# 33. Example Multi-Container Architecture

A common DevOps application may look like:

```text
                  Internet
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

Docker version:

```text
             Docker Host
                  |
          app-network
                  |
      +-----------+-----------+
      |           |           |
    nginx       api         mysql
      |           |           |
      +-----------+-----------+
```

Only Nginx may need a published port.

For example:

```text
Host:80 → nginx:80
```

Backend and MySQL can remain internal.

---

# 34. Public vs Internal Services

Good architecture:

```text
Internet
   |
   ↓
Nginx
   |
   ↓
Backend
   |
   ↓
MySQL
```

Only Nginx is publicly exposed.

Backend:

```text
Internal
```

Database:

```text
Internal
```

This reduces attack surface.

Avoid unnecessarily publishing:

```text
-p 3306:3306
```

if the database only needs to be accessed by backend containers.

---

# 35. Network Isolation

Docker networks can provide logical isolation.

Example:

```text
frontend-network

frontend
   |
   +---- nginx
```

and:

```text
backend-network

backend
   |
   +---- api
   |
   +---- mysql
```

A container can be connected to multiple networks when required.

Example:

```text
             frontend-network
                    |
                  nginx
                    |
                    |
             backend-network
                    |
                  api
                    |
                  mysql
```

This can separate public-facing and internal traffic.

---

# 36. Connecting a Container to Multiple Networks

Create networks:

```bash
docker network create frontend
docker network create backend
```

Run container:

```bash
docker run -d \
  --name api \
  --network backend \
  nginx
```

Connect it to frontend:

```bash
docker network connect frontend api
```

Now:

```text
api
 |
 +---- frontend
 |
 +---- backend
```

This can be useful for controlled communication between application tiers.

---

# 37. Docker Networking and Security

Important security principles:

### 1. Do not publish unnecessary ports

Avoid:

```bash
-p 3306:3306
```

unless external access is actually required.

### 2. Use internal networks

Keep databases and internal services on private Docker networks.

### 3. Use firewalls

Use host-level firewall controls where appropriate.

### 4. Use TLS

Protect sensitive traffic.

### 5. Use authentication

Networking alone does not provide application security.

### 6. Avoid hardcoded container IPs

Use DNS/service names.

---

# 38. Common Docker Networking Problems

## Problem 1: Port already in use

Example:

```text
bind: address already in use
```

Check:

```bash
ss -ltnp
```

or:

```bash
sudo lsof -i :8080
```

Choose another host port or stop the conflicting service.

---

## Problem 2: Container cannot reach another container

Check:

```bash
docker network ls
```

Then:

```bash
docker network inspect app-network
```

Verify both containers are attached to the same network.

---

## Problem 3: Container name does not resolve

Check whether both containers are on the same user-defined network.

Example:

```bash
docker network inspect app-network
```

Then test:

```bash
docker exec -it client getent hosts api
```

---

## Problem 4: Internet does not work inside container

Check:

```bash
docker exec -it container ip addr
```

Check routes:

```bash
docker exec -it container ip route
```

Test DNS:

```bash
docker exec -it container getent hosts google.com
```

Test connectivity:

```bash
docker exec -it container ping -c 3 8.8.8.8
```

If IP connectivity works but DNS fails, investigate DNS configuration.

---

# 39. Debugging Docker Networking

Use this flow:

```text
Container
   |
   ↓
Does interface exist?
   |
   ↓
Does IP exist?
   |
   ↓
Does route exist?
   |
   ↓
Can container reach gateway?
   |
   ↓
Can it reach another container?
   |
   ↓
Does DNS resolve?
   |
   ↓
Is application port listening?
   |
   ↓
Is host port published?
   |
   ↓
Is firewall blocking traffic?
```

---

# 40. Useful Commands for Troubleshooting

Check running containers:

```bash
docker ps
```

Inspect container:

```bash
docker inspect <container>
```

List networks:

```bash
docker network ls
```

Inspect network:

```bash
docker network inspect <network>
```

Enter container:

```bash
docker exec -it <container> sh
```

Check IP:

```bash
docker exec <container> ip addr
```

Check routes:

```bash
docker exec <container> ip route
```

Check DNS:

```bash
docker exec <container> cat /etc/resolv.conf
```

Test DNS:

```bash
docker exec <container> getent hosts google.com
```

Check listening ports:

```bash
docker exec <container> ss -lnt
```

Check host ports:

```bash
ss -ltnp
```

---

# 41. Docker Networking vs Linux Networking

Docker networking is built on Linux networking concepts.

| Docker              | Linux concept           |
| ------------------- | ----------------------- |
| Container network   | Network namespace       |
| Container interface | veth                    |
| Docker bridge       | Linux bridge            |
| Container route     | Linux routing           |
| Port publishing     | NAT / firewall rules    |
| Container DNS       | DNS service             |
| Network isolation   | Namespace/network rules |

Therefore, learning Linux networking makes Docker networking much easier.

---

# 42. Docker Networking vs Kubernetes Networking

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

Docker networking is an important foundation for understanding Kubernetes networking.

---

# 43. Real-World DevOps Example

Suppose we deploy:

```text
Frontend
Backend
Database
Redis
```

Architecture:

```text
                  Internet
                     |
                     ↓
                  Nginx
                     |
              frontend-network
                     |
                  Backend
                     |
              backend-network
                /          \
               ↓            ↓
            MySQL          Redis
```

Possible exposure:

```text
Internet → Nginx only
```

Internal:

```text
Nginx → Backend
Backend → MySQL
Backend → Redis
```

MySQL and Redis should normally not be publicly exposed.

---

# 44. Important Concept: Service Discovery

Service discovery means finding another service without manually knowing its IP address.

Bad:

```text
DATABASE_HOST=172.18.0.4
```

Better:

```text
DATABASE_HOST=mysql
```

Docker DNS resolves:

```text
mysql → container IP
```

This makes applications more resilient when containers are recreated.

---

# 45. Important Concept: Container IPs Are Ephemeral

Suppose:

```text
mysql → 172.18.0.4
```

The container is deleted and recreated.

It may become:

```text
mysql → 172.18.0.7
```

Therefore:

```text
Do not depend on container IPs.
```

Use:

```text
container/service name
```

instead.

---

# 46. Port Mapping vs Container Communication

These are different.

Container-to-container:

```text
api → mysql:3306
```

does not require publishing MySQL to the host.

Host-to-container:

```text
Browser → localhost:8080 → nginx:80
```

requires port publishing.

Remember:

```text
Container → Container
       ↓
Docker network

Host → Container
       ↓
Port publishing may be required
```

---

# 47. Example

Create network:

```bash
docker network create demo
```

Start Nginx:

```bash
docker run -d \
  --name web \
  --network demo \
  -p 8080:80 \
  nginx
```

Start client:

```bash
docker run --rm \
  --network demo \
  alpine \
  wget -qO- http://web
```

Flow:

```text
Alpine
  |
  | http://web
  ↓
Docker DNS
  |
  ↓
web container
  |
  ↓
Nginx:80
```

Notice that the client does not need:

```text
-p
```

to communicate with Nginx internally.

---

# 48. Important Docker Networking Terms

### Network Namespace

Provides isolated networking.

### veth Pair

Virtual Ethernet connection between namespaces.

### Bridge

Connects containers on the same host.

### NAT

Translates network addresses.

### Port Publishing

Maps host port to container port.

### DNS

Resolves names to IP addresses.

### Overlay

Connects networks across Docker hosts.

### Network Driver

Defines how Docker networking works.

---

# 49. Docker Networking Mental Model

Remember this:

```text
                Docker Host
                     |
          +----------+----------+
          |                     |
      docker0              user network
          |                     |
      containers            containers
          |                     |
       veth pair            veth pair
          |                     |
     namespaces             namespaces
```

External traffic:

```text
Container
    ↓
Docker Network
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

# 50. DevOps Interview Explanation

If asked:

**"How does Docker networking work?"**

A good answer is:

> Docker networking allows containers to communicate with each other, the Docker host, and external networks. On Linux, Docker uses network namespaces, veth pairs, bridges, routing, NAT, and firewall rules. Containers can use different network drivers such as bridge, host, none, and overlay. With user-defined bridge networks, Docker provides DNS-based service discovery, allowing containers to communicate using names instead of hardcoded IP addresses. Port publishing maps a host port to a container port for host or external access.

---

# 51. Most Important Things to Remember

```text
1. Containers have isolated network namespaces.
2. veth pairs connect containers to Docker networks.
3. Bridge networks are common on a single Docker host.
4. User-defined bridge networks are preferred for applications.
5. Docker provides DNS-based service discovery.
6. Use service/container names instead of container IPs.
7. -p HOST:CONTAINER publishes a port.
8. EXPOSE does not publish a port.
9. Host networking removes much of the normal network isolation.
10. None networking provides no normal external network.
11. Overlay networks can connect workloads across Docker hosts.
12. Avoid publishing unnecessary database ports.
13. Docker networking is built on Linux networking.
14. Network troubleshooting should start with interface, IP, route, DNS, port, and firewall checks.
```

---

# 52. Final Docker Networking Flow

```text
                    INTERNET
                       |
                       ↓
                 Host Interface
                       |
                       ↓
                     NAT
                       |
                       ↓
                 Docker Network
                       |
                +------+------+
                |             |
                ↓             ↓
             Container     Container
                |             |
              eth0           eth0
                |             |
           Network Namespace
                |
              veth
                |
          Docker Bridge
```

The most important mental model is:

```text
Container
   ↓
Network Namespace
   ↓
veth
   ↓
Docker Network / Bridge
   ↓
Routing + NAT
   ↓
Host Network
   ↓
External Network
```

---

# 53. Chapter Summary

Docker networking provides the communication layer required for containerized applications.

The core concepts are:

```text
Network Namespace
        ↓
veth Pair
        ↓
Bridge Network
        ↓
Container IP
        ↓
Docker DNS
        ↓
Port Publishing
        ↓
NAT
        ↓
Host Network
        ↓
Internet
```

For DevOps, the most important skills are:

* Creating Docker networks
* Connecting containers
* Understanding bridge networking
* Understanding DNS
* Publishing ports
* Understanding NAT
* Troubleshooting connectivity
* Designing isolated application networks
* Using Docker Compose networking
* Protecting internal services

Once these concepts are clear, Kubernetes networking becomes much easier to understand.
