# Docker Networking — Commands

This file contains important Docker networking commands from **beginner to advanced level**, with examples and explanations.

---

# 1. List Docker Networks

```bash
docker network ls
```

Shows all Docker networks.

Example:

```text
NETWORK ID     NAME      DRIVER    SCOPE
xxxxxx         bridge    bridge    local
xxxxxx         host      host      local
xxxxxx         none      null      local
```

---

# 2. Inspect a Docker Network

```bash
docker network inspect bridge
```

Shows detailed information about the network.

You can find:

* Network ID
* Driver
* Subnet
* Gateway
* Connected containers
* Container IP addresses

---

# 3. Create a Docker Network

```bash
docker network create app-network
```

Verify:

```bash
docker network ls
```

---

# 4. Create a Bridge Network

```bash
docker network create \
  --driver bridge \
  app-network
```

The default driver is already `bridge`, so this is equivalent to:

```bash
docker network create app-network
```

---

# 5. Create a Network with Custom Subnet

```bash
docker network create \
  --subnet 172.20.0.0/16 \
  app-network
```

Inspect:

```bash
docker network inspect app-network
```

You should see the configured subnet.

---

# 6. Create a Network with Custom Gateway

```bash
docker network create \
  --subnet 172.20.0.0/16 \
  --gateway 172.20.0.1 \
  app-network
```

---

# 7. Run Container on a Specific Network

```bash
docker run -d \
  --name web \
  --network app-network \
  nginx
```

Check:

```bash
docker network inspect app-network
```

The `web` container should appear under connected containers.

---

# 8. Run Interactive Container on a Network

```bash
docker run --rm -it \
  --network app-network \
  alpine sh
```

Inside the container:

```bash
ip addr
```

Check routes:

```bash
ip route
```

Exit:

```bash
exit
```

---

# 9. Connect an Existing Container to a Network

Suppose the container already exists:

```bash
docker network connect app-network web
```

Check:

```bash
docker network inspect app-network
```

---

# 10. Disconnect a Container from a Network

```bash
docker network disconnect app-network web
```

Verify:

```bash
docker network inspect app-network
```

---

# 11. Remove a Network

```bash
docker network rm app-network
```

Docker will not normally remove a network while containers are still connected to it.

Check first:

```bash
docker network inspect app-network
```

---

# 12. Remove Unused Networks

```bash
docker network prune
```

Docker asks for confirmation.

Be careful because unused networks will be removed.

---

# 13. Check Container Network Information

```bash
docker inspect web
```

Search specifically for networking:

```bash
docker inspect web | grep -A 30 NetworkSettings
```

---

# 14. Get Container IP Address

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web
```

Example output:

```text
172.18.0.2
```

---

# 15. Get Container Gateway

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.Gateway}}{{end}}' web
```

---

# 16. Get Container MAC Address

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' web
```

---

# 17. Get Container Network Name

```bash
docker inspect -f '{{range $name, $network := .NetworkSettings.Networks}}{{$name}}{{end}}' web
```

---

# 18. Show Published Ports

```bash
docker port web
```

Example:

```text
80/tcp -> 0.0.0.0:8080
```

This means:

```text
Host:8080 → Container:80
```

---

# 19. Publish a Container Port

```bash
docker run -d \
  --name web \
  -p 8080:80 \
  nginx
```

Test:

```bash
curl http://localhost:8080
```

---

# 20. Publish Multiple Ports

```bash
docker run -d \
  --name app \
  -p 8080:80 \
  -p 8443:443 \
  nginx
```

Check:

```bash
docker port app
```

---

# 21. Bind Published Port to Localhost

```bash
docker run -d \
  --name web \
  -p 127.0.0.1:8080:80 \
  nginx
```

Test:

```bash
curl http://127.0.0.1:8080
```

---

# 22. Publish a UDP Port

TCP is the default.

For UDP:

```bash
docker run -d \
  --name app \
  -p 5353:5353/udp \
  <image>
```

---

# 23. Publish TCP Explicitly

```bash
docker run -d \
  --name app \
  -p 8080:80/tcp \
  nginx
```

---

# 24. Check Docker Containers

```bash
docker ps
```

Show all containers:

```bash
docker ps -a
```

---

# 25. Check Container IP Using Inspect

```bash
docker inspect web
```

Look for:

```text
NetworkSettings
```

A shorter command:

```bash
docker inspect -f '{{.NetworkSettings.IPAddress}}' web
```

Note:

For containers attached to custom networks, the IP may be under the individual network entry instead.

---

# 26. Enter a Running Container

```bash
docker exec -it web sh
```

If Bash exists:

```bash
docker exec -it web bash
```

---

# 27. Check Network Interfaces Inside Container

```bash
docker exec web ip addr
```

Or:

```bash
docker exec web ip link
```

---

# 28. Check Routing Table Inside Container

```bash
docker exec web ip route
```

Example:

```text
default via 172.18.0.1 dev eth0
172.18.0.0/16 dev eth0
```

---

# 29. Check DNS Configuration Inside Container

```bash
docker exec web cat /etc/resolv.conf
```

---

# 30. Test DNS Resolution

If the container has `getent`:

```bash
docker exec web getent hosts google.com
```

For another container:

```bash
docker exec client getent hosts web
```

---

# 31. Test Container-to-Container Connectivity

Create network:

```bash
docker network create app-network
```

Start server:

```bash
docker run -d \
  --name web \
  --network app-network \
  nginx
```

Start client:

```bash
docker run --rm \
  --network app-network \
  alpine \
  wget -qO- http://web
```

This tests:

```text
client → Docker DNS → web → Nginx
```

---

# 32. Test Using Container IP

Find IP:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web
```

Then test:

```bash
docker run --rm \
  --network app-network \
  alpine \
  wget -qO- http://<CONTAINER-IP>
```

For applications, prefer the container/service name instead of the IP.

---

# 33. Test HTTP Connectivity

From the host:

```bash
curl http://localhost:8080
```

Verbose:

```bash
curl -v http://localhost:8080
```

Headers only:

```bash
curl -I http://localhost:8080
```

---

# 34. Test HTTPS

```bash
curl -v https://example.com
```

Ignore certificate verification for testing only:

```bash
curl -k https://example.com
```

Do not use `-k` as a production security solution.

---

# 35. Check Listening Ports on Host

```bash
ss -ltnp
```

Check a specific port:

```bash
ss -ltnp | grep :8080
```

Alternative:

```bash
sudo lsof -i :8080
```

---

# 36. Check Listening Ports Inside Container

```bash
docker exec web ss -lnt
```

If `ss` is not installed, use another diagnostic image/tool or inspect the application configuration.

---

# 37. Test a TCP Port with Netcat

From a suitable container:

```bash
nc -zv web 80
```

Meaning:

```text
-z → scan without sending data
-v → verbose
```

Example:

```bash
docker run --rm \
  --network app-network \
  alpine \
  nc -zv web 80
```

---

# 38. Check Docker Bridge

On the Linux host:

```bash
ip addr show docker0
```

Check link:

```bash
ip link show docker0
```

---

# 39. Show Linux Bridges

If `bridge-utils` is installed:

```bash
brctl show
```

Modern systems can also use:

```bash
ip link
```

or:

```bash
bridge link
```

---

# 40. Show Docker-Related Interfaces

```bash
ip link
```

You may see:

```text
docker0
vethXXXX
```

The exact interface names vary.

---

# 41. Show Routing Table

```bash
ip route
```

Docker networks may create routes such as:

```text
172.17.0.0/16 dev docker0
```

Exact routes depend on your configuration.

---

# 42. Show ARP/Neighbour Information

```bash
ip neigh
```

This can help troubleshoot local network communication.

---

# 43. Check Docker's Default Bridge

```bash
docker network inspect bridge
```

Look for:

```text
Subnet
Gateway
Containers
```

---

# 44. Check Network Driver

```bash
docker network inspect app-network
```

Look for:

```text
Driver
```

Example:

```text
"Driver": "bridge"
```

---

# 45. List Networks with Format

```bash
docker network ls --format 'table {{.ID}}\t{{.Name}}\t{{.Driver}}\t{{.Scope}}'
```

---

# 46. Inspect Only Network Subnet

```bash
docker network inspect -f '{{range .IPAM.Config}}{{.Subnet}}{{end}}' app-network
```

---

# 47. Inspect Network Gateway

```bash
docker network inspect -f '{{range .IPAM.Config}}{{.Gateway}}{{end}}' app-network
```

---

# 48. List Containers Attached to a Network

```bash
docker network inspect app-network
```

Look under:

```text
Containers
```

---

# 49. Find Container Network Names

```bash
docker inspect -f '{{range $name, $_ := .NetworkSettings.Networks}}{{$name}} {{end}}' web
```

---

# 50. Use Host Network

```bash
docker run --rm \
  --network host \
  nginx
```

Check:

```bash
docker inspect <container>
```

Host networking should be used intentionally because it changes normal container network isolation.

---

# 51. Use None Network

```bash
docker run --rm \
  --network none \
  alpine \
  ip addr
```

You should see the loopback interface.

---

# 52. Show Docker Network Events

```bash
docker events
```

Filter network events:

```bash
docker events --filter type=network
```

This can help when debugging network creation or deletion.

---

# 53. Docker Network Inspect with JSON Tools

```bash
docker network inspect app-network
```

If `jq` is installed:

```bash
docker network inspect app-network | jq
```

Get subnet:

```bash
docker network inspect app-network | jq '.[0].IPAM.Config'
```

---

# 54. Check Docker Information

```bash
docker info
```

This provides Docker daemon information.

Search networking information:

```bash
docker info | grep -i network
```

---

# 55. Check Docker Version

```bash
docker version
```

Short version:

```bash
docker --version
```

---

# 56. Docker Compose Network Commands

List Compose services:

```bash
docker compose ps
```

List project networks:

```bash
docker network ls
```

Compose usually creates a project-specific network.

Example:

```text
myproject_default
```

---

# 57. Start a Compose Application

```bash
docker compose up -d
```

Check:

```bash
docker compose ps
```

---

# 58. Stop a Compose Application

```bash
docker compose down
```

This removes the containers and the default Compose network created for the project.

---

# 59. Inspect Compose Network

```bash
docker network ls
```

Then:

```bash
docker network inspect <project>_default
```

---

# 60. Test Compose Service DNS

Suppose Compose contains:

```yaml
services:
  web:
    image: nginx

  client:
    image: alpine
```

From the client:

```bash
docker compose exec client getent hosts web
```

The service name:

```text
web
```

is used for service discovery.

---

# 61. Test Compose Service Connectivity

```bash
docker compose exec client wget -qO- http://web
```

This tests:

```text
client → DNS → web → nginx
```

---

# 62. View Container Logs

```bash
docker logs web
```

Follow logs:

```bash
docker logs -f web
```

Logs can help determine whether the application is actually running and listening.

---

# 63. Check Container Processes

```bash
docker top web
```

This can help determine whether the expected application process is running.

---

# 64. Check Container Configuration

```bash
docker inspect web
```

Useful sections:

```text
NetworkSettings
Config
Mounts
State
HostConfig
```

---

# 65. Check Port Mapping Quickly

```bash
docker ps
```

Example:

```text
0.0.0.0:8080->80/tcp
```

Meaning:

```text
Host 8080
     ↓
Container 80
```

---

# 66. Find Which Process Uses a Host Port

For port 8080:

```bash
sudo lsof -i :8080
```

Or:

```bash
ss -ltnp | grep :8080
```

This is useful when Docker reports:

```text
address already in use
```

---

# 67. Check Container Connectivity Step-by-Step

Start with:

```bash
docker ps
```

Then:

```bash
docker network ls
```

Then:

```bash
docker network inspect app-network
```

Then:

```bash
docker inspect web
```

Then:

```bash
docker exec web ip addr
```

Then:

```bash
docker exec web ip route
```

Then:

```bash
docker exec web cat /etc/resolv.conf
```

Finally test:

```bash
docker exec web getent hosts google.com
```

---

# 68. Complete Docker Network Health Check

Run:

```bash
docker ps
```

```bash
docker network ls
```

```bash
docker network inspect bridge
```

```bash
ip addr
```

```bash
ip route
```

```bash
ss -ltnp
```

For a specific container:

```bash
docker inspect <container>
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

---

# 69. Docker Network Troubleshooting Flow

Use this order:

```text
1. Is the container running?
        ↓
2. Is the container attached to the correct network?
        ↓
3. Does the container have an IP?
        ↓
4. Does it have a route?
        ↓
5. Does DNS work?
        ↓
6. Can it reach the target container?
        ↓
7. Is the target application listening?
        ↓
8. Is the port published correctly?
        ↓
9. Is the host firewall blocking traffic?
        ↓
10. Is an external firewall/security group blocking traffic?
```

---

# 70. Common Error: Port Already in Use

Error:

```text
bind: address already in use
```

Check:

```bash
sudo lsof -i :8080
```

or:

```bash
ss -ltnp | grep :8080
```

Solutions:

Use another host port:

```bash
docker run -d -p 8081:80 nginx
```

Or stop the process/container using the port if appropriate.

---

# 71. Common Error: Cannot Connect to Another Container

Check networks:

```bash
docker network ls
```

Inspect:

```bash
docker network inspect app-network
```

Make sure both containers are attached.

Connect if required:

```bash
docker network connect app-network container2
```

Test DNS:

```bash
docker exec container1 getent hosts container2
```

---

# 72. Common Error: DNS Failure

Check:

```bash
docker exec container cat /etc/resolv.conf
```

Test:

```bash
docker exec container getent hosts google.com
```

Test container-name resolution:

```bash
docker exec client getent hosts web
```

If container-to-container DNS works but external DNS does not, investigate the container's external DNS path.

---

# 73. Common Error: Connection Refused

Check whether the application is listening:

```bash
docker exec web ss -lnt
```

Check the expected port.

For example:

```text
0.0.0.0:80
```

Then test:

```bash
curl http://localhost:8080
```

If the host port is published correctly but the application is not listening inside the container, publishing the port will not fix the application.

---

# 74. Common Error: Connection Timeout

Check:

```bash
docker ps
```

```bash
docker network inspect app-network
```

```bash
docker exec container ip route
```

```bash
docker exec container getent hosts target
```

Then investigate:

* Firewall
* Routing
* Network configuration
* Application health
* External network rules

---

# 75. Useful One-Liners

List networks:

```bash
docker network ls
```

Inspect network:

```bash
docker network inspect bridge
```

Container IP:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web
```

Container ports:

```bash
docker port web
```

Host listening ports:

```bash
ss -ltnp
```

Container interfaces:

```bash
docker exec web ip addr
```

Container routes:

```bash
docker exec web ip route
```

Container DNS:

```bash
docker exec web cat /etc/resolv.conf
```

Container DNS test:

```bash
docker exec web getent hosts google.com
```

---

# 76. Important Command Cheat Sheet

| Task                 | Command                                      |
| -------------------- | -------------------------------------------- |
| List networks        | `docker network ls`                          |
| Inspect network      | `docker network inspect NAME`                |
| Create network       | `docker network create NAME`                 |
| Remove network       | `docker network rm NAME`                     |
| Connect container    | `docker network connect NET CONTAINER`       |
| Disconnect container | `docker network disconnect NET CONTAINER`    |
| Network cleanup      | `docker network prune`                       |
| Container details    | `docker inspect CONTAINER`                   |
| Container IP         | `docker inspect ...`                         |
| Published ports      | `docker port CONTAINER`                      |
| Run on network       | `docker run --network NET IMAGE`             |
| Host network         | `docker run --network host IMAGE`            |
| No network           | `docker run --network none IMAGE`            |
| Host interfaces      | `ip addr`                                    |
| Host routes          | `ip route`                                   |
| Host ports           | `ss -ltnp`                                   |
| Container shell      | `docker exec -it CONTAINER sh`               |
| Container interfaces | `docker exec CONTAINER ip addr`              |
| Container routes     | `docker exec CONTAINER ip route`             |
| Container DNS        | `docker exec CONTAINER cat /etc/resolv.conf` |
| Docker info          | `docker info`                                |
| Compose status       | `docker compose ps`                          |
| Compose start        | `docker compose up -d`                       |
| Compose stop         | `docker compose down`                        |

---

# 77. Commands to Memorize First

Do not try to memorize every command immediately.

Start with these:

```bash
docker network ls
```

```bash
docker network create app-network
```

```bash
docker network inspect app-network
```

```bash
docker network connect app-network container
```

```bash
docker network disconnect app-network container
```

```bash
docker inspect container
```

```bash
docker port container
```

```bash
docker exec -it container sh
```

```bash
docker exec container ip addr
```

```bash
docker exec container ip route
```

```bash
docker exec container cat /etc/resolv.conf
```

```bash
docker run -d --network app-network nginx
```

```bash
docker run -d -p 8080:80 nginx
```

---

# 78. DevOps Troubleshooting Cheat Sheet

When a Docker application is unreachable:

```text
Container problem?
        ↓
docker ps
        ↓
Network problem?
        ↓
docker network inspect
        ↓
IP problem?
        ↓
docker exec CONTAINER ip addr
        ↓
Route problem?
        ↓
docker exec CONTAINER ip route
        ↓
DNS problem?
        ↓
docker exec CONTAINER getent hosts TARGET
        ↓
Port problem?
        ↓
docker port CONTAINER
        ↓
Application problem?
        ↓
docker exec CONTAINER ss -lnt
        ↓
Host firewall problem?
        ↓
ss / firewall inspection
```

---

# 79. Final Command Flow

The most important Docker networking flow to remember is:

```text
docker network ls
        ↓
docker network inspect
        ↓
docker inspect
        ↓
docker exec
        ↓
ip addr
        ↓
ip route
        ↓
DNS test
        ↓
port test
        ↓
curl / nc
```

This command sequence is extremely useful during real-world Docker troubleshooting.

---

# 80. Final Summary

Docker networking commands help you:

```text
Create networks
      ↓
Connect containers
      ↓
Inspect networks
      ↓
Find IP addresses
      ↓
Test DNS
      ↓
Test connectivity
      ↓
Check ports
      ↓
Troubleshoot applications
```

The most important commands are:

```bash
docker network ls
docker network inspect
docker network create
docker network connect
docker network disconnect
docker inspect
docker port
docker exec
docker run --network
docker run -p
docker compose
```

Combine these with Linux networking commands:

```bash
ip addr
ip route
ip neigh
ss
curl
nc
```

and you have a strong foundation for **Docker networking troubleshooting in DevOps**.
