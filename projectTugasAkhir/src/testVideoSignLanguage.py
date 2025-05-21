from ultralytics import YOLO
import cv2 
import math

model = YOLO(r"projectTugasAkhir\model\signLanguageV8version2-100x640-18mei2025.pt")
classNames = model.names

LIGHT_BLUE = (255, 200, 100)  
WHITE = (255, 255, 255)      
RED = (0, 0, 255) 

cap = cv2.VideoCapture(0) 

if not cap.isOpened():
    raise IOError("Cannot open camera")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    results = model(frame, verbose=False)  
    
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = math.ceil(box.conf[0].item() * 100) / 100
            cls_id = int(box.cls[0].item())

            # print(f"Detected: ID={cls_id}, Name={classNames[cls_id]}, Conf={conf}")
            
            label = f"{classNames[cls_id]} {conf:.2f}"

            cv2.rectangle(frame, (x1, y1), (x2, y2), LIGHT_BLUE, 2)

            (text_width, text_height), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
            cv2.rectangle(frame, (x1, y1 - text_height - 10), (x1 + text_width, y1), LIGHT_BLUE, -1)
            
            cv2.putText(frame, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, WHITE, 2)
    
    cv2.imshow('Sign Language Detection - Camera', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()