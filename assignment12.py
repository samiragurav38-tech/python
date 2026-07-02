class Calculator:
    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def subtraction(a, b):
        return a - b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Error: Divide by 0"
        return a / b


print("Addition:", Calculator.addition(10, 5))        
print("Subtraction:", Calculator.subtraction(10, 5))  
print("Multiplication:", Calculator.multiplication(10, 5)) 
print("Divide:", Calculator.divide(10, 5))            