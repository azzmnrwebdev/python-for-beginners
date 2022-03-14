import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    passwd='',
    database='db_barang'
)
cursor = db.cursor()
sql = "INSERT INTO produk (nama,harga) VALUES (%s, %s)"
val = ("Lemari Pakaian", 10000000)
cursor.execute(sql, val)
db.commit()

print('Data berhasil diinput sebanyak', format(cursor.rowcount), "baris")
