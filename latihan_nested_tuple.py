gorengan = ('Bakwan', 'Combro', 'Misro')
sop = 'Sop Iga', 'Sop Buntut', 'Sop Kaki'
nasi = ('Nasi Goreng', 'Nasi Uduk', 'Nasi Rames')
makanan = (gorengan, sop, nasi)  # Nested Tuple

# cetak
print('------ Jenis Sop ------')
print(makanan[1])
print('------ Cetak per makanan ------')
print(makanan[0][0])
print(makanan[1][1])
print(makanan[2][1])
print('------ Cetak all makanan ------')
print(makanan)
