import cv2
import numpy as np

citra = cv2.imread(r'python\jobsheet10\img\bentukWarna.png')

if citra is not None:
    hsv = cv2.cvtColor(citra, cv2.COLOR_BGR2HSV)

    batasBawah = np.array([90, 50, 50])
    batasAtas = np.array([130, 255, 255])

    masker = cv2.inRange(hsv, batasBawah, batasAtas)
    hasil = cv2.bitwise_and(citra, citra, mask=masker)

    cv2.imshow('Citra asli', citra)
    cv2.imshow('Masker', masker)
    cv2.imshow('Citra hasil', hasil)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Gambar tidak ditemukan di path yang diberikan.")