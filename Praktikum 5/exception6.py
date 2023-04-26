class Mahasiswa:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
mahasiswa = Mahasiswa("RizkyRJ", 19)
try:
    print(mahasiswa.nim)
except AttributeError:
    print("Objek tidak memiliki atribut yang diminta!")
