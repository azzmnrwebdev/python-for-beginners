nama = "Muhammad Azzam Nur Alwi Mansyur"
matkul = "Pemrograman Python"
nilai = 63.60

# tentukan kelulusan dengan ternary
ket = "Lulus" if nilai >= 70 else "Tidak Lulus"

# tentukan grade
if(nilai >= 85 and nilai <= 100):
    grade = "A"
elif(nilai >= 70 and nilai < 85):
    grade = "B"
elif(nilai >= 60 and nilai < 70):
    grade = "C"
elif(nilai >= 50 and nilai < 60):
    grade = "D"
elif(nilai >= 25 and nilai < 50):
    grade = "E"
else:
    grade = "Tidak Lulus"

# cetak data
print("Data Nilai Mahasiswa:"
      "\nNama\t\t:", nama,
      "\nMata Kuliah\t:", matkul,
      "\nNilai Mahasiswa\t:", nilai,
      "\nKeterangan\t:", ket,
      "\nGrade\t\t:", grade)
