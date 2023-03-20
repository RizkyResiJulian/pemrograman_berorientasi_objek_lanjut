class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
    def buku(self):
        print(self.judul, "Merupakan salah satu buku terbaik karangan",self.penulis)
class Peminjaman:
    def __init__(self, nama, tanggalpinjam, tanggalhrskembali):
        self.nama = nama
        self.tanggalpinjam = tanggalpinjam
        self.tanggalhrskembali = tanggalhrskembali
    def meminjam(self):
        print(self.nama, "meminjam buku di perpustakaan pada tanggal",self.tanggalpinjam)
class PeminjamanBuku(Buku, Peminjaman):
    def __init__(self, judul, penulis, nama, tanggalpinjam, tanggalhrskembali):
        Buku.__init__(self, judul, penulis)
        Peminjaman.__init__(self, nama, tanggalpinjam, tanggalhrskembali)
    def peminjaman(self):
        print(self.nama, "meminjam buku",self.judul,"karangan",self.penulis,"pada tanggal",self.tanggalpinjam,"dan harus dikembalikan pada tanggal",self.tanggalhrskembali)
peminjamanbuku1 = PeminjamanBuku("Laskar Pelangi", "Andrea Hirata", "Rizky","20/03/2023","27/03/2023")
peminjamanbuku1.buku() 
peminjamanbuku1.meminjam() 
peminjamanbuku1.peminjaman() 