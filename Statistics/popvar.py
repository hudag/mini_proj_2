from Statistics.mean import mean
from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.square import square
from Calculator.division import division

def popvar(data):
    try:
        total = 0
        x = mean(data)
        n = len(data)
        for i in data:
            total = addition(total,square(subtraction(x, i)))
        populationvar = division(n,total)
        return populationvar
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")