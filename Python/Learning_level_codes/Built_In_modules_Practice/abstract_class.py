#
#1. 
#ABCs offer a higher level of semantic contract between clients and the implemented classes.
#
#Defining an Abstract Base Class (ABC) is a way of producing a contract between the class implementers and the callers.
# It isn't just a list of method names, but a shared understanding of what those methods should do. 
#If you inherit from this ABC, you are promising to follow all the rules described in the comments, 
#including the semantics of the print() method.
#
#2.
#you can not directly create an instance of an abstract class (here it is employee). you need to inherit it first (here the
#inheritted subclass is developer)
#
#3.
#You should either use or override or just call all the abstract methods from superclass in subclass.


from abc import ABC,abstractmethod

class employee(ABC):
    
#    def __init__(self,sal):
#        self.sal=sal
    def bonus(self,sal):
        return sal*.50
    @abstractmethod
    def calc_sal(self,sal):
        return sal*1.10
class developer(employee):
    def calc_sal(self,sal):
        return (super().calc_sal()*1.10)+super().bonus()
    
    
emp_1=developer(100000)
print(emp_1.calc_sal())
#print(help(developer))
        
    