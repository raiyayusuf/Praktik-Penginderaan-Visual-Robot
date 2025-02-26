import cv2

path_gambar = r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\kucingCape.png'

citra = cv2.imread(path_gambar, cv2.IMREAD_UNCHANGED)

if citra is None:
    print(f"Tidak dapat membaca gambar: {path_gambar}")
else:
    lebar_kecil = citra.shape[1] // 2
    tinggi_kecil = citra.shape[0] // 2
    citra_kecil = cv2.resize(citra, (lebar_kecil, tinggi_kecil))

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(citra_kecil, 'Koceengg', (130, 280), font, 2, (255, 255, 255), 2) 
    cv2.imshow('Hasil', citra_kecil)

    cv2.waitKey(0)
    cv2.destroyAllWindows()