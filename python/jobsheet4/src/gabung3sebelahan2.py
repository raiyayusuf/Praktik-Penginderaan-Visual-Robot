import cv2
import numpy as np

citraA = cv2.imread(r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\peppers2.jpg')
citraB = cv2.imread(r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\spaceman.png', cv2.IMREAD_UNCHANGED)

if citraA is None or citraB is None:
    print("Error: Gambar tidak ditemukan atau tidak dapat dibaca.")
else:
    if citraB.shape[2] == 4:
        citraB = cv2.cvtColor(citraB, cv2.COLOR_BGRA2BGR)

    scale_percent = 30
    widthA = int(citraA.shape[1] * scale_percent / 100)
    heightA = int(citraA.shape[0] * scale_percent / 100)
    citraA = cv2.resize(citraA, (widthA, heightA), interpolation=cv2.INTER_AREA)

    widthB = int(citraB.shape[1] * scale_percent / 100)
    heightB = int(citraB.shape[0] * scale_percent / 100)
    citraB = cv2.resize(citraB, (widthB, heightB), interpolation=cv2.INTER_AREA)

    if citraA.shape[1] != citraB.shape[1]:
        citraB = cv2.resize(citraB, (citraA.shape[1], int(citraB.shape[0] * citraA.shape[1] / citraB.shape[1])), interpolation=cv2.INTER_AREA)

    hasil = np.vstack((citraA, citraB))

    cv2.imshow('Hasil', hasil)
    cv2.waitKey(0)
    cv2.destroyAllWindows()