import cv2
import os

def save_image(image, save: bool):
    """
    Saves the given image to the specified path.

    Args:
        image: The image to be saved.
        save: A boolean indicating whether to save the image.

    Returns:
        The saved image.
    """

    # Save image
    if save:
        output_file = 'script/output/image.png'
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        cv2.imwrite(output_file, image)