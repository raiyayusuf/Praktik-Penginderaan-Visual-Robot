# Contoh penggunaan dilate()

import cv2
import numpy as np

citra = cv2.imread(r'python\jobsheet8\img\jepit.jpg', 0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilasi = cv2.dilate(citra, kernel, iterations=3)
hasil = np.hstack((citra, dilasi))

# Tampilkan citra asal dan hasilnya
cv2.imshow('Hasil', hasil)
cv2.waitKey(0)
