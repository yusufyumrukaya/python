import cv2
import os

video_path = "C:\\Proje\\Alex De Souza.mp4"

output_folder = "C:\\Proje"
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Hata: Video açılamadı! Dosya yolunu kontrol edin.")
    exit()

fps = int(cap.get(cv2.CAP_PROP_FPS))

frame_count = 0
screenshot_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break  
    
    if frame_count % fps == 0:
        screenshot_path = os.path.join(output_folder, f"screenshot_{screenshot_count}.jpg")
        cv2.imwrite(screenshot_path, frame)
        print(f"Kaydedildi: {screenshot_path}")
        screenshot_count += 1

    frame_count += 1
cap.release()
cv2.destroyAllWindows()
