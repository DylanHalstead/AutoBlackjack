import cv2
from ultralytics import YOLO

model = YOLO('yolov8s.pt')
capture = cv2.VideoCapture(0)

while capture.isOpened():
  success, frame = capture.read()
  if success:
    results = model.track(frame, persist=True)
    annotated_frame = results[0].plot()
    cv2.imshow("YOLOv8 Tracking", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
      break
  else:
      break
  
capture.release()
cv2.destroyAllWindows()