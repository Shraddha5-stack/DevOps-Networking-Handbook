# Project 02: Docker 3-Tier Application

## Overview

A practical 3-tier application deployed using Docker Compose.

## Architecture

Browser
   |
localhost:8090
   |
Nginx Frontend :80
   |
frontend_net
   |
Flask Backend :5000
   |
backend_net
   |
MySQL :3306

## Technologies

- Docker
- Docker Compose
- Nginx
- Python Flask
- MySQL
- Docker Bridge Networks
- Docker DNS
- Health Checks
- Persistent Volumes

## Services

| Service | Technology | Port |
|---|---|---|
| Frontend | Nginx | 8090 -> 80 |
| Backend | Flask | 5000 |
| Database | MySQL | 3306 |

## Docker Networks

### frontend_net
Connects the Nginx frontend with the Flask backend.

### backend_net
Connects the Flask backend with the MySQL database.

The database is isolated from the frontend network.

## Start Application

    docker compose up -d --build

## Check Containers

    docker compose ps

## Test Backend

    curl http://localhost:8090/api/health

Expected: backend status healthy.

## Test Database

    curl http://localhost:8090/api/db

Expected: MySQL connected.

## Test Docker DNS

    docker exec three-tier-frontend getent hosts backend
    docker exec three-tier-backend getent hosts database

## Learning Outcomes

- Docker containerization
- Docker Compose
- Multi-container application deployment
- Docker bridge networks
- Network isolation
- Docker service discovery
- Internal DNS
- Nginx reverse proxy
- Flask backend
- MySQL connectivity
- Environment variables
- Health checks
- Persistent volumes
- Troubleshooting port conflicts

## Project Status

Completed successfully.
