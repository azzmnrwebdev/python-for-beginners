import math


def tambah(bil1, bil2):  # Pertambahan
    hasil = bil1 + bil2
    print("Bilangan", bil1, "+", "Bilangan", bil2, "=", hasil)


def kurang(bil1, bil2):  # Perkurangan
    hasil = bil1 - bil2
    print("Bilangan", bil1, "-", "Bilangan", bil2, "=", hasil)


def kali(bil1, bil2):  # Perkalian
    hasil = bil1 * bil2
    print("Bilangan", bil1, "X", "Bilangan", bil2, "=", hasil)


def bagi(bil1, bil2):  # Pembagian
    hasil = bil1 / bil2
    print("Bilangan", bil1, ":", "Bilangan", bil2, "=", hasil)


def pangkat(bil1, bil2):  # Pangkat
    hasil = math.pow(bil1, bil2)
    print("Hasil Pemangkatan Bilangan", bil1,
          "^", "Bilangan", bil2, "=", hasil)


def akar(bil):  # Akar
    hasil = math.sqrt(bil)
    print("Akar dari", bil, "=", hasil)
