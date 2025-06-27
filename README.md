# YOLOv8 ile Gerçek Zamanlı İnsan Tespiti

Bu proje, [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) modelini kullanarak bir web kamerası görüntüsü üzerinden gerçek zamanlı olarak insan tespiti yapar ve ekranda tespit edilen insan sayısını gösterir.

## Özellikler

- YOLOv8 (n, s, m vb.) destekli.
- COCO veri kümesine göre insan sınıfı (class 0) tespiti.
- Gerçek zamanlı görüntü işleme ve kutu çizimi.
- Tespit edilen insan sayısının ekranda gösterimi.
- `q` tuşuna basarak uygulamayı sonlandırabilirsiniz.

## Gereksinimler

Aşağıdaki kütüphanelerin kurulu olması gerekmektedir:


pip install ultralytics opencv-python
Ayrıca yolov8n.pt gibi önceden eğitilmiş bir YOLOv8 modeli kullanılmaktadır. Model otomatik olarak indirilecektir, ancak manuel olarak da indirip aynı dizine koyabilirsiniz.

## Kullanım

python insan_tespiti.py
Kod, bilgisayarınızın varsayılan kamerasını (cv2.VideoCapture(0)) kullanarak her karede insan tespiti yapar.

## Kod Açıklaması
model = YOLO('yolov8n.pt')
YOLOv8 modelini yükler (alternatif olarak yolov8s.pt, yolov8m.pt de kullanılabilir).

>cap = cv2.VideoCapture(0)
Web kamerasından görüntü alınır.

Her bir karede:

>YOLO ile nesne tespiti yapılır.

>Sadece "insan" sınıfı (class 0) ve güven skoru %50 üzerinde olan nesneler değerlendirilir.

>İnsanlar yeşil dikdörtgenle işaretlenir.

>Ekranın sol üstünde insan sayısı gösterilir.

