# hasil :
# Azzam
# Lovina
print("Azzam\nLovina")
print("Azzam\"Lovina")  # hasil : Azzam"Lovina
print("Azzam\Lovina")  # hasil : Azzam\Lovina
print("Azzam Lovina")  # hasil : Azzam Lovina

person_satu = "Muhammad Azzam Nur Alwi Mansyur"
# hasil : Muhammad Azzam Nur Alwi Mansyur
print(person_satu)

person_dua = "Lovina Aulia"
print(person_dua + " sedang belajar")  # hasil : Lovina Aulia sedang belajar

test_satu = "INI HURUF KECIL SEMUA"
print(test_satu.lower())  # hasil : ini huruf kecil semua

test_dua = "ini huruf besar semua"
print(test_dua.upper())  # hasil : INI HURUF BESAR SEMUA

test_tiga = "Apakah ini huruf besar semua?"
# hasil : False, karena semua huruf tidak besar semua
print(test_tiga.isupper())

# hasil : True, karena semua huruf menjadi besar semua
print(test_tiga.upper().isupper())

# hasil : 31, karena menghitung total jumlah karakter
print(len(person_satu))

# hasil : L, karena mencetak array index ke 0 yaitu huruf 'L'
print(person_dua[0])

# hasil : 0, karena mencari huruf L paling awal, maka akan ditampilkan index ke berapa
print(person_dua.index("L"))

# hasil : Sarah Aulia, karena mengganti kata lama 'Lovina' menjadi 'Sarah'
print(person_dua.replace("Lovina", "Sarah"))
