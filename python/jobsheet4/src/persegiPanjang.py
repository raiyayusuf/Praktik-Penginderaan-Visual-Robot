import cv2
import numpy as np

citra = 255 * np.ones((256, 256, 3), np.uint8)

cv2.rectangle(citra, (10, 10), (250, 128), (0, 0, 0), cv2.FILLED)
cv2.rectangle(citra, (100, 80), (236, 246), (0, 0, 255), 10)

cv2.imshow('Hasil', citra)

cv2.waitKey(0)
cv2.destroyAllWindows()