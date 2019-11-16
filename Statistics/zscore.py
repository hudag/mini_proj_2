from Statistics.stdev import stdev
from Statistics.mean import mean
from Calculator.division import division
from Calculator.subtraction import subtraction

def zscore(data):
    try:
        x = mean(data)
        y = stdev(data)
        num = division(y,subtraction(x,data[0]))
        return round(num,5)
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")