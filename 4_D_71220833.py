while True:
    a = input('Silahkan masukkan hari yang ingin Anda telusuri: ').lower()
    senin = [' ', 'Ngasdos PrakAlPro', 'Muaythai']
    selasa = ['Kelas Artificial Intelligence', 'Kelas RPLBO', 'Kelas ProgWeb', 'Ngerjain Tugas ProgWeb', 'Bikin Soal UG PrakAlpro', 'Seminar Cyber Security']
    rabu = ['Kelas PrakRBLBO', 'kelas PrakProgWeb', 'Kelas Pendidikan Pancasila', 'Kelas EtProf', 'Ngasdos PrakAlPro', 'Ngerjain Tugas Keamanan Komputer']
    kamis = ['Kelas Keamanan Komputer', ' ', 'Ngasdos PrakJarKom']
    jumat = ['Kelas PrakRPLBO', ' ', 'Mengoreksi Unguided PrakAlPro', 'Mengoreksi Tugas PrakJarKom', 'Muaythai']
    sabtu = [' ', 'Photoshoot', ' ', 'Muaythai']
    if a == 'senin':
        for i in range(len(senin)):
            if senin[i] != ' ':
                print(f"Sesi ke-{i+1}: {senin[i]}")
        break
    elif a == 'selasa':
        for i in range(len(selasa)):
            if selasa[i] != ' ':
                print(f"Sesi ke-{i+1}: {selasa[i]}")
        break
    elif a == 'rabu':
        for i in range(len(rabu)):
            if rabu[i] != ' ':
                print(f"Sesi ke-{i+1}: {rabu[i]}")
        break
    elif a == 'kamis':
        for i in range(len(kamis)):
            if kamis[i] != ' ':
                print(f"Sesi ke-{i+1}: {kamis[i]}")
        break
    elif a == 'jumat':
        for i in range(len(jumat)):
            if jumat[i] != '':
                print(f"Sesi ke-{i+1}: {jumat[i]}")
        break
    elif a == 'sabtu':
        for i in range(len(sabtu)):
            if sabtu[i] != ' ':
                print(f"Sesi ke-{i+1}: {jumat[i]}")
        break
    else:
        print('Input yang anda masukkan tidak valid')