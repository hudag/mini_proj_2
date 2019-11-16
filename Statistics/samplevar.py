from Statistics.samplemean import samplemean
from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.square_root import square_root
from Calculator.division import division

def confidenceinterval(data):
    z_value = 1.05
    mean =samplemean(data)
    sd = stdev(data)
    x = len(data)
    y = division(square_root(x), sd)
    err= multiplication(z_value, y)
    a = subtraction(mean, err)
    b = addition(mean, err)
    return a, b
