from Calculator.addition import addition
from Calculator.division import division
from Statistics.Getsample import getSample


def samplemean(data, sample_size):
    total = 0
    sample = getSample(data, sample_size)
    num_values = len(sample)
    for num in sample:
        total = addition(total, num)
    return division(num_values,total)
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")