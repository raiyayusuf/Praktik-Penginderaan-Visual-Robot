import cv2
import numpy as np

path_gambar = r"python\jobsheet6\img\gedung.png"
citra = cv2.imread(path_gambar)
jumBaris, jumKolom = citra.shape[:2]

titik1 = np.float32([[10, 10], [10, 50], [50, 50]])
titik2 = np.float32([[10, 0], [20, 50], [50, 60]])
matriks = cv2.getAffineTransform(titik1, titik2)
hasil = cv2.warpAffine(citra, matriks, (jumKolom, jumBaris))

cv2.imshow('Hasil transformasi', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()