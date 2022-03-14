import pymysql
from pymysql import cursors

db = pymysql.connect(
    host="localhost",
    user="root",
    passwd='',
    database='db_barang'
)


def insertData(db):  # Menambah Data
    nama = input("Nama Pproduk: ")
    harga = float(input("Harga Produk: "))
    val = (nama, harga)
    cursor = db.cursor()
    sql = "INSERT INTO produk (nama,harga) VALUES (%s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print('Data berhasil diinput sebanyak', format(cursor.rowcount), "baris")


def showData(db):  # Menampilkan Data
    cursor = db.cursor()
    sql = "SELECT * FROM produk"
    cursor.execute(sql)
    hasil = cursor.fetchall()

    for data in hasil:
        print(data)


def updateData(db):  # Mengupdate Data
    cursor = db.cursor()
    showData(db)
    nama = input("Nama Produk: ")
    harga = float(input("Harga Produk: "))
    id = int(input("ID Produk: "))
    sql = "UPDATE produk SET nama=%s, harga=%s WHERE id=%s"
    val = (nama, harga, id)
    cursor.execute(sql, val)
    db.commit()

    print('Data berhasil diubah')


def deleteData(db):  # Menghapus Data
    cursor = db.cursor()
    showData(db)
    id = int(input("ID Produk: "))
    sql = "DELETE FROM produk WHERE id=%s"
    cursor.execute(sql, id)
    db.commit()

    print('Data berhasil dihapus')


def searchData(db):  # Mencari Data
    cursor = db.cursor()
    keyword = input("Barang/Harga yang Anda Cari: ")
    sql = "SELECT * FROM produk WHERE nama LIKE %s OR harga LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(sql, val)
    hasil = cursor.fetchall()

    for data in hasil:
        print(data)


def showMenu(db):  # Membuat Menu
    print('========== CRUD APP Python ==========')
    print("1. INPUT DATA")
    print('2. SHOW DATA')
    print("3. UPDATE DATA")
    print('4. DELETE DATA')
    print("5. SEARCH DATA")
    print('0. EXIT')
    print("--------------------------------------")
    menu = input("PILIH MENU: ")

    # logic conditional
    if(menu == "1"):
        insertData(db)
    elif(menu == "2"):
        showData(db)
    elif(menu == '3'):
        updateData(db)
    elif(menu == '4'):
        deleteData(db)
    elif(menu == '5'):
        searchData(db)
    elif(menu == "0"):
        exit()
    else:
        print('Salah Pilih Menu!')


# Logic Looping
if __name__ == "__main__":
    while(True):
        showMenu(db)
