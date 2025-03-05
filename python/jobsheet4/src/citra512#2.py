import cv2
import numpy as np

# Buat citra berwarna hitam
citra = np.zeros((512, 512, 3), np.uint8)

# Baca gambar
spaceman = cv2.imread(r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\spaceman.png', -1)

if spaceman is None:
    print("Error: Gambar tidak ditemukan atau tidak dapat dibaca.")
else:
    # Potong gambar agar sesuai dengan ukuran citra hitam (512x512)
    jumBaris = min(spaceman.shape[0], 512)
    jumKolom = min(spaceman.shape[1], 512)
    spaceman = spaceman[0:jumBaris, 0:jumKolom, :]

    # Masukkan gambar ke dalam citra hitam
    citra[0:jumBaris, 0:jumKolom, :] = spaceman[:, :, 0:3]

    # Tampilkan hasil
    cv2.imshow('Hasil', citra)
    cv2.waitKey(0)
    cv2.destroyAllWindows()