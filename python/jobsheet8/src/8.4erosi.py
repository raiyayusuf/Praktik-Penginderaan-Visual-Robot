import cv2
import numpy as np

# Perbaikan: path gambar yang benar dan format parameter yang tepat
citra = cv2.imread('python/jobsheet8/img/jepit.jpg', 0)

# Perbaikan: penulisan variabel dan parameter yang benar
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilasi = cv2.dilate(citra, kernel, iterations=3)
erosi = cv2.erode(dilasi, kernel)

hasil = np.hstack((citra, dilasi, erosi))

# Tampilkan citra asal dan hasilnya
cv2.imshow('Erosi', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()