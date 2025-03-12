# Ekualisasi histogram menggunakan CLAHE untuk citra berwarna
import cv2
import numpy as np

citra = cv2.imread('python\\jobsheet5\\img\\melon.png')
lab = cv2.cvtColor(citra, cv2.COLOR_BGR2LAB)

kanalLAB = list(cv2.split(lab))  

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

kanalLAB[0] = clahe.apply(kanalLAB[0])

lab = cv2.merge(kanalLAB)

bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

hasil = np.hstack((citra, bgr))

scale_percent = 20 
width = int(hasil.shape[1] * scale_percent / 100)
height = int(hasil.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(hasil, dim, interpolation=cv2.INTER_AREA)

cv2.imshow('Hasil', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()