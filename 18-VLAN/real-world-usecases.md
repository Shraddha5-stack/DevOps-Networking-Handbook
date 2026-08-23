# VLAN Real-World Use Cases

## 1. DevOps Environment

VLANs can separate development, testing, staging, and production networks.

Example:

- VLAN 10 → Development
- VLAN 20 → Testing
- VLAN 30 → Staging
- VLAN 40 → Production

## 2. Corporate Network

Different departments can be placed into different VLANs.

Example:

- VLAN 10 → HR
- VLAN 20 → Finance
- VLAN 30 → Engineering
- VLAN 40 → Management

## 3. Server Network

Servers can be separated from normal user devices using VLANs.

## 4. Security

VLANs can help isolate sensitive systems and limit unnecessary Layer 2 communication.

## 5. Docker Networking

Linux bridges and virtual Ethernet interfaces can be used to provide network isolation for containers.

In this practical lab, the system contains Docker bridge interfaces such as:

- `docker0`
- `br-*`
- `veth*`

These demonstrate Linux Layer 2 virtual networking.
