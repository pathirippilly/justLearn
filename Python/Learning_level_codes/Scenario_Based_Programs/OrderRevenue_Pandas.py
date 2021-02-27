import pandas as pd

orders_path=readfile(sys.argv[1])
orderitems_path=readfile(sys.argv[2])
outputpath="{}\orderRevenue.{}".format(sys.argv[5],str(time.time()))

try:

    orders=pd.read_csv(orders_path,header=None,
                   names=['order_id','order_date','customer_id','status'])
    orderitems=pd.read_csv(orderitems_path,
                           header=None,
                   names=['order_item_id','order_item_orderid','order_item_product_id','order_item_quantity',
                          'order_item_subtotal','order_item_product_price'])
    orders_subtotal = orderitems[['order_item_orderid', 'order_item_subtotal']].set_index("order_item_orderid"). \
        join(orders[['order_id', 'order_date', 'status']].set_index("order_id"))
    orders_subtotal.index.name = "order_id"
    orders_subtotal.groupby(["order_id", "order_date", "status"]).sum()

except Exception as err:
    print(f"Exception occured : {err}")

