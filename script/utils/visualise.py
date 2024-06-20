import cv2

def visualise_image(image, window_name: str = 'frame'):
    """
    Display the given image in a window with the specified name.

    Args:
        image: The image to be displayed.
        window_name: The name of the window.

    Returns:
        The displayed image.
    """
    # Display image
    cv2.imshow(window_name, image)
    return image


def visualise_bbox(image, predictions):
    """
    Visualizes bounding boxes on an image.

    Args:
        image (numpy.ndarray): The input image.
        predictions (object): The predictions object containing bounding box information.

    Returns:
        numpy.ndarray: The image with bounding boxes and class labels visualized.
    """

    # Define colours for bounding boxes
    colours = {}
    for i in range(80):
        colours[i] = (int(50+205 * (i % 2)), int(40+215 * (i % 3)), int(30+225 * (i % 5)))
    
    # Get class dictionary
    names = predictions.names

    # Draw bounding boxes with class labels and confidence scores
    for box, cls, conf in zip(predictions.boxes.xyxy, predictions.boxes.cls, predictions.boxes.conf):
        print(box, cls)
        cv2.rectangle(image, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), colours[int(cls)], 2)
        cv2.putText(image, f"{names[int(cls.numpy())]} ({conf})", (int(box[0]), int(box[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, colours[int(cls)], 2)

    return image
