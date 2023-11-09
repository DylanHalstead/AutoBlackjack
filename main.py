import os
import cv2
from roboflow import Roboflow
from dotenv import load_dotenv
load_dotenv()

rf = Roboflow(api_key=os.getenv('API_KEY', ''))
project = rf.workspace().project("playing-cards-ow27d")
model = project.version(4).model

capture = cv2.VideoCapture(0)
while capture.isOpened():
  success, frame = capture.read()
  if success:
    cv2.imwrite('temp.jpg', frame)
    predictions = model.predict('temp.jpg')

    for bounding_box in predictions:
      x0 = bounding_box['x']-bounding_box['width']/2
      y0 = bounding_box['y']-bounding_box['height']/2
      x1 = bounding_box['x']+bounding_box['width']/2
      y1 = bounding_box['y']+bounding_box['height']/2
      class_name = bounding_box['class']
      confidence_score = bounding_box['confidence']
  
      detection_results = bounding_box
      class_and_confidence = (class_name, confidence_score)
      cv2.rectangle(frame, (int(x0), int(y0)), (int(x1), int(y1)), (0, 0, 255), 2)
      cv2.putText(frame, str(class_and_confidence), (int(x0), int(y0)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
      break
  else:
      break
if os.path.exists('temp.jpg'):
  os.remove('temp.jpg')
capture.release()
cv2.destroyAllWindows()