
from pyspark.sql.functions import avg, max, min

from spark_setup import spark

df = spark.read.csv(
    "data/students.csv",
    header=True,
    inferSchema=True
)

df.select(
    avg("Marks").alias("Average"),
    max("Marks").alias("Highest"),
    min("Marks").alias("Lowest")
).show()

spark.stop()
