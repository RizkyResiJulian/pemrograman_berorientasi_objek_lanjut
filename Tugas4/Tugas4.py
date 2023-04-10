print("Nama : Rizky Resi Julian")
print("NIM  : 210511027")
print("Kelas: TI21A / R1")
print("="*25)

class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
        self.informasi = Informasi()
    
    def __repr__(self):
        return f'Nama: {self.nama}\nJenis: {self.jenis}'

class Informasi:
    def __init__(self):
        self.info = []
    
    def add_informasi(self, warna, spesies):
        self.info.append(warna)
        self.info.append(spesies)
    
    def delete_informasi(self, warna, spesies):
        self.info.remove(warna)
        self.info.remove(spesies)

class Banteng:
    def __init__(self, hewan):
        self.hewan = hewan

hewan = Hewan("T-Rex", "Karnivora")
info = Informasi()
hewan.informasi.add_informasi("Warna: Tidak diketahui","Status: Punah")
print(repr(hewan))
print(hewan.informasi.info)