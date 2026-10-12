# 08 · UDFs and pandas UDFs (Advanced)

Write custom logic in Python, and learn why built-in functions and vectorised pandas UDFs are much faster than row-by-row Python UDFs.

## What you will learn

- Choosing between built-in functions, Python UDFs, and pandas UDFs
- Why a Python UDF is slow: each row is serialised between the JVM and Python
- Vectorised pandas UDFs, which process batches as pandas Series with Apache Arrow
- Registering a UDF so SQL can call it

## Requirements

- Python 3.9+, Java 17 (or 11)
- `pip install pyspark pandas pyarrow`

## Run

```bash
python main.py
```

## Expected output (measured on a local machine)

```
built-in        0.86s  [('junior', 82500), ('senior', 217500)]
python UDF      3.09s  [('junior', 82500), ('senior', 217500)]
pandas UDF      0.77s  [('junior', 82500), ('senior', 217500)]
```

All three approaches give the same result. Only the time differs. Timings vary by machine, but the order (built-in and pandas fastest, Python UDF slowest) should hold.

Lines starting with `FutureWarning` about pandas versions appear with pandas 3.x. They are harmless.

## Key takeaways

- Use a built-in function whenever one exists. Spark optimises it and runs it inside the JVM.
- If you need custom Python, prefer a pandas UDF. It processes batches, not single rows.
- A UDF is a black box to the optimiser, so filters and column pruning cannot be pushed through it.
- Mark nulls explicitly in UDFs. A pandas Series may use `NaN` or `None` depending on the data.

## Exercises

1. Write a pandas UDF that returns the length of a string column. Compare it with `F.length`.
2. Write a pandas UDF that takes two columns and returns their maximum.
3. Time the same UDF on 3 million rows and note how the time scales.

**Previous:** `07-intermediate-windows-nulls` · **Next:** `09-advanced-partitions-cache-explain`
