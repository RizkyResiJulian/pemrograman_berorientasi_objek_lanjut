class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def perkenalan(self):
        print("Perkenalkan nama saya adalah", self.nama)
class Kelas(Mahasiswa):
    def __init__(self, nama, jk, kelas):
        super().__init__(nama, jk)
        self.kelas = kelas
    def biodata(self):
        print("Nama  :",self.nama,"\nNIM   :",self.nim,"\nKelas :",self.kelas)
kelasA = Kelas("Rizky Resi Julian", "210511027", "R1(A)")
kelasA.perkenalan() 
kelasA.biodata()