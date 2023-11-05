import cv2
import numpy as np

# Load the model
net = cv2.dnn.readNetFromCaffe('C:/Users/danie/PycharmProjects/pythonProject2/Edventure/opencv/deploy.prototxt', 'C:/Users/danie/PycharmProjects/pythonProject2/Edventure/opencv/mobilenet_iter_73000.caffemodel')

# Initialize video feed from webcam
cap = cv2.VideoCapture(0)

# Define the class labels MobileNet SSD was trained on
classNames = { 0: 'background',
    1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
    5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
    10: 'cow', 11: 'diningtable', 12: 'dog', 13: 'horse',
    14: 'motorbike', 15: 'person', 16: 'pottedplant',
    17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tvmonitor' }

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Prepare the frame to be fed to the network
    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)

    # Set the new input value for the network
    net.setInput(blob)

    # Run forward pass and get the output
    detections = net.forward()

    # Loop over the detections
    for i in range(detections.shape[2]):
        # Get the confidence of the prediction
        confidence = detections[0, 0, i, 2]

        # Filter out weak detections
        if confidence > 0.2:
            # Get the class label
            class_id = int(detections[0, 0, i, 1])
            class_name = classNames[class_id]

            # Get the bounding box coordinates
            box_x = detections[0, 0, i, 3] * frame.shape[1]
            box_y = detections[0, 0, i, 4] * frame.shape[0]
            box_width = detections[0, 0, i, 5] * frame.shape[1]
            box_height = detections[0, 0, i, 6] * frame.shape[0]

            # Draw the bounding box and label on the image
            cv2.rectangle(frame, (int(box_x), int(box_y)), (int(box_width), int(box_height)), (23, 230, 210), thickness=2)
            cv2.putText(frame, class_name, (int(box_x), int(box_y) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (23, 230, 210), 2)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Break the loop with the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture once everything is done
cap.release()
cv2.destroyAllWindows()
