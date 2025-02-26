import cv2


citra = cv2.imread(r"C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\kucingCape.png", cv2.IMREAD_UNCHANGED)

bagianA = citra[0:100, ...]

bagianB = citra[..., 250:]

cv2.imshow('Bagian A', bagianA)
cv2.imshow('Bagian B', bagianB)

cv2.waitKey(0)
cv2.destroyAllWindows()