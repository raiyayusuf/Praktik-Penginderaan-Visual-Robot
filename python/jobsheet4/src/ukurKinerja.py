import cv2
import numpy as np

path_gambar = r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\kucingCape.png'

citra = cv2.imread(path_gambar, cv2.IMREAD_GRAYSCALE)

if citra is None:
    print(f"Tidak dapat membaca gambar: {path_gambar}")
else:
    # Proses 1
    awal = cv2.getTickCount()

    jumBaris, jumKolom = citra.shape
    hasil1 = np.zeros((jumBaris, jumKolom), np.uint8)

    for brs in range(jumBaris):
        for kol in range(jumKolom):
            hasil1[brs, kol] = 255 - citra[brs, kol]

    akhir = cv2.getTickCount()
    selangWaktu1 = (akhir - awal) / cv2.getTickFrequency()
    print(f"Waktu untuk Proses 1: {selangWaktu1:.6f} detik")

    # Proses 2
    awal = cv2.getTickCount()

    hasil2 = 255 - citra

    akhir = cv2.getTickCount()
    selangWaktu2 = (akhir - awal) / cv2.getTickFrequency()
    print(f"Waktu untuk Proses 2: {selangWaktu2:.6f} detik")

    cv2.imshow('Citra Asli', citra)
    cv2.imshow('Hasil Proses 1', hasil1)
    cv2.imshow('Hasil Proses 2', hasil2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()