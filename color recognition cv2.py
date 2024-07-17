import cv2
import numpy as np

# Define color ranges in HSV
color_ranges = {
    "red": ([0, 100, 100], [10, 255, 255]),
    "green": ([40, 40, 40], [80, 255, 255]),
    "blue": ([100, 100, 100], [140, 255, 255]),
    "white": ([0, 0, 200], [180, 30, 255]),  
    "brown": ([10, 60, 60], [30, 255, 255]),  
    "black": ([0, 0, 0], [180, 255, 30]), 
}

def process_frame(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    detected_color = None

    for color_name, (lower, upper) in color_ranges.items():
        lower_bound = np.array(lower)
        upper_bound = np.array(upper)

 
        mask = cv2.inRange(hsv, lower_bound, upper_bound)


        if cv2.countNonZero(mask) > 0:
            detected_color = color_name
            break

    if detected_color:
        cv2.putText(frame, f"Detected Color: {detected_color}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    return frame

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    processed_frame = process_frame(frame)

    cv2.imshow('Color Recognition', processed_frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
