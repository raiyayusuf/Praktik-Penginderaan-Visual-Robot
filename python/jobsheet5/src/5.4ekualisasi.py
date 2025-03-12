# Ekualisasi histogram 
import cv2
import numpy as np

citra = cv2.imread('python\\jobsheet5\\img\\kucingHitamPutih.jpg', 0)

ekual = cv2.equalizeHist(citra)

hasil = np.hstack((citra, ekual))

scale_percent = 50  # ubah ukurane
width = int(hasil.shape[1] * scale_percent / 100)
height = int(hasil.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(hasil, dim, interpolation=cv2.INTER_AREA)

cv2.imshow('Hasil Ekualisasi', resized)
cv2.waitKey(0)
cv2.destroyAllWindows() 