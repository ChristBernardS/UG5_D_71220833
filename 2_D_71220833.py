def hitung_mobil(x):
    solo = 0
    surabaya = 0
    jogja = 0
    magelang = 0
    for i in range(len(x)):
        if x[i] == 'solo':
            solo += 1
        elif x[i] == 'surabaya':
            surabaya += 1
        elif x[i] == 'jogja':
            jogja += 1
        elif x[i] == 'magelang':
            magelang += 1
    print(f"Jumlah mobil Solo\t: {solo}")
    print(f"Jumlah mobil Surabaya\t: {surabaya}")
    print(f"Jumlah mobil Jogja\t: {jogja}")
    print(f"Jumlah mobil Magelang\t: {magelang}")

c = []
while True:
    a = input('Masukkan asal mobil (ketik "done" untuk keluar): ').lower()
    c.append(a)
    if a == "done":
        break

hitung_mobil(c)