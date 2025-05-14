import cv2
import numpy as np

path_gambar = r"python\jobsheet6\img\gedung.png"
citra = cv2.imread(path_gambar)
jumBaris, jumKolom = citra.shape[:2]

titikPusat = (jumKolom // 2, jumBaris // 2)
matriksRotasi = cv2.getRotationMatrix2D(titikPusat, -15, 1)
hasil = cv2.warpAffine(citra, matriksRotasi, (jumKolom, jumBaris))

cv2.imshow('Hasil translasi', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()