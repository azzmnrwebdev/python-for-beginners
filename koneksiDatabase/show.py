import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    passwd='',
    database='db_barang'
)
cursor = db.cursor()
sql = "SELECT * FROM produk"
cursor.execute(sql)
hasil = cursor.fetchall()

for data in hasil:
    print(data)
