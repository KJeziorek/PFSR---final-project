from utils.camera import Camera
from utils.preprocess import preprocess
from model.model import Model
from utils.visualise import visualise_bbox
from utils.save import save_image

import cv2
import argparse

'''
The main function for running object detection

If you want to select a specific class to detect, you can use the class_id from this dictionary:

{0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 
8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 
14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 
22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 
29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 
35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 
40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 
47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 
54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 
61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 
68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 
75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'}

'''
def parse_args():
    parser = argparse.ArgumentParser(description="Run object detection on the camera feed.")
    parser.add_argument("--camera_id", type=int, default=0, help="The ID of the camera to be opened.")
    parser.add_argument("--model_path", type=str, default=None, help="The path to the model.")
    parser.add_argument("--save", type=bool, default=False, help="If True, the image will be saved.")
    parser.add_argument("--scale", type=float, default=1.0, help="The scaling factor for resizing the image.")
    parser.add_argument("--confidence", type=float, default=0.5, help="The confidence threshold for detections.")
    parser.add_argument("--class_id", type=int, default=None, help="The class ID to detect.")
    return parser.parse_args()

def main(args):
    """
    Main function for running object detection.

    Args:
        args: An object containing the command line arguments.

    Returns:
        None
    """

    # Open camera
    cam = Camera(args.camera_id)

    # Load model
    model = Model(args.model_path)

    # Read frames from camera and display them until 'q' is pressed
    while True:
        # Read frame from camera
        ret, frame = cam.read()

        # Break if no frame is read
        if not ret:
            break

        # Preprocess frame
        frame = preprocess(frame, args.scale)

        # Perform object detection
        prediction = model.predict(frame, args)

        # Visualise bounding box
        frame = visualise_bbox(frame, prediction)
        
        # Save image if save argument is True
        save_image(frame, args.save)

        # Display frame
        cv2.imshow('frame', frame)

        # Break if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()

if __name__ == "__main__":
    args = parse_args()
    main(args)