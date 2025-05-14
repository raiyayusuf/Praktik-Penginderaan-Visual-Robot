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

huMoments = cv2.HuMoments(mom)

print("Hu Moments:")
for i, hu in enumerate(huMoments):
    print(f"Hu[{i+1}] - {hu[0]}")

mu20 = mom['mu20']
mu11 = mom['mu11']
mu02 = mom['mu02']
mu30 = mom['mu30']
mu21 = mom['mu21']
mu12 = mom['mu12']
mu03 = mom['mu03']
m00 = mom['m00']

if m00 != 0:
    nu20 = mu20 / (m00 ** (1 + 2/2))
    nu11 = mu11 / (m00 ** (1 + (1+1)/2))
    nu02 = mu02 / (m00 ** (1 + 2/2))
    nu30 = mu30 / (m00 ** (1 + 3/2))
    nu21 = mu21 / (m00 ** (1 + (2+1)/2))
    nu12 = mu12 / (m00 ** (1 + (1+2)/2))
    nu03 = mu03 / (m00 ** (1 + 3/2))
else:
    nu20 = 0
    nu11 = 0
    nu02 = 0
    nu30 = 0
    nu21 = 0
    nu12 = 0
    nu03 = 0

print("\nMomen Ternormalisasi (nu):")
print(f"nu20 - {nu20}")
print(f"nu11 - {nu11}")
print(f"nu02 - {nu02}")
print(f"nu30 - {nu30}")
print(f"nu21 - {nu21}")
print(f"nu12 - {nu12}")
print(f"nu03 - {nu03}")