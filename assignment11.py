class Student():
    College_name ="Kh College"

    def __init__(self,name):
        self.name = name

    def display(self):
        print("Student Name:",self.name)
        print("College Name:",Student.College_name)
        print()

s1 = Student("Samira Gurav")
s2 = Student("Amruata Ghatage")
s3 = Student("Tanvi Naik")
s4 = Student("Aditi Desai")
s5 = Student("Sandhya Patil")
s6 = Student("Siddhi Sorate")


s1.display()
s2.display()
s3.display()
s4.display()
s5.display()
s6.display()



    