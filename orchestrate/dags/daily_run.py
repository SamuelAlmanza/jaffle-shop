import datetime

from airflow.decorators import dag
from operators.datacoves.dbt import DatacovesDbtOperator

@dag(
    default_args={
        "start_date": datetime.datetime(2024, 1, 1, 0, 0),
        "owner": "Samuel Almanza",
        "email": "salmanza9449@gmail.com",
        "email_on_failure": True,
    },
    description="Daily dbt run",
    schedule_interval="0 12 * * *",
    tags=["version_2"],
    catchup=False,
)
def daily_run():
    run_dbt = DatacovesDbtOperator(
        task_id="run_dbt",
        bash_command="dbt build"
    )

dag = daily_run()
