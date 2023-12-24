class Animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

class Badak(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jumlah_cula, berat_badan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jumlah_cula = jumlah_cula
        self.berat_badan = berat_badan

    def info_badak(self):
        return f"Badak {self.nama} hidup di {self.hidup}, makanan utama: {self.makanan}, memiliki {self.jumlah_cula} cula, berat badan: {self.berat_badan} kg."

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.warna = warna

    def info_ikan(self):
        return f"Ikan {self.nama} hidup di {self.hidup}, makanan utama: {self.makanan}, jenis: {self.jenis}, warna: {self.warna}."

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, panjang, jenis_ular):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.panjang = panjang
        self.jenis_ular = jenis_ular

    def info_ular(self):
        return f"Ular {self.nama} hidup di {self.hidup}, makanan utama: {self.makanan}, panjang: {self.panjang} meter, jenis: {self.jenis_ular}."

badak_sumatra = Badak("Badak Sumatra", "Tumbuhan", "Hutan", "Vivipar", 2, 1200)
print(badak_sumatra.info_badak())

ikan_guppy = Ikan("Guppy", "Pelet", "Air Tawar", "Ovipar", "Guppy", "Beragam")
print(ikan_guppy.info_ikan())

ular_kobra = Ular("Kobra", "Hewan kecil", "Darat", "Ovipar", 2.5, "Kobra India")
print(ular_kobra.info_ular())
