print('------- cetak 1 s/d 30 --------')
nomer = 1
while(nomer <= 30):
    print("Nomer", nomer)
    nomer += 1  # nomer = nomer + 1

# dibalik dari 30 s/d 1
print('------- cetak 30 s/d 1 --------')
bil = 30
while(bil >= 1):
    print("Nomer", bil)
    bil -= 1  # bil = bil - 1

# bilangan genap 1 s/d 30
print('------- cetak bilangan genap 1 s/d 30 --------')
nomer = 1
while(nomer <= 30):
    if(nomer % 2 == 0):
        print("Nomer", nomer)
    nomer += 1  # nomer = nomer + 1

# bilangan ganjil 1 s/d 30
print('------- cetak bilangan ganjil 1 s/d 30 --------')
bil = 30
while(bil >= 1):
    if(bil % 2 == 1):
        print("Nomer", bil)
    bil -= 1  # bil = bil - 1
