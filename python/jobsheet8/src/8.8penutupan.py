# Contoh penggunaan transformasi penutupan
# untuk menutup lubang pada daun

import cv2
import numpy as np

# Menggunakan path yang sesuai
citra = cv2.imread('python/jobsheet8/img/daun.jpg', 0)  # Pastikan path benar
scale_percent = 50  # persentase dari ukuran asli
width = int(citra.shape[1] * scale_percent / 100)
height = int(citra.shape[0] * scale_percent / 100)
dim = (width, height)
citra = cv2.resize(citra, dim, interpolation=cv2.INTER_AREA)

# Konversi ke biner
ambang, citra_biner = cv2.threshold(citra, 160, 255, cv2.THRESH_BINARY)

# Balik warna (invert) untuk memproses lubang sebagai objek
citra_invert = 255 - citra_biner

# Membuat kernel rectangular
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

# Operasi penutupan (morphological closing)
penutupan = cv2.morphologyEx(citra_invert, cv2.MORPH_CLOSE, kernel)

# Mengembalikan ke warna asli setelah diproses
penutupan = 255 - penutupan

# Gabungkan gambar untuk perbandingan
hasil = np.hstack((citra_biner, penutupan))

# Tampilkan citra asal dan hasilnya
cv2.imshow('Hasil Penutupan Morfologi untuk Menutup Lubang', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()