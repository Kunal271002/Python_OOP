class Student: 

    # Data
    Algebra = 12
    Science = 132
    Geometry = 213

    # Parametrized constructor
    def __init__(self,subject1_marks,subject2_marks,subject3_marks):
        self.Algebra = subject1_marks
        self.Science = subject2_marks
        self.Geometry = subject3_marks

    #Average Methods
    def Average(Algebra,Geometry,Science):
        average = (Algebra + Geometry + Science)/3
        return average
    
    @staticmethod
    def Hello():
        print("Hello World")
    


Kunal = Student(12,124,234)
print(Student.Average(Kunal.Algebra,Kunal.Science,Kunal.Geometry))
print(Student.Hello())
