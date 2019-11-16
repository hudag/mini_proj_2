from StaticMethods.proportion import proportion
from StaticMethods.division import division
from StaticMethods.multiplication import multiplication
from StaticMethods.subtraction import subtraction

def varprop(data, corr):
    n = len(data)
    prop = proportion(n, corr)
    res = division(n, multiplication(prop, subtraction(1, prop)))
    return res