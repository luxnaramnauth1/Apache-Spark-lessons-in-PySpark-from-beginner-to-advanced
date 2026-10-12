# 01 · DataFrames Basics (Beginner)

Start a Spark session, create a DataFrame, and learn the difference between transformations and actions.

## What you will learn

- What a `SparkSession` is and how to create one
- What a DataFrame is: a distributed table with named, typed columns
- Inferred versus explicit schemas (`StructType`, `StructField`)
- **Lazy evaluation:** transformations build a plan, actions run it
- Common actions: `show`, `count`, `first`, `collect`

## Requirements

- Python 3.9+ and Java 17 (or 11)
- `pip install pyspark`

## Run

```bash
python main.py
```

## Expected output (abridged)

```
--- inferred schema ---
root
 |-- name: string (nullable = true)
 |-- age: long (nullable = true)
 |-- salary: double (nullable = true)

--- table ---
+-----+---+-------+
| name|age| salary|
+-----+---+-------+
|  Ada| 36|85000.0|
|Grace| 45|98000.0|
|Linus| 28|72000.0|
+-----+---+-------+

row count: 3
first row: Row(name='Ada', age=36, salary=85000.0)
```

Spark also prints `WARN` and progress messages on the console. They are harmless.

## Key takeaways

- `collect()` brings every row to the driver program. Use it only on small results. On large data it can crash your program.
- Explicit schemas avoid an extra pass over the data and prevent surprises from type inference.
- `local[*]` runs Spark on your machine using all cores. On a cluster you would omit `.master(...)` and pass it through `spark-submit`.

## Exercises

1. Create a DataFrame of your own and change the schema so `age` is an integer.
2. Use `df.describe().show()` to see summary statistics.
3. Print `df.rdd.getNumPartitions()` and explain what the number means.

**Next:** `02-beginner-select-filter`
