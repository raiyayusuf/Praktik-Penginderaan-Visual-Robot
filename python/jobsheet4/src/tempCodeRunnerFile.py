
# Periksa apakah gambar berhasil dibaca
if lena is None:
    print("Error: Gambar lena tidak ditemukan atau tidak dapat dibaca.")
elif baboon is None:
    print("Error: Gambar baboon tidak ditemukan atau tidak dapat dibaca.")
else:
    # Pastikan kedua gambar memiliki ukuran yang sama
    if lena.shape != baboon.shape:
        # Resize gambar baboon agar sesuai dengan ukuran gambar lena
        baboon = cv2.resize(baboon, (lena.shape[1], lena.shape[0]), interpolation=cv2.INTER_AREA)

    # Parameter untuk cv2.addWeighted
    alfa = 0.5  # Kontribusi gambar lena
    beta = 0.5  # Kontribusi gambar baboon
    gamma = 0   # Nilai tambahan (biasanya 0)

    # Gabungkan kedua gambar dengan cv2.addWeighted
    hasil = cv2.addWeighted(lena, alfa, baboon, beta, gamma)

    # Tampilkan hasil
    cv2.imshow('Hasil', hasil)

    # Tunggu input dari pengguna