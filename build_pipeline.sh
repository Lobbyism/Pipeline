#!/bin/bash
set -e

echo ""
echo "Starting pipeline image build process..."
echo ""

# Optional: ensure Docker Compose is up to date
# docker compose version

# --- STEP 0: Build all services defined in docker-compose.yml ---
echo "[0/1] Building all Docker services..."
docker compose build

echo ""
echo "All pipeline services built successfully."
