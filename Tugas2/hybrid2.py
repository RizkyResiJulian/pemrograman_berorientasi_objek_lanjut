class Seseorang:
    def __init__(self, name, nim):
        self.name = name
        self.nim = nim
    def get_info(self):
        print("Nama       :", self.name)
        print("NIM        :", self.nim)
# Single Inheritance
class Mahasiswa(Seseorang):
    def __init__(self, prodi):
        self.prodi = prodi
    def get_info(self):
        super().get_info()
        print("Prodi      :", self.prodi)
# Single Inheritance
class MataKuliah(Seseorang):
    def __init__(self, name, nim, matakuliah, dosen):
        super().__init__(name, nim)
        self.matakuliah = matakuliah
        self.dosen = dosen
    def get_info(self):
        super().get_info()
        print("Mata Kuliah:", self.matakuliah)
        print("Dosen      :", self.dosen)
# Multiple Inheritance
class Kelas(Mahasiswa, MataKuliah):
    def __init__(self, name, nim, prodi, matakuliah, dosen, kelas):
        Mahasiswa.__init__(self, prodi)
        MataKuliah.__init__(self, name, nim, matakuliah, dosen)
        self.kelas = kelas
    def get_info(self):
        super().get_info()
        print("Kelas      :", self.kelas)
kelasA = Kelas("Rizky Resi Julian","210511027","TIF","PBO Lanjut","Pa Freddy","R1(A)")
kelasA.get_info()