# 06 · Spark SQL and Views (Intermediate)

Query DataFrames with SQL, use temp and global views, and combine SQL with the DataFrame API.

## What you will learn

- `createOrReplaceTempView` to make a DataFrame queryable by name
- `spark.sql(...)` with `GROUP BY`, `HAVING`, `ORDER BY`, and CTEs (`WITH`)
- `spark.table(...)` to get a view back as a DataFrame
- Temp views (one session) versus global temp views (whole application)
- `explain()` to read the physical plan

## Requirements

- Python 3.9+, Java 17 (or 11), `pip install pyspark`

## Run

```bash
python main.py
```

## Expected output (abridged)

```
--- GROUP BY with HAVING ---
+--------+---------+----------+
|    city|residents|avg_salary|
+--------+---------+----------+
|  London|        2|   85000.0|
|New York|        1|   98000.0|
|Helsinki|        1|   72000.0|
+--------+---------+----------+

--- global temp view ---
+---+
|  n|
+---+
|  4|
+---+
```

## Key takeaways

- SQL and the DataFrame API compile to the same execution plan. Choose whichever is clearer for the task.
- A temp view disappears when the session ends. A global temp view lives under the `global_temp` schema.
- `explain()` shows `Exchange`, which means a shuffle. Fewer exchanges usually means a faster query.

## Exercises

1. Write a SQL query that returns the top two cities by average salary.
2. Use a CTE to split people into two groups, then compare their averages.
3. Run `EXPLAIN EXTENDED` in SQL (`spark.sql("EXPLAIN EXTENDED SELECT ...")`) and find the logical plan.

**Previous:** `05-intermediate-read-write-formats` · **Next:** `07-intermediate-windows-nulls`
