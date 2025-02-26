import cv2

path_gambar = r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\peppers2.jpg'

citra = cv2.imread(path_gambar, cv2.IMREAD_UNCHANGED)

if citra is None:
    print(f"Tidak dapat membaca gambar: {path_gambar}")
else:
    # Perkecil ukuran gambar
    lebar_kecil = citra.shape[1] // 2
    tinggi_kecil = citra.shape[0] // 2 
    citra_kecil = cv2.resize(citra, (lebar_kecil, tinggi_kecil))

    jumBaris, jumKolom = citra_kecil.shape[:2]
    xTengah = jumKolom // 2
    yTengah = jumBaris // 2

    # Buat lingkaran
    cv2.circle(citra_kecil, (xTengah, yTengah), 100, (255, 255, 255), 10)

    # Tampilkan citra yang diperkecil
    cv2.imshow('Hasil', citra_kecil)

    cv2.waitKey(0)
    cv2.destroyAllWindows()