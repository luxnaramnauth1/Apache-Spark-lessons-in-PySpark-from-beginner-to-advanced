# 02 | BEGINNER | Transformations: select, filter, withColumn, orderBy, when
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("02-select-filter")
    .master("local[*]")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("ERROR")

people = spark.createDataFrame(
    [
        ("Ada", 36, "London", 85000.0),
        ("Grace", 45, "New York", 98000.0),
        ("Linus", 28, "Helsinki", 72000.0),
        ("Alan", 41, "London", None),          # None becomes null
    ],
    ["name", "age", "city", "salary"],
)

# select: choose columns
print("--- select ---")
people.select("name", "city").show()

# filter / where: keep rows that match a condition
print("--- filter ---")
people.filter(F.col("age") > 30).show()

# Combine conditions with & and |; wrap each in parentheses
print("--- combined conditions ---")
people.where((F.col("city") == "London") & (F.col("salary").isNotNull())).show()

# withColumn: add a new column (or replace an existing one)
print("--- withColumn ---")
people.withColumn("bonus", F.col("salary") * 0.10).show()

# alias: rename a column in the output
print("--- alias ---")
people.select(F.col("name").alias("employee"), "age").show()

# orderBy: sort rows
print("--- orderBy ---")
people.orderBy(F.col("age").desc()).show()

# when / otherwise: build a conditional column (like CASE WHEN)
print("--- when / otherwise ---")
people.withColumn(
    "band",
    F.when(F.col("age") >= 40, "senior")
     .when(F.col("age") >= 30, "mid")
     .otherwise("junior"),
).show()

# distinct and limit
print("--- distinct / limit ---")
people.select("city").distinct().show()
people.limit(2).show()

spark.stop()
