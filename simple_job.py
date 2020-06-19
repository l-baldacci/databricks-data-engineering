# Entry point


from pyspark.sql import SparkSession
from validation import *

spark = SparkSession \
    .builder \
    .getOrCreate()

sourceDataDir = "dbfs:/Users/lorenzo.baldacci@databricks.com/datasets/chicago-crimes"
targetDataDir = "dbfs:/Users/lorenzo.baldacci@databricks.com/datasets/chicago-crimes-delta"

sourceDF = spark.read.format("csv").load(sourceDataDir)

standardisedDF = standardise(sourceDF)

standardisedDF.write.mode("append").format("delta").save(targetDataDir)
print("Record count: " + str(spark.read.format("delta").load(targetDataDir).count()))
