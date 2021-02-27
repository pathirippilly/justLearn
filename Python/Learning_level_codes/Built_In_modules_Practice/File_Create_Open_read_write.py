with open("A:\\lab\\data\\data-master\\data-master\\retail_db\\products\\part-00000",'r') as f:
    #l=f.read() # this will store entire content of a file as a large string
    #l=f.read().splitlines() # return a list containing each elements as each line. new line character is excluded by default
    #l=f.read().splitlines(True) # return a list containing each elements as each line. new line character is included
    #l=f.readlines() # same as f.read().splitlines(True)
    #l=f.readline() #read only single line at a time

    #   with open("A:\\lab\\test_outs\\test.csv","w") as fw: #reading from a huge file and writing to another file can be done like this
    #      for i in f: #reads only one line at a time
    #            fw.write(i) #write only one line at a time=

    #f.read(100) # this will read first 100 characters

    #def getNthLine(num): #this function will print the nth line of a file
    #   for i in range(num+1):
    #       if i==num:
    #            print(l)
    #getNthLine(22)


    def lineIndexGen(): #this function will yield a generator of starting indexes of each line
        l=f.readline()
        n=0
        while(len(l)>0):
            n=n+(l.rfind("\n")+1)
            yield  n
            l = f.readline()
    l1=lineIndexGen() #iterating through l1, we can seek any line position using f.seek(number)
    #If we want to read write files that are not in UTF-8 encoded format use 'rb' and 'wb' modes
    print(list(l1))



