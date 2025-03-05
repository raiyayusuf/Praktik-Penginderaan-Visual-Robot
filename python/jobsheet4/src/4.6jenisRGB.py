import cv2

path_gambar = r"C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\peppers2.jpg"

citra = cv2.imread(path_gambar, cv2.IMREAD_UNCHANGED)

if citra is None:
    print(f'Tidak dapat membaca berkas: {path_gambar}')
else:
    info = citra.shape
    if len(info) == 2:
        print('Citra berskala keabu-abuan')
    else:
        print('Citra berwarna')