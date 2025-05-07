import cv2

minKontur = 100
maxKontur = 400

path_gambar = r'python\jobsheet9\img\abc.png'

citra = cv2.imread(path_gambar, 0)
citraBerwarna = cv2.cvtColor(citra, cv2.COLOR_GRAY2BGR)
kontur, hierarki = cv2.findContours(citra, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for indeks in range(len(kontur)):
    panjangKontur = cv2.arcLength(kontur[indeks], True)
    if (panjangKontur >= minKontur) and (panjangKontur <= maxKontur):
        cv2.drawContours(citraBerwarna, kontur, indeks, (255, 255, 0), 3)
        
cv2.imshow("Hasil", citraBerwarna)
cv2.waitKey(0)
cv2.destroyAllWindows()