# Contoh untuk menunjukkan efek dilate()
# dengan dua ukuran kernel yang berbeda

import cv2
import numpy as np

# Menggunakan path yang benar
citra = cv2.imread('python/jobsheet8/img/daun.jpg', 0)

scale_percent = 50  # persentase dari ukuran asli
width = int(citra.shape[1] * scale_percent / 100)
height = int(citra.shape[0] * scale_percent / 100)
dim = (width, height)
citra = cv2.resize(citra, dim, interpolation=cv2.INTER_AREA)

# Konversi ke biner
ambang, biner = cv2.threshold(citra, 128, 255, cv2.THRESH_BINARY)

# Membuat kernel dengan ukuran berbeda
kernelA = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))
kernelB = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

# Operasi dilasi dengan kernel berbeda
dilasiA = cv2.dilate(biner, kernelA)
dilasiB = cv2.dilate(biner, kernelB)

# Mengatur tampilan hasil
baris1 = np.hstack((citra, biner))
baris2 = np.hstack((dilasiA, dilasiB))
hasil = np.vstack((baris1, baris2))

# Tampilkan citra asal dan hasilnya
cv2.imshow('Perbandingan Dilasi dengan Kernel Berbeda', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()