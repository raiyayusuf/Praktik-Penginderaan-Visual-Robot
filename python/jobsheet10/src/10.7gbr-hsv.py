import cv2

citra = cv2.imread(r'python\jobsheet10\img\genteng.png')

if citra is not None:
    hsv = cv2.cvtColor(citra, cv2.COLOR_BGR2HSV)
    print("Informasi untuk piksel di pojok kiri-atas:")
    print("H =", hsv[0, 0, 0])
    print("S =", hsv[0, 0, 1])
    print("V =", hsv[0, 0, 2])
else:
    print("Gambar tidak ditemukan di path yang diberikan.")