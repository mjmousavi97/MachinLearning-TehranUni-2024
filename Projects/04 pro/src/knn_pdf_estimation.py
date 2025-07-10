import numpy as np


def knn_estimation(x, samples, k):
    distances = np.sort(np.abs(samples - x))
    v = 2 * distances[k -1]

    return k / (len(samples) * v)