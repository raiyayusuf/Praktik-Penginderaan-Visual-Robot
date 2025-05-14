import cv2
import random
import sys

path_gambar = r"python\jobsheet8\img\mickey.png"
berkas = path_gambar
prob = 0.05  # Probabilitas default

citra = cv2.imread(berkas, 0)
if citra is None:
    print(f'Tidak dapat membaca berkas: {berkas}')
    sys.exit()

hasil = citra.copy()
jumBaris, jumKolom = hasil.shape[:2]

for baris in range(jumBaris):
    for kolom in range(jumKolom):
        nilaiAcak = random.random()
        if nilaiAcak < prob / 2:
            hasil[baris, kolom] = 0  # Merica
        elif nilaiAcak < prob:
            hasil[baris, kolom] = 255  # Garam

cv2.imshow('Hasil rotasi', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('mickey_garam_merica.png', hasil)