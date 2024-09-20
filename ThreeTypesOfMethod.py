class Student:
    def __init__(self,phy,chem,maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths

    # def percentage(self):
    #     return str((self.phy+self.chem+self.maths)/3)+"%"


    # also we can do this by @property method:
    @property
    def percentage(self):
        return str((self.phy +  self.chem + self.maths )/3)+"%"



std1 = Student(93,23,24)
std1.phy = 20
print(std1.percentage)

