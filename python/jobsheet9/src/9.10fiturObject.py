import cv2
import math

path_gambar = r'python\jobsheet9\img\guppyBiru.png'
citra = cv2.imread(path_gambar, 0)

kontur, hierarki = cv2.findContours(citra, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

if kontur:
    kontur_pertama = kontur[0]

    kelilingObjek = cv2.arcLength(kontur_pertama, True)
    luasObjek = cv2.contourArea(kontur_pertama)
    x, y, lebar, tinggi = cv2.boundingRect(kontur_pertama)

    convex = cv2.convexHull(kontur_pertama)
    kelilingKonveks = cv2.arcLength(convex, True)
    luasKonveks = cv2.contourArea(convex)

    kebulatanBentuk = 4 * math.pi * luasObjek / (kelilingObjek * kelilingObjek)

    if tinggi > lebar:
        lebarObjek = lebar
        panjangObjek = tinggi
    else:
        lebarObjek = tinggi
        panjangObjek = lebar

    kerampinganBentuk = lebarObjek / panjangObjek
    konveksitas = kelilingKonveks / kelilingObjek
    soliditas = luasObjek / luasKonveks
    rasioPembatasObjek = luasObjek / (lebar * tinggi)

    print("Kebulatan bentuk =", kebulatanBentuk)
    print("Kerampingan bentuk =", kerampinganBentuk)
    print("Konveksitas bentuk =", konveksitas)
    print("Soliditas bentuk =", soliditas)
    print("Rasio pembatas objek =", rasioPembatasObjek)

else:
    print("Tidak ada kontur yang ditemukan.")