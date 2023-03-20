class Kampus:
    def __init__(self, kampus):
        self.kampus = kampus
    def get_kampus(self):
        return self.kampus
class Mahasiswa(Kampus):
    def __init__(self, kampus, nama, nim, kelas):
        super().__init__(kampus)
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
    def get_nama(self):
        return self.nama
    def get_nim(self):
        return self.nim
    def get_kelas(self):
        return self.kelas
# Hierarchical Inheritance
class Maba(Mahasiswa):
    def __init__(self, kampus, nama, nim, kelas, pesantren):
        super().__init__(kampus, nama, nim, kelas)
        self.pesantren = pesantren
    def info(self):
        print ("Kampus    :", self.kampus, "\nNama      :", self.nama, "\nNIM       :", self.nim,"\nKelas     :", self.kelas, "\nPesantren :", self.pesantren, "Mengikuti")
maba1 = Maba("UMC","Rizky Resi Julian","210511027","R1","Sudah")
maba1.info()