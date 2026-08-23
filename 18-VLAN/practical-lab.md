# VLAN Practical Lab

## Objective

Understand VLAN concepts and inspect VLAN-related information on a Linux system.

---

## 1. Inspect Network Interfaces

### Command

```bash
ip -d link show

##Observation

The system contains:

lo - loopback interface
wlo1 - Wi-Fi interface
docker0 - Docker bridge
br-* - Docker bridge interfaces
veth* - virtual Ethernet interfaces

The output also shows VLAN-related bridge information such as:

vlan_filtering 0
vlan_protocol 802.1Q
vlan_default_pvid 1

## Conclusion

The command ip -d link show provides detailed information about network interfaces and Linux bridge VLAN configuration.



### Step 2 — run this now

```bash
bridge vlan show

## Observation

The Docker bridge and virtual Ethernet interfaces are using VLAN 1.

Example:

port              vlan-id
br-768b5ee9c7a5   1 PVID Egress Untagged
docker0           1 PVID Egress Untagged
veth52f4bbf       1 PVID Egress Untagged

## Meaning
VLAN 1 - default VLAN
PVID - Port VLAN ID
Egress Untagged - outgoing frames are sent without a VLAN tag

#Conclusion

The current Docker bridge networks are using the default VLAN 1 configuration.


### Step 3 — next command

Run:

```bash
ip -d link show type vlan


##  Observation

The command returned no output.

##  Meaning

No VLAN interfaces are currently configured on this system.

#Conclusion

The system does not currently have a dedicated VLAN interface configured.


### Step 4 — Check VLAN filtering

Run:

```bash
bridge -d vlan show


## Observation

The Docker bridge and virtual Ethernet interfaces are using VLAN 1.

The output shows:

PVID - Port VLAN ID
Egress Untagged - outgoing traffic is untagged
state forwarding - the interface is forwarding traffic
mcast_router 1 - multicast router functionality is enabled

Example

```bash 
docker0           1 PVID Egress Untagged
                    state forwarding mcast_router 1
## Conclusion

The detailed VLAN information confirms that the current Docker bridge network uses the default VLAN 1 and its ports are forwarding traffic.


### Step 5 — VLAN concept check

Now run:

```bash
bridge link



