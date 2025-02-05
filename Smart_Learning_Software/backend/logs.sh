#!/bin/bash

LOG_FILE="docker_logs.log"

# Clear the previous logs
echo "Clearing old logs and starting fresh in $LOG_FILE..."
> "$LOG_FILE"  # Clears the file

# Append new logs continuously
echo "Appending new logs to $LOG_FILE..."
docker-compose logs -f >> "$LOG_FILE" 2>&1