# cara mengecilkan citra

import cv2

citra = cv2.imread(r'jobsheet6\img\peppers.jpg')

jumlahBaris, jumlahKolom = citra.shape[:2]
hasil = cv2.resize(citra, (int(0.5 * jumlahBaris), int(0.5 * jumlahKolom)))

# tampilan 
cv2.imshow('Awal', citra)
cv2.imshow('Hasil', hasil)

cv2.waitKey(0)
cv2.destroyAllWindows()