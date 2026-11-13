
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-4.3.0-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-4.3.0-FDEE21?style=for-the-badge&logo=apachespark&logoColor=black)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Java](https://img.shields.io/badge/Java-JDK-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

![Learning](https://img.shields.io/badge/Status-Actively%20Learning-2EA44F?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

# Apache Spark & PySpark — Learning Repository

![](https://miro.medium.com/v2/resize:fit:1400/1*wDEi5sAwEqcXnE3skgVHzg.jpeg)



A hands-on learning repository dedicated to **Apache Spark, PySpark, and Big Data Engineering**. This repository documents my journey of learning distributed data processing, working with Spark DataFrames, performing data transformations, and building scalable data pipelines.

The goal is to develop practical knowledge of Apache Spark, from fundamental concepts to industry-level Big Data applications.

---

## About Apache Spark

**Apache Spark** is an open-source, distributed computing framework designed for large-scale data processing. It enables parallel processing of massive datasets across multiple CPU cores or distributed clusters.

**PySpark** is the Python API for Apache Spark, allowing developers to perform distributed data processing using Python.

### Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Programming language |
| Apache Spark 4.3.0 | Distributed data processing |
| PySpark | Python interface for Spark |
| Java | JVM execution environment |
| VS Code | Development environment |
| PowerShell | Command-line execution |

---

## Environment Setup

The following environment has been configured for local Spark development:

- Operating System: Windows
- Java: Installed and configured
- Apache Spark: 4.3.0
- Python: 3.12.3
- PySpark: Configured with Apache Spark
- Py4J: Spark-compatible dependency

### Verify Installation

Check Java:

```bash
java -version
```

Check Spark:

```bash
spark-submit --version
```

Launch PySpark:

```bash
pyspark
```

---

## Repository Structure

```text
spark-practice/
│
├── spark_setup.py
│
├── spark01.py
├── spark02.py
├── spark03.py
├── spark04.py
├── spark05.py
├── spark07.py
├── spark08.py
├── spark09.py
│
├── data/
│   └── students.csv
│
└── README.md
```

### Common Spark Configuration

`spark_setup.py` contains the reusable Spark environment configuration and SparkSession initialization.

Other Python programs import the shared SparkSession instead of repeating the configuration.

---

## Practical Learning Modules

### Module 1: Spark Fundamentals

- Introduction to Apache Spark
- Understanding PySpark
- Creating SparkSession
- Understanding SparkContext
- Creating DataFrames
- Understanding DataFrame schemas

### Module 2: DataFrame Operations

| File | Practical | Description |
|---|---|---|
| 01 | First DataFrame | Creating DataFrames using Python collections |
| 02 | Select Columns | Selecting specific columns |
| 03 | Filtering | Filtering records using conditions |
| 04 | Sorting | Sorting records in ascending and descending order |
| 05 | GroupBy | Grouping records by department |
| 06 | Aggregation | Calculating average, maximum and minimum |
| 07 | Adding Columns | Creating new columns using conditional logic |
| 08 | Drop Duplicates | Removing duplicate records |



## Repository Philosophy

This repository follows a practical, step-by-step learning approach.

Rather than focusing only on theoretical concepts, each module includes executable Python programs to understand how Apache Spark processes data.

**Learning by building. Understanding by executing. Scaling through distributed computing.**

---

**Technologies:** Python | Apache Spark | PySpark | Java | Big Data Engineering

**Status:** Actively Learning and Building 

go through this vedio 

"https://youtu.be/JjIwAMXUvYc?si=UvdPBbTEhORqBvrT"