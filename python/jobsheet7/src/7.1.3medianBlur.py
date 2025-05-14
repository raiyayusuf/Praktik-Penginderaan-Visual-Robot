import cv2
import numpy as np

path_gambar = r"python\jobsheet8\img\mickey.png"
citra = cv2.imread(path_gambar)

blur1 = cv2.medianBlur(citra, 5)
blur2 = cv2.medianBlur(citra, 45)

hasil = np.hstack((citra, blur1, blur2))

cv2.imshow('Hasil', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()