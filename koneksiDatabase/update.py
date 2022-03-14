import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    passwd='',
    database='db_barang'
)
cursor = db.cursor()
sql = "UPDATE produk SET nama=%s, harga=%s WHERE id=%s"
val = ("Kuklas 2 Pintu", 11000000, 1)
cursor.execute(sql, val)
db.commit()

print('Data berhasil diubah')
