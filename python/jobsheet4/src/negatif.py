import cv2

path_gambar = r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\kucingCape.png'

citra = cv2.imread(path_gambar, cv2.IMREAD_GRAYSCALE)  # dalam mode grayscale

if citra is None:
    print(f"Tidak dapat membaca gambar: {path_gambar}")
else:
    cv2.imshow('Citra asli', citra)

    hasil = 255 - citra  #  operasi negatif pada gambar
    cv2.imshow('Citra hasil', hasil)

    cv2.waitKey(0)  
    cv2.destroyAllWindows()  