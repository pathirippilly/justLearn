from pyspark.sql import SparkSession
from pyspark.sql.types import  *
from pyspark.sql.functions import *
from pyspark.sql.window import Window


spark=SparkSession.builder.master("local").appName("LastNordersperday").getOrCreate()
spark.sparkContext.setLogLevel("INFO")
orders=spark.read.csv("A:\\mygit\\projects\\Data_sets\\data-master\\retail_db\\orders").\
    toDF("order_id","order_date","order_customer_id","order_status").\
    select(col("order_id").cast(IntegerType()),to_timestamp("order_date",
                                                            "yyyy-MM-dd HH:mm:ss").alias("order_date"),
           col("order_customer_id").cast(IntegerType()),"order_status")
window=Window.partitionBy(orders.order_date).orderBy(orders.order_id.desc())
LastordersPerday=orders.select(col('*'),row_number().over(window).alias('row_number_f')).\
    where((col('row_number_f') <= 1)).drop('row_number_f').orderBy(desc("order_date"))
LastordersPerday.show ()

