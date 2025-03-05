import cv2
import numpy as np

citra = cv2.imread(r"C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\peppers2.jpg")

if citra is None:
    print("Error: Gambar tidak ditemukan atau tidak dapat dibaca.")
else:
    scale_percent = 50
    width = int(citra.shape[1] * scale_percent / 100)
    height = int(citra.shape[0] * scale_percent / 100)
    dimensi_baru = (width, height)
    citra = cv2.resize(citra, dimensi_baru, interpolation=cv2.INTER_AREA)

    jumBaris = citra.shape[0]
    jumKolom = citra.shape[1]

    noi = np.zeros((jumBaris, jumKolom), np.uint8)

    biru, hijau, merah = cv2.split(citra)

    citraB = cv2.merge((biru, noi, noi))
    citraG = cv2.merge((noi, hijau, noi))
    citraR = cv2.merge((noi, noi, merah))

    cv2.imshow('Kanal biru', citraB)
    cv2.imshow('Kanal hijau', citraG)
    cv2.imshow('Kanal merah', citraR)

    cv2.waitKey(0)
    cv2.destroyAllWindows()