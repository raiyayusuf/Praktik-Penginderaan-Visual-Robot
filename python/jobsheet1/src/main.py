import cv2 
 
img = cv2.imread(r"C:\Raiya Yusuf Priatmojo\python\img\kucing2.jpg") 

cv2.imshow('cat',img) 
cv2.imwrite('save cat.png',img) 

cv2.waitKey(0) 
cv2.destroyAllWindows()