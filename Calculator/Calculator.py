from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.division import division
from Calculator.multiplication import multiplication
from Calculator.square import square
from Calculator.square_root import square_root

class Calculator:
    result=0

    def _init_(self):
        pass

    def add(self, a, b):
        self.result= addition(a,b)
        return self.result

    def subtract(self, a, b):
        self.result= subtraction(a,b)
        return self.result

    def multiply(self, a, b):
        self.result= multiplication(a,b)
        return self.result

    def divide(self, a, b):
        self.result= division(a,b)
        return self.result

    def doubled(self, a):
        self.result = square(a)
        return self.result

    def sq_root(self, a):
        self.result = square_root(a)
        return self.result