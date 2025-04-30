# Contoh penggunaan erode()
# dengan melibatkan iterations

import cv2
import numpy as np

# Menggunakan path yang sesuai
citra = cv2.imread('python/jobsheet8/img/jepit.jpg', 0)

# Membuat kernel untuk operasi morfologi
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# Operasi dilasi dan erosi dengan iterations=3
dilasi = cv2.dilate(citra, kernel, iterations=3)
erosi = cv2.erode(dilasi, kernel, iterations=3)

# Menggabungkan gambar untuk ditampilkan
hasil = np.hstack((citra, dilasi, erosi))  # Menambahkan citra asli untuk perbandingan

# Menampilkan hasil
cv2.imshow('Erosi2', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()