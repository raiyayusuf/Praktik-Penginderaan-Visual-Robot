import cv2
import numpy as np

citra = np.zeros((512, 512, 3), np.uint8)
alfa = np.zeros((512, 512), np.uint8)

spaceman = cv2.imread(r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\spaceman.png', -1)

if spaceman is None:
    print("Error: Gambar spaceman tidak ditemukan atau tidak dapat dibaca.")
else:
    jumBaris = spaceman.shape[0]
    jumKolom = spaceman.shape[1]

    if jumBaris > 512 or jumKolom > 512:
        spaceman = cv2.resize(spaceman, (512, 512), interpolation=cv2.INTER_AREA)
        jumBaris = 512
        jumKolom = 512

    citra[0:jumBaris, 0:jumKolom, :] = spaceman[:, :, 0:3]
    alfa[0:jumBaris, 0:jumKolom] = spaceman[:, :, 3]

    cadar = cv2.merge([alfa, alfa, alfa])
    kebalikan = cv2.bitwise_not(cadar)

    cv2.imshow('Cadar', cadar)
    cv2.imshow('Kebalikan', kebalikan)

    goldhill = cv2.imread(r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\peppers2.jpg')

    if goldhill is None:
        print("Error: Gambar background tidak ditemukan atau tidak dapat dibaca.")
    else:
        goldhill = cv2.resize(goldhill, (512, 512), interpolation=cv2.INTER_AREA)

        hasil_and = cv2.bitwise_and(goldhill, kebalikan)
        cv2.imshow('Hasil AND', hasil_and)
        print(hasil_and.shape)

        hasil_add = cv2.add(hasil_and, citra)
        cv2.imshow('Hasil ADD', hasil_add)

        cv2.waitKey(0)
        cv2.destroyAllWindows()