from Calculator.division import division
from Calculator.subtraction import subtraction
from Calculator.addition import addition

def median(data):
    n = len(data)
    data.sort()

    if n % 2 == 0:
        median1 = data[division(2,n)]
        median2 = data[subtraction(1,division(2,n))]
        median = division(2,addition(median1,median2))
    else:
        median = data[division(2,n)]

    return median