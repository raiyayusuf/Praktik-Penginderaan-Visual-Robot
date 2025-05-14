import cv2
import numpy as np

path_gambar = r"python\jobsheet6\img\gedung.png"
citra = cv2.imread(path_gambar)
hasil = cv2.flip(citra, 0)
gab = np.hstack((citra, hasil))
cv2.imshow('Hasil pencerminan', gab)
cv2.waitKey(0)
cv2.destroyAllWindows()