from ultralytics import YOLO


class Model:
    """
    A class representing a model for object detection.

    Args:
        model_path (str, optional): The path to the model. Defaults to None. If None, the default model is used.

    Attributes:
        model: The underlying YOLO model.

    Methods:
        predict: Performs object detection on an image.
        getBox: Retrieves the bounding box from a prediction.

    """

    def __init__(self, model_path: str = None):

        if model_path is None:
            model_path = 'yolov8n.pt'
        self.model = YOLO(model_path)
    
    def predict(self, img, args=None):
        """
        Performs object detection on an image.

        Args:
            img: The input image.

        Returns:
            The prediction result.

        """

        return self.model.predict(img, 
                                  conf=args.confidence, 
                                  classes=args.class_id)[0]
    
    def getBox(self, prediction):
        """
        Retrieves the bounding box from a prediction.

        Args:
            prediction: The prediction result.

        Returns:
            The bounding box coordinates.

        """
        return prediction.xyxy[0]