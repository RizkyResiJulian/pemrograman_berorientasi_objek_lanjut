class Seseorang:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def get_info(self):
        print("Nama:", self.name)
        print("Alamat:", self.address)
# Single Inheritance
class Pembeli(Seseorang):
    def __init__(self, kodepembeli):
        self.kodepembeli = kodepembeli
    def get_info(self):
        super().get_info()
        print("Kode Pembelian:", self.kodepembeli)
# Single Inheritance
class Barang(Seseorang):
    def __init__(self, name, address, barang, harga):
        super().__init__(name, address)
        self.barang = barang
        self.harga = harga
    def get_info(self):
        super().get_info()
        print("Nama Barang:", self.barang)
        print("Harga:", self.harga)
# Multiple Inheritance
class Penjualan(Pembeli, Barang):
    def __init__(self, name, address, kodepembeli, barang, harga, status):
        Pembeli.__init__(self, kodepembeli)
        Barang.__init__(self, name, address, barang,harga)
        self.status = status
    def get_info(self):
        super().get_info()
        print("Status Pembelian:", self.status)
penjualanA = Penjualan("Rizky","Cirebon","12345","IPhone 14","14jt","Dalam Perjalanan")
penjualanA.get_info()