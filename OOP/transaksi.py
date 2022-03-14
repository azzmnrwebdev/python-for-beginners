from Bank import *

# Ciptakan Object
gigi = Bank('011021', 'Muhammad Azzam Nur Alwi Mansyur', 50000000)
cr7 = Bank('011022', 'Ronaldo', 70000000)
leo = Bank('011023', 'Messi', 90000000)
vina = Bank('011024', 'Lovina AUlia', 1000000000)

# gunakan fungsi-fungsi yang tersedia di class Bank
gigi.nabung(100000000)
leo.nabung(20000000)
cr7.tarik(23000000)
leo.tarik(5000000)
gigi.tarik(70000000)

# cetak nasabah
gigi.cetak()
cr7.cetak()
leo.cetak()
vina.cetak()
print('Jumlah Nasabah: ', Bank.jumlahNasabah)
