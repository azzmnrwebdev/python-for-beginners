import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    passwd=''
)

print('Sukses Koneksi')
