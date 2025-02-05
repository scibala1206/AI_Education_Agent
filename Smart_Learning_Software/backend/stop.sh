#!/bin/bash

echo "Stopping Docker Compose services..."
docker-compose down

echo "Removing unused Docker resources..."
docker system prune -f --volumes

echo "Pruning unused Docker images..."
docker image prune -a -f

echo "All Docker containers, images, and unused volumes are cleaned up."