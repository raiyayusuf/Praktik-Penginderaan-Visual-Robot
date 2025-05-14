import cv2
import numpy as np

path_gambar = r"python\jobsheet6\img\gedung.png"
citra = cv2.imread(path_gambar)
jumBaris, jumKolom = citra.shape[:2]

matriks = np.float32([[-1, 0, jumKolom], [0, 1, 0]])
hasil = cv2.warpAffine(citra, matriks, (jumKolom, jumBaris))

gab = np.hstack((citra, hasil))
cv2.imshow('Hasil pencerminan', gab)
cv2.waitKey(0)
cv2.destroyAllWindows()