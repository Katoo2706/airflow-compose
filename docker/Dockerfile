FROM apache/airflow:3.0.0

# Set the desired Airflow version
ARG AIRFLOW_VERSION=3.0.0

# Set the working directory
WORKDIR /app

# Switch back to the root user temporarily to copy the requirements file
USER root
COPY requirements.txt /app/requirements.txt
RUN chown airflow: /app/requirements.txt
USER airflow

# Upgrade pip
RUN pip install --upgrade pip

# Install the required packages
RUN pip install --no-cache-dir --ignore-installed -r requirements.txt

# Start Airflow webserver (modify this command as per your requirements)
CMD ["airflow", "webserver"]
