import cv2
import numpy as np

path_gambar = r'python\jobsheet9\img\guppyBiru.png'
citra = cv2.imread(path_gambar, 0)
citraBerwarna = cv2.cvtColor(citra, cv2.COLOR_GRAY2BGR)
kontur, hierarki = cv2.findContours(citra, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

if kontur:
    x, y, lebar, tinggi = cv2.boundingRect(kontur[0])
    cv2.rectangle(citraBerwarna, (x, y), (x + lebar, y + tinggi), (255, 255, 0), 2)

    persegiPanjang = cv2.minAreaRect(kontur[0])
    kotak = cv2.boxPoints(persegiPanjang)
    kotak = np.int32(kotak)
    cv2.drawContours(citraBerwarna, [kotak], 0, (128, 128, 128), 2)

    cv2.imshow("Hasil", citraBerwarna)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Tidak ada kontur yang ditemukan.")