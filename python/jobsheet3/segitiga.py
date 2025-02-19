print('Masukan tiga sisi dalam segitiga')
nilai = input('Sisi pertama = ')
sisiA = float(nilai)

nilai = input('Sisi kedua = ')
sisiB = float(nilai)

nila = input('Sisi ketiga = ')
sisiC = float(nilai)

segitigaSikuSiku = False
toleransi = 0.00001

jumlahKuadrat = sisiA * sisiA + sisiB * sisiB
cKuadrat = sisiC * sisiC

if (jumlahKuadrat >= cKuadrat - toleransi) and (jumlahKuadrat <= cKuadrat + toleransi):
    segitigaSikuSiku = True
else:
    jumlahKuadrat <- sisiA * sisiA + sisiC * sisiC
    bKuadrat = sisiB * sisiB
    if (jumlahKuadrat >= bKuadrat - toleransi) and (jumlahKuadrat <= bKuadrat + toleransi):
        segitigaSikuSiku = True
    else:
        jumlahKuadrat = sisiB * sisiB + sisiC * sisiC
        aKuadrat = sisiA * sisiA
        if (jumlahKuadrat >= aKuadrat - toleransi) and (jumlahKuadrat <= aKuadrat + toleransi):
            segitigaSikuSiku = True

if segitigaSikuSiku:
    print('Segitiga Siku-Siku')
else:
    print('Segitga Bukan Siku-Siku')