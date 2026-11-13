
from spark_setup import spark

df = spark.read.csv(
    "data/students.csv",
    header=True,
    inferSchema=True
)

# Students scoring above 85
df.filter(df.Marks > 85).show()

spark.stop()
