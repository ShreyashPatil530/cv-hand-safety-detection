import cv2
import numpy as np
from utils.hand_detection import detect_hand

# Virtual boundary (rectangle)
BOUNDARY_X1, BOUNDARY_Y1 = 200, 100
BOUNDARY_X2, BOUNDARY_Y2 = 450, 350

# Distance thresholds
SAFE_DIST = 200       # Far away
WARNING_DIST = 120    # Medium distance
DANGER_DIST = 60      # Very close / inside


def compute_distance(px, py):
    """Distance from the hand to the RECTANGLE center."""
    rect_cx = (BOUNDARY_X1 + BOUNDARY_X2) // 2
    rect_cy = (BOUNDARY_Y1 + BOUNDARY_Y2) // 2
    return int(np.sqrt((px - rect_cx) ** 2 + (py - rect_cy) ** 2))


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    hand_center, mask = detect_hand(frame)

    # Draw boundary
    cv2.rectangle(frame, (BOUNDARY_X1, BOUNDARY_Y1),
                  (BOUNDARY_X2, BOUNDARY_Y2), (255, 255, 255), 2)

    state_text = "SAFE"
    color = (0, 255, 0)

    if hand_center is not None:
        hx, hy = hand_center
        cv2.circle(frame, (hx, hy), 10, (255, 0, 0), -1)

        distance = compute_distance(hx, hy)

        # SAFE = far
        if distance > SAFE_DIST:
            state_text = "SAFE"
            color = (0, 255, 0)

        # WARNING = middle range
        elif WARNING_DIST < distance <= SAFE_DIST:
            state_text = "WARNING"
            color = (0, 255, 255)

        # DANGER = close OR inside the box
        if (
            BOUNDARY_X1 < hx < BOUNDARY_X2 and
            BOUNDARY_Y1 < hy < BOUNDARY_Y2
        ) or distance <= DANGER_DIST:
            state_text = "DANGER"
            color = (0, 0, 255)
            cv2.putText(frame, "DANGER DANGER", (120, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    # Show text
    cv2.putText(frame, state_text, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.3, color, 3)

    cv2.imshow("Hand Tracking POC", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
