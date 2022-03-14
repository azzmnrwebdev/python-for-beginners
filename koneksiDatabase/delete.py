import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    passwd='',
    database='db_barang'
)
cursor = db.cursor()
sql = "DELETE FROM produk WHERE id=%s"
id = 4
cursor.execute(sql, id)
db.commit()

print('Data berhasil dihapus')
