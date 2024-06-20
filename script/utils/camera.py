import cv2


class Camera:
    """
    Represents a camera object that can be used to capture frames.

    Args:
        camera_id (int): The ID of the camera to be opened. Defaults to 0.

    Attributes:
        camera: The OpenCV VideoCapture object representing the camera.

    Methods:
        read(): Reads a frame from the camera.
        release(): Releases the camera.

    """

    def __init__(self, camera_id: int = 0):
        """
        Initializes a new instance of the Camera class.

        Args:
            camera_id (int): The ID of the camera to be opened. Defaults to 0.
        """
        # Open camera
        self.camera = cv2.VideoCapture(camera_id)

    def read(self):
        """
        Reads a frame from the camera.

        Returns:
            tuple: A tuple containing the success flag and the captured frame.
        """
        # Read frame from camera
        return self.camera.read()

    def release(self):
        """
        Releases the camera.
        """
        # Release camera
        self.camera.release()