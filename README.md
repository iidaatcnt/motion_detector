# Motion Detector

A simple Python script that uses OpenCV to detect motion from a webcam feed.

## Features

-   Real-time motion detection using background subtraction.
-   Visualizes detected motion with bounding boxes.
-   Filters out minor noise for better accuracy.

---

## Getting Started (Recommended Method)

This method runs the script directly on your machine (macOS, Linux, Windows).

### Prerequisites

-   Python 3
-   pip (Python's package installer)

### 1. Clone the Repository

```bash
git clone <repository-url>
cd motion_detector
```

### 2. Install Dependencies

Install the necessary Python libraries using `requirements.txt`.

```bash
python3 -m pip install -r requirements.txt
```

### 3. Run the Script

Execute the script to start the motion detector.

```bash
python3 motion_detector.py
```

A window named "Motion Detector" will appear, showing your camera feed.

### 4. How to Stop

To quit the program, make sure the "Motion Detector" window is active by clicking on it, then press the **`q`** key.

---

## Docker Instructions (Advanced)

A `Dockerfile` is provided to run the application in a containerized environment.

**Note:** Accessing hardware like cameras and forwarding GUI applications from a Docker container is complex and platform-dependent. The local method above is recommended for simplicity.

### 1. Build the Image

```bash
docker build -t motion-detector .
```

### 2. Run the Container

Running the container requires extra configuration to connect to the host's camera and display.

**On Linux:**

You may be able to grant the container access to the camera device and X11 socket.

```bash
# Allow local connections to the X server
xhost +127.0.0.1

# Run the container
docker run --rm -it \
    --device=/dev/video0 \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    motion-detector
```

**On macOS (with XQuartz):**

1.  Install and run [XQuartz](https://www.xquartz.org/).
2.  In XQuartz settings, go to the "Security" tab and enable "Allow connections from network clients".
3.  In your Mac's terminal, allow local connections: `xhost +localhost`
4.  Run the container, pointing it to the XQuartz socket:

```bash
docker run --rm -it -e DISPLAY=host.docker.internal:0 motion-detector
```

Even with these steps, camera access from the container on macOS is not guaranteed due to Docker for Mac's architecture.

