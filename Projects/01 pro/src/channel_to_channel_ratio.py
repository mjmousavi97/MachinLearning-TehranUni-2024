import numpy as np

def channel_ratio_classifier(image_list, channel1, channel2, thresh=1):
    """    
    Classifies images based on the ratio of average intensity between two specified color channels.

    :param image_list: List or array of RGB images (each image must be of shape H x W x 3).
    :type image_list: list or np.ndarray
    :param channel1: Index of the numerator channel (0=Red, 1=Green, 2=Blue).
    :type channel1: int
    :param channel2: Index of the denominator channel (0=Red, 1=Green, 2=Blue).
    :type channel2: int
    :param thresh: Threshold to compare the ratio against (default is 1).
    :type thresh: float, optional
    :return: Array of predictions (0 if ratio > threshold, else 1).
    :rtype: np.ndarray
    """
    predictions = []
    for image in image_list:
        image_average = np.mean(image.reshape(-1, 3), axis=0)

        if (image_average[channel1] / (image_average[channel2] + 1e-6)) > thresh:
            predictions.append(0)
        else:
            predictions.append(1)

    return np.array(predictions)