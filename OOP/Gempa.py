class Gempa:
    # member 1 variabel 1
    lokasi = ''
    skala = 0

    # member 2 constructor
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    # member 3 method or fungsi
    def dampak(self):
        if(self.skala < 2):
            ket = "Tidak Terasa"
        elif(self.skala >= 2 and self.skala < 4):
            ket = "Bangunan Retak-Retak"
        elif(self.skala >= 2 and self.skala < 6):
            ket = "Bangunan Roboh"
        else:
            ket = "Bangunan Roboh dan berpotensi tsunami"

        print(
            "Lokasi Gempa\t: ", self.lokasi,
            '\nSkala\t\t: ', self.skala, "ricther"
            "\nDampak\t\t: ", ket,
            '\n-----------------------------'
        )
