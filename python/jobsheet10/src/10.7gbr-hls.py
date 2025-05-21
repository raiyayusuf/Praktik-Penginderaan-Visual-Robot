import cv2

citra = cv2.imread(r'python\jobsheet10\img\genteng.png')

if citra is not None:
    hls = cv2.cvtColor(citra, cv2.COLOR_BGR2HLS)
    print("Informasi untuk piksel di pojok kiri-atas:")
    print("H =", hls[0, 0, 0])
    print("L =", hls[0, 0, 1])
    print("S =", hls[0, 0, 2])
else:
    print("Gambar tidak ditemukan di path yang diberikan.")