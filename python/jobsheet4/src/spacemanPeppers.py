import cv2
import numpy as np

# Buat citra berwarna hitam
citra = np.zeros((512, 512, 3), np.uint8)

# Baca gambar yang akan ditempel
spaceman = cv2.imread(r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\spaceman.png', 8)

if spaceman is None:
    print("Error: Gambar spaceman tidak ditemukan atau tidak dapat dibaca.")
else:
    jumBaris = spaceman.shape[0]
    jumKolom = spaceman.shape[1]

    # Jika gambar spaceman melebihi ukuran 512x512, resize
    if jumBaris > 512 or jumKolom > 512:
        spaceman = cv2.resize(spaceman, (512, 512), interpolation=cv2.INTER_AREA)
        jumBaris = 512
        jumKolom = 512

    # Tempelkan gambar spaceman ke citra hitam
    citra[0:jumBaris, 0:jumKolom, :] = spaceman[:, :, 0:3]

    # Baca gambar background
    goldhill = cv2.imread(r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\peppers2.jpg')

    if goldhill is None:
        print("Error: Gambar background tidak ditemukan atau tidak dapat dibaca.")
    else:
        # Resize gambar background agar sesuai dengan ukuran citra (512x512)
        goldhill = cv2.resize(goldhill, (512, 512), interpolation=cv2.INTER_AREA)

        # Lakukan operasi penambahan
        hasil = cv2.add(goldhill, citra)

        # Tampilkan hasil
        cv2.imshow('Hasil', hasil)
        cv2.waitKey(0)
        cv2.destroyAllWindows()