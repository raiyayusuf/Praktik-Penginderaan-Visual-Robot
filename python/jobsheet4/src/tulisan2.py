import cv2

path_gambar = r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\kucingCape.png'

citra = cv2.imread(path_gambar, cv2.IMREAD_UNCHANGED)

if citra is None:
    print(f"Tidak dapat membaca gambar: {path_gambar}")
else:
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX | cv2.FONT_ITALIC
    cv2.putText(citra, 'Koceengg', (60, 280), font, 3, (255, 255, 255), 2) 

    cv2.imshow('Hasil', citra)

    cv2.waitKey(0)
    cv2.destroyAllWindows()