from Person import *


class Mahasiswa(Person):
    # member 1 variabel
    prodi = ''
    semester = 0

    # member 2 konstruktor
    def __init__(self, nama, gender, umur, prodi, semester):
        super().__init__(nama, gender, umur)
        self.prodi = prodi
        self.semester = semester

    # member 3 method or fungsi
    def cetak(self):
        super().cetak()
        print("Program Studi\t: ", self.prodi,
              '\nSemester\t: ', self.semester,
              '\n-------------------------------------')
