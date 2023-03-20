class Hewan:
    def __init__(self, nama):
        self.nama = nama
    def speak(self):
        print(f"{self.nama} memiliki suara kukuruyukkkkkk")
class Aves(Hewan):
    def __init__(self, nama, kaki):
        super().__init__(nama)
        self.kaki = kaki
    def foot(self):
        print(f"{self.nama} memiliki jumlah kaki {self.kaki}")
class Ayam(Aves):
    def __init__(self, nama, kaki, berkembangbiak):
        super().__init__(nama, kaki)
        self.berkembangbiak = berkembangbiak
    def info(self):
        print(f"{self.nama} adalah hewan berkaki {self.kaki} termasuk kedalam aves karena berkembang biak dengan cara {self.berkembangbiak}")
ayamA = Ayam("Ayam", 2, "bertelur")
ayamA.speak()
ayamA.foot()
ayamA.info()