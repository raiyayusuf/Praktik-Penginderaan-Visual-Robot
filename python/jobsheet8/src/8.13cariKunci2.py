import cv2
import numpy as np

path_gambar = r"python\jobsheet8\img\kunci.png"
citra = cv2.imread(path_gambar, 0)

kernelA = np.array((
    [ 0,  0,  0],
    [ 1,  1,  0],
    [-1,  1,  1]
), dtype=np.int8)

kernelB = np.array((
    [ 0,  0, -1],
    [ 1,  1,  0],
    [ 1,  1,  0]
), dtype=np.int8)

hasilA = cv2.morphologyEx(citra, cv2.MORPH_HITMISS, kernelA)
hasilB = cv2.morphologyEx(citra, cv2.MORPH_HITMISS, kernelB)

hasil = np.hstack((citra, hasilA * 255, hasilB * 255))

cv2.imshow("Hasil", hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()