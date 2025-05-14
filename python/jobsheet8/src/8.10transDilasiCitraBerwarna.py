import cv2
import numpy as np

path_gambar = r"python\jobsheet8\img\mickey.png"
citra = cv2.imread(path_gambar)

kernelA = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
kernelB = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernelC = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

dilasiA = cv2.dilate(citra, kernelA)
dilasiB = cv2.dilate(citra, kernelB)
dilasiC = cv2.dilate(citra, kernelC)

hasil = np.hstack((citra, dilasiA, dilasiB, dilasiC))

cv2.imshow('Hasil', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()