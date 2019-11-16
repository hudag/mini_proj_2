from Statistics.samplemean import samplemean
from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.square import square
from Calculator.division import division

def samplevar(data):
    total=0
    x = samplemean(data,3)
    n = len(data)
    for i in data:
        total = addition(total, square(subtraction(x, i)))
    samplevar = division(n-1,total)
    return samplevar
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")
