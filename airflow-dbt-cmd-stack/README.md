# Airflow DBT Command Stack

A ready-to-use Docker Compose setup for running Apache Airflow with DBT (Data Build Tool) integration.

## Overview

This project provides a complete stack for data transformation workflows:

- **Apache Airflow** (v2.10.5) for orchestration
- **DBT** for data transformations
- **PostgreSQL** as the backend database for both Airflow and as a target database for DBT

## Prerequisites

- Docker and Docker Compose
- Git
- Basic knowledge of Airflow and DBT

## Quick Start

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd airflow-dbt-cmd-stack
   ```

2. Make the deploy script executable:
   ```bash
   chmod +x deploy.sh
   ```

3. Create or copy your DBT project into the `dbt_psql` directory:
   ```bash
   # Either initialize a new DBT project
   dbt init dbt_psql
   
   # Or copy an existing one
   cp -r /path/to/your/dbt/project dbt_psql
   ```

4. Run the deploy script:
   ```bash
   ./deploy.sh
   ```

5. Access the Airflow UI:
   - URL: http://localhost:8080
   - Username: admin
   - Password: admin123

## Important Access Information

### Airflow
- **URL**: http://localhost:8080
- **Username**: admin
- **Password**: admin123

### PostgreSQL
- **Host**: localhost
- **Port**: 5432
- **Database**: airflow
- **Username**: postgres
- **Password**: postgres

## Project Structure

```
.
├── Dockerfile                # Custom Airflow image with DBT
├── README.md                 # This documentation
├── deploy.sh                 # Deployment script
├── docker-compose.yml        # Docker Compose configuration
├── dbt_psql/                 # Your DBT project directory
└── pipelines/
    ├── dags/                 # Airflow DAG files
    │   ├── example_dag.py    # Example DAG for running DBT commands
    │   ├── config/           # Configuration files
    │   │   └── constants.py  # Project constants
    │   └── utils/            # Utility functions
    │       └── dbt_command.py# DBT command executor
    ├── logs/                 # Airflow logs
    └── plugins/              # Airflow plugins
```

## Running DBT Commands in Airflow

The project includes an example DAG (`example_dag.py`) that demonstrates how to run DBT commands:

1. `dbt debug` - Validates your DBT project configuration
2. `dbt run` - Runs your DBT models
3. `dbt test` - Tests your DBT models

## Adding Custom DBT Projects

1. Place your DBT project in the `dbt_psql` directory
2. Update the `profiles.yml` in your DBT project to use the PostgreSQL database
3. Make sure to reference the correct path in `config/constants.py` (default is `/opt/airflow/dbt_psql`)

## Customization

- To add custom Python packages, update the `requirements.txt` file
- To customize Airflow configuration, edit the environment variables in `docker-compose.yml`
- To adjust DBT settings, modify the `dbt_psql/profiles.yml` file

## Troubleshooting

If you encounter issues:

1. Check the logs: `docker-compose logs airflow-webserver`
2. Verify DBT installation: `docker-compose exec airflow-worker dbt --version`
3. Test DBT connection: `docker-compose exec airflow-worker bash -c "cd /opt/airflow/dbt_psql && dbt debug"`

## License

This project is licensed under the Apache License 2.0.

