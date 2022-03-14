print('----------- Cetak Angka 1 - 20 ---------------')
angka = 20
for no in range(angka):
    no += 1  # no = no + 1, menggunakan assigment
    print('angka', no)

# cetak bilangan genap
print('----------- Cetak Bilangan Genap diantara 1 - 20 ---------------')
angka = 20
for no in range(angka):
    no += 1  # no = no + 1, menggunakan assigment
    if(no % 2 == 0):
        print('Bill. Genap', no)

# cetak bilangan ganjil
print('----------- Cetak Bilangan Ganjil diantara 1 - 20 ---------------')
angka = 20
for no in range(angka):
    no += 1  # no = no + 1, menggunakan assigment
    if(no % 2 == 1):
        print('Bill. Ganjil', no)
