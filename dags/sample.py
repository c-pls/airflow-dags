from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define the default arguments for the DAG
default_args = {
    'start_date': datetime(2023, 10, 5),  # Adjust the date if necessary
    'retries': 1,
}

# Define the DAG
with DAG(
    'hello_world_dag',  # DAG name
    default_args=default_args,
    schedule_interval='@daily',  # Schedule interval (once a day)
    catchup=False,  # Prevent backfilling
) as dag:

    # Define the first task with BashOperator
    hello_task = BashOperator(
        task_id='print_hello',  # Task name
        bash_command='echo "Hello World!"',  # Bash command to execute
    )

    # Optionally, you can define additional tasks
    goodbye_task = BashOperator(
        task_id='print_goodbye',
        bash_command='echo "Goodbye World!"',
    )

    # Set task dependencies (hello_task will run before goodbye_task)
    hello_task >> goodbye_task
