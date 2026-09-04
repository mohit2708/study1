 ## 🎯What is Apache Airflow?
* Apache Airflow is an open-source workflow **orchestration tool** used to schedule, automate, and monitor data pipelines and workflows.
* **Hindi:-** Airflow helps you automate tasks that need to run in a specific order and at specific times.

## 🎯What is a DAG?
* A DAG (Directed Acyclic Graph) is a collection of tasks organized with dependencies that define the execution order of a workflow in Apache Airflow. It ensures tasks run in the correct sequence without any circular dependencies.
* DAG (Directed Acyclic Graph) is the **core concept of Apache Airflow.** It represents a workflow and defines:
  * What tasks need to run
  * In what order they should run
  * Dependencies between tasks

#### Example
* Extract Data must finish before Transform Data
* Transform Data must finish before Load Data
* Load Data must finish before Send Email
* **This complete workflow is called a DAG.**
```pyhton
Extract Data
     ↓
Transform Data
     ↓
Load Data
     ↓
Send Email
```

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print("Hello Airflow")

with DAG(
    dag_id="hello_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@daily"
) as dag:

    task1 = PythonOperator(
        task_id="say_hello",
        python_callable=hello
    )
```

#### Directed Acyclic Graph (DAG) ka matlab
* **Directed** → Tasks ek direction/order mein chalti hain.
* **Acyclic** → Workflow mein loop/cycle nahi hota. Task A → B → C ke baad wapas A nahi ja sakta.
* **Graph** → Multiple tasks aur unke connections/dependencies ka structure.
```python
Task A: Get Data
       ↓
Task B: Process Data
       ↓
Task C: Save Data
       ↓
Task D: Send Email
```
* A → B → C → D :- Ye **Directed** hai kyunki direction A se D ki taraf hai.
* Ye Acyclic hai kyunki: A → B → C → D → A ❌ (aisa loop nahi hai.)



### Why is it called Directed Acyclic Graph?
* Directed → Tasks have a specific execution direction.
* Acyclic → No circular loops are allowed.
* Graph → Tasks and dependencies form a graph structure.


## Where are Airflow Logs Stored?
* By default, Airflow task logs are stored in the **logs/ directory** of the Airflow home directory.
```python
~/airflow/
├── dags/
├── logs/
│   └── dag_id/
│       └── task_id/
│           └── execution_date/
├── plugins/
└── airflow.cfg
```

## What is a Scheduler in Airflow?
* The Airflow Scheduler is responsible for monitoring DAGs, creating DAG runs according to their schedules, checking task dependencies, and scheduling eligible tasks for execution.
* Airflow ka Scheduler dags/ folder mein DAG files ko periodically check karta hai.
* Hindi:- Scheduler Airflow ka ek important component hai jo decide karta hai ki kaunsa task kab run hoga.

