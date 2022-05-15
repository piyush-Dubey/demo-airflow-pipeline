from airflow.models import DAG
from airflow.operators.python import PythonOperator
import pendulum

from move_data import move_data_x_to_y


with DAG(
        dag_id="move_data_x_to_y",
        start_date=pendulum.yesterday(tz="UTC"),
        schedule_interval="@daily",
        catchup=False,
        # default_args={"retries": 1},
) as dag:
    op2 = PythonOperator(
        task_id="move_data",
        python_callable=move_data_x_to_y
    )
