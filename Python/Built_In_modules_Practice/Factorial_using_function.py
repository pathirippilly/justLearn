#factorial of a number
#user have to provide the number for which factorial is need to be calculated


def fact(num):
    res=0
    temp=0
    if(not(num[0]=='-' and num[1:len(num)].isnumeric() ) and num.isnumeric() == False):
    
            print("please enter a  integer  only")
           
        
    else:
         num=int(num)
         temp=abs(num)
         
        
         if ( temp == 0 or temp == 1 ):
            res = 1
         else:
              while(temp-1>0):
                  res=res+(temp*(temp-1))
                  temp-=1
    
    
         if(num<0):
           res*=-1
           return res
         else:
           return res
       


num=input("Eneter the number : ")
print(fact(num))


   


    
    



