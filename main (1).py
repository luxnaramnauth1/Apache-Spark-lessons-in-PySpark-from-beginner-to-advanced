# 05 | INTERMEDIATE | Reading and writing CSV, JSON, and Parquet; schemas; partitioning
import os
import tempfile

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

spark = (
    SparkSession.builder
    .appName("05-read-write")
    .master("local[*]")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("city", StringType(), True),
    StructField("salary", DoubleType(), True),
])

people = spark.createDataFrame(
    [
        ("Ada", 36, "London", 85000.0),
        ("Grace", 45, "New York", 98000.0),
        ("Linus", 28, "Helsinki", 72000.0),
        ("Alan", 41, "London", 91000.0),
    ],
    schema,
)

# Use a temporary folder so the example leaves nothing behind
base = tempfile.mkdtemp(prefix="spark_io_")

# ---- CSV: human-readable, no types stored ----------------------------------------------
csv_path = os.path.join(base, "people_csv")
people.write.mode("overwrite").option("header", True).csv(csv_path)

# Read with an explicit schema (fast and predictable)
csv_df = spark.read.option("header", True).schema(schema).csv(csv_path)
print("--- CSV read with explicit schema ---")
csv_df.show()

# Read with inferred schema (convenient, but needs an extra pass over the data)
inferred_df = spark.read.option("header", True).option("inferSchema", True).csv(csv_path)
print("--- CSV inferred types ---")
inferred_df.printSchema()

# ---- JSON: one object per line ----------------------------------------------------------
json_path = os.path.join(base, "people_json")
people.write.mode("overwrite").json(json_path)
print("--- JSON read ---")
spark.read.json(json_path).orderBy("name").show()

# ---- Parquet: columnar, compressed, keeps types. The standard for analytics. ---------------
parquet_path = os.path.join(base, "people_parquet")
(
    people.write.mode("overwrite")
    .partitionBy("city")                     # one folder per city
    .parquet(parquet_path)
)

print("--- partition folders on disk ---")
print(sorted(os.listdir(parquet_path)))

# Reading with a filter on the partition column reads only the matching folder
print("--- London only (partition pruning) ---")
spark.read.parquet(parquet_path).filter("city = 'London'").show()

# Write modes: overwrite, append, ignore, errorifexists (default)
print("--- append one more row ---")
extra = spark.createDataFrame([("Tove", 33, "Helsinki", 76000.0)], schema)
extra.write.mode("append").partitionBy("city").parquet(parquet_path)
print("row count after append:", spark.read.parquet(parquet_path).count())

spark.stop()
