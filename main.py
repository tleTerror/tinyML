import cv2
import numpy as np
import tensorflow.lite as tflite

# Load TensorFlow Lite model
interpreter = tflite.Interpreter(model_path="mobilenet_v1_1.0_224_quant.tflite")
interpreter.allocate_tensors()

# Load class labels from file
with open("labels.txt", "r") as f:
    labels = f.read().splitlines()



# Get input/output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
input_shape = input_details[0]['shape']

# Print model input type
print("Model expects dtype:", input_details[0]['dtype'])

# Open webcam
cap = cv2.VideoCapture(0)

cv2.namedWindow("Gesture Recognition", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Gesture Recognition", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while cap.isOpened():

    ret, frame = cap.read()
    if not ret:
        break

    # Resize image to model's expected size
    img_resized = cv2.resize(frame, (input_shape[1], input_shape[2]))

    # Convert image to correct dtype
    if input_details[0]['dtype'] == np.uint8:
        img_resized = np.expand_dims(img_resized, axis=0).astype(np.uint8)  # Keep as UINT8
    else:
        img_resized = np.expand_dims(img_resized, axis=0).astype(np.float32) / 255.0  # Convert to FLOAT32

    # Run inference
    interpreter.set_tensor(input_details[0]['index'], img_resized)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Get predicted label
    # Get predicted class index
    prediction = np.argmax(output_data)
    label = f"Prediction: {labels[prediction]}"  # Update with class labels

    # Display result
    cv2.putText(frame, "press q to quit", (frame.shape[1] - 200, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.putText(frame, label, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Gesture Recognition", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
