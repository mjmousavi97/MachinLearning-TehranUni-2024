import os
from PIL import Image
import numpy as np


def load_fruit_images(folder_path):
    apple_images = []
    banana_images =[]

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(folder_path, filename)
            try:
                img = Image.open(img_path).convert('RGB')
                img_array = np.array(img)

                if filename.lower().startswith('a'):
                    apple_images.append(img_array)
                elif filename.lower().startswith('b'):
                    banana_images.append(img_array)

            except Exception as e:
                print(f"Error processing {filename}: {e}")

    return apple_images, banana_images