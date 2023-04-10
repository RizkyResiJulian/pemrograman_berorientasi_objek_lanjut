print("Nama : Rizky Resi Julian")
print("NIM  : 210511027")
print("Kelas: TI21A / R1")
print("="*25)

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    
    def __repr__(self):
        return f'{self.nama} {self.nim}'
    
class Anggota:
    def __init__(self):
        self.anggotas = []
    
    def add_anggota(self, anggota):
        self.anggotas.append(anggota)

class Kel_KKM:
    def __init__(self, mahasiswa):
        self.mahasiswa = mahasiswa

mahasiswa1 = Mahasiswa("Rizky Resi Julian", 210511027)
mahasiswa2 = Mahasiswa("Budi Gunawan", 210511000)
mahasiswa = Anggota()
mahasiswa.add_anggota(mahasiswa1)
mahasiswa.add_anggota(mahasiswa2)
kelompok = Kel_KKM(mahasiswa)
print(repr(kelompok.mahasiswa.anggotas))