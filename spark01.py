
from spark_setup import spark

data = [
    (1, "Avishek", 85),
    (2, "Rahul", 90),
    (3, "Amit", 78)
]

df = spark.createDataFrame(
    data, ["ID", "Name", "Marks"]
)

df.show()

spark.stop()
