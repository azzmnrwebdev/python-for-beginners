import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    passwd='',
    database='db_barang'
)
cursor = db.cursor()
sql = '''CREATE TABLE produk(
    id int primary key auto_increment,
    nama varchar(45),
    harga float
)'''
cursor.execute(sql)

print('Tabel barang berhasil dibuat')
