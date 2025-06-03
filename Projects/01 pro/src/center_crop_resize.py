from PIL import Image
import numpy as np

def center_crop_and_resize(images: list, target_size: tuple =(256, 256)):
    """
    Center crop each image to square (1:1), then resize to target size.

    Parameters:
    - images: list of numpy arrays (images)
    - target_size: tuple (width, height) to resize to (default: (256, 256))

    Returns:
    - list of processed images as numpy arrays
    """
    processed_images = []

    for img_array in images:
        # Convert numpy array back to PIL Image for easier processing
        img = Image.fromarray(img_array)

        width, height = img.size
        min_dim = min(width, height)

        # Calculate cropping box to center crop to square
        left = (width - min_dim) // 2
        top = (height - min_dim) // 2
        right = left + min_dim
        bottom = top + min_dim

        cropped_img = img.crop((left, top, right, bottom))

        # Resize to target size (e.g., 256x256)
        resized_img = cropped_img.resize(target_size)

        # Convert back to numpy array
        processed_images.append(np.array(resized_img))

    return processed_images
