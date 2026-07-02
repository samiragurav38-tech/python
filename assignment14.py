class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):  
    def __init__(self, name, age, roll):
        super().__init__(name, age)  
        self.roll = roll
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll: {self.roll}")

s = Student("samira", 20, 10)
s.display()
