import cv2
import numpy as np

path_gambar = r"python\jobsheet6\img\gedung.png"
citra = cv2.imread(path_gambar)
jumBaris, jumKolom = citra.shape[:2]

matriks = np.float32([[1, 0, 50], [0, 1, 100]])
hasil = cv2.warpAffine(citra, matriks, (jumKolom, jumBaris))

cv2.imshow('Hasil translasi', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()