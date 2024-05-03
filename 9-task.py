"""
reate a Python class representing a basic calculator with methods for addition, subtraction, multiplication, and division. - A
"""

class BasicCalculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):

        if b == 0:
            return 0
        return a / b


calculator = BasicCalculator()

a = 10
b = 5

print(calculator.add(a, b))        # Qo'shish
print(calculator.subtract(a, b))   # Ayirish
print(calculator.multiply(a, b))   # Ko'paytirish
print(calculator.divide(a, b))     # Bo'lish
