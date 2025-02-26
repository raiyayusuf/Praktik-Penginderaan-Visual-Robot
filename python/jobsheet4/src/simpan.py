import cv2

path_gambar = r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\kucingCape.png'

citra = cv2.imread(path_gambar, cv2.IMREAD_GRAYSCALE)

if citra is None:
    print(f"Tidak dapat membaca gambar: {path_gambar}")
else:
    hasil = 255 - citra
    cv2.imwrite('hasil.png', hasil)
    print('Citra telah disimpan di hasil.png')