import cv2
import numpy as np

path_gambar = r'python\jobsheet9\img\guppyBiru.png'
citra = cv2.imread(path_gambar, 0)
citraBerwarna = cv2.cvtColor(citra, cv2.COLOR_GRAY2BGR)
kontur, hierarki = cv2.findContours(citra, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

if kontur:
    if len(kontur[0]) >= 30:  # Ellipse fitting memerlukan minimal 5 titik
        elips = cv2.fitEllipse(kontur[0])
        cv2.ellipse(citraBerwarna, elips, (255, 255, 0), 2)
    else:
        print("Kontur tidak memiliki cukup titik untuk fitting elips.")

    cv2.imshow("Hasil", citraBerwarna)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Tidak ada kontur yang ditemukan.")