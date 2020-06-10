from unittest import TestCase
from validation import *
from pyspark.sql.types import *
from pyspark.sql import SparkSession


class Test(TestCase):
    def test_standardise(self):
        spark = SparkSession \
            .builder \
            .getOrCreate()
        s = StructType([
            StructField("id", IntegerType()),
            StructField("a", StringType()),
            StructField("b", StringType())
            ])
        cdcSet = {(1, 'a1', 'b1'), (3, 'a3', 'b3')}
        cdcDf = spark.createDataFrame(cdcSet, schema=s)

        resultDf = standardise(cdcDf)

        resultSet = set(resultDf.rdd.map(lambda row : (row[0], row[1], row[2])).collect())

        self.assertEqual(cdcSet, resultSet)
        # self.fail()
