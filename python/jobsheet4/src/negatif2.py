import cv2

path_gambar = r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\kucingCape.png'

citra = cv2.imread(path_gambar, cv2.IMREAD_GRAYSCALE)  # Membaca gambar dalam mode grayscale

if citra is None:
    print(f"Tidak dapat membaca gambar: {path_gambar}")
else:
    cv2.imshow('Citra asli', citra)

    hasil = citra + 50  # Menambahkan 50 ke setiap nilai piksel
    cv2.imshow('Citra hasil', hasil)

    cv2.waitKey(0)  
    cv2.destroyAllWindows()  