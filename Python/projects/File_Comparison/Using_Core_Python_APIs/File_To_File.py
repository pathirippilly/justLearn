import os
import sys
import time
import datetime
from functools import wraps
from collections import Counter,deque


# functions

begint=datetime.datetime.now()

print "execution started at : {}\n".format(datetime.datetime.now())

# def fn_timer(function):
#     @wraps(function)
#     def function_timer(*args, **kwargs):
#         bt = datetime.datetime.now()
#         result = function(*args, **kwargs)
#         et = datetime.datetime.now()
#         print ("Total time running function %s: %s seconds" %
#                (function.func_name, str(et - bt))
#                )
#         return result
#     return function_timer

# @fn_timer
def fileCount(file_counter=None):
    row_cnt=reduce(lambda x,y : x+y,file_counter.itervalues())
    col_cnt=len(file_counter.most_common(1)[0][0].split(","))
    yield row_cnt,col_cnt

# @fn_timer
def fileSize(file_path):
    sz=os.path.getsize(file_path)
    sz_str="{} bytes".format(sz)
    if sz>1000000000:
        sz = round(sz/1000000000.0,2)
        sz_str = "{} GB".format(sz)
    elif sz>1000000:
        sz = round(sz/1000000.0,2)
        sz_str = "{} MB".format(sz)
    elif sz>1000:
        sz = round(sz/1000.0,2)
        sz_str = "{} KB".format(sz)
    yield sz_str

# @fn_timer
def fileDetailing(file_path="",file_counter=None):
    print "FILE DETAILING"
    print "**************\n"
    print "FILE_NAME:{}".format(file_path)
    print"SIZE: {}".format(next(fileSize(file_path)))
    cnt = (x for x in next(fileCount(file_counter)))
    print "RECORD_COUNT: {}".format(next(cnt))
    print "COLUMN_COUNT: {}\n".format(next(cnt))
# @fn_timer
def fullValidation(output_path="",source=None,target=None):
    # bt=datetime.datetime.now()

    source=deque(sorted(source,key=lambda x : x.split(",")[0]))
    
    # et=datetime.datetime.now()
    # print "source deque sorting has taken : {}\n".format(et-bt)
    
    # bt = datetime.datetime.now()
    
    target=deque(sorted(target,key=lambda x : x.split(",")[0]))
    
    # et=datetime.datetime.now()

    # print "Target deque sorting has taken : {}\n".format(et - bt)

    # bt = datetime.datetime.now()
    compared=deque((x,y) for (x,y) in zip(source, target) if x != y)
    # et = datetime.datetime.now()

    # print "conflict record preparation has taken : {}\n".format(et - bt)


    # bt = datetime.datetime.now()
    if len(compared) > 0:
        error_report = "{}\\file_diff.{}".format(output_path, int(time.time()))
        print error_report
        print "FULL DATA VALIDATION FAILED!!\n"
        print "Please find the conflicting records of source and target in {}\n".format(error_report)
        with open(error_report, 'w+') as f:
            f.write("SOURCE|TARGET\n")
            for line in compared:
                f.write("{}|{}\n".format(line[0].strip(), line[1].strip()))
        # et = datetime.datetime.now()

        # print "conflict record logging has taken : {}\n".format(et - bt)
    

    else:
        print "FULL DATA VALIDATION SUCCESSFULLY COMPLETED\n"
# @fn_timer

def dupFind(dup_counter=None,output_path=""):

    # bt = datetime.datetime.now()
    duplicates = ((x, c) for x, c in dup_counter.iteritems() if c > 1)
    dup_count= reduce(lambda x,y : x+y , dup_counter.itervalues()) - len(dup_counter)
    # et = datetime.datetime.now()
    # print "duplicates prepration has taken {}\n".format(et - bt)
    print "Number of Duplicate records found: {}\n".format(dup_count)

    dup_report="{}\dup.{}".format(output_path, int(time.time()))

    print "Please find the duplicate records  in {}\n".format(dup_report)
    # bt=datetime.datetime.now()
    with open(dup_report, 'w+') as f:
        f.write("RECORD|DUPLICATE_COUNT\n")
        for line in duplicates:
            f.write("{}|{}\n".format(line[0].strip(), line[1]).strip())
    # et=datetime.datetime.now()
    # print "Duplication logging has taken {}\n".format(et - bt)

def completeTest(source=None,target=None):
    if  target.most_common(1)[0][1]>1 and source.most_common(1)[0][1]>1:
        print "Both Source: {} and Target: {} is having duplicates\n".format(sys.argv[1], sys.argv[2])
        print "Handling Duplication of Source:\n"
        dupFind(source, output_path)
        print "Handling Duplication of Target:\n"
        dupFind(target, output_path)
        print"SOURCE vs TARGET:FULL DATA VALIDATION IGNORING THE DUPLICATES OF BOTH SOURCE AND TARGET\n"
        fullValidation(output_path, source,target)
    elif target.most_common(1)[0][1] > 1:
        print "Target : {} is having duplicate records\n".format(sys.argv[2])
        dupFind(target, output_path)
        print"SOURCE vs TARGET:FULL DATA VALIDATION IGNORING THE DUPLICATES OF TARGET\n"
        fullValidation(output_path, source, target)
    elif source.most_common(1)[0][1] > 1:
        print "Source  : {} is having duplicate records\n".format(sys.argv[1])
        dupFind(source, output_path)
        print"SOURCE vs TARGET:FULL DATA VALIDATION IGNORING THE DUPLICATES OF SOURCE\n"
        fullValidation(output_path, source, target)
    else :
        print "NO DUPLICATES ARE FOUND IN SOURCE AND TARGET\n"
        fullValidation(output_path, source, target)

# Variable initialisation

flag=1
output_path = sys.argv[3]

# File Existence Check
if len(sys.argv)==4:
    for fil in sys.argv[:3]:
        if not os.path.isfile(fil):
            print "{} is not a file or file does not exist.Please enter a valid file\n".format(fil)
            flag=0
            break
    if not os.path.exists(output_path):
        flag=0
        print "{} does not exist".format(output_path)
else:
    flag=0
    print "invalid Number of Arguments Provided\n"

# Main Validation
if flag==1:
    # Opening files and adding the contents in to a list
    # bt=datetime.datetime.now()
    with open(sys.argv[1]) as source,open(sys.argv[2]) as target:
        src = Counter(source)
        tgt = Counter(target)
    # et=datetime.datetime.now()

    # print "file deque prepration has taken {}\n".format(et - bt)


    # file detailing
    print "SOURCE\n"
    fileDetailing(sys.argv[1],src)
    print "TARGET\n"
    fileDetailing(sys.argv[2], tgt)

    # file Validation
    print "SOURCE vs TARGET : COLUMN COUNT VALIDATION\n"
    if len(src.most_common(1)[0][0].split(","))==len(tgt.most_common(1)[0][0].split(",")):
        print "COLUMN COUNT CHECK SUCCEEDED\n"
        print "SOURCE vs TARGET : RECORD COUNT VALIDATION\n"
        if len(src) == len(tgt) :

            print "RECORD COUNT TEST SUCCEEDED IGNORING THE DUPLICATES IF ANY\n"

            print"SOURCE vs TARGET:FULL DATA VALIDATION\n"
            completeTest(src,tgt)

        else:
            print "RECORD COUNT TEST FAILED\n"

            print"SOURCE vs TARGET:FULL DATA VALIDATION\n"

            completeTest(src, tgt)
    else:
        print "COLUMN COUNT CHECK FAILED!!"
        print""
        if len(src.most_common(1)[0][0].split(",")) > len(tgt.most_common(1)[0][0].split(",")):
            print "SOURCE IS HAVING MORE NUMBER OF COLUMNS THAN TARGET!!\n"
        else:
            print "TARGET IS HAVING MORE NUMBER OF COLUMNS THAN SOURCE!!\n"

endt=datetime.datetime.now()

print "execution finished at : {}\n".format(datetime.datetime.now())
print "total time taken {} seconds\n".format(endt-begint)



