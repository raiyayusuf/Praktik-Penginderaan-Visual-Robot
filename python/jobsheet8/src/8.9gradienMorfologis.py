# Transformasi Gradien Morfologis
import cv2
import numpy as np

# Load gambar
citra = cv2.imread('python/jobsheet8/img/daun.jpg', 0)  # Membaca gambar dalam mode grayscale
scale_percent = 50  # persentase dari ukuran asli
width = int(citra.shape[1] * scale_percent / 100)
height = int(citra.shape[0] * scale_percent / 100)
dim = (width, height)
citra = cv2.resize(citra, dim, interpolation=cv2.INTER_AREA)

# 1. Contoh Dasar Gradien Morfologis
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
gradien = cv2.morphologyEx(citra, cv2.MORPH_GRADIENT, kernel)

# 2. Perbandingan dengan Operasi Dasar
dilasi = cv2.dilate(citra, kernel)
erosi = cv2.erode(citra, kernel)
gradien_manual = dilasi - erosi  # Cara manual menghitung gradien

# 3. Contoh dengan Kernel Berbeda
kernel_besar = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
gradien_besar = cv2.morphologyEx(citra, cv2.MORPH_GRADIENT, kernel_besar)

# Tampilkan hasil
hasil = np.hstack((citra, dilasi, gradien))
cv2.imshow('Gambar 8. Transformasi Gradien Morfologis', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()