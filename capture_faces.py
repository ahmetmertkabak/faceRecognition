import cv2
import os
import time

# Kamera başlatma
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Kamera açılamadı!")
    exit()

# Çözünürlük ayarlama
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Yüz tespiti için cascade sınıflandırıcı
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Klasör oluştur
if not os.path.exists('dataset'):
    os.makedirs('dataset')

# Kullanıcı adını al
name = input("Lütfen adınızı girin: ")
user_path = os.path.join('dataset', name)
if not os.path.exists(user_path):
    os.makedirs(user_path)

count = 0
total_images = 30
last_capture_time = time.time()

print("Yüz fotoğrafları çekiliyor. Kameraya bakın ve yüzünüzü farklı açılarla döndürün...")
print(f"Toplam {total_images} fotoğraf çekilecek.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Görüntü alınamıyor!")
        break

    # Görüntüyü ayna gibi çevir
    frame = cv2.flip(frame, 1)
    
    # Yüz Tespiti
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    current_time = time.time()
    
    for (x, y, w, h) in faces:
        # Yüz çerçevesi çiz
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Her 0.5 saniyede bir fotoğraf çek
        if current_time - last_capture_time >= 0.5 and count < total_images:
            img_path = os.path.join(user_path, f'{name}_{count}.jpg')
            face_img = frame[y:y+h, x:x+w]
            
            # Fotoğrafı kaydet
            if face_img.size > 0:
                cv2.imwrite(img_path, face_img)
                print(f"Fotoğraf {count+1}/{total_images} kaydedildi!")
                count += 1
                last_capture_time = current_time
    
    # Kalan fotoğraf sayısını göster
    cv2.putText(frame, f"Kalan: {total_images-count}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Görüntüyü göster
    cv2.imshow('Yuz Tanima Sistemi', frame)
    
    # Tüm fotoğraflar çekildiyse veya q tuşuna basıldıysa çık
    if count >= total_images:
        print("Tüm fotoğraflar başarıyla kaydedildi!")
        break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Temizlik
cap.release()
cv2.destroyAllWindows()

print(f"İşlem tamamlandı. {count} fotoğraf {user_path} klasörüne kaydedildi.")
