import numpy as np

def calculate_metrics(y_true, y_pred):
    """
    Computes confusion matrix, accuracy, precision, recall, and F1-score 
    for binary classification results.

    :param y_true: Ground truth labels (0 or 1)
    :type y_true: numpy.ndarray
    :param y_pred: Predicted labels (0 or 1)
    :type y_pred: numpy.ndarray
    :return: Dictionary with confusion matrix and metrics
    :rtype: dict
    """
    tn = np.sum((y_true == 0) & (y_pred == 0))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    tp = np.sum((y_true == 1) & (y_pred == 1))

    confusion_matrix = np.array([
        [tn, fp],
        [fn, tp]
    ])

    total = tn + fp + fn + tp
    accuracy = (tp + tn) / total if total > 0 else 0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1_score = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

    return {
        "confusion_matrix": confusion_matrix,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1_score
    }