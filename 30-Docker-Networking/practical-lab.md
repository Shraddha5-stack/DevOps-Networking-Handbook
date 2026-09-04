# Docker Networking — Practical Lab

This lab provides hands-on practice with Docker networking from **basic to advanced level**.

You will practice:

* Docker networks
* Bridge networking
* Container IP addresses
* Container-to-container communication
* Docker DNS
* Port publishing
* Network isolation
* Multiple networks
* Docker Compose networking
* Network troubleshooting

---

# 1. Prerequisites

Check Docker:

```bash
docker --version
```

Check Docker daemon:

```bash
docker info
```

Check running containers:

```bash
docker ps
```

If Docker is not running, start it according to your Linux distribution.

---

# 2. Lab Cleanup

Before starting, remove old lab containers if they exist.

```bash
docker rm -f web client server 2>/dev/null || true
```

Remove the lab network if it already exists:

```bash
docker network rm app-network 2>/dev/null || true
```

---

# 3. List Existing Docker Networks

Run:

```bash
docker network ls
```

You should normally see networks such as:

```text
bridge
host
none
```

Understand:

```text
bridge → normal container networking
host   → host networking
none   → no normal network
```

---

# 4. Inspect the Default Bridge

Run:

```bash
docker network inspect bridge
```

Look for:

* Driver
* Subnet
* Gateway
* Containers

Find the bridge interface on Linux:

```bash
ip addr show docker0
```

Also check:

```bash
ip link show docker0
```

---

# 5. Run Your First Container

Run:

```bash
docker run -d --name web nginx
```

Check:

```bash
docker ps
```

Inspect:

```bash
docker inspect web
```

Check its IP:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web
```

Record the IP:

```text
Web container IP:
____________________
```

---

# 6. Check Networking Inside the Container

Run:

```bash
docker exec web ip addr
```

You should see interfaces such as:

```text
lo
eth0
```

Check routes:

```bash
docker exec web ip route
```

Check DNS:

```bash
docker exec web cat /etc/resolv.conf
```

---

# 7. Check Nginx Port

Check ports inside the container:

```bash
docker exec web ss -lnt
```

Nginx normally listens on:

```text
80
```

Now check published ports:

```bash
docker port web
```

You may see no host mapping because we did not use `-p`.

---

# 8. Test Container from the Host

Find the container IP:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web
```

Then test:

```bash
curl http://<CONTAINER-IP>
```

Replace `<CONTAINER-IP>` with the actual IP.

Example:

```bash
curl http://172.17.0.2
```

You should receive the Nginx HTML response if the host can directly reach that container IP in your environment.

---

# 9. Publish a Port

Remove the previous container:

```bash
docker rm -f web
```

Create a new one:

```bash
docker run -d \
  --name web \
  -p 8080:80 \
  nginx
```

Check:

```bash
docker ps
```

You should see something similar to:

```text
0.0.0.0:8080->80/tcp
```

---

# 10. Test Port Publishing

Run:

```bash
curl http://localhost:8080
```

You should receive the Nginx response.

Test with verbose output:

```bash
curl -v http://localhost:8080
```

Check the port:

```bash
docker port web
```

Understand:

```text
Host:8080
    ↓
Docker port mapping
    ↓
Container:80
    ↓
Nginx
```

---

# 11. Create a User-Defined Network

Create:

```bash
docker network create app-network
```

Check:

```bash
docker network ls
```

Inspect:

```bash
docker network inspect app-network
```

Record:

```text
Network subnet:
____________________

Gateway:
____________________
```

---

# 12. Run a Web Container on the Custom Network

Run:

```bash
docker run -d \
  --name web \
  --network app-network \
  nginx
```

Check:

```bash
docker ps
```

Inspect:

```bash
docker network inspect app-network
```

You should see `web` connected to the network.

---

# 13. Start a Client Container

Run:

```bash
docker run -d \
  --name client \
  --network app-network \
  alpine \
  sleep 3600
```

Check:

```bash
docker ps
```

---

# 14. Test Container-to-Container DNS

From the client:

```bash
docker exec client getent hosts web
```

Expected result:

```text
<IP-ADDRESS> web
```

This demonstrates Docker's internal DNS-based service discovery.

Important:

```text
client
   |
   ↓
Docker DNS
   |
   ↓
web
```

---

# 15. Test Container-to-Container HTTP

Run:

```bash
docker exec client wget -qO- http://web
```

You should receive the Nginx HTML response.

This proves:

```text
client
  ↓
DNS
  ↓
web
  ↓
Nginx:80
```

No `-p` option is required for this internal communication.

---

# 16. Check Client Network Configuration

Run:

```bash
docker exec client ip addr
```

Then:

```bash
docker exec client ip route
```

Then:

```bash
docker exec client cat /etc/resolv.conf
```

Observe:

* Client IP
* Default gateway
* DNS configuration
* Network interface

---

# 17. Inspect the Custom Network

Run:

```bash
docker network inspect app-network
```

Find:

```text
Subnet
Gateway
Containers
```

You should see:

```text
web
client
```

Both containers should have IP addresses.

---

# 18. Test Connectivity Using Container Name

Run:

```bash
docker exec client wget -qO- http://web
```

The important part is:

```text
http://web
```

not:

```text
http://172.x.x.x
```

This demonstrates service discovery.

---

# 19. Test Connectivity Using Container IP

Find the IP:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web
```

Then:

```bash
docker exec client wget -qO- http://<WEB-IP>
```

Compare:

```text
Using IP:
http://172.x.x.x

Using name:
http://web
```

Preferred approach:

```text
Use the name.
```

---

# 20. Connect an Existing Container to Another Network

Create another network:

```bash
docker network create second-network
```

Check:

```bash
docker network ls
```

Connect `web`:

```bash
docker network connect second-network web
```

Inspect:

```bash
docker inspect web
```

The container should now have connections to:

```text
app-network
second-network
```

---

# 21. Check Multiple Network Interfaces

Run:

```bash
docker exec web ip addr
```

You may see more than one network interface depending on the container and environment.

Inspect:

```bash
docker inspect web
```

Look at:

```text
NetworkSettings
```

---

# 22. Disconnect from a Network

Run:

```bash
docker network disconnect second-network web
```

Verify:

```bash
docker network inspect second-network
```

The `web` container should no longer appear there.

---

# 23. Network Isolation Test

Create two networks:

```bash
docker network create network-a
docker network create network-b
```

Create container A:

```bash
docker run -d \
  --name container-a \
  --network network-a \
  nginx
```

Create container B:

```bash
docker run -d \
  --name container-b \
  --network network-b \
  nginx
```

Check:

```bash
docker network inspect network-a
```

and:

```bash
docker network inspect network-b
```

The containers are on different networks.

Try:

```bash
docker exec container-a getent hosts container-b
```

The name should not resolve simply because the containers are on separate user-defined networks.

---

# 24. Connect the Networks Through One Container

Connect `container-a` to `network-b`:

```bash
docker network connect network-b container-a
```

Now:

```text
network-a
   |
container-a
   |
network-b
   |
container-b
```

Test:

```bash
docker exec container-a getent hosts container-b
```

This demonstrates how a container can participate in multiple networks.

---

# 25. Port Publishing vs Internal Communication

We have:

```text
web
 |
 | internal Docker network
 ↓
client
```

No port publishing is needed.

But for browser access:

```text
Browser
   |
   ↓
Host:8080
   |
   ↓
Container:80
```

we need:

```bash
-p 8080:80
```

Remember:

```text
Container → Container
       ↓
Docker network

Host → Container
       ↓
Port publishing
```

---

# 26. Localhost Port Binding Lab

Remove web:

```bash
docker rm -f web
```

Run:

```bash
docker run -d \
  --name web \
  -p 127.0.0.1:8080:80 \
  nginx
```

Check:

```bash
docker port web
```

Test:

```bash
curl http://127.0.0.1:8080
```

This binds the host port specifically to localhost.

---

# 27. Host Networking Lab

Run:

```bash
docker run -d \
  --name host-nginx \
  --network host \
  nginx
```

Check:

```bash
docker ps
```

Inspect:

```bash
docker inspect host-nginx
```

Check host ports:

```bash
ss -ltnp
```

Important:

Host networking changes the normal container network isolation model.

Remove after testing:

```bash
docker rm -f host-nginx
```

---

# 28. None Networking Lab

Run:

```bash
docker run --rm \
  --network none \
  alpine \
  ip addr
```

You should normally see the loopback interface.

Check:

```bash
docker run --rm \
  --network none \
  alpine \
  ip route
```

Understand:

```text
none
 ↓
No normal external container networking
```

---

# 29. Docker Network Information

Run:

```bash
docker network ls
```

Then:

```bash
docker network inspect app-network
```

Record:

```text
Driver:
____________________

Subnet:
____________________

Gateway:
____________________

Connected containers:
____________________
```

---

# 30. Inspect Linux Docker Bridge

On the host:

```bash
ip addr show docker0
```

Check:

```bash
ip link show docker0
```

Check routes:

```bash
ip route
```

Look for Docker-related private networks.

---

# 31. Check Docker-Related Virtual Interfaces

Run:

```bash
ip link
```

You may see:

```text
docker0
vethXXXX
```

The exact veth interface names depend on the current containers and Docker environment.

---

# 32. Check Host Listening Ports

Run:

```bash
ss -ltnp
```

Check specifically:

```bash
ss -ltnp | grep :8080
```

Alternative:

```bash
sudo lsof -i :8080
```

This is useful when Docker reports:

```text
address already in use
```

---

# 33. Port Conflict Lab

Try to start another container using the same host port:

```bash
docker run -d \
  --name web2 \
  -p 8080:80 \
  nginx
```

You may receive a port conflict because `8080` is already being used by `web`.

Check:

```bash
ss -ltnp | grep :8080
```

Fix by using another host port:

```bash
docker run -d \
  --name web2 \
  -p 8081:80 \
  nginx
```

Test:

```bash
curl http://localhost:8081
```

---

# 34. Docker DNS Lab

Create:

```bash
docker network create dns-lab
```

Start server:

```bash
docker run -d \
  --name server \
  --network dns-lab \
  nginx
```

Start client:

```bash
docker run -d \
  --name client \
  --network dns-lab \
  alpine \
  sleep 3600
```

Test:

```bash
docker exec client getent hosts server
```

Test HTTP:

```bash
docker exec client wget -qO- http://server
```

This demonstrates:

```text
server name
    ↓
Docker DNS
    ↓
server IP
```

---

# 35. DNS Failure Investigation

Check DNS:

```bash
docker exec client cat /etc/resolv.conf
```

Check name resolution:

```bash
docker exec client getent hosts server
```

Check network membership:

```bash
docker network inspect dns-lab
```

Make sure both containers are attached to the same user-defined network.

---

# 36. Container Route Troubleshooting

Run:

```bash
docker exec client ip route
```

Look for a default route similar to:

```text
default via <gateway> dev eth0
```

Then inspect the network:

```bash
docker network inspect dns-lab
```

Compare the gateway with the container route.

---

# 37. Container IP Troubleshooting

Run:

```bash
docker exec client ip addr
```

Find the `eth0` address.

Then:

```bash
docker inspect client
```

Compare the address.

Questions:

```text
Does the container have an IP?
        ↓
Is it on the correct network?
        ↓
Is the gateway correct?
```

---

# 38. Application Port Troubleshooting

Check the server:

```bash
docker exec server ss -lnt
```

Nginx should normally listen on port:

```text
80
```

Then test:

```bash
docker exec client wget -qO- http://server:80
```

If DNS works but connection fails, check whether the application is listening.

---

# 39. Complete Troubleshooting Exercise

Create:

```bash
docker network create troubleshoot-net
```

Run:

```bash
docker run -d \
  --name server \
  --network troubleshoot-net \
  nginx
```

Run client:

```bash
docker run -d \
  --name client \
  --network troubleshoot-net \
  alpine \
  sleep 3600
```

Now troubleshoot in this order.

### Step 1 — Check containers

```bash
docker ps
```

### Step 2 — Check network

```bash
docker network inspect troubleshoot-net
```

### Step 3 — Check client IP

```bash
docker exec client ip addr
```

### Step 4 — Check route

```bash
docker exec client ip route
```

### Step 5 — Check DNS

```bash
docker exec client getent hosts server
```

### Step 6 — Check server port

```bash
docker exec server ss -lnt
```

### Step 7 — Test application

```bash
docker exec client wget -qO- http://server
```

---

# 40. Docker Compose Networking Lab

Create a directory:

```bash
mkdir -p ~/docker-network-lab
cd ~/docker-network-lab
```

Create:

```bash
nano compose.yaml
```

Add:

```yaml
services:

  web:
    image: nginx
    ports:
      - "8080:80"

  client:
    image: alpine
    command: ["sh", "-c", "sleep 3600"]
```

Save the file.

---

# 41. Start Compose Application

Run:

```bash
docker compose up -d
```

Check:

```bash
docker compose ps
```

List networks:

```bash
docker network ls
```

You should see a project-specific network.

---

# 42. Inspect Compose Network

Find the network:

```bash
docker network ls
```

Then:

```bash
docker network inspect <project>_default
```

The exact project/network name depends on the directory and Compose configuration.

---

# 43. Test Compose DNS

Run:

```bash
docker compose exec client getent hosts web
```

The service name:

```text
web
```

should resolve.

Test HTTP:

```bash
docker compose exec client wget -qO- http://web
```

This demonstrates Compose service discovery.

---

# 44. Test Compose Port Publishing

From the host:

```bash
curl http://localhost:8080
```

Architecture:

```text
Host
 |
 | 8080
 ↓
web:80
```

Inside Compose:

```text
client
  |
  | http://web
  ↓
web:80
```

---

# 45. Stop Compose Application

Run:

```bash
docker compose down
```

Check:

```bash
docker compose ps
```

Check networks:

```bash
docker network ls
```

---

# 46. Docker Network Security Exercise

Create:

```bash
docker network create frontend-net
docker network create backend-net
```

Create backend:

```bash
docker run -d \
  --name backend \
  --network backend-net \
  nginx
```

Create database simulation:

```bash
docker run -d \
  --name database \
  --network backend-net \
  nginx
```

Create frontend:

```bash
docker run -d \
  --name frontend \
  --network frontend-net \
  nginx
```

Architecture:

```text
frontend-net

frontend
```

and:

```text
backend-net

backend
   |
database
```

The frontend is isolated from the backend network.

---

# 47. Connect Backend to Frontend Network

Run:

```bash
docker network connect frontend-net backend
```

Now:

```text
frontend-net
      |
  frontend
      |
    backend
      |
backend-net
      |
  database
```

This creates a controlled connection between the two network segments.

---

# 48. Test Network Isolation

From frontend:

```bash
docker exec frontend getent hosts database
```

It should not resolve simply because `database` is only on `backend-net`.

From backend:

```bash
docker exec backend getent hosts database
```

It should resolve because both are on `backend-net`.

---

# 49. Observe Network Changes

Run:

```bash
docker network inspect frontend-net
```

Then:

```bash
docker network inspect backend-net
```

Observe which containers belong to each network.

---

# 50. Cleanup Lab Containers

Remove containers:

```bash
docker rm -f web client server web2 container-a container-b backend database frontend 2>/dev/null || true
```

Remove networks:

```bash
docker network rm app-network second-network network-a network-b dns-lab troubleshoot-net frontend-net backend-net 2>/dev/null || true
```

If Compose is still running:

```bash
docker compose down 2>/dev/null || true
```

---

# 51. Verify Cleanup

Check containers:

```bash
docker ps -a
```

Check networks:

```bash
docker network ls
```

Make sure your lab resources have been removed.

---

# 52. Practical Questions

Answer these after completing the lab.

### Question 1

What is the difference between:

```bash
-p 8080:80
```

and:

```bash
--network app-network
```

Answer:

```text
-p → publishes a container port to the host
--network → attaches the container to a Docker network
```

---

### Question 2

Why should you use container/service names instead of container IPs?

Answer:

```text
Container IPs can change when containers are recreated.
Docker DNS allows applications to use stable names.
```

---

### Question 3

How do two containers communicate?

Answer:

```text
When they share a compatible Docker network,
they can communicate through the Docker network
and Docker DNS can resolve their names.
```

---

### Question 4

Does `EXPOSE 80` publish port 80?

Answer:

```text
No.
EXPOSE documents the container port.
-p is used to publish the port.
```

---

### Question 5

What command shows Docker networks?

```bash
docker network ls
```

---

### Question 6

What command shows detailed network information?

```bash
docker network inspect <network>
```

---

### Question 7

How do you connect an existing container to a network?

```bash
docker network connect <network> <container>
```

---

### Question 8

How do you disconnect it?

```bash
docker network disconnect <network> <container>
```

---

### Question 9

How do you find the host process using port 8080?

```bash
ss -ltnp | grep :8080
```

or:

```bash
sudo lsof -i :8080
```

---

### Question 10

What is the Docker networking troubleshooting order?

```text
Container
   ↓
Network
   ↓
IP
   ↓
Route
   ↓
DNS
   ↓
Port
   ↓
Application
   ↓
Firewall
```

---

# 53. Hands-On Challenge

Complete this without looking at the previous steps.

## Requirement

Create:

```text
network: devops-net
container: nginx-server
container: test-client
```

The containers must:

* Use the same user-defined network.
* Resolve each other by name.
* Communicate using HTTP.
* Nginx should listen on port 80.
* Host should access Nginx through port 8085.

---

## Expected Architecture

```text
                  Host
                   |
                 :8085
                   |
                   ↓
             nginx-server
                   |
              devops-net
                   |
              test-client
```

---

## Expected Commands

You should be able to write these yourself:

```bash
docker network create devops-net
```

```bash
docker run -d \
  --name nginx-server \
  --network devops-net \
  -p 8085:80 \
  nginx
```

```bash
docker run -d \
  --name test-client \
  --network devops-net \
  alpine \
  sleep 3600
```

Test DNS:

```bash
docker exec test-client getent hosts nginx-server
```

Test HTTP:

```bash
docker exec test-client wget -qO- http://nginx-server
```

Test from host:

```bash
curl http://localhost:8085
```

Inspect:

```bash
docker network inspect devops-net
```

Cleanup:

```bash
docker rm -f nginx-server test-client
docker network rm devops-net
```

---

# 54. Final Practical Checklist

After completing this lab, you should be able to perform:

```text
[ ] List Docker networks
[ ] Create a Docker network
[ ] Inspect a network
[ ] Run a container on a network
[ ] Find a container IP
[ ] Check container interfaces
[ ] Check container routes
[ ] Check container DNS
[ ] Test container-to-container DNS
[ ] Test container-to-container HTTP
[ ] Publish a port
[ ] Test published ports
[ ] Find port conflicts
[ ] Connect a container to another network
[ ] Disconnect a container
[ ] Understand network isolation
[ ] Use host networking
[ ] Use none networking
[ ] Understand Docker Compose networking
[ ] Troubleshoot Docker networking
[ ] Design a basic multi-container network
```

---

# 55. Key Commands to Practice Again

Run these from memory:

```bash
docker network ls
```

```bash
docker network create devops-net
```

```bash
docker network inspect devops-net
```

```bash
docker run -d --network devops-net nginx
```

```bash
docker network connect devops-net <container>
```

```bash
docker network disconnect devops-net <container>
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
docker exec <container> cat /etc/resolv.conf
```

```bash
docker exec <container> getent hosts <target>
```

```bash
docker exec <container> wget -qO- http://<target>
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

---

# 56. Final Lab Architecture

The complete Docker networking model practiced in this lab is:

```text
                         HOST
                           |
                    Port Publishing
                           |
                         :8080
                           |
                           ↓
                    +-------------+
                    |    Nginx    |
                    |  Container  |
                    +-------------+
                           |
                         eth0
                           |
                    Network Namespace
                           |
                         veth
                           |
                    Docker Network
                           |
             +-------------+-------------+
             |                           |
             ↓                           ↓
        test-client                 backend
             |                           |
             +----------- DNS ------------+
                           |
                    Container Names
                           |
                    Internal Traffic
```

The key DevOps lesson is:

```text
Public traffic
      ↓
Published port
      ↓
Application container

Internal traffic
      ↓
Docker network
      ↓
Service/container name
      ↓
Docker DNS
```

Docker networking is not just about assigning IP addresses. It is about **connectivity, service discovery, isolation, port exposure, routing, and troubleshooting**.
