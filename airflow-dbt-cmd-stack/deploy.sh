#!/bin/bash
set -e

export DBT_FOLDER="dbt_psql"

echo "📁 Checking environment file..."
# Create the .env file from .env.example if it doesn't exist
if [ ! -f .env ]; then
    echo "⚙️  Creating .env file from .env.example..."
    cp .env.example .env
fi

echo "🔧 Normalizing line endings for all .sh files..."
# Convert Windows line endings to Unix (important if using Git on Windows)
find . -name "*.sh" -type f -exec sed -i '' -e 's/\r$//' {} \;

echo "📦 Verifying DBT project existence..."
# Check if DBT project directory is valid
if [ ! -d "$DBT_FOLDER/models" ]; then
    echo "❌ WARNING: '$DBT_FOLDER' does not appear to contain a valid DBT project."
    echo "👉 You should create or copy a DBT project into '$DBT_FOLDER' before proceeding."
    echo "💡 Example: dbt init $DBT_FOLDER"
    exit 1
fi

# Check if docker-compose is available
if ! command -v docker compose &> /dev/null && ! command -v docker-compose &> /dev/null; then
    echo "❌ ERROR: docker compose or docker-compose is not installed."
    echo "👉 Please install Docker and Docker Compose first."
    exit 1
fi

# Use either 'docker compose' or 'docker-compose' depending on version
DOCKER_COMPOSE="docker-compose"
if command -v docker compose &> /dev/null; then
    DOCKER_COMPOSE="docker compose"
fi

echo "🐳 Building Docker image for Airflow..."
$DOCKER_COMPOSE build

echo "🚀 Starting Airflow services..."
$DOCKER_COMPOSE up -d

echo "⏳ Waiting for services to be fully up..."
sleep 10

echo "🔍 Checking running containers..."
$DOCKER_COMPOSE ps

echo "📄 Recent logs from Airflow webserver:"
$DOCKER_COMPOSE logs --tail=20 airflow-webserver

# Extract credentials from .env file if it exists
USERNAME="admin"
PASSWORD="admin123"

echo ""
echo "✅================================================================"
echo "✅ Airflow is now running!"
echo "🌐 Access the Airflow UI at: http://localhost:8080"
echo "👤 Username: $USERNAME"
echo "🔑 Password: $PASSWORD"
echo "✅================================================================"
