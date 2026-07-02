print("-----Student Management System-----")
class Student():
    def __init__(self,name,roll_no,course):
        self.name=name
        self.roll_no=roll_no
        self.course=course

    def display(self):
        print(f"Name : {self.name}")
        print(f"Roll_No : {self.roll_no}")
        print(f"Course : {self.course}")

class CollegeStudent(Student):
    def __init__(self, name, roll_no, course):
        super().__init__(name, roll_no, course)

    def display(self):
        return super().display()

s1 =Student("Sam",100,"BCA")
s1.display()

print()

s2 =CollegeStudent("Mira",101,"BCA")
s2.display()



            
        