import cv2
import math

path_gambar = r"python\jobsheet9\img\guppyBiru.png"
citra = cv2.imread(path_gambar, 0)

if citra is None:
    print(f"Error: Could not open or read the image at: {path_gambar}")
    exit()

kontur, hierarki = cv2.findContours(citra, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

if not kontur:
    print("Error: No contours found in the image.")
    exit()

mom = cv2.moments(kontur[0])
hu = cv2.HuMoments(mom)

print("Momen Hu dengan penerapan logaritma:")
for i in range(0, 7):
    hu[i] = -1 * math.copysign(1.0, hu[i]) * math.log10(abs(hu[i]))
    print(f"hu[{i}] - {hu[i][0]}")