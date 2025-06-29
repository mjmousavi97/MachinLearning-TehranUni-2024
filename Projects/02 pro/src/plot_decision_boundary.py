import numpy as np
import matplotlib.pyplot as plt

def simple_plot_decision_boundary(classifier, X, y):
    """
    Plot the decision boundary of a trained classifier along with data points.

    This function creates a mesh grid over the feature space, predicts the class 
    labels for each point in the grid using the given classifier, and then uses
    contourf to visualize the decision regions. It also overlays the original 
    data points on top of the decision boundary.

    Parameters
    ----------
    classifier : object
        A trained classifier object that implements a `predict` method 
        accepting an array of shape (n_samples, n_features).

    X : np.ndarray of shape (n_samples, 2)
        The input feature data. Must be 2-dimensional (for plotting).

    y : np.ndarray of shape (n_samples,)
        The class labels corresponding to each data point in `X`.

    Returns
    -------
    None
        This function only plots the figure and does not return anything.
    """
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 100),
        np.linspace(y_min, y_max, 100)
    )

    grid_points = np.c_[xx.ravel(), yy.ravel()]

    Z = classifier.predict(grid_points)
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.3)

    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k')

    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title("Decision Boundary")
    plt.show()