import cv2
import numpy as np

path_gambar = r'python\jobsheet9\img\hurufA.jpg'
citra = cv2.imread(path_gambar, 0)
citraBerwarna = cv2.cvtColor(citra, cv2.COLOR_GRAY2BGR)
kontur, hierarki = cv2.findContours(citra, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
terbesar = 0
posisi = -1

for indeks in range(len(kontur)):
    luas = cv2.contourArea(kontur[indeks])
    if indeks == 0:
        terbesar = luas
        posisi = 0
    else:
        if luas > terbesar:
            posisi = indeks
            terbesar = luas

citra_hasil = np.zeros_like(citraBerwarna)
if posisi != -1:
    cv2.drawContours(citra_hasil, kontur, posisi, (255, 255, 255), -1)

cv2.imshow("Hasil", citra_hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()