# Switching Practical Lab

## Objective

Understand Linux network interfaces, bridges, MAC forwarding information, and neighbor information.

---

## 1. Display Network Interfaces

### Command

```bash
ip link show

## Purpose

🔹 Displays network interfaces and their current state.

## Observation

The system contains:

lo - loopback interface
wlo1 - Wi-Fi interface
docker0 - Docker bridge
br-* - Docker bridge interfaces
veth* - virtual Ethernet interfaces


## 2. Display Interfaces in Brief Format

### Command

```bash
ip -br link

## Purpose

Provides a compact view of network interfaces and their state.

## 4. Display Forwarding Database

### Command

```bash
bridge fdb show

## Purpose

Displays forwarding database entries containing MAC addresses learned by Linux bridges.


##5. Display Neighbor Information

### Command

```bash
ip neigh

## Purpose

Displays IP-to-MAC neighbor information used for local network communication.

### Key Learning

Switching forwards Layer 2 frames using MAC addresses.

Linux bridges provide software-based Layer 2 switching and are commonly used by Docker networking.
