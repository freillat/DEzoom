import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder \
    .master("local[*]") \
    .appName('test') \
    .getOrCreate()

df = spark.read.parquet('yellow_tripdata_2024-10.parquet')

df = df.withColumn('pickup_date', F.to_date(df.tpep_pickup_datetime))

print(df.select('pickup_date').filter(df.pickup_date == '2024-10-15').count())

df = df.withColumn('diff_hours_col', ( F.col("tpep_dropoff_datetime").cast("long") - F.col("tpep_pickup_datetime").cast("long") ) / 3600)

# maxhours = df.agg({"diff_hours_col": "max"}).collect()[0][0]
maxhours = df.agg(F.max("diff_hours_col")).collect()[0][0]

print(maxhours)

df_count = df.groupBy("PULocationID").agg(F.count("*").alias("entry_count"))
min_count = df_count.agg(F.min("entry_count")).collect()[0][0]
result = df_count.filter(F.col("entry_count") == min_count)
result.show()