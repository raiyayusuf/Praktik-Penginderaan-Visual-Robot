# Contoh untuk menunjukkan efek erode()
#    untuk mendapatkan tepi objek

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

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
erosi = cv2.erode(citra, kernel)
tepi = citra - erosi

hasil = np.hstack((citra, tepi))

# Tampilkan citra asal dan hasilnya
cv2.imshow('Hasil Erosi untuk Memisahkan Daun', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()