## Installation

```bash
export AIRFLOW_HOME=$(pwd)

airflow db init
airflow db  upgrade #For migration

airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email abc@example.com
```

```bash
airflow standalone

OR 

airflow webserver --port 8080 && \
airflow scheduler
``` 