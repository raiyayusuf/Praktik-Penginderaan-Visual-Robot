import cv2
import numpy as np

path_gambar = r"python\jobsheet8\img\mickey.png"
citra = cv2.imread(path_gambar, 0)

kernel = np.float32([[-2, 0, 0],
                   [ 0, 0, 0],
                   [ 0, 0, 2]])

terfilter = cv2.filter2D(citra, -1, kernel)

hasil = np.hstack((citra, terfilter))

cv2.imshow('Hasil', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()