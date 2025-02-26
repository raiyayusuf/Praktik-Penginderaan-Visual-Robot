import cv2

path_gambar = r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\peppers2.jpg'

citra = cv2.imread(path_gambar, cv2.IMREAD_UNCHANGED)

if citra is None:
    print(f"Tidak dapat membaca gambar: {path_gambar}")
else:
    lebar_kecil = citra.shape[1] // 3
    tinggi_kecil = citra.shape[0] // 3 
    citra_kecil = cv2.resize(citra, (lebar_kecil, tinggi_kecil))

    jumBaris, jumKolom = citra_kecil.shape[:2]
    xTengah = jumKolom // 2
    yTengah = jumBaris // 2

    # garis tegak
    cv2.line(citra_kecil, (xTengah, 0), (xTengah, jumBaris - 1), (128, 128, 128), 5)

    # garis mendatar
    cv2.line(citra_kecil, (0, yTengah), (jumKolom - 1, yTengah), (128, 128, 128), 5)

    cv2.imshow('Hasil', citra_kecil)

    cv2.waitKey(0)
    cv2.destroyAllWindows()