import sys
import time
from itertools import groupby,starmap


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


orderitems=readfile(sys.argv[1])
orderitems.sort(key=lambda x : x.split(",")[1])
outputpath="{}\orderRevenue.{}".format(sys.argv[2],str(time.time()))

order_subtotal_map=map(lambda x : (int(x.split(",")[1]),float(x.split(",")[4])),orderitems)
subtotal_group=groupby(order_subtotal_map,lambda x :x[0])

order_rev_per_order={}
for i in subtotal_group:
    order_rev_per_order[i[0]]=round(sum(list(map(lambda x : x[1],i[1]))),2)

with open(outputpath,'w+') as f:
    f.write("ORDERID|REVENUE\n")
    for i in order_rev_per_order.items():
        f.write("{}|{}\n".format(i[0],round(i[1],2)))






