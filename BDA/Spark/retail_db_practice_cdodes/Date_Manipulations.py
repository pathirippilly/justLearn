from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from datetime import date,time,datetime
from pyspark.sql.types import *

# Convert a timestamp string of format "MM/dd/yyyy HH:mm:ss.SSSSSS" to "yyyy/MM/dd HH:mm:ss.SSSSSS" and save it as timestamp
spark=SparkSession.builder.master("local").appName("DateManipulation").getOrCreate()
df = spark.createDataFrame([('12/21/2015 23:21:20.689523', "product1")], ['dt', "product_name"])
df = df.withColumn('row_index', monotonically_increasing_id())


def convert_fmt(date_time):
    return datetime.strptime(datetime.strptime(date_time, "%m/%d/%Y %H:%M:%S.%f").strftime("%Y/%m/%d %H:%M:%S.%f"),
                             "%Y/%m/%d %H:%M:%S.%f")


df_new = df.rdd.map(lambda x: (x.asDict()["row_index"], convert_fmt(x.asDict()["dt"]))).toDF(["index", "dt_new"])
df = df_new.join(df, df_new.index == df.row_index).drop("row_index", "index", "dt")
df=df.withColumn("day_of_mn",dayofmonth("dt_new")). \
    withColumn("dt_6mnts", add_months(df.dt_new, 6)).\
    withColumn("utc_time",to_utc_timestamp("dt_new", "UTC")).\
    withColumn("year_beg",trunc("dt_new","YYYY")).\
    withColumn("year",year("dt_new")). \
    withColumn("month",month("dt_new"))
df.printSchema()
df.show()
