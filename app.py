import os
import cv2
# from roboflow import Roboflow
from dotenv import load_dotenv
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated
#Import dependencies
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from tensorflow.keras.layers import Input, Conv2D, Dense, Flatten, Dropout, MaxPool2D
from tensorflow.keras.utils import to_categorical, plot_model
from tensorflow.keras.models import Model
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array

load_dotenv()

# rf = Roboflow(api_key=os.getenv('API_KEY', ''))
# project = rf.workspace().project("playing-cards-ow27d")
# model = project.version(4).model

model = YOLO('runs/detect/train7/weights/best.pt')

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while capture.isOpened():
  success, frame = capture.read()
  if success:
    cv2.imwrite('temp.jpg', frame)
    predictions = model.predict('temp.jpg')

    for r in predictions:
        
        annotator = Annotator(frame)
        
        boxes = r.boxes
        for box in boxes:
            
            b = box.xyxy[0]  # get box coordinates in (top, left, bottom, right) format
            c = box.cls
            annotator.box_label(b, model.names[int(c)])
          
    frame = annotator.result()  
    cv2.imshow('YOLO V8 Detection', frame)     
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  else:
      break
if os.path.exists('temp.jpg'):
  os.remove('temp.jpg')
capture.release()
cv2.destroyAllWindows()
