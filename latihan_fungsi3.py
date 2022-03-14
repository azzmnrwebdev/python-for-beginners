def person(nama='Muhammad Azzam Nur Alwi Mansyur', pekerjaan='Mahasiswa', hobby="Ngoding"):
    print('Nama\t\t: %s'
          "\nPekerjaan\t: %s"
          '\nHobby\t\t: %s'
          % (nama, pekerjaan, hobby))
    print('----------------------------------------')


# Panggil Fungsi
person()
person('Lovina', 'Digital Marketing', 'Melukis')
person('Ficri Hani', hobby='Mendaki')
person(pekerjaan='Fullstack Web Development')
