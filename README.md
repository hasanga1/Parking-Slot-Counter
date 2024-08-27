# Parking Slot Detection System

This project demonstrates a computer vision application for detecting available parking slots in a parking lot. The system uses OpenCV to process video footage and identify whether a parking slot is occupied or available.

# Screenshots

https://github.com/user-attachments/assets/0ffe6621-0969-47e0-82f6-42abcc779282

## Features

- **Real-time Parking Slot Detection**: Processes video footage to detect available parking slots.
- **Interactive Slot Definition**: Allows users to manually define parking slot positions in an image using mouse clicks.
- **Visual Feedback**: Displays the status of each parking slot in the video with color-coded rectangles (green for available, red for occupied).

## Prerequisites

To run this project, you need the following dependencies:

- Python 3.x
- OpenCV (`cv2`)
- Numpy (`numpy`)
- cvzone

You can install the required libraries using pip:

```bash
pip install opencv-python numpy cvzone
```


# How to Run

- Define Parking Slots
    
    First, you need to define the parking slots using the slotdefine.py script. This script allows you to manually add or remove parking slots by clicking on the parking lot image.

    ```bash
    python slotDefine.py
    ```
    - Left Mouse Button: Add a new parking slot at the clicked position.
    - Right Mouse Button: Remove a parking slot if clicked inside it.
    - Press 'q': Save the defined slots and exit the application.

- Detect Parking Slot Availability
    
    Once you have defined the parking slots, you can run the app.py script to start detecting available parking slots in real-time from a video feed.

    ```bash
    python app.py
    ```

    This script uses a video file named carPark.mp4. Ensure the video file is in the same directory as the script.

- Results
    
    The application will display the video feed with colored rectangles indicating the status of each parking slot:
    - Green: Available
    - Red: Occupied
    - The number of available parking slots is displayed on the top-left corner of the video.

# Files

- slotdefine.py: Script to define and save parking slot positions in an image.
- app.py: Main application script to process video feed and detect parking slot availability.
- carPark.png: Image of the parking lot used for defining slots.
- carPark.mp4: Video of the parking lot used for real-time slot detection.
- slotPos: File that stores the defined parking slot positions.

# Acknowledgments

- OpenCV for providing the computer vision tools to implement this project.
- cvzone for easy-to-use functions for computer vision and video processing.

# Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements.
