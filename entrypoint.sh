#!/bin/bash

echo "Waiting for PostgreSQL to be ready..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.1
done
echo "PostgreSQL is ready!"

# Check if database exists
DB_EXISTS=$(PGPASSWORD=$POSTGRES_PASSWORD psql -h $POSTGRES_HOST -U $POSTGRES_USER -tAc "SELECT 1 FROM pg_database WHERE datname='$POSTGRES_DB'")

if [ -z "$DB_EXISTS" ]; then
    echo "Creating database $POSTGRES_DB..."
    PGPASSWORD=$POSTGRES_PASSWORD psql -h $POSTGRES_HOST -U $POSTGRES_USER -c "CREATE DATABASE $POSTGRES_DB"
    echo "Database created successfully!"

    # Run migrations only if database was just created
    echo "Running initial database migrations..."
    alembic revision --autogenerate -m "initial migration"
    alembic upgrade head
else
    echo "Database $POSTGRES_DB already exists."
fi

# Start the application
echo "Starting the application..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
