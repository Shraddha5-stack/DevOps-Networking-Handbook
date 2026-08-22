# Switching Troubleshooting

## 1. Check Network Interfaces

```bash
ip -br link

## 2. Check Linux Bridges

```bash
bridge link

## 3. Check Forwarding Database

```bash
bridge fdb show

## 4. Check Neighbor Information


```bash
ip neigh 

## 5. Check Docker Networks


```bash
docker network ls

## 6. Inspect Docker Bridge

```bash 
docker network inspect bridge
