import glob as g
import re,os

#Declaring and initializing list
lst=[]
lines=[]

#removing the outputfile if it exists on the output directory(note:please provide your own direcctory)
os.remove('A:\\lab\\SPYDER\\output_dir\\out_fil.txt')
#creating and opening the output file in append mode
fp_out=open('A:\\lab\\SPYDER\\output_dir\\out_fil.txt','a')
#getting the input files in input directory(note:please provide your own direcctory)
for fileName in g.glob('A:\\lab\\SPYDER\\EXTERNAL_WORK\\v*.txt'):
    lst.clear()
    lines.clear()
    print(fileName)
    #opening the inout file
    fp=open(fileName,'r')
    #reading the lines
    lines = fp.readlines()
    #getting the index of MAG column
    indx=list(filter(None,lines[1].split(" "))).index('MAG')

    i=2
    

    while (i<lines.__len__()):
    # if next # comes it will break the loop
        if(re.match('#',lines[i])):
                    
                    break
        else:
            
     #adding the output value in to another list       
            lst.append(list(filter(None,lines[i].split(" ")))[indx])
        i+=1
    print(lst)
    #writing the output value in to output file
    fp_out.write(",".join(str(x) for x in lst))
    fp_out.write('\n')
fp_out.close()
    
   

