# 04 · Joins (Intermediate)

Combine DataFrames with inner, outer, semi, and anti joins, and speed up small-table joins with broadcasting.

## What you will learn

- Join types: `inner`, `left`, `left_semi`, `left_anti`
- Joining on a shared column name (`on="customer_id"`) versus an explicit condition
- Using aliases to disambiguate columns with the same name
- `broadcast()`: sending a small table to every executor so no shuffle is needed

## Requirements

- Python 3.9+, Java 17 (or 11), `pip install pyspark`

## Run

```bash
python main.py
```

## Expected output (abridged)

```
--- left_anti: customers without orders ---
+-----------+-----+-------+
|customer_id| name|country|
+-----------+-----+-------+
|          3|Linus|     FI|
|          4| Alan|     GB|
+-----------+-----+-------+

--- broadcast join: total spent per customer ---
+-----+-----+
| name|spent|
+-----+-----+
|Grace| 75.0|
|  Ada| 70.0|
+-----+-----+
```

Row order inside a join result is not guaranteed. Add `orderBy` if you need a fixed order.

## Key takeaways

- `left_semi` and `left_anti` return only left-side columns and never duplicate rows. They are often faster and clearer than a join followed by `distinct`.
- Join on column names when both sides share them. This avoids duplicated key columns.
- Broadcast the smaller side when it fits in memory (default threshold is about 10 MB, configurable with `spark.sql.autoBroadcastJoinThreshold`).
- The order of joins matters for large data. Filter early.

## Exercises

1. Find customers who spent more than 50 in total.
2. Use `explain()` on a join and find the join strategy (for example `BroadcastHashJoin` or `SortMergeJoin`).
3. Remove the `broadcast()` call and compare the query plans.

**Previous:** `03-beginner-aggregations` · **Next:** `05-intermediate-read-write-formats`
