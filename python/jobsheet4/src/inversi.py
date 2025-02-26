import cv2
import numpy as np

path_gambar = r"C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\kucingCape.png"

citra = cv2.imread(path_gambar, cv2.IMREAD_GRAYSCALE)

if citra is None:
    print(f'Tidak dapat membaca berkas: {path_gambar}')
else:
    jumBaris, jumKolom = citra.shape
    hasil = np.zeros((jumBaris, jumKolom), np.uint8)

    for brs in range(jumBaris):
        for kol in range(jumKolom):
            hasil[brs, kol] = 255 - citra[brs, kol]

    cv2.imshow('Asli', citra)
    cv2.imshow('Hasil', hasil)
    cv2.waitKey(0)
    cv2.destroyAllWindows()