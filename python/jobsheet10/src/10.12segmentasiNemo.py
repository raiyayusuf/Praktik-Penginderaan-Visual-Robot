import cv2
import numpy as np

citra = cv2.imread(r'python\jobsheet10\img\nemo.jpg')

if citra is not None:
    hsv = cv2.cvtColor(citra, cv2.COLOR_BGR2HSV)

    oranyeMuda = np.array([2, 128, 128])
    oranyeGelap = np.array([20, 255, 255])

    putihMuda = np.array([0, 0, 160])
    putihGelap = np.array([179, 255, 255])

    masker_oranye = cv2.inRange(hsv, oranyeMuda, oranyeGelap)
    masker_putih = cv2.inRange(hsv, putihMuda, putihGelap)

    masker = cv2.bitwise_or(masker_oranye, masker_putih)
    hasil = cv2.bitwise_and(citra, citra, mask=masker)

    scale_percent = 30
    width = int(citra.shape[1] * scale_percent / 100)
    height = int(citra.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_citra = cv2.resize(citra, dim, interpolation=cv2.INTER_AREA)
    resized_masker = cv2.resize(masker, dim, interpolation=cv2.INTER_AREA)
    resized_hasil = cv2.resize(hasil, dim, interpolation=cv2.INTER_AREA)

    resized_masker_gray = cv2.cvtColor(resized_masker, cv2.COLOR_GRAY2BGR)

    concatenated_output = np.concatenate((resized_citra, resized_masker_gray, resized_hasil), axis=1)

    cv2.imshow('Nemo', concatenated_output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Gambar tidak ditemukan di path yang diberikan.")