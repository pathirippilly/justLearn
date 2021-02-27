import sys
import time
from collections import Counter


def readfile(file_path):
    try:

        with open(file_path) as f:
            contents = Counter(f)
        return contents
    except OSError as err:
        print("OS error: {}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
def orderrevenue(order_items=None):
    revenue={}
    try:
        for items in order_items:
            orderitem=(int(items.strip().split(",")[1]),float(items.strip().split(",")[4]))
            if revenue.get(orderitem[0]):
                revenue[orderitem[0]]+=orderitem[1]
            else:
                revenue[orderitem[0]]=orderitem[1]
        return revenue
    except ValueError as err :
        print(f"ValueError : {err}")



orderitems=readfile(sys.argv[1])
outputpath="{}\orderRevenue.{}".format(sys.argv[2],str(time.time()))

revenue=orderrevenue(orderitems)

with open(outputpath,'w+') as f:
    f.write("ORDERID|REVENUE\n")
    for i in revenue.items():
        f.write("{}|{}\n".format(i[0],round(i[1],2)))




