from bs4 import BeautifulSoup

soup = BeautifulSoup(
    "<html><p>Ini Paragraf Halaman Web</p></html>", "html.parser")  # menggunakan html.parser
print(soup)

soup = BeautifulSoup(
    "<html><p>Ini Paragraf Halaman Web</p></html>", "html5lib")  # html5lib
print(soup)

soup = BeautifulSoup(
    "<html><p>Ini Paragraf Halaman Web</p></html>", "lxml")  # menggunakan lxml
print(soup)

soup = BeautifulSoup(
    "<html><p>Ini Paragraf Halaman Web</p></html>", "xml")  # menggunakan xml
print(soup)
