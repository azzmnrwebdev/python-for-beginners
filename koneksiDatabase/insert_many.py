import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    passwd='',
    database='db_barang'
)
cursor = db.cursor()
sql = "INSERT INTO produk (nama,harga) VALUES (%s, %s)"
pdk = [("Mesin Cuci", 12000000), ("AC", 7000000), ("Sofa", 5000000)]

for val in pdk:
    cursor.execute(sql, val)
    db.commit()

print('Data berhasil diinput')
