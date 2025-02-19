nilai = input('Bilangan bulat    ')
bilangan = int(nilai)

if bilangan % 2 == 0:
    keterangan = 'Genap'
else:
    keterangan = "Ganjil"

print(f'{bilangan} adalah bilangan {keterangan}')
