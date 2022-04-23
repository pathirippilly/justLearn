#num=int(input("please enter the input: "))
#lst=range(1,num+1)
#lst_out=[]
#lst_chk=[]
#for i in lst:
#    for j in lst:
#        for k in lst:
#            if(i!=j and i!=k and j!=k and {i,j,k} not in lst_chk):
#                if(i**2+j**2==k**2):
#                    #print(i," ",j," ",k)
#                    lst_chk=lst_chk+[{i,j,k}]
#                    lst_out=lst_out+[(i,j,k)]
#                    
#print (lst_out)

from math import sqrt
num=int(input("please enter the input: "))
for i in range(1,num+1):
    for j in range(i+1, num+1):
        k_sqr=i**2 + j**2
        k=int(sqrt(k_sqr))
        #print(k)
        if((k_sqr - k**2) == 0 and k in range(1,num+1)):
            print(i,j,k)
        
