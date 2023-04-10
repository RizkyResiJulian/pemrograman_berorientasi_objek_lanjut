print("Nama : Rizky Resi Julian")
print("NIM  : 210511027")
print("Kelas: TI21A / R1")
print("="*25)

class Penulis:
    def __init__(self, nama, judul):
        self.nama = nama
        self.judul = judul
        self.informasi = Informasi()
    
    def __repr__(self):
        return f'{self.nama}'
        return f'{self.judul}'

class Informasi:
    def __init__(self):
        self.info = []
    
    def add_informasi(self, penerbit, harga):
        self.info.append(penerbit)
        self.info.append(harga)
    
    def delete_informasi(self, penerbit, harga):
        self.info.remove(penerbit)
        self.info.remove(harga)

class Buku:
    def __init__(self, penulis):
        self.penulis = penulis

penulis = Penulis("Rizky Resi Julian", "Tikus Kantor")
info = Informasi()
penulis.informasi.add_informasi(2023, "Rp.75.000")
print(repr(penulis))
print(penulis.informasi.info)