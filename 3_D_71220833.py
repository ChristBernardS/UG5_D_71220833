import math
while True:
    a = input('Masukkan jarak awal (dalam meter): ')
    try:
        a = int(a)
        b = []
        for i in range(5, 7):
            x = input(f'Masukkan sudut elevasi pada menit ke-{i} (dalam derajat): ')
            b.append(x)
        c = int(b[0])
        d = int(b[1])
        e = abs(a*math.tan(c))
        f = abs(a*math.tan(d)-math.tan(c))
        g = abs(f*math.tan(d))
        print(f'Ketinggian drone pada menit ke-5 adalah {round(e, ndigits=2)} meter')
        print(f'Selisih ketinggian drone saat menit ke-5 dan ke-6 adalah {round(g, ndigits=2)} meter')
    except:
        break