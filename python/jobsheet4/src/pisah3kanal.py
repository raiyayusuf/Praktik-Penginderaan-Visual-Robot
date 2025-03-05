import cv2

citra = cv2.imread(r"C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\peppers2.jpg")

if citra is None:
    print("Error: Gambar tidak ditemukan atau tidak dapat dibaca.")
else:
    scale_percent = 50  
    width = int(citra.shape[1] * scale_percent / 100)
    height = int(citra.shape[0] * scale_percent / 100)
    dimensi_baru = (width, height)

    citra_kecil = cv2.resize(citra, dimensi_baru, interpolation=cv2.INTER_AREA)

    biru, hijau, merah = cv2.split(citra_kecil)

    cv2.imshow('Kanal biru', biru)
    cv2.imshow('Kanal hijau', hijau)
    cv2.imshow('Kanal merah', merah)

    cv2.waitKey(0)
    cv2.destroyAllWindows()