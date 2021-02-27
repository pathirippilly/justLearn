#factorial of a number
#user have to provide the number for which factorial is need to be calculated
res=0
temp=0
num=input("Eneter the number : ")
if(not(num[0]=='-' and num[1:len(num)].isnumeric() ) and num.isnumeric() == False):

        print("please enter a  integer  only")
       
    
else:
     num=int(num)
     temp=abs(num)
     print(num)
    
     if ( temp == 0 or temp == 1 ):
        res = 1
     else:
          while(temp-1>0):
              res=res+(temp*(temp-1))
              temp-=1


     if(num<0):
       res*=-1
       print('factorial of '+str(num) + ' is ' + str(res) )
     else:
       print('factorial of '+str(num) + ' is ' + str(res) )
       
   


    
    



