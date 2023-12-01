#!/bin/sh

# Wait for the PostgreSQL database to be ready
until nc -z -v -w30 db 5432
do
  echo "Waiting for PostgreSQL to start..."
  sleep 1
done

# Run Alembic migrations
alembic upgrade head

# Start the UVicorn server
uvicorn server.src.main:app --host 0.0.0.0 --port ${SERVER_PORT:-8000}
