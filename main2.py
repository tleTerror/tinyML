import cv2

# Open the default camera (0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Camera", frame)

    # Press spacebar to capture the image
    if cv2.waitKey(1) & 0xFF == ord(' '):  
        cv2.imwrite("captured_image.jpg", frame)
        print("Image captured and saved as captured_image.jpg")
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
