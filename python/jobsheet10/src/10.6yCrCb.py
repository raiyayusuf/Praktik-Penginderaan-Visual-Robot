import cv2

citra = cv2.imread(r'python\jobsheet10\img\guppyBiru.png')
if not citra is None:
    yCrCb = cv2.cvtColor(citra, cv2.COLOR_BGR2YCrCb)
    print("Informasi untuk piksel di pojok kiri-atas:")
    print("Y =", yCrCb[0, 0, 0])
    print("Cr =", yCrCb[0, 0, 1])
    print("Cb =", yCrCb[0, 0, 2])