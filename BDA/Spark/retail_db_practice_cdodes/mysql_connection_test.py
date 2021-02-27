from pyspark.sql import SparkSession

spark=SparkSession.builder.master("local").appName("mysqlConnectionTest").getOrCreate()

orders=spark.read.jdbc(url="jdbc:mysql://ms.itversity.com",table="retail_db.order_items",
                       properties={"user":"retail_user","password":"itversity"})

orderitems=spark.read.jdbc("jdbc:mysql://ms.itversity.com","retail_db.order_items",
                numPartitions=4,column="order_item_order_id",lowerBound=10000,upperBound=20000,
                properties={"user":"retail_user","password":"itversity"})
orderrevenue=spark.read.jdbc("jdbc:mysql://ms.itversity.com","(select order_date,round(sum(order_item_subtotal),2) as revenue from retail_db.orders o join retail_db.order_items oi "
                                                             "on (o.order_id=oi.order_item_order_id and o.order_status in('CLOSED','COMPLETE')) group by order_date) a",
                             properties={"user":"retail_user","password":"itversity"})

orders=spark.read.jdbc("jdbc:mysql://ms.itversity.com","retail_db.orders",predicates= ["order_status in('CLOSED')"],properties={"user":"retail_user","password":"itversity"})

orderrevenue.show()