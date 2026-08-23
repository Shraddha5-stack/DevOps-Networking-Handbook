# VLAN Interview Questions

## 1. What is a VLAN?

A VLAN (Virtual Local Area Network) is a logical network created on a physical network to divide a network into separate broadcast domains.

## 2. Why are VLANs used?

VLANs are used to:

- Separate networks logically
- Reduce broadcast traffic
- Improve security
- Organize users and systems
- Improve network management

## 3. What is a VLAN ID?

A VLAN ID is a number used to identify a VLAN. VLAN IDs range from 1 to 4094 for normal IEEE 802.1Q VLANs.

## 4. What is a PVID?

PVID means Port VLAN ID. It identifies the VLAN assigned to untagged incoming traffic on a port.

## 5. What is VLAN tagging?

VLAN tagging adds an IEEE 802.1Q tag to an Ethernet frame so the network can identify which VLAN the frame belongs to.

## 6. What is an access port?

An access port normally carries traffic for a single VLAN and sends/receives untagged traffic.

## 7. What is a trunk port?

A trunk port carries traffic for multiple VLANs, normally using VLAN tags.

## 8. What is the difference between a VLAN and a subnet?

A VLAN is a Layer 2 logical network separation, while a subnet is a Layer 3 IP network.

## 9. Can different VLANs communicate?

Yes, but communication between different VLANs requires Layer 3 routing, usually through a router or Layer 3 switch.

## 10. How do you check VLANs in Linux?

You can use:

```bash
bridge vlan show


For detailed information:

```bash 
bridge -d vlan show

## 11. How do you check Linux VLAN interfaces?

```bash 
ip -d link show type vlan

## 12. What is VLAN 1?

VLAN 1 is commonly the default VLAN on many network devices. In Linux bridge output, VLAN 1 may appear as the default PVID/untagged VLAN.


