import cv2
import numpy as np

path_gambar = r'python\jobsheet9\img\guppyBiru.png'
citra = cv2.imread(path_gambar, 0)
citraBerwarna = cv2.cvtColor(citra, cv2.COLOR_GRAY2BGR)
kontur, hierarki = cv2.findContours(citra, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

if kontur:
    (x, y), radius = cv2.minEnclosingCircle(kontur[0])
    pusat = (int(x), int(y))
    radius = int(radius)
    cv2.circle(citraBerwarna, pusat, radius, (255, 255, 0), 2)

    cv2.imshow("Hasil", citraBerwarna)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Tidak ada kontur yang ditemukan.")