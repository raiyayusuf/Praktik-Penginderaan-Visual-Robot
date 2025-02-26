import cv2

path_gambar = r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\kucingCape.png'

citra = cv2.imread(path_gambar, cv2.IMREAD_GRAYSCALE)

if citra is None:
    print(f"Tidak dapat membaca gambar: {path_gambar}")
else:
    ambang, biner = cv2.threshold(citra, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    cv2.imshow('Asli', citra)
    cv2.imshow(f'Otsu - nilai ambang = {int(ambang)}', biner)

    cv2.waitKey(0)
    cv2.destroyAllWindows()