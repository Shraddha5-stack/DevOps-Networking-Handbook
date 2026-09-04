# 🐳 Docker Networking

## 📌 Overview

Docker networking allows containers to communicate with:

* Other containers
* The Docker host
* External networks
* The internet
* Databases
* APIs
* Load balancers
* Other Docker networks

Docker networking is an important concept for DevOps because applications commonly run as multiple interconnected containers.

---

# 🎯 Learning Objectives

By completing this chapter, you will understand:

* What Docker networking is
* How Docker containers communicate
* Docker network drivers
* Docker bridge networking
* Docker host networking
* Docker none networking
* Custom bridge networks
* Container-to-container communication
* Container-to-host communication
* Port publishing
* DNS-based container discovery
* Network isolation
* Docker network namespaces
* veth pairs
* Docker bridge
* NAT
* Docker Compose networking
* Docker networking troubleshooting

---

# 🧠 Docker Networking Architecture

A simplified Docker networking architecture:

```text
                    Internet
                       |
                       |
                  Docker Host
                       |
                  docker0 bridge
                       |
          +------------+------------+
          |                         |
      Container A              Container B
       eth0                     eth0
          |                         |
       App :80                  App :80
```

Docker uses Linux networking technologies underneath.

Important components include:

```text
Network Namespace
       ↓
veth pair
       ↓
Linux Bridge
       ↓
Routing / NAT
       ↓
External Network
```

---

# 🌐 Docker Network Drivers

Docker provides different network drivers.

| Driver  | Purpose                                                   |
| ------- | --------------------------------------------------------- |
| bridge  | Common networking for containers                          |
| host    | Container uses host network                               |
| none    | No networking                                             |
| overlay | Multi-host Docker networking                              |
| macvlan | Container gets a network identity on the physical network |
| ipvlan  | Similar concept using Linux ipvlan                        |

The most commonly encountered driver for basic Docker networking is:

```text
bridge
```

---

# 🔵 Bridge Network

Docker's bridge networking allows containers to communicate through a Linux bridge.

Conceptually:

```text
Container A
    |
   eth0
    |
   veth
    |
docker0
    |
   veth
    |
   eth0
    |
Container B
```

Check the bridge:

```bash
ip addr show docker0
```

---

# 🔌 Port Publishing

Suppose a container runs nginx on port 80.

Run:

```bash
docker run -d --name nginx -p 8080:80 nginx
```

The mapping is:

```text
Host port 8080
      |
      v
Container port 80
```

Access:

```text
http://localhost:8080
```

Test:

```bash
curl http://localhost:8080
```

---

# 🔗 Container-to-Container Communication

Create a custom network:

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

Containers connected to the same user-defined bridge network can communicate using Docker's internal networking and DNS.

---

# 🧭 Docker DNS

On a user-defined Docker network, containers can generally reach each other using container names.

Example:

```text
web
 |
 | HTTP request
 v
api
```

Example:

```bash
curl http://api:8080
```

This is much better than relying on dynamically changing container IP addresses.

---

# 🔐 Network Isolation

Docker networks can isolate containers.

Example:

```text
Network A
+-------------------+
| web               |
| api               |
+-------------------+

Network B
+-------------------+
| database          |
| internal-service  |
+-------------------+
```

A container is only connected to the networks assigned to it.

---

# 🖥️ Host Network

Run:

```bash
docker run --network host nginx
```

With host networking, the container uses the host's network namespace rather than a separate normal container network namespace.

This changes how ports and networking behave.

---

# 🚫 None Network

Run:

```bash
docker run --network none nginx
```

The container has networking heavily restricted and does not have normal external network connectivity.

This can be useful when network access is not required.

---

# 🧱 Docker and Linux Networking

Docker networking is built using Linux networking features.

Important concepts:

```text
Docker
  |
  +---- Network Namespace
  |
  +---- veth Pair
  |
  +---- Linux Bridge
  |
  +---- Routing
  |
  +---- NAT
  |
  +---- iptables/nftables
```

Understanding Linux networking makes Docker networking much easier to understand.

---

# 🐳 Docker Networking Commands

List networks:

```bash
docker network ls
```

Inspect a network:

```bash
docker network inspect bridge
```

Create a network:

```bash
docker network create app-network
```

Connect container:

```bash
docker network connect app-network <container>
```

Disconnect:

```bash
docker network disconnect app-network <container>
```

Remove network:

```bash
docker network rm app-network
```

---

# 🔍 Troubleshooting Docker Networking

When a container cannot communicate with another container, check:

```bash
docker ps
docker network ls
docker network inspect <network>
docker inspect <container>
```

Then test connectivity:

```bash
docker exec <container> ping <target>
```

or:

```bash
docker exec <container> curl http://<target>:<port>
```

Check listening ports:

```bash
docker exec <container> ss -lntup
```

Check host ports:

```bash
sudo ss -lntup
```

---

# 🎯 DevOps Importance

Docker networking is important when deploying:

* Microservices
* Web applications
* APIs
* Databases
* Reverse proxies
* CI/CD systems
* Monitoring systems
* Development environments

For example:

```text
              Internet
                  |
                  v
             Reverse Proxy
                  |
          +-------+-------+
          |               |
          v               v
       Frontend          API
                           |
                           v
                       Database
```

Each component may run in a separate container.

---

# 📚 Chapter Structure

This chapter contains:

### `README.md`

Overview and architecture.

### `notes.md`

Detailed Docker networking concepts.

### `commands.md`

Docker networking command reference.

### `practical-lab.md`

Hands-on Docker networking experiments.

### `interview-questions.md`

Docker networking interview questions and DevOps scenarios.

---

# 🏆 Final Goal

By the end of this chapter, you should be able to explain:

> **How Docker containers communicate with each other, how Docker connects containers to the host and external networks, how port publishing works, and how Docker uses Linux networking underneath.**

---

# 🔑 Key Concept

Remember this flow:

```text
Container
    ↓
Network Namespace
    ↓
veth pair
    ↓
Docker Bridge
    ↓
Routing / NAT
    ↓
Host Network
    ↓
External Network
```

This is the foundation of Docker networking.
