import cv2
import numpy as np

path_gambar = r'python\jobsheet9\img\hurufA2new.png'
citra = cv2.imread(path_gambar, 0)
jumBaris = citra.shape[0]
jumKolom = citra.shape[1]
citraKontur = np.zeros((jumBaris, jumKolom, 3), np.uint8)
kontur, hierarki = cv2.findContours(citra, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(citraKontur, kontur, -1, (230, 216, 173), 2)
citraRGB = cv2.merge((citra, citra, citra))
hasil = np.hstack((citraRGB, citraKontur))
cv2.imshow("Hasil", hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()