class Employee:
    raise_percentage = 1.05
    def     __init__(self,first,last,email,salary):
        """
        :param  first: first name
        :type first : str
        :param last:  last name
        :type last : str
        :param email: email
        :type email : str
        :param salary: salary of the employee
        :type salary: int
        """
        self.first = first
        self.last = last
        self.email = email
        self.salary = salary
        if self.salary<10000:
            self.grade="C"
        elif self.salary<20000:
            self.grade = "B"
        else:
            self.grade = "A"
    def apply_raise(self):
        self.salary=self.salary*self.raise_percentage
    @classmethod
    def set_raise_percentage(cls,percentage):
        cls.raise_percentage=percentage
    @classmethod
    def from_string(cls,string):
        first,last,email,salary=string.split("-")
        return cls(first,last,email,int(salary))
    def __str__(self):
       return f"{self.first} {self.last}"
    def __add__(self, other):
        return self.salary + other.salary
emp1=Employee("akhil","pathirippilly","abc@cde.com",50000)
emp2=Employee("akhil","pathirippilly","abc@cde.com",1000)
# print(emp1) #this will return the name of the employee --> overrrided the __str__ method
# print(emp1 + emp2) # this will add the salary of the emloyees --> overrrided the __add__ method
# print(emp1.grade,emp2.grade) # this will return the grade of the employee
# emp1.apply_raise()# raising salary using apply_raise() regular method
# print(emp1.salary)
# Employee.set_raise_percentage(1.1) #setting class variable using class method
# emp3 = Employee.from_string("rick-siegal-rsiegal@abc.com-25000") #alternative constructer using

# class deveoper(Employee):
#     raise_percentage = 1.2
#     def __init__(self,first,last,email,salary,prog_lang):
#         super().__init__(first,last,email,salary)
#         self.prog_lang=prog_lang
#
# mng1=deveoper("akhil","pathirippilly","abc@cde.com",50000,'python')



class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    @property
    def email(self):
        return f"{self.last}.{self.first}@email.com"
    @fullname.setter
    def fullname(self,fname):
        first, last = fname.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print(f"{self.fullname} is deleted" )
        self.first = None
        self.last = None



emp3=Employee('shukur','ibrahim')
emp3.first="hassan"
print(emp3.fullname) # fullname() will be converted into an attribute by @property
print(emp3.email) # email() will be converted into an attribute by @property
emp3.fullname="abdul rahman" # this will utilises the setter @fullname.setter
print(emp3.fullname)
print(emp3.email)
del emp3.fullname # this will utilises the setter @fullname.deleter

