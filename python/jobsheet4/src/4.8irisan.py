import cv2

citra = cv2.imread(r"C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\kucingCape.png")

bagian = citra[180:490, 170:425]

cv2.imshow('Irisan', bagian)
cv2.waitKey(0)