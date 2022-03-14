class Person:
    # member 1 variabel
    nama = ''
    gender = ''
    umur = 0

    # member 2 konstruktor
    def __init__(self, nama, gender, umur):
        self.nama = nama
        self.gender = gender
        self.umur = umur

    # member 3 method or fungsi
    def cetak(self):
        print("Nama\t\t: ", self.nama,
              '\nJenis Kelamin\t: ', self.gender,
              "\nUmur\t\t: ", self.umur, 'tahun')
