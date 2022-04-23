class user:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self._age=age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        if value>=0:
            self._age=value
        else:
            raise ValueError("age can not be negative!!")
    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"
    @fullname.setter
    def fullname(self,name):
        self.fname,self.lname=name.split(" ")
    

user1=user('Akhil','pathirippilly',56)
print(user1.age)
user1.age=20
print(user1.age)
print(user1.fullname)
user1.fullname="Akshay Sathian"
print(user1.fname)
