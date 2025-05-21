import cv2

citra = cv2.imread(r'python\jobsheet10\img\genteng.png')

if citra is not None:
    lab = cv2.cvtColor(citra, cv2.COLOR_BGR2Lab)
    print("Informasi untuk piksel di pojok kiri-atas:")
    print("L =", lab[0, 0, 0])
    print("a =", lab[0, 0, 1])
    print("b =", lab[0, 0, 2])
else:
    print("Gambar tidak ditemukan di path yang diberikan.")