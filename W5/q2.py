import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName('test') \
    .getOrCreate()

df = spark.read.parquet('yellow_tripdata_2024-10.parquet')
df_repartitioned = df.repartition(4)
df_repartitioned.write.mode("overwrite").parquet("output/yellow_tripdata_2024-10_repartitioned.parquet")

spark.stop()