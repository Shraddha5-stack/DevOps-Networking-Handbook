# Troubleshooting

## 1. Port Already in Use

If Docker reports bind: address already in use, check the port:

    sudo ss -ltnp | grep :8090

Change the host port in docker-compose.yml if necessary.

## 2. Check Container Status

    docker compose ps

## 3. Check Logs

    docker compose logs frontend
    docker compose logs backend
    docker compose logs database

Follow backend logs:

    docker compose logs -f backend

Press Ctrl+C to stop following logs.

## 4. Test Backend

    curl http://localhost:8090/api/health

## 5. Test Database

    curl http://localhost:8090/api/db

## 6. Test Docker DNS

    docker exec three-tier-frontend getent hosts backend
    docker exec three-tier-backend getent hosts database

## 7. Restart Application

    docker compose down
    docker compose up -d --build

## Troubleshooting Workflow

Check containers -> Check logs -> Check ports -> Check networks -> Check DNS -> Test application endpoints
