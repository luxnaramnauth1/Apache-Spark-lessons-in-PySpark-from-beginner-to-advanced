# 01 | BEGINNER | SparkSession, DataFrames, schemas, and actions
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

spark = (
    SparkSession.builder
    .appName("01-dataframes-basics")
    .master("local[*]")          # run locally using all CPU cores
    .getOrCreate()
)
spark.sparkContext.setLogLevel("ERROR")

# A DataFrame is a distributed table with named, typed columns.
# Spark is LAZY: transformations build a plan; actions (show, count, collect) run it.
data = [("Ada", 36, 85000.0), ("Grace", 45, 98000.0), ("Linus", 28, 72000.0)]

# 1. Let Spark infer the schema (convenient, but slower on big data)
inferred = spark.createDataFrame(data, ["name", "age", "salary"])
print("--- inferred schema ---")
inferred.printSchema()

# 2. Define the schema explicitly (safer and faster)
schema = StructType([
    StructField("name", StringType(), nullable=False),
    StructField("age", IntegerType(), nullable=True),
    StructField("salary", DoubleType(), nullable=True),
])
people = spark.createDataFrame(data, schema)

print("--- table ---")
people.show()

# 3. Actions trigger computation
print("row count:", people.count())
print("columns:", people.columns)
print("first row:", people.first())
print("as Python list:", people.collect())   # pulls ALL rows to the driver: small data only

# 4. A DataFrame from a numeric range
print("--- range ---")
spark.range(5).show()

spark.stop()
