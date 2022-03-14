# Nested Loop menggunakan FOR
print("---- cetak nested loop FOR ----")
for i in range(15):
    for j in range(i+1):
        print("*", end='')
    print("")

print("\n")

# dibalik
a = 15
for i in range(a):
    for j in range(0, a - 1):
        print('*', end='')
    a -= 1  # a = a -1
    print('')

print("\n")

# latihan nested loop ke 4
a = 15
s = a - 1  # for space
for i in range(a):  # baris
    for j in range(s):  # spasi
        print(' ', end='')
    s -= 1  # s = s - 1

    # mencetak bintang
    for j in range(0, i + 1):
        print('* ', end='')
    print('')

print("\n")

# Nested Loop menggunakan WHILE
print('--------- cetak nested loop WHILE -----------')
string = ""
baris = 1
while baris <= 15:
    col = baris
    # Looping Colum
    while col > 0:
        string += '*'
        col -= 1  # col = col - 1
    string += "\n"
    baris += 1  # baris = baris + 1
print(string)
