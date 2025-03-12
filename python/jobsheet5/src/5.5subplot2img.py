import cv2
from matplotlib import pyplot as plt

citra1 = cv2.imread('python\\jobsheet5\\img\\melon.png')
citra2 = cv2.imread(r'python\jobsheet5\img\peppers2.jpg')

scale_percent = 20
width1 = int(citra1.shape[1] * scale_percent / 100)
height1 = int(citra1.shape[0] * scale_percent / 100)
dim1 = (width1, height1)
resized1 = cv2.resize(citra1, dim1, interpolation=cv2.INTER_AREA)

width2 = int(citra2.shape[1] * scale_percent / 100)
height2 = int(citra2.shape[0] * scale_percent / 100)
dim2 = (width2, height2)
resized2 = cv2.resize(citra2, dim2, interpolation=cv2.INTER_AREA)

rgb1 = resized1[..., ::-1]
rgb2 = resized2[..., ::-1]

plt.subplot(121)
plt.imshow(rgb1)
plt.xticks([]), plt.yticks([])
plt.title('Kolom 1')

plt.subplot(122)
plt.imshow(rgb2)
plt.xticks([]), plt.yticks([])
plt.title('Kolom 2')

plt.show()