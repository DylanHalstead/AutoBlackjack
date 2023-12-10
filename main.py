import cv2
from ultralytics import YOLO
import numpy as np
from card import Card
from hand import Hand

model = YOLO('runs/detect/train/weights/best.pt')

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while capture.isOpened():
  success, frame = capture.read()
  if success:
    print("--------------------FRAME-------------------")
    results = model.track(frame, persist=True, verbose=False)
    annotated_frame = results[0].plot()
    result = results[0].cpu().boxes

    names = model.names
    detect_xyxy = result.xyxy.tolist() if result.xyxy is not None else []
    card_positions = [box for box in detect_xyxy]

    # Store Cards in a dictionairy with their bounding boxes
    class_bbox_dict = {}
    for c, bbox in zip(result.cls, detect_xyxy):
      class_id = int(c)
      class_name = names[class_id]
      if class_name not in class_bbox_dict:
        class_bbox_dict[class_name] = []
      
      x1, y1, x2, y2 = bbox
      top_left = {'x': x1, 'y': y1}
      bottom_right = {'x': x2, 'y': y2}
      card = Card(class_name, top_left, bottom_right)
      class_bbox_dict[class_name].append(card)

    # Proximity threshold used for grouping cards
    proximity_threshold = 400
    grouped_hands = []
    assigned = set()

    # For every type of card found, i.e. QD, KH, etc, 
    current_hand = Hand([])
    for class_name, positions in class_bbox_dict.items():
      if len(positions) > 0:
        for position in enumerate(positions):
          print(f"Located {position[1].card_string} at {position[1]}")
          current_hand.add_card(position[1])
        grouped_hands.append(current_hand)

    # temp static dealer
    dealer_hand = Hand([Card('7D', 0, 0)])

    for hand in grouped_hands:
      # draw a bounding box around the grouped cards
      cards = hand.cards
      x_coords = [card.top_left['x'] for card in cards]
      y_coords = [card.top_left['y'] for card in cards]

      x_min = min(x_coords)
      y_min = min(y_coords)
      x_max = max([card.bottom_right['x'] for card in cards])
      y_max = max([card.bottom_right['y'] for card in cards])

      cv2.rectangle(annotated_frame, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)
      cv2.putText(annotated_frame, hand.calculate_best_action(dealer_hand.cards[0]), (int(x_min), int(y_min)-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Cards', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()