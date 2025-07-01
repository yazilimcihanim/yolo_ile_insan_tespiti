🧠 YOLO ile Gerçek Zamanlı İnsan Tespiti
Bu proje, YOLOv8 (You Only Look Once) derin öğrenme modeli ile bir webcam görüntüsü üzerinde gerçek zamanlı insan tespiti yapar. 
Kullanıcı dostu bir arayüz (GUI) ile çalışır ve anlık olarak insan sayısını gösterir.

🚀 Özellikler
✅ Gerçek zamanlı tespit: Webcam görüntüsünde sadece insanları (person sınıfı) algılar.
🎯 Yüksek doğruluk: YOLOv8 modelinden gelen sonuçlara göre %50 üzeri güvenilirlikteki insanlar sayılır.
🖼️ Görsel arayüz: Tkinter tabanlı şık ve sade bir kullanıcı arayüzü.
🟢 Başlat / Durdur butonları ile kullanım kolaylığı.


🧰 Gereksinimler
Aşağıdaki kütüphanelerin kurulu olması gerekir:
>pip install ultralytics opencv-python pillow
ultralytics kütüphanesi, YOLOv8 modellerini çalıştırmak için gereklidir.

#Kullanımı

“Başlat” butonuna basarak webcam görüntüsünü başlatın.
Algılanan insanlar kare içine alınarak ekranda gösterilir.
Anlık insan sayısı üst kısımda görüntülenir.
“Durdur” butonuyla işlem durdurulabilir.


🧠 YOLOv8 Hakkında
>>Bu uygulama varsayılan olarak yolov8n.pt (nano model) kullanır. Daha yüksek doğruluk için aşağıdaki modellerle değiştirilebilir:

yolov8s.pt (small)
yolov8m.pt (medium)
yolov8l.pt (large)
yolov8x.pt (xlarge)

>>Model değiştirmek için şu satırı güncelleyin:

self.model = YOLO('yolov8n.pt')  # yolov8s.pt vb. ile değiştirebilirsiniz,


🧪 Geliştirici Notları

>Sadece cls == 0 (yani insan) sınıfı filtrelenmiştir.
>Tespit güven eşiği (confidence_threshold) %50 olarak ayarlanmıştır.
>Her karede insan sayısı yeniden hesaplanır ve ekrana yazılır.
>Uygulama, sistemdeki varsayılan kamerayı (cv2.VideoCapture(0)) kullanır.


