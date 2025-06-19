import numpy as np


def channel_prediction(xs, channel, thresh=20, target_class=0):
    """
        Predicts class labels for a list of RGB images based on the average intensity of a specified color channel.
    If the average intensity of the selected channel is greater than the threshold, the image is classified
    as the target class; otherwise, it is classified as the opposite class.

    :param xs: List or array of RGB images. Each image should be a 3D array (height x width x 3).
    :type xs: list or numpy.ndarray

    :param channel: The color channel to use for prediction (0 = Red, 1 = Green, 2 = Blue).
    :type channel: int

    :param thresh: Threshold for the average channel intensity. Default is 20.
    :type thresh: int, optional

    :param target_class: Class label to assign when the average channel value exceeds the threshold.
                         Default is 0. The opposite class (1 - target_class) is assigned otherwise.
    :type target_class: int, optional

    :return: An array of predicted class labels (0 or 1) for each image.
    :rtype: numpy.ndarray
    """
    predictions = []

    for x in xs:
        image_average = np.mean(x.reshape(-1, 3), axis=0)

        if image_average[channel] > thresh:
            predictions.append(target_class)
        else:
            predictions.append(1 - target_class)
    
    return np.array(predictions)