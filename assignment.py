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

# fibonacci 
def fibonacci(n):
    a, b = 0,1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
N = int(input("Enter N: "))
fibonacci(N)
    
# palindrome

def palindrome(x):
   s=str(x).lower()
   return s==s[::-1]
number=input("Enter number:")
text=input("Enter string:")
print(f"{number} -> {'Palindrome' if palindrome(number)else'Not palindrome'}")
print(f"{text} -> {'palindrome'if palindrome(text)else'Not palindrome'}")   


# squaers,cube
numbers2= [1,2,3,4,5]
squares=list(map(lambda x:x*x,numbers2))
print(squares)


cube=list(map(lambda x:x**3,numbers2))
print(cube)




    