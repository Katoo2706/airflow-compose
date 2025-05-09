FROM apache/airflow:2.10.5-python3.10

USER root

# Install OpenJDK-11
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         openjdk-17-jre-headless \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
RUN export JAVA_HOME

# Download jars
RUN mkdir -p /opt/airflow/jars && \
    curl https://jdbc.postgresql.org/download/postgresql-42.5.4.jar --output /opt/airflow/jars/postgresql-42.5.4.jar

COPY requirements.txt /

USER airflow

RUN pip install -r /requirements.txt
