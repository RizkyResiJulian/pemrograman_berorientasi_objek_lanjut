class Pesawat:
    def __init__(self, nama, tahunproduksi):
        self.nama = nama
        self.tahunproduksi = tahunproduksi
    def display_info(self):
        return 

class JenisPesawat:
    def __init__(self, jenis):
        self.jenis = jenis
    def display_info(self):
        return

class Kapasitas:
    def __init__(self, kapasitas, jaraktempuh):
        self.kapasitas = kapasitas
        self.jaraktempuh = jaraktempuh
    def display_info(self):
        return

class PesawatPenumpang(Pesawat, JenisPesawat, Kapasitas):
    def __init__(self, nama, tahunproduksi, jenis, kapasitas, jaraktempuh):
        Pesawat.__init__(self, nama, tahunproduksi)
        JenisPesawat.__init__(self, jenis)
        Kapasitas.__init__(self, kapasitas, jaraktempuh)
    def display_info(self):
        super().display_info()
        print(f"Nama: {self.nama}")
        print(f"Tahun Produksi: {self.tahunproduksi}")
        print(f"Jenis: {self.jenis}")
        print(f"Kapasitas: {self.kapasitas}")
        print(f"Jarak Tempuh: {self.jaraktempuh}")        
pesawatA = PesawatPenumpang("Boeing 747", "1967", "Jumbo Jet Penumpang", "600", "18000 km")
pesawatA.display_info()
