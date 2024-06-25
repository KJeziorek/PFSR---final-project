# Final Project for "Python for Scientific Research"

This repository contains the code for the final project of the course "Python for Scientific Research". The project involves reading data from a web camera, preprocessing it, processing it through a Convolutional Neural Network, and visualizing detections on the image.

## Setup

To run this project in script form, you need to install all required packages. I used a Conda environment, which is easy to operate. You can use the following commands to set up the environment:

```bash
conda create -n final python=3.9
conda activate final
pip install opencv-python matplotlib
pip install ultralytics
```

## Running the Code

Navigate to the `script` folder to use one of the two provided scripts.

### `run_camera.py`

This script reads an image from the camera and visualizes it. It accepts three possible arguments:

- `--camera_id`: Selects the ID of the camera. If you have only one camera, it should be `0`.
- `--scale`: Resizes the input image based on the scale factor (e.g., an initial image of 640x480 scaled by 0.5 returns 320x240). The default is `0.5`.
- `--save`: If `True`, saves the image to the folder `script/output/image.png`. The default is `False`.

### `run_detection.py`

This script reads an image from the camera, preprocesses it, performs detection, and visualizes it. It accepts six possible arguments:

- `--camera_id`: Selects the ID of the camera. If you have only one camera, it should be `0`.
- `--scale`: Resizes the input image based on the scale factor (e.g., an initial image of 640x480 scaled by 0.5 returns 320x240). The default is `0.5`.
- `--save`: If `True`, saves the image to the folder `script/output/image.png`. The default is `False`.
- `--model_path`: If you download a model from the [Ultralytics GitHub page](https://github.com/ultralytics/ultralytics), you can provide the path to it. If not provided, it will download the selected model. The default is `None`.
- `--confidence`: You can select the confidence threshold to filter good detections from poor ones.
- `--class_id`: You can select a specific object to detect from the list below. The default is `None`, which uses all classes.


### Detection Models
You can select one of the following models to perform detection:
```
yolov8@.pt or yolov8@.pt where @={n, s, l, m or x} (default=yolov8n.pt)

Image below presents the comparison of the models in terms of speed and accuracy:

```

<div align="center">
  <img src="yolo-comparison-plots.png" width="1000px"/><br>
</div>


### Class IDs

```
{0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'}
```