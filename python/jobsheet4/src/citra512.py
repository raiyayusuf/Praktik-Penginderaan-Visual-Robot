import cv2
import numpy as np

citra = np.zeros((512, 512, 3), np.uint8)

spaceman = cv2.imread(r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\spaceman.png', -1)

if spaceman is None:
    print("Error: Gambar tidak ditemukan atau tidak dapat dibaca.")
else:
    dimensi_baru = (512, 512)
    spaceman = cv2.resize(spaceman, dimensi_baru, interpolation=cv2.INTER_AREA)

    citra[:, :, :] = spaceman[:, :, 0:3]

    cv2.imshow('Hasil', citra)
    cv2.waitKey(0)
    cv2.destroyAllWindows()