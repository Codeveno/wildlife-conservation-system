import cv2
import torch
from ultralytics import YOLO
import cvzone
import math
from playsound import playsound
from test import send_alert
import os
from PIL import Image
import time
import datetime

# specify the path of the audio file
audio_file_path = 'police-operation-siren-144229.mp3'

initial = 0

# Load models
model = torch.hub.load('ultralytics/yolov5', 'custom', 'C:/Users/dkb03/Desktop/Wildlife-Conservation/ml_model/md_v5a.0.0.pt')
model_ppe = YOLO("C:/Users/dkb03/Desktop/Wildlife-Conservation/ml_model/best.pt")
model_ani = YOLO("C:/Users/dkb03/Desktop/Wildlife-Conservation/ml_model/Re_best.pt")

def generate_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone', 'Safety Vest', 'machinery', 'vehicle']
    classAniNames = ["Person", "Elephant", "Leopard", "Arctic_Fox", "Chimpanzee", "Jaguar", "Lion", "Orangutan", "Panda", "Panther", "Rhino", "Cheetah"]

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        result = model(frame)
        cropped_img = []
        cropped_animal = []

        for box in result.xyxy[0]:
            x1, y1, x2, y2, confidence, label_idx = box.tolist()
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            class_label = model.names[int(label_idx)]

            if class_label == 'animal':
                color = (0, 255, 0)
                thickness = 2
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, thickness)
                label = f"{class_label}: {confidence:.2f}"
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness)
                cropped_animal.append(frame[y1:y2, x1:x2])
            else:
                cropped_img.append(frame[y1:y2, x1:x2])

        alert_required = False
        for box_img in cropped_img:
            results = model_ppe(box_img)
            unique_labels = {}

            for box in results[0].boxes:
                cls = int(box.cls[0])
                currentClass = classNames[cls]
                conf = math.ceil((box.conf[0] * 100)) / 100
                label, confidence = currentClass, conf

                if currentClass in ['Mask', 'NO-Mask', 'Safety Cone', 'machinery', 'vehicle']:
                    continue

                if label not in unique_labels or confidence > math.ceil((unique_labels[label].conf[0] * 100)) / 100:
                    unique_labels[label] = box

            for box in unique_labels.values():
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                myColor = (127, 255, 0)
                currentClass = classNames[int(box.cls[0])]

                if currentClass in ['NO-Hardhat', 'NO-Safety Vest']:
                    myColor = (0, 0, 255)
                    alert_required = True
                    cvzone.putTextRect(box_img, f'{currentClass} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1, colorB=myColor, colorT=(255, 255, 255), colorR=(0, 0, 255), offset=5)
                    cv2.rectangle(box_img, (x1, y1), (x2, y2), myColor, 3)

        prev = ''
        for box_img in cropped_animal:
            results = model_ani(box_img)
            for box in results[0].boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                currentClass = classAniNames[int(box.cls[0])]
                myColor = (127, 255, 0)

                if prev == '':
                    prev = currentClass
                elif prev != currentClass:
                    alert_required = True
                    cvzone.putTextRect(box_img, f'{currentClass} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1, colorB=myColor, colorT=(255, 255, 255), colorR=(0, 0, 255), offset=5)
                    cv2.rectangle(box_img, (x1, y1), (x2, y2), myColor, 3)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

        global initial
        if alert_required and (initial == 0 or (datetime.datetime.now() - initial).total_seconds() > 30):
            cv2.imwrite("output.jpg", frame)
            send_alert("output.jpg")
            initial = datetime.datetime.now()
            os.remove('C:/Users/dkb03/Desktop/Wildlife-Conservation/output.jpg')

    cap.release()
    cv2.destroyAllWindows()