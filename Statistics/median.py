from Calculator.division import division
from Calculator.subtraction import subtraction
from Calculator.addition import addition

def median(data):
    n = len(data)
    data.sort()

    if n % 2 == 0:
        median1 = data[int(division(2,n))]
        median2 = data[int(subtraction(1,division(2,n)))]
        mdn = division(2,addition(median1,median2))
    else:
        mdn = data[int(division(2,n))]

    return mdn
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")