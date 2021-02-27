from pyspark.sql import SparkSession
from pyspark.sql.types import  *
from pyspark.sql.functions import *
from pyspark.sql.window import Window
from datetime import date,time,datetime

spark=SparkSession.builder.master("local").appName("OrderRevenueperDate").getOrCreate()
ordersschema=StructType(
[StructField("order_id",IntegerType(),False),StructField("order_date",TimestampType(),False),
StructField("order_customer_id",IntegerType(),False),StructField("order_status",StringType(),False)])

orderitemsschema=StructType(
[StructField("order_item_id",IntegerType(),False),StructField("order_item_order_id",IntegerType(),False),
StructField("order_item_product_id",IntegerType(),False),StructField("order_item_quantity",IntegerType(),False),
 StructField("order_item_subtotal", FloatType(), False),StructField("order_item_product_price", FloatType(), False)])

ordersrdd=spark.sparkContext.textFile('A:\\mygit\\projects\\Data_sets\\data-master\\retail_db\\orders').\
    map(lambda x : (int(x.split(",")[0]),datetime.
                    strptime(x.split(",")[1],"%Y-%m-%d %H:%M:%S.%f"),
                    int(x.split(",")[2]),x.split(",")[3]))

orderitemsrdd=spark.sparkContext.textFile('A:\\mygit\\projects\\Data_sets\\data-master\\retail_db\\order_items').\
    map(lambda x : (int(x.split(",")[0]),int(x.split(",")[1]),int(x.split(",")[2]),
        int(x.split(",")[3]),float(x.split(",")[4]),float(x.split(",")[5])))

orders=spark.createDataFrame(ordersrdd,ordersschema)
orderitems=spark.createDataFrame(orderitemsrdd,orderitemsschema)


orderstojoin=orders.filter(orders.order_status.isin("CLOSED","COMPLETE")).select("order_id","order_date")
orderitemstojoin=orderitems.select("order_item_order_id","order_item_subtotal")
ordersfinal=orderstojoin.join(orderitemstojoin,orderstojoin.order_id==orderitemstojoin.order_item_order_id).\
    drop("order_item_order_id","order_id")
orderrevenueperDate=ordersfinal.groupBy("order_date").sum("order_item_subtotal").\
    withColumn("revenue",round("sum(""order_item_subtotal"")",2)).\
    drop("sum(""order_item_subtotal"")")
orderrevenueperDate.show()

