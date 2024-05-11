import streamlit as st
from PIL import Image
from ultralytics import YOLO

@st.cache_data
def process_image(uploaded_file, _model, confidence_threshold):
  """
  Processes an uploaded image for face mask detection.

  Args:
      uploaded_file (Streamlit File Uploader): The uploaded image file.
      confidence_threshold (float): The confidence threshold for detections.

  Returns:
      Image: The processed image with detected faces and masks highlighted.
  """

  # Read Image
  image = Image.open(uploaded_file)

  # Run inference on the image with the confidence threshold set
  results = _model(image, conf=confidence_threshold)  # return a list of Results objects
  for result in results:
    result.save(filename='result.jpg')

  # Return the detected image result
  result_image = Image.open('result.jpg')
  return result_image
