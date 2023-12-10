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
      # bbox_dict = {'top_left': top_left, 'bottom_right': bottom_right}
      # class_bbox_dict[class_name].append(bbox_dict)
      card = Card(class_name, top_left, bottom_right)
      class_bbox_dict[class_name].append(card)

    # Proximity threshold used for grouping cards
    # proximity_threshold = 400
    empty_hand = []
    # assigned = set()
    dealer = None


    print("    LOOP: For class_name, positions in class_bbox_dict.items():")
    # For every type of card found, i.e. QD, KH, etc, 
    current_hand = Hand(empty_hand)
    for class_name, positions in class_bbox_dict.items():
    #   print(f"Class Name: {class_name}")
      if len(positions) > 0:
        for position in enumerate(positions):
            # If the card is higher than Dealer, assign it to Dealer and add dealer back to hand
            print(f"Located {position[1]}")
            current_hand.add_card(position[1])
            if dealer is not None:
                if position[1].top_left['y'] < dealer.top_left['y']:
                    current_hand.add_card(dealer)
                    current_hand.remove_card(position[1])
                    dealer = position[1]
                # Ensure the Dealer card is not in the hand if it identifies both corners of Dealer
                for card_in_hand in current_hand.cards:
                    if card_in_hand.card_string == dealer.card_string:
                        current_hand.remove_card(card_in_hand)
            else:
              current_hand.remove_card(position[1])
              dealer = position[1]

    # Drawing bounding boxes around grouped cards
    # print("       LOOP: For for hand in grouped_hands:")
    if dealer is not None:
      print(f"Dealer: {dealer}")
      if len(current_hand.cards) > 0:
          # print(f"Current Hand: {current_hand}")
          # print(f"Current Hand Cards: {current_hand.cards}")
          # print(f"Current Hand Sum: {current_hand.get_sum()}")
          # Hard coding dealer hand for now as a 7
          print(f"Best Action: {current_hand.calculate_best_action(dealer)}")
      else: 
          print("No hand found")
    else:
       print("No cards found")
      
    # for hand in grouped_hands:
    #   cards = hand.cards
    #   print(f"Hand.Cards: {cards}")
    #   if len(cards) > 1:
    #     print("Grouped cards:")
    #     print([card.value_string for card in cards])
    #     x_coords = [card.top_left['x'] for card in cards]
    #     y_coords = [card.top_left['y'] for card in cards]

    #     x_min = min(x_coords)
    #     y_min = min(y_coords)
    #     x_max = max([card.bottom_right['x'] for card in cards])
    #     y_max = max([card.bottom_right['y'] for card in cards])

    #     cv2.rectangle(annotated_frame, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)

    cv2.imshow('Cards', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()