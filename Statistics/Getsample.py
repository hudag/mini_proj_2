from random import random


def getSample(data, sample_size):
    random_values = random.choice(data, k=sample_size)
    return random_values