import cv2

citra = cv2.imread(r"C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\peppers.jpg")

citra[180:490, 170:425] = [255, 0, 0]

cv2.imshow('Hasil', citra)
cv2.waitKey(0)
cv2.destroyAllWindows()