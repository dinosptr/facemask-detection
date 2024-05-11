import streamlit as st

def main():
  st.title("Face Mask Detection")
  st.write("Welcome to the face mask detection app! This app helps you detect whether someone in an image is wearing a face mask correctly or not.")

  st.header("Problem Statement")
  st.subheader("Problem Statements :thinking_face:")
  st.write("In the midst of the COVID-19 pandemic, proper face mask usage has become crucial to prevent the spread of the virus. However, many people still do not wear masks correctly, such as not covering their noses and mouths completely.")

  st.subheader("Goals :dart:")
  st.write("- Develop a face mask detection model that can identify whether someone is using a mask correctly.")
  st.write("- Create an application that allows users to upload images and get predictions on whether the mask is being used correctly.")

  st.header("Solution")
  st.subheader("Solution Statements :computer:")
  st.write("To achieve these goals, I will use the YOLOv8 object detection algorithm to detect faces and masks in images. YOLOv8 is a state-of-the-art object detection algorithm that is known for its speed and accuracy.")
  st.write("I will integrate YOLOv8 with a web application created using Streamlit. This application will allow users to upload images and see the detection results, including whether the mask is being used correctly or not.")

if __name__ == "__main__":
  main()
