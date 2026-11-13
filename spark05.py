
from spark_setup import spark

df = spark.read.csv(
    "data/students.csv",
    header=True,
    inferSchema=True
)

df.groupBy("Department").count().show()

spark.stop()
