from Person import *


class Dosen(Person):
    # member 1 variabel
    gelar = ''
    jabatan = ''
    gaji = 0

    # member 2 konstruktor
    def __init__(self, nama, gender, umur, gelar, jabatan):
        super().__init__(nama, gender, umur)
        self.gelar = gelar
        self.jabatan = jabatan

    # member 3 method or fungsi
    def setGaji(self, uang):
        self.gaji += uang

    def cetak(self):
        super().cetak()
        print("Gelar\t\t: ", self.gelar,
              '\nJabatan\t\t: ', self.jabatan,
              "\nGaji\t\t:  Rp.", format(self.gaji, ','),
              '\n-------------------------------------')
