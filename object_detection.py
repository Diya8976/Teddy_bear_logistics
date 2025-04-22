import cv2
import torch
import time

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Function to detect teddy bears from the CCTV footage
def detect_teddy_bear(frame):
    results = model(frame)  # Running detection on the frame
    return results

def capture_and_detect():
    # Open the webcam or CCTV footage (video file)
    cap = cv2.VideoCapture(0)  # For webcam, or replace 0 with video file path
    
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to read frame.")
            break

        # Check if the frame is 3D or 4D
        if len(frame.shape) == 3:  # Single image (height, width, channels)
            b, ch, h, w = 1, *frame.shape  # Set batch size to 1, then get the rest of the shape
        else:
            b, ch, h, w = frame.shape  # For batch of images

        # Run object detection on the frame
        results = detect_teddy_bear(frame)

        # Display the results (bounding boxes, labels, etc.)
        results.render()  # Renders the results on the frame
        
        # Show the frame with detected objects
        cv2.imshow('Teddy Bear Detection', frame)
        
        # Wait for 1 ms, and check if 'q' is pressed to exit
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Exiting...")
            break
        elif key == ord('s'):  # Optional: press 's' to save the current frame
            cv2.imwrite('teddy_bear_detected.jpg', frame)
            print("Frame saved as teddy_bear_detected.jpg")
        
        time.sleep(0.1)  # Adjust the sleep time based on frame rate

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    capture_and_detect()
