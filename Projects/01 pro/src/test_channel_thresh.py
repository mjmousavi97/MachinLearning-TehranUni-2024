import matplotlib.pyplot as plt
import numpy as np
from src.predict_by_color_channel import channel_prediction


def find_best_threshold(xs, ys, channel, target_class=0, thresh_range=(15, 255)):
    """
    Finds the optimal threshold value for the given color channel that maximizes prediction accuracy 
    using the channel_prediction function. Plots the number of correct predictions vs. threshold.

    :param xs: List or array of input images (each image is expected to be a 3D array, e.g., HxWx3).
    :type xs: list or numpy.ndarray

    :param ys: True labels corresponding to the input images.
    :type ys: list or numpy.ndarray

    :param channel: Index of the color channel to evaluate (0=Red, 1=Green, 2=Blue).
    :type channel: int

    :param target_class: The class label to predict when the average channel intensity exceeds the threshold.
                         Default is 0.
    :type target_class: int, optional

    :param thresh_range: Tuple indicating the range of threshold values to test (start, end).
                         Thresholds will be tested from thresh_range[0] to thresh_range[1] - 1.
                         Default is (15, 90).
    :type thresh_range: tuple(int, int), optional

    :return: A tuple containing:
             - best_thresh (int): The threshold value that gave the highest number of correct predictions.
             - best_accuracy (float): The corresponding accuracy (correct / total).
    :rtype: tuple(int, float)
    """
    thresholds = np.arange(thresh_range[0], thresh_range[1])
    correct_counts = []

    for thresh in thresholds:
        y_pred = channel_prediction(xs, channel=channel, thresh=thresh, target_class=target_class)
        correct = np.sum(y_pred == ys)
        correct_counts.append(correct)

    plt.plot(thresholds, correct_counts)
    plt.xlabel("Threshold")
    plt.ylabel("Correct Predictions")
    plt.title("Accuracy vs. Threshold")
    plt.grid(True)
    plt.show()

    best_index = np.argmax(correct_counts) 
    best_thresh = thresholds[best_index]
    best_accuracy = correct_counts[best_index] / len(xs)

    return best_thresh, best_accuracy
