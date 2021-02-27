import sys
import configparser as cp

try:
        from pyspark import SparkContext, SparkConf

        props = cp.RawConfigParser()
        props.read("/home/pathirippilly/spark2_jobs/src/main/python/application.properties")
        conf = SparkConf(). \
                setAppName("RevenuePerProductForMonth"). \
                setMaster(props.get(sys.argv[1],"executionmode"))
        sc =  SparkContext(conf = conf)
        inputpath = props.get(sys.argv[1],"input_base_dir")
        outputpath= props.get(sys.argv[1],"output_base_dir")
        month=props.get(sys.argv[1],"month")
        localdir=props.get(sys.argv[1],"local_dir")
        path = sc._gateway.jvm.org.apache.hadoop.fs.Path
        filesystem=sc._gateway.jvm.org.apache.hadoop.fs.FileSystem
        configuration=sc._gateway.jvm.org.apache.hadoop.conf.Configuration

        fs=filesystem.get(configuration())

        if(fs.exists(path(inputpath)) == False):
                print("inputpath doesnot exists")
        else:
                if(fs.exists(path(outputpath))):
                        fs.delete(path(outputpath),True)

                orders=inputpath + "/orders"
                counter=sc.accumulator(0)
                def OrderTuples(order):
                        counter.add(1)
                        return (int(order.split(",")[0]),1)
                ordersFiltered = sc.textFile(orders). \
                    filter(lambda order : month in order.split(",")[1]). \
                    map(lambda order : OrderTuples(order))
                print(counter)
                orderitems=inputpath + "/order_items"
                orderitemsFiltered = sc.textFile(orderitems). \
                        map(lambda oi : (int(oi.split(",")[1]),(int(oi.split(",")[2]),float(oi.split(",")[4]))))
                revenueByProductId=orderitemsFiltered.join(ordersFiltered).map(lambda rec : rec[1][0]).reduceByKey(lambda x,y: x+y)

                with open(localdir + "/products/part-00000") as file:
                        products=file.read().splitlines()
                productsDict=dict(map(lambda p : (int(p.split(",")[0]),p.split(",")[2]),products))
                productsBroadcast=sc.broadcast(productsDict)
                revenueByProductName=revenueByProductId.map(lambda p : f"{productsBroadcast.value[p[0]]}\t{round(p[1],2)}")
                for i in revenueByProductName.take(10):
                        print(i)
                revenueByProductName.coalesce(1).saveAsTextFile(outputpath)
                print(f"COUNTER IS:{counter}")
except ImportError as e:
        print("Can not import spark modules",e)
sys.exit(1)
