from Calculator.addition import addition
from Calculator.division import division

def mean(data):
    try:
        num_values = len(data)
        total = 0
        for num in data:
            total = addition(total, num)

        m= division(num_values,total)
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")
        return m
