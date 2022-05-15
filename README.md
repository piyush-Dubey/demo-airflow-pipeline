# Demo Airflow pipeline

1. Build custom docker image using the following command
> docker build . -f Dockerfile --pull --tag my-airflow-image:0.0.1
2. Ensure that the docker image tag name is updated in the .env file. For ex:
> AIRFLOW_IMAGE_NAME=my-airflow-image:0.0.1
3. Build docker compose (this will add the necessary SQL data required)
> docker-compose up --build
4. Access Airflow Webserver at localhost:5884
5. Notice that there may be DAG parsing errors at this stage.
6. In order to solve this, go to Admin>Connections and add 2 Postgres connections with the following details:
   a. For source database:
	   1. host: host.docker.internal
	   2. port: 5400
	   3. connection id: database_x
   b. For destination database:
	   1. host: host.docker.internal
	   2. port: 5401
	   3. connection id: database_y
7. Please note that the host details for the database may vary depending on the system where Docker is installed. This installation was found working on a Mac. For more information, refer to https://docs.docker.com/desktop/mac/networking/#use-cases-and-workarounds
8. After adding the connections for source and destination database, refresh the DAGs and the parsing error should be solved.
9. Trigger the DAG and notice that the data is present in the destination database.
> docker exec -it <container-id-destination-db> psql -U airflow

