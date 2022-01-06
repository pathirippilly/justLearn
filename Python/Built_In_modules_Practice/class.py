class test():
    #__init__ is the constructer here.we can initialize all class variables here.
    #self is basically referring to the instance of the object. You need to have self on every method under a class
    #All variables which are not under self instance is local variables which can not be accessed by any objects
    
    def __init__(self,num):
        self.num=num
        self.factorial=self.fact(str(num))
        
    def fact(self,num):
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
           #superTest is the class referring to the super class test.It can access all class variables of test
class superTest(test):
    def __init__(self,num):
        super().__init__(num)
        self.square=self.sqr(num)
    def sqr(self,num):
        res=int(num)*int(num)
        return res
    

#inp_1 is the object created over superTest   
inp_1=superTest(60)

#this will print the square of the input number.Basically this is the output of sqr method inside superTest class
print(inp_1.square)
#this will print the factorial of the input number.Basically this is the output of fact method of super class test
print(inp_1.factorial)
#this will print the dictionary of variables and valuses assigned to it that can be accessed by the object inp_1
print(inp_1.__dict__)
#this will show you how the entire proccess is happening
print(help(inp_1))



