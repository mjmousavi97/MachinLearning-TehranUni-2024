import numpy as np
import matplotlib.pyplot as plt
from src.channel_to_channel_ratio import channel_ratio_classifier

def find_best_ratio_thresh(xs, ys, channel1, channel2, threshold=(0.1, 3.0)):
    """
    Finds the best threshold for the ratio between two color channels that maximizes prediction accuracy.

    :param xs: List or array of input images (3D RGB).
    :type xs: list or numpy.ndarray
    :param ys: True class labels for the images.
    :type ys: list or numpy.ndarray
    :param channel1: Index of the numerator channel (e.g., 0 for red).
    :type channel1: int
    :param channel2: Index of the denominator channel (e.g., 2 for blue).
    :type channel2: int
    :param threshold: Tuple (start, end) for threshold values to test. Default is (0.1, 3.0).
    :type thresh_range: tuple(float, float)
    :param step: Step size for thresholds. Default is 0.1.
    :type step: float

    :return: Tuple (best_thresh, best_accuracy)
    :rtype: tuple(float, float)
    """
    thresholds = np.arange(threshold[0], threshold[1], step=0.1)
    correct_counts = []

    for thresh in thresholds:
        y_pred = channel_ratio_classifier(xs, channel1=channel1, channel2=channel2, thresh=thresh)
        correct = np.sum(y_pred == ys)
        correct_counts.append(correct)

    plt.plot(thresholds, correct_counts)
    plt.xlabel("Channel Ratio Threshold")
    plt.ylabel("Correct Predictions")
    plt.title("Accuracy vs. Ratio Threshold")
    plt.grid(True)
    plt.show()

    best_index = np.argmax(correct_counts)
    best_thresh = thresholds[best_index]
    best_accuracy = correct_counts[best_index] / len(xs)

    return best_thresh, best_accuracy