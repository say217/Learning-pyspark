
from spark_setup import spark

df = spark.read.csv(
    "data/students.csv",
    header=True,
    inferSchema=True
)

df.select("Name", "Marks").show()

spark.stop()
