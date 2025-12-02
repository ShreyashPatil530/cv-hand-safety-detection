import cv2
import numpy as np

def detect_hand(frame):
    """
    Detect hand using color segmentation + contour detection.
    Returns: center_point (x, y) or None
    """

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Skin color range (tuned for typical lighting)
    lower = np.array([0, 30, 60], dtype=np.uint8)
    upper = np.array([20, 150, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower, upper)

    # Clean noise
    mask = cv2.GaussianBlur(mask, (7, 7), 0)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        return None, mask

    # Largest contour → assumes it's the hand
    cnt = max(contours, key=cv2.contourArea)

    if cv2.contourArea(cnt) < 1000:  # too small (noise)
        return None, mask

    # Hand center
    M = cv2.moments(cnt)
    if M["m00"] == 0:
        return None, mask

    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])

    return (cx, cy), mask
