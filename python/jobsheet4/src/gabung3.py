import cv2

lena = cv2.imread(r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\spaceman.png', cv2.IMREAD_UNCHANGED)
baboon = cv2.imread(r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\peppers2.jpg')

if lena is None:
    print("Error: Gambar lena tidak ditemukan atau tidak dapat dibaca.")
elif baboon is None:
    print("Error: Gambar baboon tidak ditemukan atau tidak dapat dibaca.")
else:
    if lena.shape[2] == 4:
        lena = cv2.cvtColor(lena, cv2.COLOR_BGRA2BGR)

    if lena.shape != baboon.shape:
        baboon = cv2.resize(baboon, (lena.shape[1], lena.shape[0]), interpolation=cv2.INTER_AREA)

    hasilA = cv2.addWeighted(baboon, 0.5, lena, 0.5, 0)
    cv2.imshow('Alfa: 0.5, beta: 0.5, gamma: 0', hasilA)

    hasilB = cv2.addWeighted(baboon, 0.7, lena, 0.3, 0)
    cv2.imshow('Alfa: 0.7, beta: 0.3, gamma: 0', hasilB)

    hasilC = cv2.addWeighted(baboon, 0.3, lena, 0.7, 0)
    cv2.imshow('Alfa: 0.3, beta: 0.7, gamma: 0', hasilC)

    cv2.waitKey(0)
    cv2.destroyAllWindows()