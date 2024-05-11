import cv2
import os
import shutil

def save_uploaded_file(uploaded_file):
    """
    Saves an uploaded file to the uploads directory.

    Args:
        uploaded_file (Streamlit File Uploader): The uploaded file.

    Returns:
        str: The path to the saved file.
    """

    file_name = "uploaded_file.jpg"
    os.makedirs("uploads", exist_ok=True)  # Create 'uploads' directory if it doesn't exist
    with open(os.path.join("uploads", file_name), "wb") as f:
        f.write(uploaded_file.getbuffer())

    return os.path.join("uploads", file_name)

def clear_directory(directory):
    """
    Clears the contents of a directory.

    Args:
        directory (str): The directory path to clear.
    """

    if os.path.exists(directory):
        shutil.rmtree(directory)  # Recursively remove contents

def display_detected_frames(confidence_threshold, model, st_frame, image):
    """
    Displays detected faces and masks on a video frame using YOLOv8.

    Args:
        confidence_threshold (float): The confidence threshold for detections.
        model (YOLO): The YOLOv8 model instance.
        st_frame (Streamlit Element): The Streamlit element to display the video.
        image (numpy.ndarray): The video frame as a NumPy array.
    """

    results = model.predict(image, conf=confidence_threshold)  # Predict detections
    res_plotted = results[0].plot()  # Plot detections on the frame
    st_frame.image(res_plotted, caption='Detected Video', channels="BGR", use_column_width=True)
