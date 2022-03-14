print('---------- Banyak Inputan ------------')
name = input("Nama: ")
gender = str(input('Jenis Kelamin: '))
age = int(input("Umur: "))
weight = float(input('Berat Badan: '))

# cetak data
print("Your Name\t: %s"
      "\nJenis Kelamin\t: %s"
      "\nUmur\t\t: %i tahun"
      '\nBerat Badan\t: %.2f tahun' % (name, gender, age, weight)
      )
