import cv2

path_gambar = r'python\jobsheet9\img\guppyBiru.png'
citra = cv2.imread(path_gambar, 0)

kontur, hierarki = cv2.findContours(citra, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

if kontur:
    keliling = cv2.arcLength(kontur[0], True)
    print("Keliling =", keliling)
else:
    print("Tidak ada kontur yang ditemukan.")