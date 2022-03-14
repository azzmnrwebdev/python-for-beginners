# struktur kendali if
pelanggan = "Muhammad Azzam Nur Alwi Mansyur"
totalBelanja = 190000

# if(totalBelanja >= 100000):
#     keterangan = "Selamat anda mendapatkan voucher game"
# else:
#     keterangan = "Terima kasih sudah berbelanja di Toko Kami"
# ternary
# keterangan = (totalBelanja >= 100000) ? "Selamat anda mendapatkan voucher game" : "Terima kasih sudah berbelanja di Toko Kami"
keterangan = "Selamat anda mendapatkan voucher game" if totalBelanja >= 150000 else "Terima kasih sudah berbelanja di Toko Kami"

print("Pelanggan", pelanggan, "telah berbelanja", totalBelanja,
      "maka ia mendapatkan", keterangan)
