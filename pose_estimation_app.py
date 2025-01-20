import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image

# MediaPipe Pose setup
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Streamlit app setup
st.title("Human Pose Estimation")
st.write("Upload an image or use your webcam to detect human poses in real-time.")

# Function to process an image
def process_image(image):
    with mp_pose.Pose(static_image_mode=True, model_complexity=2) as pose:
        # Convert the image from BGR to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)

        if not results.pose_landmarks:
            st.warning("No pose detected in the image!")
            return None

        # Draw landmarks on the image
        annotated_image = image.copy()
        mp_drawing.draw_landmarks(
            annotated_image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
        )
        return annotated_image

# Function to process webcam feed
def process_webcam():
    cap = cv2.VideoCapture(0)  # Open webcam
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        stframe = st.empty()  # Placeholder for the webcam feed
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                st.warning("Unable to access webcam.")
                break
            # Convert BGR to RGB
            image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(image_rgb)

            # Draw landmarks
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    results.pose_landmarks,
                    mp_pose.POSE_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                    mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
                )
            stframe.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB")

    cap.release()

# Sidebar for file upload or webcam selection
option = st.sidebar.selectbox("Choose an option:", ["Upload Image", "Use Webcam"])

if option == "Upload Image":
    uploaded_file = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image_np = np.array(image)
        processed_image = process_image(image_np)
        if processed_image is not None:
            st.image(processed_image, caption="Pose Estimation Result", use_column_width=True)

elif option == "Use Webcam":
    st.warning("Ensure your webcam is connected.")
    process_webcam()
