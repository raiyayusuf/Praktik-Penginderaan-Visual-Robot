import cv2
import random
import sys
import numpy as np

path_gambar = r"python\jobsheet7\img\genteng.png"
berkas = path_gambar
sigma = 10
mu = 0

citra = cv2.imread(berkas, 0)
if citra is None:
    print(f'Tidak dapat membaca berkas: {berkas}')
    sys.exit()

hasil = citra.copy()
jumBaris, jumKolom = hasil.shape[:2]

for baris in range(jumBaris):
    for kolom in range(jumKolom):
        nilaiBaru = hasil[baris, kolom] + random.gauss(mu, sigma)
        if nilaiBaru > 255:
            nilaiBaru = 255
        elif nilaiBaru < 0:
            nilaiBaru = 0
        hasil[baris, kolom] = int(nilaiBaru)

cv2.imshow('Hasil rotasi', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('genteng_gaussian.png', hasil)