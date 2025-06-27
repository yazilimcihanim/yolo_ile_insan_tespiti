import cv2
from ultralytics import YOLO

# YOLOv8 modelini yükle (pre-trained)
model = YOLO('yolov8n.pt')  # veya yolov8s.pt, yolov8m.pt gibi

# Webcam aç
cap = cv2.VideoCapture(0)

confidence_threshold = 0.5  # %50 güven eşiği

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO ile tespit
    results = model(frame)[0]

    # İnsan sınıfı 0'dır (COCO dataset'e göre)
    count = 0
    for box in results.boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        if cls == 0 and conf > confidence_threshold:  # İnsan sınıfı ve güven eşiği
            count += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Sayaç yazısı
    cv2.putText(frame, f'Insan Sayisi: {count}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)

    # Görüntüyü göster
    cv2.imshow("Webcam - Insan Tespiti", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
