from Statistics.mean import mean
from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.square import square
from Calculator.division import division

def popvar(data):
    total = 0
    x = mean(data)
    n = len(data)
    for i in data:
        total = addition(square(subtraction(x, i)))
    populationvar = division(total, n)
    return populationvar