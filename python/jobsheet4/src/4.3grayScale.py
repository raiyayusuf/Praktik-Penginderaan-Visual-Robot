import cv2

path_image = r"C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\image\kucingHitamPutih.jpg"

citra = cv2.imread(path_image, cv2.IMREAD_GRAYSCALE)
if citra is not None:
    cv2.imshow('Gambar Koceng', citra)
    cv2.waitKey(0)

