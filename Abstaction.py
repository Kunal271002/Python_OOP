class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clush = False


    def start(self):
        self.cluch = True
        self.acc = True
        print("Car Started..")

car1 = Car()
car1.start()