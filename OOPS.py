# class Student: 
#     name = "Kunal Sharma"

# s1 = Student()
# print(s1.name)

class Car:

    # Data 
    Car_Name = "Anonymous"
    Car_color = "White"

    # Default Constructors
    def __init__(self):
       pass

    # Parametrized Constructors
    def __init__(self,name,color):
       self.Car_Name = name
       self.Car_color = color

    # Methods
    def Name():
       print("Welcome To OOPS")



car1 = Car("Mercedes","Blue")
car2 = Car("BMW","Red")
print(Car.Name())
print(car1.Car_Name,car1.Car_color)
print(car2.Car_Name,car2.Car_color)