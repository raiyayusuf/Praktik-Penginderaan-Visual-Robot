import cv2
import numpy as np

path_gambar = r"python\jobsheet8\img\daun.png"
citra = cv2.imread(path_gambar, 0)

ambang, citra = cv2.threshold(citra, 160, 255, cv2.THRESH_BINARY)

citra = 255 - citra

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

penutupan = cv2.morphologyEx(citra, cv2.MORPH_CLOSE, kernel)
blackhat = cv2.morphologyEx(citra, cv2.MORPH_BLACKHAT, kernel)

hasil = np.hstack((citra, penutupan, blackhat))

cv2.imshow('Hasil', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()