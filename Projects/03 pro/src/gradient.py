import numpy as np


def compute_gradient(X, y, weights):
    prediction = np.dot(X, weights)
    difference =  prediction - y
    return np.dot(X.T, difference) / X.shap[0]