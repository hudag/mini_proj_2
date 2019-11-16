from Statistics.popvar import popvar
from Calculator.square_root import square_root

def stdev(data):
    base= popvar(data)
    std = square_root(base)
    return std
