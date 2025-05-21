import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
from operator import itemgetter

def fSegitiga(a, b, c, h):
    if h == b:
        derajat = 1.0
    elif h > a and h < b:
        derajat = (h - a) / (b - a)
    elif h > b and h < c:
        derajat = (c - h) / (c - b)
    else:
        derajat = 0.0
    return derajat

def fSegitigaKiri(a, b, h):
    if h == b:
        derajat = 1.0
    elif h > a and h < b:
        derajat = (h - a) / (b - a)
    else:
        derajat = 0.0
    return derajat

def fSegitigaKanan(a, b, h):
    if h == a:
        derajat = 1.0
    elif h > a and h < b:
        derajat = (b - h) / (b - a)
    else:
        derajat = 0.0
    return derajat

def fTrapesium(a, b, c, d, h):
    if h > a and h < b:
        derajat = (h - a) / (b - a)
    elif h >= b and h <= c:
        derajat = 1.0
    elif h > c and h < d:
        derajat = (d - h) / (d - c)
    else:
        derajat = 0.0
    return derajat

def fMerah(h, s, v):
    if (h == 0 and s == 0) or (v == 0):
        derajat = 0.0
    else:
        derajat = fSegitigaKanan(170, 21, h) + fSegitigaKiri(190, 255, h)
    return derajat

def fHijau(h, s, v):
    if (h == 0 and s == 0) or (v == 0):
        derajat = 0.0
    else:
        derajat = fTrapesium(43, 65, 105, 128, h)
    return derajat

def fKuning(h, s, v):
    if (h == 0 and s == 0) or (v == 0):
        derajat = 0.0
    else:
        derajat = fSegitiga(21, 43, 65, h)
    return derajat

def fBiru(h, s, v):
    if (h == 0 and s == 0) or (v == 0):
        derajat = 0.0
    else:
        derajat = fTrapesium(128, 155, 180, 191, h)
    return derajat

def fUngu(h, s, v):
    if (h == 0 and s == 0) or (v == 0):
        derajat = 0.0
    else:
        derajat = fSegitiga(180, 191, 213, h)
    return derajat

def fCyan(h, s, v):
    if (h == 0 and s == 0) or (v == 0):
        derajat = 0.0
    else:
        derajat = fSegitiga(105, 128, 155, h)
    return derajat

def fOrange(h, s, v):
    if (h == 0 and s == 0) or (v == 0):
        derajat = 0.0
    else:
        derajat = fSegitiga(0, 21, 43, h)
    return derajat

def fMagenta(h, s, v):
    if (h == 0 and s == 0) or (v == 0):
        derajat = 0.0
    else:
        derajat = fSegitiga(191, 213, 234, h)
    return derajat

def fPink(h, s, v):
    if (h == 0 and s == 0) or (v == 0):
        derajat = 0.0
    else:
        derajat = fSegitiga(213, 234, 255, h)
    return derajat

def fPutih(h, s, v):
    if s <= 10 and v >= 250:
        derajat = 1.0
    else:
        derajat = 0.0
    return derajat

def fAbuAbu(h, s, v):
    if h == 0 and (s > 15 and v < 250):
        derajat = 1.0
    else:
        derajat = 0.0
    return derajat

def fHitam(h, s, v):
    if h == 0 and s == 0 and v < 15:
        derajat = 1.0
    else:
        derajat = 0.0
    return derajat

def cariWarna(warna, lokdir):
    senarai = [] # Kosongkan senarai
    # Proses untuk mendapatkan nama-nama berkas
    for root, direktori, daftarBerkas in os.walk(lokdir):
        for namaBerkas in daftarBerkas:
            print(namaBerkas)
            citra = cv2.imread(lokdir + "/" + namaBerkas)
            if citra is None:
                continue
            tinggi, lebar = citra.shape[:2]
            # Konversi ke HSV
            hsv = cv2.cvtColor(citra, cv2.COLOR_BGR2HSV)
            nilaiAnggota = 0.0
            anggotaMerah = 0.0
            anggotaBiru = 0.0
            anggotaCyan = 0.0
            anggotaHijau = 0.0
            anggotaMagenta = 0.0
            anggotaOranye = 0.0
            anggotaPink = 0.0
            anggotaUngu = 0.0
            anggotaPutih = 0.0
            anggotaHitam = 0.0
            anggotaAbuAbu = 0.0
            anggotaKuning = 0.0
            # Proses untuk semua piksel dalam sebuah citra
            for y in range(0, tinggi):
                for x in range(0, lebar):
                    h = hsv[y, x, 0]
                    s = hsv[y, x, 1]
                    v = hsv[y, x, 2]
                    nilaiAnggotaMerah = fMerah(h, s, v)
                    if nilaiAnggotaMerah > 0:
                        anggotaMerah += nilaiAnggotaMerah
                    nilaiAnggotaBiru = fBiru(h, s, v)
                    if nilaiAnggotaBiru > 0:
                        anggotaBiru += nilaiAnggotaBiru
                    nilaiAnggotaCyan = fCyan(h, s, v)
                    if nilaiAnggotaCyan > 0:
                        anggotaCyan += nilaiAnggotaCyan
                    nilaiAnggotaHijau = fHijau(h, s, v)
                    if nilaiAnggotaHijau > 0:
                        anggotaHijau += nilaiAnggotaHijau
                    nilaiAnggotaMagenta = fMagenta(h, s, v)
                    if nilaiAnggotaMagenta > 0:
                        anggotaMagenta += nilaiAnggotaMagenta
                    nilaiAnggotaOranye = fOrange(h, s, v)
                    if nilaiAnggotaOranye > 0:
                        anggotaOranye += nilaiAnggotaOranye
                    nilaiAnggotaKuning = fKuning(h, s, v)
                    if nilaiAnggotaKuning > 0:
                        anggotaKuning += nilaiAnggotaKuning
                    nilaiAnggotaPink = fPink(h, s, v)
                    if nilaiAnggotaPink > 0:
                        anggotaPink += nilaiAnggotaPink
                    nilaiAnggotaUngu = fUngu(h, s, v)
                    if nilaiAnggotaUngu > 0:
                        anggotaUngu += nilaiAnggotaUngu
                    nilaiAnggotaPutih = fPutih(h, s, v)
                    if nilaiAnggotaPutih > 0:
                        anggotaPutih += nilaiAnggotaPutih
                    nilaiAnggotaHitam = fHitam(h, s, v)
                    if nilaiAnggotaHitam > 0:
                        anggotaHitam += nilaiAnggotaHitam
                    nilaiAnggotaAbuAbu = fAbuAbu(h, s, v)
                    if nilaiAnggotaAbuAbu > 0:
                        anggotaAbuAbu += nilaiAnggotaAbuAbu
            maks = max(anggotaMerah, anggotaBiru, anggotaCyan, anggotaHijau, anggotaMagenta, anggotaOranye, anggotaPink, anggotaUngu, anggotaPutih, anggotaHitam, anggotaAbuAbu, anggotaKuning)
            bobot = 0
            if warna == "merah":
                if maks == anggotaMerah:
                    bobot = maks
            elif warna == "biru":
                if maks == anggotaBiru:
                    bobot = maks
            elif warna == "cyan":
                if maks == anggotaCyan:
                    bobot = maks
            elif warna == "hijau":
                if maks == anggotaHijau:
                    bobot = maks
            elif warna == "magenta":
                if maks == anggotaMagenta:
                    bobot = maks
            elif warna == "jingga":
                if maks == anggotaOranye:
                    bobot = maks
            elif warna == "pink":
                if maks == anggotaPink:
                    bobot = maks
            elif warna == "ungu":
                if maks == anggotaUngu:
                    bobot = maks
            elif warna == "putih":
                if maks == anggotaPutih:
                    bobot = maks
            elif warna == "hitam":
                if maks == anggotaHitam:
                    bobot = maks
            elif warna == "abu-abu":
                if maks == anggotaAbuAbu:
                    bobot = maks
            elif warna == "kuning":
                if maks == anggotaKuning:
                    bobot = maks
            # Sisipkan ke senarai
            if bobot > 0:
                senarai.append((namaBerkas, bobot))
    # Pengurutan senarai menurut bobot secara urut turun
    sorted(senarai, key=itemgetter(1), reverse=True)
    jum = len(senarai)
    print("Jumlah citra =", jum)
    if jum > 24:
        n = 4
        m = int((jum + 3) / n)
        print("m =", m, ", n =", n)
    else:
        m = jum
        n = 1
    # Susun citra
    indeks = 0
    plt.figure(figsize=(12, 12))
    for baris in range(0, m):
        for kolom in range(0, n):
            if indeks < jum:
                namaBerkas = senarai[indeks][0]
                citra = cv2.imread(lokdir + "/" + namaBerkas)
                if citra is not None:
                    rgb = cv2.cvtColor(citra, cv2.COLOR_BGR2RGB)
                    plt.subplot(m, n, indeks + 1)
                    plt.imshow(rgb)
                    plt.xticks([]), plt.yticks([])
                    plt.title(senarai[indeks][0], size=8)
                    indeks += 1
    # Tampilkan citra
    plt.show()
    return

# Program utama
warnaDicari = "merah"
lokasiDirektori = r"python\jobsheet10\img\kotakWarna.jpg" # Perhatikan: ini adalah path file, bukan direktori
if os.path.isdir(lokasiDirektori):
    cariWarna(warnaDicari, lokasiDirektori)
else:
    print(f"Error: Direktori '{lokasiDirektori}' tidak ditemukan.")