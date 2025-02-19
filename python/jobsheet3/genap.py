nilai = input('Bilangan Bulat    ')
bilangan = int(nilai)

keterangan = 'Ganjil'
if bilangan % 2 == 0:
    keterangan = 'Genap'

print(f'{bilangan} adalah bilangan {keterangan}')