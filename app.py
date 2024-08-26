import cv2
import pickle
import cvzone
import numpy as np

# Path to video file
videoDir = 'carPark.mp4'

# Initialize video capture object
cap = cv2.VideoCapture(videoDir)

# Parking slot dimensions
parkingSlotWidth = 100
parkingSlotHeight = 40

# Function to check parking slots and visualize status
def checkSlots(preprocessedFrame, originalFrame):
    spaceCounter = 0

    # Iterate through each parking slot position
    for pos in posList:
        # Crop the slot area from the preprocessed frame
        x, y = pos
        crop = preprocessedFrame[y:y + parkingSlotHeight, x:x + parkingSlotWidth]
        
        # Count non-zero pixels in the cropped slot
        countPixels = cv2.countNonZero(crop)
        
        # Display the pixel count on the original frame
        cvzone.putTextRect(originalFrame, str(countPixels), (x, y + parkingSlotHeight - 5), scale=1, thickness=1, offset=0)

        # Determine the color for the rectangle (Green for available, Red for occupied)
        if countPixels < 700:
            color = (0, 255, 0)
            spaceCounter += 1
        else:
            color = (0, 0, 255)

        # Draw a rectangle around the parking slot
        cv2.rectangle(originalFrame, pos, (pos[0] + parkingSlotWidth, pos[1] + parkingSlotHeight), color=color, thickness=2)

    # Display the count of available slots on the frame
    cvzone.putTextRect(originalFrame, f'Available: {spaceCounter}', (50, 50), scale=2, thickness=3, offset=10)

# Function to preprocess the frame for slot detection
def preprocessing(frame):
    # Convert frame to grayscale
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurFrame = cv2.GaussianBlur(grayFrame, (3, 3), 1)
    
    # Apply adaptive thresholding to detect edges
    thresholdFrame = cv2.adaptiveThreshold(blurFrame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    
    # Apply median blur to smooth the frame
    medianFrame = cv2.medianBlur(thresholdFrame, 5)
    
    # Dilate the frame to fill in gaps
    kernel = np.ones((3, 3), np.uint8)
    dilatedFrame = cv2.dilate(medianFrame, kernel, iterations=1)
    
    return dilatedFrame

# Load the parking slot positions from a file
with open('slotPos', 'rb') as f:
    posList = pickle.load(f)

while True:
    # Loop the video if it reaches the end
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    # Read a frame from the video
    success, frame = cap.read()
    if not success:
        break

    # Preprocess the frame
    preprocessedFrame = preprocessing(frame)

    # Check each slot and visualize the status
    checkSlots(preprocessedFrame, frame)

    # Display the original frame with annotations
    cv2.imshow("Parking Slot Detection", frame)
    
    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
cap.release()
cv2.destroyAllWindows()
