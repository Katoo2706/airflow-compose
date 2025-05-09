# Airflow 3.0 Docker Deployment

This repository contains the configuration files needed to deploy Apache Airflow 3.0 using Docker Compose.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- At least 4GB of RAM allocated to Docker

## Project Structure

Once deployed, the project will create the following directory structure:

```
airflow-compose/
├─ docker-compose.yml    # Docker Compose configuration
├─ config/                 # Directory for config file
├─ docker/                 # Directory for dockerfile
├─ pipelines/              # Directory for pipelines, includes dags, logs, 
```

## Setup Instructions

### 1. Start all Airflow services:

```bash
docker-compose up -d
```

This will start the following services:
- PostgreSQL database
- Redis message broker
- Airflow Webserver
- Airflow Scheduler
- Airflow Worker
- Airflow Triggerer
- Flower (Celery monitoring tool)

### 2. Access Airflow UI
Once the services are up and running (after 5 minutes running docker compose), you can access:

- **Airflow UI**: http://localhost:8080
  - Username: airflow
  - Password: airflow
- **Flower UI** (Celery monitoring): http://localhost:5555

## Managing Airflow

### Adding DAGs

Place your DAG files in the `dags` directory. They will be automatically picked up by Airflow.

### Custom Plugins

Place your custom plugins in the `plugins` directory.

### Custom Configurations

If you need to customize Airflow configurations, you can add them to the `config` directory.

### Logs

Airflow logs will be stored in the `logs` directory.

## Stopping Airflow

To stop all services:

```bash
docker-compose down
```

To stop services and remove volumes (this will delete your data):

```bash
docker-compose down -v
```

## Restarting Services

To restart all services:

```bash
docker-compose restart
```

To restart a specific service (e.g., the webserver):

```bash
docker-compose restart airflow-webserver
```

## Scaling Workers

To scale the number of worker instances:

```bash
docker-compose up -d --scale airflow-worker=3
```

## Troubleshooting

### Check Logs

To check logs for a specific service:

```bash
docker-compose logs airflow-webserver
```

For continuous log monitoring:

```bash
docker-compose logs -f airflow-webserver
```

### Container Health Checks

To check the status of your containers:

```bash
docker-compose ps
```

### Accessing Containers

To enter a running container:

```bash
docker exec -it airflow-webserver bash
```

## Upgrading Airflow

To upgrade Airflow in the future:

1. Update the image version in `docker-compose.yml`
2. Run `docker-compose down`
3. Run `docker-compose up -d`

## Security Considerations

- Change the default admin password immediately after the first login
- Consider using environment variables or a secret manager for sensitive credentials
- Set up SSL/TLS for production environments
- Configure proper authentication backends