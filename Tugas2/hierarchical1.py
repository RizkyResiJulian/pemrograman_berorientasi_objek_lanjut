class Pesawat:
    def __init__(self, nama):
        self.nama = nama
    def info(self):
        return
class Jet(Pesawat):
    def __init__(self, nama, jenis):
        super().__init__(nama)
        self.jenis = jenis
    def info(self):
        return
class Helikopter(Pesawat):
    def __init__(self, nama, jenis):
        super().__init__(nama)
        self.jenis = jenis
    def info(self):
        return
# turunan Hierarchical Inheritance
class Boeing (Jet):
    def __init__(self, nama, jenis, kapasitas):
        super().__init__(nama, jenis)
        self.kapasitas = kapasitas
    def info(self):
        print ("Nama :",self.nama,"\nJenis :",self.jenis,"\nKapasitas :",self.kapasitas,"Penumpang")
pesawatA = Boeing("Boeing 747","Jumbo Jet","600")
pesawatA.info()