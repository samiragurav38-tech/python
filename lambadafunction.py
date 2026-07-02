add = lambda a,b:a+b
print(add(10,20))
print(max(10,20))

numbers= [10,55,40,23,50]
squares=list(map(lambda x:x*x,numbers))
print(squares)
even=list(filter(lambda x:x%2==0,numbers))
print(even)

num=[1,2,3,4,5]
cube=list(map(lambda x:x**3,num))
print(cube)

import math
print(math.sqrt(25))
print(math.pi)

from math import sqrt
print(sqrt(45))


