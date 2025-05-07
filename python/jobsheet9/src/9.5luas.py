import cv2

path_gambar = r'python\jobsheet9\img\guppy.jpeg'
citra = cv2.imread(path_gambar, 0)
kontur, hierarki = cv2.findContours(citra, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

if kontur:
    luas = cv2.contourArea(kontur[0])
    print("Luas =", luas)
else:
    print("Tidak ada kontur yang ditemukan.")