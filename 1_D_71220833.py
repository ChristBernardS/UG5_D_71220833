def ganti_kata(x, y, z):
    for i in range(len(a)):
        if b == a[i]:
            a[i] = c
    d = (' '.join(a))
    print(f"Kalimat baru : {d}")

a = input('Masukkan kalimat : ').split(' ')
b = input('Kata yang dicari : ')
c = input('Diganti menjadi : ')
ganti_kata(a, b, c)