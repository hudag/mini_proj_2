from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.Getsample import getSample


def sample_mean(data, sample_size):
    total = 0
    sample = getSample(data, sample_size)
    num_values = len(sample)
    for num in sample:
        total = addition(total, num)
    return division(total, num_values)