from ultralytics import YOLO
import cv2

# Load the YOLOv8 pretrained model
model = YOLO('yolov8n.pt')  # You can also use 'yolov8s.pt', 'yolov8m.pt', etc.

# Open the webcam (0) or use a CCTV feed path
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv8 inference
    results = model(frame)

    # Draw results on frame
    annotated_frame = results[0].plot()

    # Display the frame
    cv2.imshow('Teddy Bear Detection', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
