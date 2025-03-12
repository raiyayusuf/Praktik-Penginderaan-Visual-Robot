import cv2
import matplotlib.pyplot as plt

citra = cv2.imread(r'python\jobsheet5\img\peppers.jpg')

if citra is None:
    print("Error: Gambar tidak ditemukan atau tidak dapat dibaca.")
else:
    warna = ('b', 'g', 'r')
    for i, col in enumerate(warna):
        histo = cv2.calcHist([citra], [i], None, [256], [0, 256])
        plt.plot(histo, color=col)
        plt.xlim([0, 256])

    plt.title('Histogram Gambar')
    plt.xlabel('Intensitas Piksel')
    plt.ylabel('Jumlah Piksel')
    plt.show()