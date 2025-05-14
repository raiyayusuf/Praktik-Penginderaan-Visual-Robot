import cv2
import math

def perolehFitur(berkasCitra):
    citra = cv2.imread(berkasCitra, 0)
    if citra is None:
        print(f"Error: Could not open or read image: {berkasCitra}")
        return None, None, None, None, None
    kontur, hierarki = cv2.findContours(citra, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if not kontur:
        print(f"Error: No contours found in image: {berkasCitra}")
        return None, None, None, None, None
    kelilingObjek = cv2.arcLength(kontur[0], True)
    luasObjek = cv2.contourArea(kontur[0], False)
    x, y, lebar, tinggi = cv2.boundingRect(kontur[0])
    convex = cv2.convexHull(kontur[0])
    kelilingKonveks = cv2.arcLength(convex, True)
    luasKonveks = cv2.contourArea(convex, False)
    if kelilingObjek > 0:
        kebulatanBentuk = 4 * math.pi * luasObjek / (kelilingObjek * kelilingObjek)
    else:
        kebulatanBentuk = 0
    if tinggi > lebar:
        lebarObjek = lebar
        panjangObjek = tinggi
    else:
        lebarObjek = tinggi
        panjangObjek = lebar
    kerampinganBentuk = lebarObjek / panjangObjek if panjangObjek > 0 else 0
    konveksitas = kelilingKonveks / kelilingObjek if kelilingObjek > 0 else 0
    soliditas = luasObjek / luasKonveks if luasKonveks > 0 else 0
    mom = cv2.moments(kontur[0])
    hu = cv2.HuMoments(mom)
    return kerampinganBentuk, kebulatanBentuk, konveksitas, soliditas, hu

def jarakEuclidean(fx1, fx2, fx3, fx4, huX, fy1, fy2, fy3, fy4, huY):
    jarak = (fx1 - fy1) ** 2 + (fx2 - fy2) ** 2 + \
            (fx3 - fy3) ** 2 + (fx4 - fy4) ** 2
    for indeks in range(0, 7):
        jarak += (huX[indeks][0] - huY[indeks][0]) ** 2
    jarak = math.sqrt(jarak)
    return jarak

ftA1, ftA2, ftA3, ftA4, huA = perolehFitur(r"python\jobsheet9\img\guppyBiru.png")
ftB1, ftB2, ftB3, ftB4, huB = perolehFitur(r"python\jobsheet9\img\guppyKuning.png")
ftE1, ftE2, ftE3, ftE4, huE = perolehFitur(r"python\jobsheet9\img\guppyUngu.png")
ftD1, ftD2, ftD3, ftD4, huD = perolehFitur(r"python\jobsheet9\img\guppyPutih.png")
ftC1, ftC2, ftC3, ftC4, huC = perolehFitur(r"python\jobsheet9\img\guppyMerah.png")

if ftA1 is not None and ftB1 is not None:
    jarakBA = jarakEuclidean(ftB1, ftB2, ftB3, ftB4, huB, ftA1, ftA2, ftA3, ftA4, huA)
    print(f"guppi-2 = {jarakBA}")

if ftA1 is not None and ftC1 is not None:
    jarakCA = jarakEuclidean(ftC1, ftC2, ftC3, ftC4, huC, ftA1, ftA2, ftA3, ftA4, huA)
    print(f"guppi-3 = {jarakCA}")

if ftA1 is not None and ftD1 is not None:
    jarakDA = jarakEuclidean(ftD1, ftD2, ftD3, ftD4, huD, ftA1, ftA2, ftA3, ftA4, huA)
    print(f"guppi-4 = {jarakDA}")

if ftA1 is not None and ftE1 is not None:
    jarakEA = jarakEuclidean(ftE1, ftE2, ftE3, ftE4, huE, ftA1, ftA2, ftA3, ftA4, huA)
    print(f"guppi-5 = {jarakEA}")