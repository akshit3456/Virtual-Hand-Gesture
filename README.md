****Virtual Hand Gesture Zoom****
**Overview**

This project implements a virtual hand gesture-based zooming system using OpenCV and cvzone's HandTrackingModule. It allows users to zoom in and out of an image on the screen by simply using their hands, eliminating the need for a physical touch interface.

**Features**

- Hand Detection: Uses OpenCV and cvzone's HandDetector to track both hands in real-time.

- Gesture-Based Zooming: Detects if both hands show the index and middle fingers up (indicating a zoom gesture).

- Dynamic Scaling: Measures the distance between both hands and adjusts the image size accordingly.

- Smooth Resizing: The image is resized dynamically based on the hand movements.

- Webcam Integration: Captures real-time video input to detect hands and gestures.

- Real-Time Interaction: Users can manipulate images interactively, making it a natural and intuitive experience.

**How It Works**

1. Hand Detection:

The program captures video from the webcam and detects hands using cvzone’s HandDetector.

2. Gesture Recognition:

If both hands show the index and middle fingers up, the system detects a zoom gesture.

3. Distance Calculation:

The distance between both hands' center points is measured.

4. Zooming Effect:

If the distance increases, the image enlarges.

If the distance decreases, the image shrinks.

The zoom is smooth and responsive to hand movements.
