import cv2
import numpy as np

citra = np.array((
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
), dtype=np.uint8)

kernel = np.array((
    [1, 0, 0],
    [1, 0, 1],
    [0, 0, 1],
    [0, 0, 1]
), dtype=np.uint8)

el = cv2.erode(citra, kernel)
e2 = cv2.erode(1 - citra, 1 - kernel)
hasil = el & e2

print(hasil)

cv2.imshow("Hasil", (hasil * 255).astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()