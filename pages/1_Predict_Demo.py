import streamlit as st
import cv2
from image_processing import process_image
from video_processing import display_detected_frames, save_uploaded_file, clear_directory
from yolo_model import load_model

# Load the YOLOv8 model (moved to a separate function)
model = load_model()

def main():
    # User interface elements in the sidebar
    st.sidebar.title("Options")
    input_type = st.sidebar.radio("Select Input Type", ["Image", "Video", "Webcam"])
    confidence_threshold = st.sidebar.slider("Confidence Threshold", min_value=0.0, max_value=1.0, value=0.5, step=0.05)

    if input_type == "Image":
        st.title("Face Mask Detection")
        option = st.radio(
            "Choose Image Source:",
            ("Upload Image", "Take Picture"),
            horizontal=True
        )

        if option == "Upload Image":
            upload_icon = ":camera:"
            uploaded_file = st.file_uploader(f"{upload_icon} Upload Image", type=["jpg", "jpeg", "png"])

            if uploaded_file is not None:
                processed_image = process_image(uploaded_file, model, confidence_threshold)
                st.image(processed_image, caption='Result: Face Mask Detection', use_column_width=True)

        # Functionality for capturing images using webcam (implementation is deferred)
        elif option == "Take Picture":
            # Use st.camera_input to take a picture
            image = st.camera_input("Take a picture")

            if image is not None:
                # Process images using st.cache
                result_image = process_image(image, model, confidence_threshold)

                # Show detection results
                st.image(result_image, caption='Result FaceMask Detection', use_column_width=True)

    elif input_type == "Video":
        st.title("Upload Video for Face Mask Detection")
        upload_icon = ":movie_camera:"
        uploaded_video = st.file_uploader(f"{upload_icon} Upload Video (Max 200MB)", type=["mp4", 'gif'], accept_multiple_files=False)

        if uploaded_video is not None:
            video_path = save_uploaded_file(uploaded_video)
            video_bytes = uploaded_video.read()
            st.video(video_bytes)
            st.write("Processing video... Please wait.")

            try:
                vid_cap = cv2.VideoCapture(video_path)
                st_frame = st.empty()
                while (vid_cap.isOpened()):
                    success, image = vid_cap.read()
                    if success:
                        display_detected_frames(confidence_threshold, model, st_frame, image)
                    else:
                        vid_cap.release()
                        break
            except Exception as e:
                st.sidebar.error("Error loading video: " + str(e))
            finally:
                clear_directory("uploads")  # Clear temporary files after video processing

    elif input_type == "Webcam":
        webcam_icon = ":camera:"
        st.title(f"{webcam_icon} Face Mask Detection using Webcam")
        st.info("Webcam support is currently under development.")

if __name__ == "__main__":
    main()
