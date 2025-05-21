import cv2
import numpy as np

citra = cv2.imread(r'python\jobsheet10\img\bentukWarna.png')

if citra is not None:
    hsv = cv2.cvtColor(citra, cv2.COLOR_BGR2HSV)

    # Rentang nilai HSV untuk warna hijau
    batasBawahA = np.array([35, 50, 50])
    batasAtasA = np.array([85, 255, 255])

    batasBawahB = np.array([35, 50, 50])
    batasAtasB = np.array([85, 255, 255])

    maskerA = cv2.inRange(hsv, batasBawahA, batasAtasA)
    maskerB = cv2.inRange(hsv, batasBawahB, batasAtasB)
    masker = cv2.bitwise_or(maskerA, maskerB)

    # Pengurangan noise pada masker
    masker_blur = cv2.GaussianBlur(masker, (5, 5), 0)

    # Deteksi lingkaran dengan Hough Transform
    lingkaran = cv2.HoughCircles(masker_blur, cv2.HOUGH_GRADIENT, 1, 20,
                                param1=50, param2=30, minRadius=0, maxRadius=0)

    if lingkaran is not None:
        lingkaran_bulat = np.uint16(np.around(lingkaran))
        for (x, y, r) in lingkaran_bulat[0, :]:
            cv2.circle(citra, (x, y), r, (255, 0, 0), 2)        # Lingkaran luar berwarna biru
            cv2.circle(citra, (x, y), 3, (255, 255, 255), -1)  # Titik tengah berwarna putih

        cv2.imshow('Lingkaran Hijau', citra)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Tidak ada lingkaran hijau terdeteksi!")
else:
    print("Gambar tidak ditemukan di path yang diberikan.")