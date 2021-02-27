


import sys
import os



from pyspark.sql import SparkSession,Row
import pyspark.sql.functions as F
from pyspark.sql.types import *


jobName=sys.argv[1]


# In[ ]:


spark=SparkSession.builder.appName(jobName).enableHiveSupport().getOrCreate()
spark.sparkContext.setLogLevel("DEBUG")


# In[ ]:





# In[8]:





oiDf=spark.read.json("/public/retail_db_json/order_items")
oDf=spark.read.json("/public/retail_db_json/orders")

print(f"count of orders:{oDf.count()}")
print(f"count of order items:{oiDf.count()}")

orders=oiDf.join(oDf,oiDf.order_item_id==oDf.order_id,'left').select([*oiDf.columns,'order_customer_id','order_status'])

#Processed order summarization


#Order summary per status
orders_sum_to_status=orders.groupBy("order_status").agg(F.sum("order_item_subtotal").cast(DecimalType(18, 2)).alias("total_amt"),F.count("order_item_id").alias("order_items_total")).withColumn("order_status",F.when(F.col("order_status").isNull(),F.lit("EXCEPTION")).otherwise(F.col("order_status")))

#order summary per product
orders_sum_to_product=orders.where("order_status is not null").groupBy("order_item_product_id").agg(F.sum("order_item_subtotal").cast(DecimalType(18, 2)).alias("total_amt"),F.sum("order_item_quantity").alias("tot_qty"))

#order summary per customer
orders_sum_to_customer=orders.where("order_status is not null").groupBy("order_customer_id").agg(F.sum("order_item_subtotal").cast(DecimalType(18, 2)).alias("total_amt"))

#order summary per customer for each product
orders_sum_to_customer_product=orders.where("order_status is not null").groupBy("order_customer_id","order_item_product_id").agg(F.sum("order_item_subtotal").cast(DecimalType(18, 2)).alias("total_amt"),F.sum("order_item_quantity").alias("tot_qty"))

#order summary per customer for each status
orders_sum_to_customer_status=orders.where("order_status is not null").groupBy("order_customer_id","order_status").agg(F.count("order_item_order_id").alias("orders_total"),F.sum("order_item_subtotal").cast(DecimalType(18, 2)).alias("total_amt"))


#Exception orders
orders_exception=orders.where("order_status is null").withColumn('order_status',F.lit('EXCEPTION')).drop("order_customer_id")

#Exception order summary
orders_ex_sum_to_prod=orders_exception.groupBy("order_item_product_id").agg(F.sum("order_item_subtotal").cast(DecimalType(18, 2)).alias("total_amt"),F.sum("order_item_quantity").alias("tot_qty"))

#wrting aggregated tables to hive


orders_sum_to_status.write.mode("overwrite").saveAsTable("pathirippilly_db.orders_sum_to_status")
orders_sum_to_product.write.mode("overwrite").saveAsTable("pathirippilly_db.orders_sum_to_product")
orders_sum_to_customer.write.mode("overwrite").saveAsTable("pathirippilly_db.orders_sum_to_customer")
orders_sum_to_customer_product.write.mode("overwrite").saveAsTable("pathirippilly_db.orders_sum_to_customer_product")
orders_sum_to_customer_status.write.mode("overwrite").saveAsTable("pathirippilly_db.orders_sum_to_customer_status")
orders_exception.write.mode("overwrite").saveAsTable("pathirippilly_db.orders_exception")
orders_ex_sum_to_prod.write.mode("overwrite").saveAsTable("pathirippilly_db.orders_ex_sum_to_prod")




