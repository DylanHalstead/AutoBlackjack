import cv2
from ultralytics import YOLO
import numpy as np

model = YOLO('runs/detect/train7/weights/best.pt')

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while capture.isOpened():
  success, frame = capture.read()
  if success:
    results = model.track(frame, persist=True, verbose=False)
    annotated_frame = results[0].plot()
    result = results[0].cpu().boxes
    detect_xyxy = result.xyxy.tolist() if result.xyxy is not None else []

    card_positions = [box for box in detect_xyxy]

    proximity_threshold = 400
    grouped_hands = []
    assigned = set()

    for i, card1 in enumerate(card_positions):
      if i not in assigned:
        hand = [card1]
        assigned.add(i)

        for j, card2 in enumerate(card_positions[i + 1:]):
          if np.linalg.norm(np.array(card1)[:2] - np.array(card2)[:2]) < proximity_threshold:
            hand.append(card2)
            assigned.add(j)

        grouped_hands.append(hand)

    # Drawing bounding boxes around grouped cards
    for hand in grouped_hands:
      if len(hand) > 1:
        x_coords = [card[0] for card in hand]
        y_coords = [card[1] for card in hand]

        x_min = min(x_coords)
        y_min = min(y_coords)
        x_max = max(x_coords)
        y_max = max(y_coords)
        # print("Card: " + str(hand[0]))

        cv2.rectangle(annotated_frame, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)

    cv2.imshow('Cards', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()