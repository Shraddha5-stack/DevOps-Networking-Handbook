# Routing

## Overview

Routing is the process of selecting a path for network traffic to travel from a source to a destination.

In Linux, routing is handled using a routing table. The routing table contains information about destination networks, gateways, network interfaces, and route metrics.

## Why Routing Is Important in DevOps

Routing is important for DevOps because applications, servers, containers, and cloud resources need to communicate with each other.

A DevOps engineer should understand routing to:

- Troubleshoot network connectivity
- Understand default gateways
- Configure static routes
- Troubleshoot servers
- Understand Docker networking
- Understand Kubernetes networking
- Work with AWS and cloud networking
- Diagnose packet-routing problems

## Important Routing Concepts

### 1. Routing Table

A routing table contains rules that tell Linux where to send network traffic.

View it with:

```bash
ip route


### 2. Destination

The destination is the network or IP address that the packet needs to reach.

Example:

8.8.8.8


###3. Gateway

A gateway is a device that forwards traffic from one network to another.

Example:

192.168.1.1

###4. Network Interface

A network interface is used to send and receive network traffic.

Example:

wlo1


###5. Default Route

The default route is used when there is no more specific route for the destination.

Example:

default via 192.168.1.1 dev wlo1

Basic Routing Flow

Application
     |
     v
Linux Kernel
     |
     v
Routing Table
     |
     v
Gateway / Interface
     |
     v
Destination Network


Example

If the Linux system needs to communicate with 8.8.8.8, Linux checks its routing table to determine which route should be used.

For example:

Destination: 8.8.8.8
Gateway:     192.168.1.1
Interface:   wlo1
Source IP:   192.168.1.5

The traffic flows approximately like this:

Laptop
192.168.1.5
    |
    | wlo1
    v
Gateway
192.168.1.1
    |
    v
Internet
    |
    v
8.8.8.8


Common Commands

## Learning Goals

After completing this chapter, you should be able to:

- Explain what routing is
- Read a Linux routing table
- Identify a default gateway
- Identify a network interface
- Determine how Linux reaches a destination
- Understand basic route selection
- Troubleshoot basic routing problems
