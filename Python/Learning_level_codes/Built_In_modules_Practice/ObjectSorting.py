class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary = salary
    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)
e1=Employee('akhil',22,123654)
e2=Employee('sijil',20,23546)
e3=Employee('akash',25,12345698)
employees=[e1,e2,e3]
emp_sorted =  sorted(employees,key=lambda x : x.salary)
print(emp_sorted)