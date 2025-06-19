import numpy as np
import random
import matplotlib.pyplot as plt


def plot_random_images(num_images, image_list, labels=None, random_seed=42, figsize=(15, 15)):
    """
    Displays a set of randomly selected images from a given list in a square grid layout.

        
    :param num_images: Number of images to randomly select and display.
    :type num_images: int

    :param image_list: A list (or array) of images, where each image is a NumPy array suitable for plt.imshow().
    :type image_list: list or numpy.ndarray

    :param labels: Optional list of labels to use as titles for each displayed image.
    :type labels: list, optional

    :param random_seed: Seed for NumPy's random number generator to ensure reproducibility.
    :type random_seed: int, optional

    :param figsize: Tuple specifying the width and height of the overall figure in inches.
    :type figsize: tuple, optional
    """
    np.random.seed(random_seed)

    grid_size = int(np.ceil(np.sqrt(num_images)))
    fig, axes = plt.subplots(grid_size, grid_size, figsize=figsize)

    selected_indices = np.random.choice(a=len(image_list),size=num_images, replace=False)

    axes = axes.ravel()

    for idx, img_idx in enumerate(selected_indices):
        axes[idx].imshow(image_list[img_idx])
        axes[idx].axis('off')

        if labels is not None:
            axes[idx].set_title(labels[img_idx], pad=10, fontsize=12)

    for idx in range(num_images, (grid_size * grid_size)):
        axes[idx].axis('off')

    plt.tight_layout()
    plt.show()
    
    np.random.seed(None)