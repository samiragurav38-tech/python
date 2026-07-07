def prime(num):
    if num < 2:
        return False
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True
numbers =[2, 4, 5, 6, 4]

for num in numbers:
    if prime(num):
       print(num,"is a prime number.")
    else:
        print(num,"is a not prime number.")
print("----------") 


# fibonacci 
def fibonacci(n):
    a, b = 0,1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
N = int(input("Enter N: "))
fibonacci(N)
print()



# palindromes
def is_palindrome(value):
    value = str(value)

    if value == value[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
print("121 ->", is_palindrome(121))
print("123 ->", is_palindrome(123))
print("madam ->", is_palindrome("madam"))
print("hello ->", is_palindrome("hello"))
print("----------") 


#Armstrong Number
def is_armstrong(num):
    digits = len(str(num))
    total = sum(int(digit) ** digits for digit in str(num))

    return total == num

numbers = [153, 370, 123]

for n in numbers:
    if is_armstrong(n):
        print(f"{n} is an Armstrong Number")
    else:
        print(f"{n} is Not an Armstrong Number")
print("----------") 


#Lambda function squaers,cube
square = lambda x: x ** 2

cube = lambda x: x ** 3

maximum = lambda a, b: a if a > b else b

even_odd = lambda n: "Even" if n % 2 == 0 else "Odd"

c_to_f = lambda c: (c * 9/5) + 32

print("Square of 5:", square(5))
print("Cube of 3:", cube(3))
print("Maximum of 10 and 20:", maximum(10, 20))
print("7 is", even_odd(7))
print("25°C =", c_to_f(25), "°F")




    