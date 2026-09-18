### 🎯**What is ETL?**
* ETL stands for **Extract, Transform, and Load**. It is a process used to collect data from multiple sources, transform it according to business requirements, and load it into a target system such as a data warehouse.

### 🎯**What are the three stages of ETL?**
| Stage     | Description                                          |
| --------- | ---------------------------------------------------- |
| Extract   | Collect data from source systems                     |
| Transform | Clean, validate, filter, aggregate, and modify data  |
| Load      | Load data into the target database or data warehouse |

### 🎯**What ETL tools have you used?**
* Apache Airflow
* PySpark
* Talend
* Informatica
* SSIS
* AWS Glue
* Python + Pandas

### 🎯**What are common data sources in ETL?**
* MySQL
* PostgreSQL
* Oracle
* SQL Server
* CSV Files
* Excel Files
* APIs
* JSON/XML
* SFTP/FTP
* Cloud Storage (S3, Azure Blob)
* Kafka Streams

### 🎯**What transformations are commonly performed?**
* Remove duplicates
* Handle NULL values
* Data type conversion
* Data validation
* Filtering records
* Aggregations
* Joining multiple tables
* Standardizing formats

### 🎯**What is Full Load?**
* In Full Load, all records are extracted and loaded every time.
* **Advantage**: Simple
* **Disadvantage**: Slow for large datasets
```bash
100000 rows
↓
Load all 100000 rows
```

### 🎯**What is Incremental Load?**
* Only new or modified records are extracted and loaded.
* Advantage: Faster and efficient
```bash
100000 rows already loaded
10 rows changed
↓
Load only 10 rows
```


### 🎯**What is CDC (Change Data Capture)?**
* CDC captures only the records that have changed since the last load.
```bash
Salary: 50000 → 60000
```
* Only this changed record is processed.

### 🎯**What is a Data Warehouse?**
* A Data Warehouse is a centralized repository used for reporting and analytics.
* Examples:
  * Snowflake
  * Amazon Redshift
  * Google BigQuery
  * Azure Synapse

### 🎯**ETL vs ELT?**
* दोनों का उद्देश्य data को source से target system तक ले जाना है, लेकिन Transform कब होता है, यही मुख्य अंतर है।
| ETL                            | ELT                                            |
| ------------------------------ | ---------------------------------------------- |
| Extract → Transform → Load     | Extract → Load → Transform                     |
| पहले transform करते हैं        | पहले load करते हैं                             |
| फिर target में load करते हैं   | target में load करने के बाद transform करते हैं |
| Traditional approach           | Modern cloud approach                          |
| Small/medium data के लिए अच्छा | Large data के लिए अच्छा                        |

### 🎯**Suppose you have 100 GB data. Which would you prefer?**
* For large-scale data processing in cloud environments, I would prefer ELT because modern data warehouses can efficiently perform transformations after loading, reducing the burden on ETL servers and improving scalability.

### 🎯**What is Batch Processing?**
* Data is processed at scheduled intervals.
* Tools:
  * Airflow
  * Informatica
  * SSIS
```bash
Daily at 1 AM
```

### 🎯**What is Real-Time Processing?**
* Data is processed immediately after it is generated.
```bash
Website Click
↓
Kafka
↓
Real-time Dashboard
```

### 🎯**Batch vs Real-Time Processing?**
| Batch          | Real-Time         |
| -------------- | ----------------- |
| Scheduled      | Immediate         |
| Large volume   | Continuous stream |
| Less expensive | More complex      |


### 🎯**Explain an ETL project you worked on.**
* In my project, data was extracted from MySQL databases, CSV files, and REST APIs. We used Python and SQL for transformation, including data validation, deduplication, and business calculations. The processed data was loaded into a reporting database for dashboard generation. Incremental loading was implemented to improve performance.