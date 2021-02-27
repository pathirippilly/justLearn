"""
Problem statement:
Get COMPLETE Orders from order data set
filter out orders placed in 2013-07-25
Get order items for given order id
And now calculate order revenue for each orders
And Save it as another file

This Code uses in built  filter, map and 3rd party reduce for calculating revenue

"""
import sys
import time
from functools import reduce


def readfile(file_path):
    try:

        with open(file_path) as f:
            contents = f.read().splitlines()
        return contents
    except OSError as err:
        print("OS error: {}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

orders=readfile(sys.argv[1])
orderitems=readfile(sys.argv[2])
outputpath="{}\orderRevenue.{}".format(sys.argv[5],str(time.time()))
status = sys.argv[3]
orderdate = sys.argv[4]


complete_orders_20130725=list(filter(lambda x : x.split(",")[3] == status and
                                           x.split(",")[1].split(" ")[0] == orderdate, orders))

complete_orders_20130725_mapped=list(map(lambda x : int(x.split(",")[0]),complete_orders_20130725))


order_items_filtered =  list(filter(lambda x : int(x.split(",")[1])
                                               in complete_orders_20130725_mapped,orderitems))
order_items_filtered_mapped = list(map(lambda x : (int(x.split(",")[1]),float(x.split(",")[4])),order_items_filtered))

Revenue_order_dict = {}
for i in order_items_filtered_mapped:
    Revenue_order_dict.setdefault(i[0], []).append(i[1])

order_rev_per_order={}
for i in Revenue_order_dict.items():
    order_rev_per_order[i[0]]=reduce(lambda x,y:x+y,i[1])

with open(outputpath,'w+') as f:
    f.write("ORDERID|REVENUE\n")
    for i in order_rev_per_order.items():
        f.write("{}|{}\n".format(i[0],round(i[1],2)))