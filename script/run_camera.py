from utils.camera import Camera
from utils.preprocess import preprocess
from utils.visualise import visualise_image
from utils.save import save_image

import cv2
import argparse

def parse_args():
    """
    Parse command line arguments.

    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description="Visualise the camera feed.")
    parser.add_argument("--camera_id", type=int, default=0, help="The ID of the camera to be opened.")
    parser.add_argument("--scale", type=float, default=0.5, help="The scaling factor for resizing the image.")
    parser.add_argument("--save", type=bool, default=False, help="True if you want to save the image.")
    return parser.parse_args()


def main(args):
    """
    Main function to run the camera.

    Args:
        args (object): An object containing the camera ID, scale and save.

    Returns:
        None
    """

    # Open camera
    cam = Camera(args.camera_id)

    # Read frames from camera and display them until 'q' is pressed
    while True:
        # Read frame from camera
        ret, frame = cam.read()

        # Break if no frame is read
        if not ret:
            break

        # Preprocess frame
        frame = preprocess(frame, args.scale)

        # Display frame
        visualise_image(frame)

        # Save image if save argument is True
        save_image(frame, args.save)

        # Break if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    # Release camera
    cam.release()

if __name__ == '__main__':
    args = parse_args()
    main(args)