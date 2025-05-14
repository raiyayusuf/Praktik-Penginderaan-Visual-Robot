import cv2
import numpy as np
import math

path_gambar = r"python\jobsheet6\img\gedung.png"
citra = cv2.imread(path_gambar)
jumBaris, jumKolom = citra.shape[:2]

matriks = np.float32([[1, 0, 0], [0.25, 1, 0]])
hasil = cv2.warpAffine(citra, matriks, (jumKolom, int(1.4 * jumBaris)))
tinggi_hasil = hasil.shape[0]
tinggi_citra = citra.shape[0]
lebar_citra = citra.shape[1]
channels_citra = citra.shape[2] if len(citra.shape) == 3 else 1
padding_atas = (tinggi_hasil - tinggi_citra) // 2
padding_bawah = tinggi_hasil - tinggi_citra - padding_atas

if channels_citra == 3:
    citra_padded = cv2.copyMakeBorder(citra, padding_atas, padding_bawah, 0, 0, cv2.BORDER_CONSTANT, value=[0, 0, 0])
else:
    citra_padded = cv2.copyMakeBorder(citra, padding_atas, padding_bawah, 0, 0, cv2.BORDER_CONSTANT, value=0)

gab = np.hstack((citra_padded, hasil))
cv2.imshow('Hasil pembengkokan', gab)
cv2.waitKey(0)
cv2.destroyAllWindows()