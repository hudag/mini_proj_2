from Calculator.square_root import square_root
from Statistics.samplemean import samplemean
from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.square import square
from Calculator.division import division

def samplestdev(data):
    total=0
    x = samplemean(data)
    n = len(data)
    for i in data
        total = addition(total, square(subtraction(x, i)))
    den = division(n-1,total)
    samplestd = square_root(den)
    return samplestd