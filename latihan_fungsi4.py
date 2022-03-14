def hitungGaji():
    # ----------- Input Data ------------
    nama = input('Nama Pegawai\t: ')
    jabatan = input("Jabatan\t\t: ")
    agama = input('Agama\t\t: ')
    jumlah = int(input("Jumlah Anak\t: "))
    # ----------- Tentukan Gapok ----------

    def gapok(jabatan):
        return{
            'General Manager': 20000000,
            'Manager': 10000000,
            "Staf": 5000000
        }[jabatan]

    # ---------- Tunjangan Jabatan ---------
    tunjab = 0.2 * gapok(jabatan)

    # ---------- Tunjangan Keluarga ----------
    persen = 0.1
    if(jumlah > 0 and jumlah < 4):
        tunkel = gapok(jabatan) * persen
    elif(jumlah > 3):
        tunkel = gapok(jabatan) * persen * (jumlah-(jumlah - 3))
    else:
        tunkel = 0

    # --------- Tentukan Gaji Kotor ----------
    gajiKotor = gapok(jabatan) + tunkel

    # --------- Tentukan Zakat ----------
    zakat = (0, 0.025 * gajiKotor)[gajiKotor >= 6000000 and agama == "Islam"]

    # --------- Tentukan Gaji Bersih -----------
    gajiBersih = gapok(jabatan) + tunkel - zakat

    # cetak data
    print('Nama Pegawai\t: %s'
          "\nJabatan\t\t: %s"
          '\nAgama\t\t: %s'
          "\nJumlah Anak\t: %i"
          '\nGaji Pokok\t: %i'
          "\nTunj Jabatan\t: %i"
          '\nGaji Kotor\t: %i'
          "\nZakat Profesi\t: %i"
          '\nGaji Bersih\t: %i' % (nama, jabatan, agama, jumlah, gapok(jabatan), tunjab, gajiKotor, zakat, gajiBersih))


# panggil fungsi
hitungGaji()
