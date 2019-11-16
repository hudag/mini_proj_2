from Statistics.samplemean import samplemean
from Statistics.stdev import stdev
from Calculator.division import division
from Calculator.squareroot import squareroot
from Calculator.multiplication import multiplication
from Calculator.subtraction import subtraction
from Calculator.addition import addition

def confidence_interval(data):
    z_value = 1.05
    mean =samplemean(data)
    sd = tdev(data)
    x = len(data)
    y = division(squareroot(x), sd)
    margin_of_error = multiplication(z_value, y)
    a = subtraction(mean, margin_of_error)
    b = addition(mean, margin_of_error)
    return a, b