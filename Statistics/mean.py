from Calculator.addition import addition
from Calculator.division import division

def mean(data):
    num_values = 0
    total = 0
    for num in data:
        total = addition(total, num)
        num_values = addition(num_values,1)
    return division(total, num_values)