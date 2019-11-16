from Calculator.square_root import square_root
from Statistics.samplevar import samplevar

def samplestdev(data):
    x = samplevar(data)
    samplestd = square_root(x)
    return samplestd