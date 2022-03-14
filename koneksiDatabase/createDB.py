import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    passwd=''
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE db_barang")

print('Database Berhasil dibuat')
