# Switching

## What is Switching?

Switching is the process of forwarding network frames between devices in the same network.

A network switch uses MAC addresses to decide where frames should be forwarded.

## How a Switch Works

1. A device sends a frame.
2. The switch receives the frame.
3. The switch learns the source MAC address.
4. The switch checks its MAC address table.
5. The frame is forwarded through the appropriate port.

## MAC Address Table

A switch maintains a forwarding/MAC address table containing MAC addresses and associated ports.

## Linux and Switching

Linux can provide software-based switching using bridges.

Docker commonly creates Linux bridge interfaces such as:

- `docker0`
- `br-*`

Virtual Ethernet interfaces (`veth`) can connect containers to these bridges.

## Key Difference

### Switch

Works mainly with MAC addresses at Layer 2.

### Router

Uses IP addresses to route traffic between different networks at Layer 3.
