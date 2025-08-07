# Motion Detector Specifications

## 1. Overview

This program detects motion by comparing the live video feed from a camera to an initial static background frame. Detected motion is highlighted with a green bounding box in real-time.

## 2. Features

-   **Real-time Motion Detection**: Captures video from the default camera and processes it frame by frame.
-   **Background Subtraction**: Uses the first captured frame as a static background reference.
-   **Noise Reduction**: Applies a Gaussian blur to both the background and current frames to reduce noise and improve detection accuracy.
-   **Difference Highlighting**: Calculates the absolute difference between the background and the current frame to identify areas with changes.
-   **Thresholding**: Converts the difference image into a binary (black and white) image, making it easier to isolate areas of significant motion.
-   **Contour Detection**: Identifies the outlines of the motion areas.
-   **Visual Feedback**: Draws a green rectangle around detected objects in the output window.
-   **Noise Filtering**: Ignores very small contours to avoid false positives from minor noise.

## 3. How It Works (Algorithm)

1.  **Initialization**: The program initializes a connection to the default camera (index 0).
2.  **Background Capture**: It captures the first valid frame, converts it to grayscale, applies a Gaussian blur, and stores it as the reference background (`bg_gray`).
3.  **Main Loop**: The program enters a loop to process the video feed continuously.
    a.  It reads a new frame from the camera.
    b.  The new frame is also converted to grayscale and blurred (`gray`).
    c.  It computes the absolute difference between `bg_gray` and `gray`, resulting in a `frame_delta`.
    d.  A binary threshold is applied to `frame_delta`. Pixels with a difference value greater than 25 are turned to white (255), and the rest to black (0).
    e.  It finds the contours (outlines) of the white regions in the thresholded image.
    f.  For each contour found, it checks if its area is above a minimum size (500 pixels) to filter out noise.
    g.  If a contour is large enough, a green bounding box is drawn around it on the original color frame.
4.  **Display**: The final frame with the bounding boxes is displayed in a window titled "Motion Detector".
5.  **Termination**: The loop continues until the user presses the 'q' key while the display window is active. Upon termination, the camera is released and all windows are closed.

## 4. User Interaction

-   To **start** the program, execute the script.
-   To **stop** the program, click on the "Motion Detector" window to ensure it is in focus, then press the `q` key on the keyboard.
