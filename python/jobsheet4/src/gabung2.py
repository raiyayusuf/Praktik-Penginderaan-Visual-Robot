import cv2

lena = cv2.imread(r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\spaceman.png')
baboon = cv2.imread(r'C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\peppers2.jpg')

if lena is None:
    print("Error: Gambar lena tidak ditemukan atau tidak dapat dibaca.")
elif baboon is None:
    print("Error: Gambar baboon tidak ditemukan atau tidak dapat dibaca.")
else:
    if lena.shape != baboon.shape:
        baboon = cv2.resize(baboon, (lena.shape[1], lena.shape[0]), interpolation=cv2.INTER_AREA)

    alfa = 0.5  
    beta = 0.5  
    gamma = 0 

    hasil = cv2.addWeighted(lena, alfa, baboon, beta, gamma)

    cv2.imshow('Hasil', hasil)

    cv2.waitKey(0)
    cv2.destroyAllWindows()