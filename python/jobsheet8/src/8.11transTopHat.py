import cv2
import numpy as np

path_gambar = r"python\jobsheet8\img\beras.png"
citra = cv2.imread(path_gambar, 0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))

tophat = cv2.morphologyEx(citra, cv2.MORPH_TOPHAT, kernel)
pembukaan = cv2.morphologyEx(citra, cv2.MORPH_OPEN, kernel)

hasil = np.hstack((citra, pembukaan, tophat))

cv2.imshow('Hasil', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()