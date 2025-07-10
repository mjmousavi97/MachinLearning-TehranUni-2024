import numpy as np


def gaussian_parzen_estimation(x, samples, h=0.1):
    sum_sample = 0
    for sample in samples:
        sum_sample += np.exp(-(x - sample)**2 / (2 * h**2))

    return sum_sample / (len(samples) * h * np.sqrt(2 * np.pi))
