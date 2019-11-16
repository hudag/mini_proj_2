from Calculator.addition import addition
from Calculator.division import division

def mean(data):
    num_values = len(data)
    total = 0
    for num in data:
        total = addition(total, num)

    m= division(num_values,total)
    return m
