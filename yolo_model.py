from ultralytics import YOLO

def load_model():
  """
  Loads the pre-trained YOLOv8 face mask detection model.

  Returns:
      YOLO: The loaded YOLOv8 model instance.
  """

  return YOLO('models/yolov8s_facemask.pt')
