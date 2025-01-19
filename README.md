# human-pose-estimation-using-machine-learning
<b> This project leverages cutting-edge machine learning techniques to detect and track human poses in real time. It is designed to analyze human motion for a variety of applications, including fitness tracking, sports analytics, healthcare, and interactive systems like AR/VR.

## An example of a graphical skeleton is shown below:

![image](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*JUXSz1Vy5S7OiIz26DPgew.png)

# So how does it work?
<b> Backend Workflow
✍ Image Mode:
Reads the uploaded image.
Converts it to RGB and processes it using Mediapipe Pose Estimation.
Returns a processed image with pose landmarks to the frontend.

<b>✍ Video Mode:
Processes each video frame using Mediapipe Pose.
Generates a processed video by overlaying pose landmarks frame-by-frame.
Outputs the final video for seamless playback.

<b>✍ Webcam Mode:
Captures live frames from the webcam.
Applies Mediapipe Pose in real time.
Displays dynamic results on the frontend.

<b>MediaPipe uses TensorFlow Lite in the backend to perform pose estimation efficiently. The process begins with a person detection module, which identifies the region of interest (ROI) in the frame containing the human body. This cropped ROI is then passed to the pose estimator, which predicts the keypoints or landmarks within the human body. MediaPipe Pose Estimation detects a total of 33 keypoints on the body, including key regions such as the head, shoulders, elbows, wrists, hips, knees, and ankles.

<b>Key Features of MediaPipe Pose Estimation:
<b>1.3D Pose Estimation: MediaPipe Pose estimates the x, y, and z coordinates for each landmark, where:

1. x and y represent the 2D position of a landmark.
2. z gives the depth of a landmark relative to others, providing an indication of how far or close a specific point is to the camera.
This depth information allows for a more accurate understanding of body posture, enabling the model to detect and track poses in three-dimensional space.

2. Real-time Performance: MediaPipe Pose uses BlazePose, a cutting-edge research model, to achieve high-fidelity pose tracking. This solution is optimized for real-time inference, allowing it to run efficiently on a wide range of devices including mobile phones, desktops, and laptops.

3. Potential Applications: The ability to detect keypoints in real-time is valuable across various use cases such as yoga, dance, fitness applications, and AR.
Fitness and sports motion analysis.
Gesture recognition for interactive applications.
Motion tracking in gaming or animation.
Examples:
a) Quantifying physical exercises: Ensuring correct form and tracking progress over time.
b) Sign language recognition: Mapping hand gestures to text or speech.
c) Augmented Reality (AR): Overlaying digital elements on the human body based on pose data.

![image](https://user-images.githubusercontent.com/48796009/228968898-73de4945-1957-4656-a17a-c4180c49dbe7.png)


 MediaPipe Pose real-world 3D coordinates

https://user-images.githubusercontent.com/48796009/228969800-b6e3092a-75a0-4660-9d42-e02f6f4ff4e5.mp4



## Pose Estimation Quality

To assess the effectiveness of MediaPipe Pose, we evaluate the model using different datasets across various domains:

Yoga: Predicting the pose of individuals performing yoga.
Dance: Capturing dynamic movements in dance.
HIIT: Tracking physical exercise movements during high-intensity interval training.
These validation datasets help demonstrate the model's ability to detect keypoints consistently, even for individuals positioned 2-4 meters from the camera.


## Categories of human pose detection:


1.2D Pose Estimation

2. 3D Pose Estimation

3. Rigid Pose Estimation (6D Pose Estimation)

4. Single Pose Estimation
   
5. Multi-Pose Estimation
# Human Pose detection with OpenCV Output:
OpenCV Output for Human Pose Detection
The output of a pose detection system, such as the one in OpenCV, typically includes:
Skeleton Visualization: A graphical skeleton is drawn over the human body using lines to connect the predicted keypoints.
Pose Confidence: Confidence scores that indicate how likely the model is that the detected pose is correct.


![image output](https://github.com/user-attachments/assets/b0a0bbaf-468d-4e1b-93ee-b1c9917c4da4)
