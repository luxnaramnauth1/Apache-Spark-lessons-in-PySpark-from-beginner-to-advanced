# Apache Spark Lessons (PySpark): Beginner to Advanced

Ten runnable PySpark lessons, each in its own folder with a `main.py` program and a `README.md`. Work through them in order: each builds on the one before.

## Learning path

| # | Folder | Level | Topics |
|---|--------|-------|--------|
| 01 | `01-beginner-dataframes-basics` | Beginner | SparkSession, DataFrames, schemas, lazy evaluation, actions |
| 02 | `02-beginner-select-filter` | Beginner | `select`, `filter`, `withColumn`, `orderBy`, `when` |
| 03 | `03-beginner-aggregations` | Beginner | `groupBy`, `agg`, filtering aggregates, global totals |
| 04 | `04-intermediate-joins` | Intermediate | Inner, left, semi, anti joins; broadcast joins |
| 05 | `05-intermediate-read-write-formats` | Intermediate | CSV, JSON, Parquet; schemas; write modes; partitioning |
| 06 | `06-intermediate-spark-sql-views` | Intermediate | Spark SQL, temp and global views, CTEs, `explain` |
| 07 | `07-intermediate-windows-nulls` | Intermediate | Window functions (`row_number`, running totals, `lag`); null handling |
| 08 | `08-advanced-udfs-pandas` | Advanced | Python UDFs vs pandas UDFs; performance |
| 09 | `09-advanced-partitions-cache-explain` | Advanced | Partitions, shuffles, caching, query plans, AQE |
| 10 | `10-advanced-structured-streaming` | Advanced | Streaming, event time, watermarks, windows, `foreachBatch` |

## Requirements

- Python 3.9 or newer
- Java 17 (or 11). Spark does not run without a JVM.
- `pip install pyspark pandas pyarrow`

Check that Java is installed with `java -version`.

## Run a lesson

```bash
cd 01-beginner-dataframes-basics
python main.py
```

Each lesson uses `local[*]`, which runs Spark on your computer with all available cores. No cluster is needed.

## Notes

- Spark prints `WARN` messages and progress bars to the console. They are normal.
- Lesson 08 may show `FutureWarning` messages about pandas versions. They are harmless.
- Each program creates its own `SparkSession` and stops it at the end.
- Row order in join and window results is not guaranteed. Add `orderBy` when you need a fixed order.

## Suggested study approach

1. Read the lesson's `README.md`.
2. Run `main.py` and compare the output with the expected output.
3. Change one thing at a time and predict the result.
4. Do the exercises at the end of each README.
5. Open the Spark UI while a lesson runs (the URL is printed at the start of lessons 09 and 10) to see jobs, stages, and tasks.
