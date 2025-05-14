import cv2
import numpy as np

path_gambar = r"python\jobsheet7\img\genteng.png"
citra = cv2.imread(path_gambar, 0)
jumSaris, jumKolom = citra.shape[:2]
citra = cv2.resize(citra, (int(0.5 * jumKolom), int(0.5 * jumSaris)))

kernelA = np.float32([[0, -1, 0],
                   [-1, 4, -1],
                   [0, -1, 0]])

kernels = np.float32([[-1, -1, -1],
                   [-1, 8, -1],
                   [-1, -1, -1]])

kernelC = np.float32([[1, -2, 1],
                   [-2, 4, -2],
                   [1, -2, 1]])

filterA = cv2.filter2D(citra, -1, kernelA)
filters = cv2.filter2D(citra, -1, kernels)
filterC = cv2.filter2D(citra, -1, kernelC)

baris1 = np.hstack((citra, filterA))
baris2 = np.hstack((filters, filterC))

hasil = np.vstack((baris1, baris2))

cv2.imshow('Hasil', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()