FROM apache/airflow:2.3.0-python3.8
USER root
RUN apt-get update \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
