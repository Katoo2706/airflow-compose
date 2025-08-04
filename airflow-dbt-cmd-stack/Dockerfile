FROM apache/airflow:2.10.5-python3.10
USER root

# Install OpenJDK-17 and git
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         openjdk-17-jre-headless \
         git \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
RUN export JAVA_HOME

# Download PostgreSQL JDBC driver
RUN mkdir -p /opt/airflow/jars && \
    curl https://jdbc.postgresql.org/download/postgresql-42.5.4.jar --output /opt/airflow/jars/postgresql-42.5.4.jar

# Create directory for dbt project with proper permissions
RUN mkdir -p /opt/airflow/dbt_psql /opt/airflow/dbt_psql/logs /opt/airflow/dbt_psql/target

# Copy requirements first (for better layer caching)
COPY requirements.txt /

# Copy the dbt project files into the container, relying on .dockerignore to exclude unnecessary folders
COPY ./dbt_psql /opt/airflow/dbt_psql/

# Set proper ownership and permissions AFTER copying files
RUN chown -R airflow:root /opt/airflow/dbt_psql && \
    chmod -R 755 /opt/airflow/dbt_psql && \
    chmod -R 777 /opt/airflow/dbt_psql/logs && \
    chmod -R 777 /opt/airflow/dbt_psql/target

USER airflow

RUN pip install -r /requirements.txt