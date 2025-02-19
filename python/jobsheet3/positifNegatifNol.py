nilai = input('Bilangan bulat   ')
bilangan = int(nilai)

if bilangan == 0:
    keterangan = 'Nol'
elif bilangan > 0:
    keterangan = "Positif"
else:
    keterangan = 'Negatif'

print(f'{bilangan} adalah bilangan {keterangan}')