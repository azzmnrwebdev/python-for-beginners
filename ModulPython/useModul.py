import myModul as hitung
import myModul
from myModul import bagi
from myModul import *
from myModul import kurang as k, bagi as b
print('--------- Panggil Modul ----------')
myModul.tambah(10, 5)
myModul.kurang(10, 5)
myModul.kali(3, 5)
myModul.pangkat(2, 3)
myModul.akar(9)

print('--------- Panggil Modul Cara kedua di aliaskan ----------')
hitung.tambah(10, 5)
hitung.kurang(10, 5)
hitung.kali(3, 5)
hitung.pangkat(2, 3)
hitung.akar(9)

print('--------- Panggil Modul Cara ketiga sebagian method ----------')
bagi(15, 3)
bagi(21, 3)
bagi(20, 4)

print('--------- Panggil Modul Cara ke-empat all method ----------')
tambah(10, 5)
kurang(10, 5)
kali(3, 5)
bagi(21, 3)
pangkat(2, 3)
akar(9)

print('--------- Panggil Modul Cara ketiga sebagian method ----------')
k(15, 3)
b(21, 3)
k(20, 4)
