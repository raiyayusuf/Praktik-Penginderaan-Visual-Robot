import cv2
import numpy as np

path_gambar = r'python\jobsheet9\img\abc.png'
citra = cv2.imread(path_gambar, 0)
citraBerwarna = cv2.cvtColor(citra, cv2.COLOR_GRAY2BGR)
kontur, hierarki = cv2.findContours(citra, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
terpanjang = 0
posisi = -1

for indeks in range(len(kontur)):
    keliling = cv2.arcLength(kontur[indeks], True)
    if indeks == 0:
        terpanjang = keliling
        posisi = 0
    else:
        if keliling > terpanjang:
            posisi = indeks
            terpanjang = keliling

citra_hasil = np.zeros_like(citraBerwarna)
if posisi != -1:
    cv2.drawContours(citra_hasil, kontur, posisi, (255, 255, 255), -1)

cv2.imshow("Hasil", citra_hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()