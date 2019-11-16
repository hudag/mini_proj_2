from Statistics.samplemean import samplemean
from Statistics.stdev import stdev
from Calculator.division import division
from Calculator.square_root import square_root
from Calculator.multiplication import multiplication
from Calculator.subtraction import subtraction
from Calculator.addition import addition
from Statistics.zscore import zscore

def confidenceinterval(data):
    try:
        z = zscore(data)
        mean = samplemean(data)
        sd = stdev(data)
        x = len(data)
        y = division(square_root(x), sd)
        err = multiplication(z, y)
        a = subtraction(mean, err)
        b = addition(mean, err)
        return a, b
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")