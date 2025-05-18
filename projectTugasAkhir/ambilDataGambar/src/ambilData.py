import cv2
import os

# Path folder untuk menyimpan gambar
folder_path = r'projectTugasAkhir\ambilDataGambar\hasilGambar'
os.makedirs(folder_path, exist_ok=True)

# Buka kamera (0 = default camera)
cap = cv2.VideoCapture(0)

# Hitung jumlah file yang sudah ada dengan nama brambanggoreng
index = 1
while os.path.exists(os.path.join(folder_path, f'brambanggoreng{index}.png')):
    index += 1

print("Tekan 'm' untuk ambil gambar, 'q' untuk keluar.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Gagal mengambil frame dari kamera.")
        break

    # Tampilkan video
    cv2.imshow('Camera', frame)

    # Ambil input keyboard
    key = cv2.waitKey(1) & 0xFF

    if key == ord('m'):
        filename = f'brambanggoreng{index}.png'
        filepath = os.path.join(folder_path, filename)
        cv2.imwrite(filepath, frame)
        print(f"Gambar disimpan: {filepath}")
        index += 1

    elif key == ord('q'):
        print("Keluar dari kamera.")
        break

# Bersihkan
cap.release()
cv2.destroyAllWindows()
