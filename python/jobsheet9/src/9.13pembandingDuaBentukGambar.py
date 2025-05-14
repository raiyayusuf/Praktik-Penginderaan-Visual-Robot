import cv2

path_guppi1 = r"python\jobsheet9\img\guppyBiru.png"
path_guppi2 = r"python\jobsheet9\img\guppyKuning.png"
path_guppi3 = r"python\jobsheet9\img\guppyMerah.png"
path_guppi4 = r"python\jobsheet9\img\guppyPutih.png"
path_guppi5 = r"python\jobsheet9\img\guppyUngu.png"

guppi1 = cv2.imread(path_guppi1, 0)
guppi2 = cv2.imread(path_guppi2, 0)
guppi3 = cv2.imread(path_guppi3, 0)
guppi4 = cv2.imread(path_guppi4, 0)
guppi5 = cv2.imread(path_guppi5, 0)

if guppi1 is None or guppi2 is None or guppi3 is None or guppi4 is None or guppi5 is None:
    print("Error: Could not open or read one or more image files.")
    exit()

kontur_guppi1, _ = cv2.findContours(guppi1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
kontur_guppi2, _ = cv2.findContours(guppi2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
kontur_guppi3, _ = cv2.findContours(guppi3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
kontur_guppi4, _ = cv2.findContours(guppi4, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
kontur_guppi5, _ = cv2.findContours(guppi5, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

if not kontur_guppi1 or not kontur_guppi2 or not kontur_guppi3 or not kontur_guppi4 or not kontur_guppi5:
    print("Error: Could not find contours in one or more images.")
    exit()

jarakA = cv2.matchShapes(kontur_guppi2[0], kontur_guppi1[0], cv2.CONTOURS_MATCH_I1, 0)
jarakB = cv2.matchShapes(kontur_guppi3[0], kontur_guppi1[0], cv2.CONTOURS_MATCH_I1, 0)
jarakC = cv2.matchShapes(kontur_guppi4[0], kontur_guppi1[0], cv2.CONTOURS_MATCH_I1, 0)
jarakD = cv2.matchShapes(kontur_guppi5[0], kontur_guppi1[0], cv2.CONTOURS_MATCH_I1, 0)

print(f"guppi-2 terhadap guppi-1 = {jarakA}")
print(f"guppi-3 terhadap guppi-1 = {jarakB}")
print(f"guppi-4 terhadap guppi-1 = {jarakC}")
print(f"guppi-5 terhadap guppi-1 = {jarakD}")