
from pyspark.sql.functions import when

from spark_setup import spark

df = spark.read.csv(
    "data/students.csv",
    header=True,
    inferSchema=True
)

df = df.withColumn(
    "Result",
    when(df.Marks >= 80, "Pass").otherwise("Needs Improvement")
)

df.show()

spark.stop()
