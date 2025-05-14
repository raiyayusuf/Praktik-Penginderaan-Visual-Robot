import cv2
import numpy as np

path_gambar = r"python\jobsheet8\img\mickey.png"
citra = cv2.imread(path_gambar)

kernelA = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
kernelB = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernelC = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

erosiA = cv2.erode(citra, kernelA)
erosiB = cv2.erode(citra, kernelB)
erosiC = cv2.erode(citra, kernelC)

hasil = np.hstack((citra, erosiA, erosiB, erosiC))

cv2.imshow('Hasil', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()