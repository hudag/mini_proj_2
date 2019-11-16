from Statistics.stdev import stdev
from Statistics.mean import mean
from Calculator.division import division
from Calculator.subtraction import subtraction

def array(data):
    x = mean(data)
    y = stdev(data)
    num = division(y,subtraction(x,data[0]))
    return round(num,5)