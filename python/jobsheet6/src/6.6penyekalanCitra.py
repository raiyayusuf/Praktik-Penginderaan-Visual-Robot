import cv2
import numpy as np

path_gambar = r"python\jobsheet6\img\gedung.png"
citra = cv2.imread(path_gambar)
jumBaris, jumKolom = citra.shape[:2]

matriksSkala = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
hasil = cv2.warpAffine(citra, matriksSkala, (jumKolom, jumBaris))

cv2.imshow('Hasil penyekalaan', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()