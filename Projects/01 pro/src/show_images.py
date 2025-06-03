import matplotlib.pyplot as plt

def show_images(images, labels=None, title=None, max_images=5):
    """
    Display a few images from the list with optional labels.

    Parameters:
    - images: list of numpy arrays (images)
    - labels: list of strings or ints (one per image)
    - title: optional title for the whole figure
    - max_images: max number of images to display
    """
    n = min(len(images), max_images)
    plt.figure(figsize=(15, 3))

    if title:
        plt.suptitle(title, fontsize=16)

    for i in range(n):
        plt.subplot(1, n, i+1)
        plt.imshow(images[i])
        plt.axis('off')
        
        if labels is not None and i < len(labels):
            plt.title(str(labels[i]), fontsize=12)

    plt.show()
