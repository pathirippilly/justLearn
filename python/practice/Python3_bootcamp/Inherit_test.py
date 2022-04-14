class Animal:
    def __init__(self,species,name):
        self.name=name
        self.species=species
    def __repr__(self):
        return f"{self.name} is a {self.species}"
    def make_sound(self,sound):
        return f"{self.name} makes {sound}"
class Dog(Animal):
    def __init__(self,name,breed,toy):
        super().__init__("Dog",name)
        self.breed=breed
        self.toy=toy
    def play(self):
        return f"{self.name} plays {self.toy}"
myPet=Dog('Tommy','Siberian Husky','Ball')
print(myPet.make_sound("BoW Bow"))

