dataNilai = {'Muhammad Azzam Nur Alwi Mansyur': 100, 'Lovina Aulia': 90,
             'Ficri Hanip': 85, 'Yusuf Fadilah': 75, 'Shayid': 60, "Jilan": 50}

dataNilai['Lovina Aulia'] = 95  # ubah data
dataNilai.pop('Shayid')
del dataNilai['Yusuf Fadilah']

# cetal all
print('Data Nilai', dataNilai)
# cetak nilai or value nya saja
for nilai in dataNilai.values():
    print("Daftar Nilai", nilai)
# cetak key or index nya saja
for nama in dataNilai.keys():
    print("Daftar Mahasiswa:", nama)
# cetak all item secara manual
for nama, nilai in dataNilai.items():
    ket = ('Tidak Lulus', 'Lulus')[nilai > 75]
    print("Daftar Mahasiswa:", nama,
          '\nNilai:', nilai, "dinyatakan", ket)

# Penjelasan Dictionary :
# Dictionary bersifat mutable, artinya nilainya
# dapat kita ubah-ubah. Untuk mengubah nilai dictionary,
# kita bisa lakukan seperti ini:
# cth : nama_dic["kunci"] = "Nilai Baru"

# Cara Menghapus Dictionary :
# Method pop() = method yang berfungsi
# untuk mengeluarkan item dari dictionary.
# cth: nilai.pop('Azzam')

# Method del() = method yang berfungsi untuk
# menghapus suatu variabel dari memori
# cth: del nilai['Azzam']
