
from spark_setup import spark

data = [
    (1, "Avishek"),
    (2, "Rahul"),
    (2, "Rahul"),
    (3, "Amit")
]

df = spark.createDataFrame(data, ["ID", "Name"])

df.show()

print("After removing duplicates:")

df.dropDuplicates().show()

spark.stop()
