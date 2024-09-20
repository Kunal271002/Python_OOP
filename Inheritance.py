class Car:
    @staticmethod
    def start():
        print("Car Started..")

    @staticmethod
    def stop():
        print("Car Stopped..")


class ToyotaCar(Car):
    def __init__(self,Brand):
        self.Brand = Brand

car1 = ToyotaCar("Fortune")
car1 = ToyotaCar("Supra")

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1  = Fortuner("Diesel")
car1.start()