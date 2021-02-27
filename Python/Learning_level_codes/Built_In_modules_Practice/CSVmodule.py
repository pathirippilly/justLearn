import csv
#using regular reader and writer , the output is a list for each line it reads

with open("A:\\lab\\data\\data-master\\data-master\\retail_db\\products\\part-00000",'r') as f:
    csv_reader=csv.reader(f) # this is a generator object which contains each line as a list
    #next(csv_reader) # using this , we can skip the header
    with open("A:\\lab\\test_outs\\test.csv", "w") as fw:
        csv_writer=csv.writer(fw,delimiter="\037")
        for i in csv_reader:
            csv_writer.writerow(i)

#using dict reader and writer , the output is a dictionary for each line

with open("A:\\lab\\test_outs\\test.csv", "r") as fr:
    csv_reader=csv.DictReader(fr,delimiter="\037",fieldnames=["prod_id","cutomer_id","prod_name","prod_desc","unit_price","imageURL"])
    with open("A:\\lab\\test_outs\\test1.csv", "w",newline='') as fw:
        csv_writer=csv.DictWriter(fw,fieldnames=["prod_id","prod_name"])
        csv_writer.writeheader()
        for i in csv_reader:
           i= {k: v for k, v in i.items() if k in ["prod_id","prod_name"]}
           csv_writer.writerow(i)