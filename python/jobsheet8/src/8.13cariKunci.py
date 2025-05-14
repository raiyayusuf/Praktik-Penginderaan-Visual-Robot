import cv2
import numpy as np

path_gambar = r"python\jobsheet8\img\kunci.png"
citraAsal = cv2.imread(path_gambar, 0)

citra = citraAsal // 255

kernelA = np.array((
    [0, 1, 1],
    [0, 1, 1],
    [0, 1, 1]
), dtype=np.uint8)

kernelB = np.array((
    [0, 0, 0],
    [1, 1, 1],
    [1, 1, 1]
), dtype=np.uint8)

elA = cv2.erode(citra, kernelA)
e2A = cv2.erode(1 - citra, 1 - kernelA)
hasilA = (elA & e2A) * 255

elB = cv2.erode(citra, kernelB)
e2B = cv2.erode(1 - citra, 1 - kernelB)
hasilB = (elB & e2B) * 255

hasil = np.hstack((citraAsal, hasilA, hasilB))

cv2.imshow("Hasil", hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()