import cv2
import numpy as np
from matplotlib import pyplot as plt

citra = cv2.imread('python/jobsheet5/img/melon.png', 0)
ekual = cv2.equalizeHist(citra)

scale_percent = 20
width = int(citra.shape[1] * scale_percent / 100)
height = int(citra.shape[0] * scale_percent / 100)
dim = (width, height)
citra_resized = cv2.resize(citra, dim)
ekual_resized = cv2.resize(ekual, dim)

plt.subplot(121)        
plt.imshow(citra_resized, cmap = plt.get_cmap('gray'), vmin = 0, vmax = 255)
plt.xticks([]), plt.yticks([])
plt.title('Citra semula')

plt.subplot(122)
plt.imshow(ekual_resized, cmap = plt.get_cmap('gray'), vmin = 0, vmax = 255)
plt.xticks([]), plt.yticks([])
plt.title('Citra hasil')

plt.show()