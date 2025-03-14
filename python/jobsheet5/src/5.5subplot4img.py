import cv2
from matplotlib import pyplot as plt

citra1 = cv2.imread(r'python\jobsheet5\img\melon.png')
citra2 = cv2.imread('python\\jobsheet5\\img\\peppers.jpg')
citra3 = cv2.imread(r'python\jobsheet5\img\peppers2.jpg')
citra4 = cv2.imread(r'python\jobsheet5\img\melon.png')

if citra1 is None or citra2 is None or citra3 is None or citra4 is None:
    print("Error: Salah satu gambar tidak dapat dibuka. Periksa path gambar.")
    exit()

    scale_percent = 20
    width = int(citra1.shape[1] * scale_percent / 100)
    height = int(citra1.shape[0] * scale_percent / 100)
    dim = (width, height)

resized1 = cv2.resize(citra1, dim, interpolation=cv2.INTER_AREA)
resized2 = cv2.resize(citra2, dim, interpolation=cv2.INTER_AREA)
resized3 = cv2.resize(citra3, dim, interpolation=cv2.INTER_AREA)
resized4 = cv2.resize(citra4, dim, interpolation=cv2.INTER_AREA)

rgb1 = resized1[..., ::-1]
rgb2 = resized2[..., ::-1]
rgb3 = resized3[..., ::-1]
rgb4 = resized4[..., ::-1]
plt.subplot(221)
plt.imshow(rgb1)
plt.xticks([]), plt.yticks([])
plt.title('Gambar1')

plt.subplot(222)
plt.imshow(rgb2)
plt.xticks([]), plt.yticks([])
plt.title('Gambar2')

plt.subplot(223)
plt.imshow(rgb3)
plt.xticks([]), plt.yticks([])
plt.title('Gambar3')

plt.subplot(224)
plt.imshow(rgb4)
plt.xticks([]), plt.yticks([])
plt.title('Gambar4')

plt.show()