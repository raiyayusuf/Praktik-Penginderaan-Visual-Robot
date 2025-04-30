# Contoh untuk menunjukkan efek ukuran kernel
#    pada transformasi erosi dan pembukaan

import cv2
import numpy as np

# Menggunakan path yang benar (sesuaikan dengan kebutuhan)
citra = cv2.imread('python/jobsheet8/img/daun.jpg', 0)  
scale_percent = 50  # persentase dari ukuran asli
width = int(citra.shape[1] * scale_percent / 100)
height = int(citra.shape[0] * scale_percent / 100)
dim = (width, height)
citra = cv2.resize(citra, dim, interpolation=cv2.INTER_AREA)

# Membuat kernel dengan bentuk elips dan ukuran berbeda
kernelA = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
kernelB = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (12, 12))

# Operasi morfologi
erosi = cv2.erode(citra, kernelA)
pembukaanA = cv2.morphologyEx(citra, cv2.MORPH_OPEN, kernelA)
pembukaanB = cv2.morphologyEx(citra, cv2.MORPH_OPEN, kernelB)

# Mengatur tampilan hasil          
baris1 = np.hstack((citra, erosi))
baris2 = np.hstack((pembukaanA, pembukaanB))
hasil = np.vstack((baris1, baris2))

# Tampilkan citra asal dan hasilnya
cv2.imshow('Pengaruh Ukuran Kernel pada Erosi dan Opening', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()