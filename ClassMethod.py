class Person:
    Name = "Ananomyous"

    # def changeName(self,Name):
    #     # Person.Name = Name    
    #     # or
    #     self.__class__.Name = Name  
               
    @classmethod
    def ChangeName(cls,Name):
        cls.Name = Name

person1 = Person()
person1.ChangeName("Kunal Sharma")
print(Person.Name)
print(person1.Name)