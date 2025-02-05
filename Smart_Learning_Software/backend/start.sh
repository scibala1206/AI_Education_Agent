#!/bin/bash


# Start Docker service
sudo systemctl start docker

echo "Starting Docker Compose services..."
docker-compose up --build -d

echo "Waiting for containers to be healthy..."
sleep 5

docker ps

echo "FastAPI application should now be running."