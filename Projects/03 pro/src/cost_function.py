import numpy as np


def compute_cost(X, y, weights):
    prediction = np.dot(X, weights)
    cost = np.mean((prediction - y) ** 2) / 2

    return cost