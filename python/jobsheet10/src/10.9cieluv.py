import cv2

citra = cv2.imread(r'python\jobsheet10\img\genteng.png')

if citra is not None:
    luv = cv2.cvtColor(citra, cv2.COLOR_BGR2Luv)
    print("Informasi untuk piksel di pojok kiri-atas:")
    print("L =", luv[0, 0, 0])
    print("u =", luv[0, 0, 1])
    print("v =", luv[0, 0, 2])
else:
    print("Gambar tidak ditemukan di path yang diberikan.")