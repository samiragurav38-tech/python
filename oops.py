class student:
    def __init__(self, name, age):
      self.name = name
      self.age = age

    def introduce(self):
        print("Hello my name is ",self.name)
 
 
s1 =student("sam",21)
s2 =student("abcd",25)
s3 =student("samira",21)
s4 =student("aditi",22)

print(f"Name of student: {s1.name} and Age of student: {s1.age}")
print(f"Name of student: {s2.name} and Age of student: {s2.age}")
print(f"Name of student: {s3.name} and Age of student: {s3.age}")
print(f"Name of student: {s4.name} and Age of student: {s4.age}")

s1.introduce()

# Employee
print("----Employee Details----")
class Employee:
   def __init__(self,Emp_name,Emp_age,Emp_contact):
      self.Emp_name = Emp_name 
      self.Emp_age = Emp_age
      self.Emp_contact = Emp_contact

 
e1 = Employee("Sam", 21, "9876543210")
e2 = Employee("Aditi", 22, "9123456789")

print(e1.Emp_name)
print(e1.Emp_age)
print(e1.Emp_contact)

print("------------------------")
#polymorphism

class Dog():
   def sound(self):
      print("Bark")

class Cat():
   def sound(self):
      print("Meow") 

class Cow():
   def sound(self):
      print("Moo")

d =Dog()
d.sound()     

c =Cat()
c.sound()     

co =Cow()
co.sound()     

print("------------------------")
class Payment():
   def pay(self):
      print(f"Paid Amount")

class UPI(Payment):
   def pay(self,amount):
      self.amount=amount
      print(f"Paid {self.amount} via UPI")

class Card(Payment):
   def pay(self,amount):
      self.amount=amount
      print(f"Paid {self.amount} via Card")

u =UPI()
u.pay(1000)

c =Card()
c.pay(500)

p =Payment()
p.pay()

#encapsulation
class Student():
  def __init__(self):
    self.name ="sam"
    self.__age = 20
  
  def edit(self,age):
      if age >=0 and age <=18:
        self.__age = age
        
      else:
        print("you can't vote")

  def show(self):
    print(self.__age)
    print(self.name)

s = Student()
s.edit(18)
s.show()








  