# Docker 3-Tier Networking

## Network Architecture

This project uses two Docker bridge networks.

### frontend_net

Frontend communicates with Backend.

### backend_net

Backend communicates with Database.

## Why Two Networks?

Network separation provides better isolation between application tiers.

Frontend -> Backend: allowed
Backend -> Database: allowed
Frontend -> Database: not directly connected

## Docker DNS

Docker Compose provides internal DNS using service names.

The frontend resolves the backend using the service name backend.
The backend resolves MySQL using the service name database.

Test Docker DNS:

    docker exec three-tier-frontend getent hosts backend
    docker exec three-tier-backend getent hosts database

## Useful Commands

    docker network ls
    docker network inspect project-02-docker-three-tier_frontend_net
    docker network inspect project-02-docker-three-tier_backend_net

## Interview Answer

Docker Compose provides internal DNS that allows containers to communicate using service names instead of hard-coded IP addresses. In this project, the frontend communicates with the backend through frontend_net, while the backend communicates with MySQL through backend_net.
