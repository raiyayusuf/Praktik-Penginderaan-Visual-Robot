import cv2
import numpy as np
import sys

path_gambar = r"python\jobsheet8\img\mickey.png"
citra = cv2.imread(path_gambar, 0)
if citra is None:
    print('Berkas citra tak dapat dibaca')
    sys.exit()

terfilter = cv2.fastNlMeansDenoising(citra, None, 30)

hasil = np.hstack((citra, terfilter))

cv2.imshow('Hasil', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()