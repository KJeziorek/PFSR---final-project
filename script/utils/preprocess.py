import cv2

def preprocess(image, scale: float = 0.5):
    """
    Preprocesses an image by resizing it.

    Args:
        image (numpy.ndarray): The input image to be preprocessed.
        scale (float, optional): The scaling factor for resizing the image. Defaults to 0.5.

    Returns:
        numpy.ndarray: The preprocessed image.
    """
    return cv2.resize(image, (0, 0), fx=scale, fy=scale)