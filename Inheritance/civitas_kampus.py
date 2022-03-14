from Dosen import *
from Mahasiswa import *

# membuat object
d1 = Dosen('Azzam Nur', 'L', 23, 'S.Kom, M.kom', "Pemrograman Backend")
d2 = Dosen('Lovina Aulia', 'p', 22, 'S.Kom, M.kom', "Kaprodi TI")
m1 = Mahasiswa('Yusuf Fadillah', 'L', 20, 'Teknik Informatika', 5)
m2 = Mahasiswa('Ficri Hani', 'L', 20, 'Sistem Informatika', 5)

# object set gaji
d1.setGaji(80000000)
d2.setGaji(93000000)

# cetak data
d1.cetak()
d2.cetak()
m1.cetak()
m2.cetak()
