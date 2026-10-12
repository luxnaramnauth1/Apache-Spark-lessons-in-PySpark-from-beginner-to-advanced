# 09 | ADVANCED | Partitions, shuffles, caching, query plans, and adaptive execution
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("09-partitions-explain")
    .master("local[*]")
    .config("spark.sql.shuffle.partitions", "8")        # default is 200; tune to your data
    .config("spark.sql.adaptive.enabled", "true")       # Adaptive Query Execution
    .getOrCreate()
)
spark.sparkContext.setLogLevel("ERROR")

df = spark.range(0, 2_000_000).withColumn("bucket", F.col("id") % 10)

# ---- 1. Partitions: how the data is split across tasks ----------------------------------------
print("initial partitions:", df.rdd.getNumPartitions())

# repartition: full shuffle. Use it to increase partitions or to group by a key.
by_key = df.repartition(8, "bucket")
print("after repartition(8, 'bucket'):", by_key.rdd.getNumPartitions())

# coalesce: merges partitions WITHOUT a full shuffle. Use it to reduce partitions before writing.
few = by_key.coalesce(2)
print("after coalesce(2):", few.rdd.getNumPartitions())

# ---- 2. Caching: keep a result in memory when it is reused --------------------------------------
evens_of_three = df.filter(F.col("id") % 3 == 0).cache()
print("first count (computes and caches):", evens_of_three.count())
print("second count (reads from cache):", evens_of_three.count())
evens_of_three.unpersist()                          # free the memory when done

# ---- 3. Query plans: read them to find expensive shuffles --------------------------------------
summary = df.groupBy("bucket").agg(F.count("*").alias("rows"), F.avg("id").alias("avg_id"))
print("--- formatted physical plan (look for Exchange = shuffle) ---")
summary.explain(mode="formatted")

# ---- 4. Broadcast hint: force a small table to be broadcast ----------------------------------
small = spark.createDataFrame([(0, "zero"), (1, "one"), (2, "two")], ["bucket", "label"])
joined = df.join(F.broadcast(small), "bucket").groupBy("label").count()
print("--- join plan (look for BroadcastHashJoin) ---")
joined.explain(mode="simple")

spark.stop()
