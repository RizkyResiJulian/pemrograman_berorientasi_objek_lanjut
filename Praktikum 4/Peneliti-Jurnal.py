print("Nama : Rizky Resi Julian")
print("NIM  : 210511027")
print("Kelas: TI21A / R1")
print("="*25)

class Peneliti:
    def __init__(self, nama, judul):
        self.nama =  nama
        self.judul = judul
    
class Jurnal:
    def __init__(self, peneliti, judul):
        self.peneliti = peneliti
        self.judul = judul
    
    def judul_jurnal(self):
        for peneliti in self.peneliti:
            print(peneliti.peneliti, peneliti.judul)
    
jurnal1 = Jurnal("Rizky Resi Julian","= " "Intel oh intel")
jurnal2 = Jurnal("Budi","= ""First Line Of Defence")
jurnal = Jurnal([jurnal1, jurnal2], "Kumpulan Jurnal-Jurnal")
jurnal.judul_jurnal()