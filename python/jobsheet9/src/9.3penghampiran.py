import cv2
import numpy as np

path_gambar = r'python\jobsheet9\img\guppyTrans2.png'
citra = cv2.imread(path_gambar, 0)

if citra is None:
    print("Error: Gambar tidak dapat dibaca")
    exit()

citraBerwarna = cv2.cvtColor(citra, cv2.COLOR_GRAY2BGR)
kontur, hierarki = cv2.findContours(citra, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

if kontur:
    kontur_pertama = kontur[0]
    print("Jumlah piksel semula:", len(kontur_pertama))
    
    epsilon = 0.001 * cv2.arcLength(kontur_pertama, True)
    approx = cv2.approxPolyDP(kontur_pertama, epsilon, True)
    
    print("Jumlah piksel sekarang:", len(approx))
    
    cv2.drawContours(citraBerwarna, [approx], -1, (255, 0, 255), 8)
    
    cv2.imshow("Hasil", citraBerwarna)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Tidak ada kontur yang ditemukan.")