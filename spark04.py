
from spark_setup import spark

df = spark.read.csv(
    "data/students.csv",
    header=True,
    inferSchema=True
)

# Highest marks first
df.orderBy(df.Marks.desc()).show()

spark.stop()
