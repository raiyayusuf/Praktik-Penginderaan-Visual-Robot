# Contoh untuk menunjukkan efek erode()
#    untuk memisahkan sejumlah daun
#    yang bersinggungan

import cv2
import numpy as np

# Menggunakan path yang benar
citra = cv2.imread('python/jobsheet8/img/daun.jpg', 0)

# Resize gambar - tentukan lebar baru atau skala
scale_percent = 50  # persentase dari ukuran asli
width = int(citra.shape[1] * scale_percent / 100)
height = int(citra.shape[0] * scale_percent / 100)
dim = (width, height)

citra = cv2.resize(citra, dim, interpolation=cv2.INTER_AREA)

# Konversi ke biner
ambang, biner = cv2.threshold(citra, 30, 255, cv2.THRESH_BINARY)

# Membuat kernel dengan ukuran berbeda
kernelA = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))
kernelB = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 6))

# Operasi erosi dengan kernel berbeda
erosiA = cv2.erode(biner, kernelA)
erosiB = cv2.erode(biner, kernelB)

# Mengatur tampilan hasil
baris1 = np.hstack((citra, biner))
baris2 = np.hstack((erosiA, erosiB))
hasil = np.vstack((baris1, baris2))

# Tampilkan citra asal dan hasilnya
cv2.imshow('Hasil Erosi untuk Memisahkan Daun', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()