# Ekualisasi histogram untuk citra berwarna 
import cv2
import numpy as np

citra = cv2.imread('python\\jobsheet5\\img\\melon.png')

lab = cv2.cvtColor(citra, cv2.COLOR_BGR2LAB)

kanalLAB = list(cv2.split(lab))  # Mengubah tuple menjadi list

kanalLAB[0] = cv2.equalizeHist(kanalLAB[0])

lab = cv2.merge(kanalLAB)

bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

hasil = np.hstack((citra, bgr))

scale_percent = 20
width = int(hasil.shape[1] * scale_percent / 100)
height = int(hasil.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(hasil, dim, interpolation=cv2.INTER_AREA)

cv2.imshow('Hasil Ekual Warna', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()