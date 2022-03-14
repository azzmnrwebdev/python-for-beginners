# membuat array
ar_aniamls = ['Ayam', 'Ikan', ' Kucing', 'Musang', 'Kambing']
# mengedit buah index ke 2 menjadi APEL
ar_aniamls[2] = 'Hiu'
# menghapus buah index ke 4
del ar_aniamls[4]
# tambah data list
ar_aniamls.insert(2, 'Burung')
ar_aniamls.append('Singa')

# cetak all element list
# print("Buah index ke-2:", ar_buah[2])
for animal in ar_aniamls:
    print("Nama Hewan:", animal)

# memotong list index 1 s/d 5
print('Memotong List Animals Index 1-5:', ar_aniamls[1:5])
