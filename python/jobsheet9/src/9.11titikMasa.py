import cv2

path_gambar = r"python\jobsheet9\img\abcd.png"
citra = cv2.imread(path_gambar, 0)

citraBerwarna = cv2.merge((citra, citra, citra))

kontur, hierarki = cv2.findContours(citra, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for k in kontur:
    mom = cv2.moments(k)
    if mom["m00"] != 0:
        x = int(mom["m10"] / mom["m00"])
        y = int(mom["m01"] / mom["m00"])
        cv2.circle(citraBerwarna, (x, y), 3, (255, 255, 0), -1)

cv2.imshow("Hasil", citraBerwarna)
cv2.waitKey(0)
cv2.destroyAllWindows()