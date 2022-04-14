"""
Problem statement:
Get COMPLETE Orders from order data set
filter out orders placed in 2013-07-25
Get order items for given order id
And now calculate order revenue for each orders
And Save it as another file

This Code uses Custom filter, map and reduce for calculating revenue

"""
import sys
import time
from collections import deque


def readfile(file_path):
    try:

        with open(file_path) as f:
            contents = deque(f)
        return contents
    except OSError as err:
        print("OS error: {}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def myFilter(c,f):
    newC=[]
    for i in c:
        if f(i):
            newC.append(i)
    return newC
def myMapper(c,f):
    newC=[]
    for i in c:
        newC.append(f(i))
    return newC
def myReducer(c,f):
    t = c[0]
    for i in c[1:]:
        t=f(t,i)
    return t

orders=readfile(sys.argv[1])
orderitems=readfile(sys.argv[2])
outputpath="{}\orderRevenue.{}".format(sys.argv[5],str(time.time()))
status=sys.argv[3]
orderdate=sys.argv[4]

complete_orders=myFilter(orders,lambda x : (x.strip().split(",")[3]==status))
complete_orders_20130725 =  myFilter(complete_orders,lambda x : (x.split(",")[1].
                                                                 split(" ")[0]==orderdate))
filtered_orders_mapped=myMapper(complete_orders_20130725,lambda x: (int(x.split(",")[0]),
                                                                    x.split(",")[3],x.split(",")[1]))
orderitems_mapped=myMapper(orderitems,lambda x : (int(x.split(",")[1]),float(x.split(",")[4])))

orders_alone = myMapper(filtered_orders_mapped,lambda x : x[0])

filtered_orders_orderitems=myFilter(orderitems_mapped,lambda x : x[0] in orders_alone)

Revenue_order_dict = {}
for i in filtered_orders_orderitems:
    Revenue_order_dict.setdefault(i[0], []).append(i[1])

order_rev_per_order={}
for i in Revenue_order_dict.items():
    order_rev_per_order[i[0]]=myReducer(i[1],lambda x,y:x+y)

with open(outputpath,'w+') as f:
    f.write("ORDERID|REVENUE\n")
    for i in order_rev_per_order.items():
        f.write("{}|{}\n".format(i[0],round(i[1],2)))







