class Car:

    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started..")

    @staticmethod
    def stop():
        print("Car Stopped..")


class ToyotaCar(Car):
    def __init__(self,Brand,type):
        self.Brand = Brand
        super().__init__(type)
        super().start()

car1 = ToyotaCar("Pirus","Electric")
print(Car.type)