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

    # Baca gambar
  image = Image.open(uploaded_file)

  # Jalankan inferensi pada gambar dengan confidence threshold yang ditetapkan
  results = _model(image, conf=confidence_threshold)  # return a list of Results objects
  for result in results:
    result.save(filename='result.jpg')

  # Tampilkan hasil deteksi
  result_image = Image.open('result.jpg')
  return result_image