from StaticMethods.division import division

def proportion(size, corr):
    if corr is None:
        corr = 3
    result = division(corr, size)
    return result
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")