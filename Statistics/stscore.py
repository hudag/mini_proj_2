from Statistics.stdev import stdev
from Statistics.mean import mean
from Calculator.division import division
from Calculator.subtraction import subtraction

def stscore(data):
    x = mean(data)
    y = stdev(data)
    num = division(subtraction(i,x),y)
    return num