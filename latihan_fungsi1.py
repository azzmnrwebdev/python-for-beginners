def hitungUmur(tahun_ini):
    nama = input("Nama: ")
    tahunLahir = int(input('Tahun Lahir: '))
    umur = tahun_ini - tahunLahir

    # cetak umur
    print("Mahasiswa bernama %s lahir tahun %i berumur %i tahun" %
          (nama, tahunLahir, umur))


# panggil fungsi
hitungUmur(2035)
