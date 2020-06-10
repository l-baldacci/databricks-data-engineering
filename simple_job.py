from pyspark.sql import SparkSession
from validation import *

spark = SparkSession \
    .builder \
    .getOrCreate()

print("Testing simple count")
# The Spark code will execute on the Databricks cluster.
print(spark.range(100).count())

spark.sql("SHOW databases").show()

spark.sql('CREATE DATABASE IF NOT EXISTS lorenzo_baldacci_test')
# spark.sql('CREATE TABLE IF NOT EXISTS test.t (id INT, a STRING, b STRING) USING delta')

spark.sql("SHOW databases").show()
spark.sql("USE lorenzo_baldacci_test").show()
spark.sql("SHOW tables").show()

print("End testing simple count")

# cdcDf = spark.read.load("examples/src/main/resources/file.csv", format="csv", sep=",", inferSchema="true", header="true").cache()
#
# standardise(cdcDf).createOrReplaceTempView("cdcFeed")
#
# spark.sql("""
# MERGE INTO silver_table st
# USING cdcFeed cdc
# ON st.id = cdc.id
# WHEN MATCHED THEN
#  UPDATE SET
#   a = cdc.a,
#   b = clv.b
# WHEN NOT MATCHED
#  THEN INSERT (id, a, b)
#    VALUES (cdc.id, cdc.a, cdc.b)
# """)