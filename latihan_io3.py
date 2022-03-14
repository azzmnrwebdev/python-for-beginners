# membuat aplikasi sederhana
print('------ Luas Bidang ------')
print('Pilih Bidang:'
      '\n1. Lingkaran'
      '\n2. Segitiga'
      '\n3. Persegi Panjang'
      )
pilihan = int(input("Pilih No. "))

# logic
if(pilihan == 1):
    bidang = 'Lingkaran'
    jari2 = float(input('Jari2: '))
    luas = 3.14 * jari2 * jari2

    # cetak
    print('Luas bidang %s dengan jari2 %2.f = %.2f' %
          (bidang, jari2, luas))
elif(pilihan == 2):
    bidang = 'Segitiga'
    alas = float(input('Alas: '))
    tinggi = float(input("Tinggi: "))
    luas = 0.5 * alas * tinggi

    # cetak
    print("Luas bidang %s dengan alas %.2f dan tinggi %.2f" ' = %.2f' %
          (bidang, alas, tinggi, luas))
elif(pilihan == 3):
    bidang = 'Persegi Panjang'
    panjang = float(input('Panjang: '))
    lebar = float(input("Lebar: "))
    luas = panjang * lebar

    # cetak
    print("Luas bidang %s dengan panjang %.2f dan luas %.2f" ' = %.2f' %
          (bidang, panjang, lebar, luas))
else:
    print("Bidang yang anda pilih belum ada")
