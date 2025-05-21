import cv2
import numpy as np

citra = cv2.imread(r'python\jobsheet10\img\bentukWarna.png')

if citra is not None:
    hsv = cv2.cvtColor(citra, cv2.COLOR_BGR2HSV)

    # Rentang nilai HSV untuk warna merah (karena Hue merah melingkar)
    batasBawahA = np.array([159, 20, 20])
    batasAtasA = np.array([179, 255, 255])

    batasBawahB = np.array([0, 20, 20])
    batasAtasB = np.array([20, 255, 255])

    maskerA = cv2.inRange(hsv, batasBawahA, batasAtasA)
    maskerB = cv2.inRange(hsv, batasBawahB, batasAtasB)
    masker = cv2.bitwise_or(maskerA, maskerB)

    hasil = cv2.bitwise_and(citra, citra, mask=masker)

    cv2.imshow('Citra asli', citra)
    cv2.imshow('Masker', masker)
    cv2.imshow('Citra hasil', hasil)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Gambar tidak ditemukan.")