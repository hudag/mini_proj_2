import math
from Statistics.mean import mean
from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.square import square
from Calculator.division import division
from Calculator.square_root import square_root


def stdev(data):

    total = 0
    x = mean(data)
    n = len(data)
    for i in data:
        total = addition(square(subtraction(x,i)))
    new = division(total,n)
    std = square_root(new2)
    return std
