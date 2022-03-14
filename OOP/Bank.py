class Bank:
    # member 1 variabel 1
    norek = ''
    nama = ''
    saldo = 0
    jumlahNasabah = 0  # Variabel Static
    BANK = 'Bank Syariah Nurul Fikri'  # Variabel Konstanta

    # member 2 constructor
    def __init__(self, no, nasabah, saldo):
        self.norek = no
        self.nama = nasabah
        self.saldo = saldo
        Bank.jumlahNasabah += 1

    # member 3 method
    def nabung(self, uang):
        self.saldo += uang  # self.saldo = self.saldo + uang

    def tarik(self, uang):
        self.saldo -= uang  # self.saldo = self.saldo - uang

    def cetak(self):
        print(Bank.BANK,
              '\n================',
              "\nNomor Rekening\t: ", self.norek,
              '\nNama Nasabah\t: ', self.nama,
              "\nSaldo\t\t:  Rp.", format(self.saldo, ','),
              '\n================')
