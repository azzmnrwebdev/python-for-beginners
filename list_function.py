lucky_number = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jimmy", "Oscar", "Tommy", "Oscar"]
friends2 = friends.copy()

# hasil : ['Kevin', 'Karen', 'Jimmy', 'Oscar', 'Tommy', 'Oscar', 4, 8, 15, 16, 23, 42]
friends.extend(lucky_number)  # menambahkan array dengan method 'extend'

# hasil : ['Kevin', 'Karen', 'Jimmy', 'Oscar', 'Tommy', 'Oscar', 'Creed']
friends.append("Creed")  # menambahkan data paling akhir dengan method 'append'

# hasil : ['Kevin', 'Kelly', 'Karen', 'Jimmy', 'Oscar', 'Tommy', 'Oscar']
friends.insert(1, "Kelly") # menyisipkan 1 data bernama 'Kelly' di posisi index ke 1

# hasil : ['Kevin', 'Karen', 'Oscar', 'Tommy', 'Oscar']
friends.remove("Jimmy")  # untuk menghapus 1 isi array bernama 'Jimmy'

# hasil : []
# friends.clear() # untuk menghapus semua isi array

# hasil : ['Kevin', 'Kelly', 'Karen', 'Oscar', 'Tommy', 'Oscar', 4, 8, 15, 16, 23, 42, 'Creed']
print(friends)

# hasil : ['Kevin', 'Karen', 'Jimmy', 'Oscar', 'Tommy', 'Oscar']
print(friends2)

# hasil : 0, karena kevin berapa pada index ke 0
print(friends.index("Kevin"))

# hasil : 'Mike' is not in list, karena di dalam array tidak ada data bernama Mike
# print(friends.index("Mike")) # ERROR!

# hasil : 2, karena jumlah data yang bernama oscar ada 2
print(friends.count("Oscar"))

numbers = [42, 16, 23, 15, 8, 4]
# hasil : [4, 8, 15, 16, 23, 42]
numbers.sort()  # diurutkan mulai dari yang angka kecil sampai besar
print(numbers)

#hasil : [42, 23, 16, 15, 8, 4]
numbers.reverse()  # diurutkan mulai dari yang angka besar sampai kecil
print(numbers)
