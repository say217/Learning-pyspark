
import os
import sys

os.environ["SPARK_HOME"] = r"C:\spark"
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
os.environ["PYTHONPATH"] = (
    r"C:\spark\python;"
    r"C:\spark\python\lib\py4j-0.10.9.9-src.zip"
)

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SparkPractice") \
    .master("local[*]") \
    .getOrCreate()
