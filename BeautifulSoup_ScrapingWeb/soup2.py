from bs4 import BeautifulSoup

dokumen = '''
<!DOCTYPE html>
<html>
<head>
<title>Modul BeautifulSoup</title>
</head>
<body>

<p class="judul">Menggunakan Modul BeautifulSoup</p>
<p class="paragraf">Ini isi paragraf ...</p>

</body>
</html>

'''

# Cetak Menggunakan html5lib
htmlSoup = BeautifulSoup(dokumen, "html5lib")

judul = htmlSoup.find('p', class_="judul")
paragraf = htmlSoup.find('p', class_="paragraf")
paragrafSaja = htmlSoup.find('p', class_="judul").text

print(judul)
print(paragraf)
print(paragrafSaja)
print("================================")

# cetak all
allParagraf = htmlSoup.find_all('p')
print(allParagraf)
