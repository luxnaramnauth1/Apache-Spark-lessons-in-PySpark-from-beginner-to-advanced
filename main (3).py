# 06 | INTERMEDIATE | Spark SQL, temp views, CTEs, and mixing SQL with the DataFrame API
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("06-spark-sql")
    .master("local[*]")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("ERROR")

people = spark.createDataFrame(
    [
        ("Ada", 36, "London", 85000.0),
        ("Grace", 45, "New York", 98000.0),
        ("Linus", 28, "Helsinki", 72000.0),
        ("Alan", 41, "London", None),
    ],
    ["name", "age", "city", "salary"],
)

# A temp view gives a DataFrame a name that SQL can use.
# It lasts for this SparkSession only.
people.createOrReplaceTempView("people")

print("--- simple query ---")
spark.sql("SELECT name, age FROM people WHERE age > 30 ORDER BY age DESC").show()

print("--- GROUP BY with HAVING ---")
spark.sql("""
    SELECT city,
           COUNT(*)                 AS residents,
           ROUND(AVG(salary), 2)    AS avg_salary
    FROM people
    GROUP BY city
    HAVING COUNT(*) >= 1
    ORDER BY residents DESC
""").show()

print("--- CTE (WITH clause) ---")
spark.sql("""
    WITH senior AS (
        SELECT * FROM people WHERE age >= 40
    )
    SELECT name, city FROM senior
""").show()

print("--- mixing SQL and the DataFrame API ---")
spark.table("people").where("city = 'London'").select("name", "salary").show()

# A global temp view is visible to every SparkSession in the application.
# It lives in the reserved database global_temp.
people.createOrReplaceGlobalTempView("people_global")
print("--- global temp view ---")
spark.sql("SELECT COUNT(*) AS n FROM global_temp.people_global").show()

print("--- query plan for the GROUP BY ---")
spark.sql("SELECT city, COUNT(*) FROM people GROUP BY city").explain()

spark.stop()
