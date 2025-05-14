import cv2

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

print(f"hu[0] - {hu[0][0]}")
print(f"hu[1] - {hu[1][0]}")
print(f"hu[2] - {hu[2][0]}")
print(f"hu[3] - {hu[3][0]}")
print(f"hu[4] - {hu[4][0]}")
print(f"hu[5] - {hu[5][0]}")
print(f"hu[6] - {hu[6][0]}")