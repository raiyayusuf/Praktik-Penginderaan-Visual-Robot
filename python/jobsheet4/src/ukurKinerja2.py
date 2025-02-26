import cv2

path_gambar = r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\kucingCape.png'

citra = cv2.imread(path_gambar, cv2.IMREAD_GRAYSCALE)

if citra is None:
    print(f"Tidak dapat membaca gambar: {path_gambar}")
else:
    ambang, binerA = cv2.threshold(citra, 128, 255, cv2.THRESH_BINARY)
    ambang, binerB = cv2.threshold(citra, 128, 255, cv2.THRESH_BINARY_INV)

    cv2.imshow('Asli', citra)
    cv2.imshow('THRESH_BINARY', binerA)
    cv2.imshow('THRESH_BINARY_INV', binerB)

    cv2.waitKey(0)
    cv2.destroyAllWindows()