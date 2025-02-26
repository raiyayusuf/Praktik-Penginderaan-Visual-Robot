import cv2
import numpy as np

citra = 255 * np.ones((256, 256, 3), np.uint8)

titik = np.array([[10, 128], [200, 10], [180, 120], [240, 240]], np.int32)
cv2.polylines(citra, [titik], True, (0, 0, 0), 3)

cv2.imshow('Hasil', citra)

cv2.waitKey(0)
cv2.destroyAllWindows()