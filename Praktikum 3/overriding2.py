class Harimau:
    def bersuara(self):
        print("Roarrrrr!!!")
class Serigala:
    def bersuara(self):
        print("Auuuuuuuuuu!!!")
def cetak_suara(objek):
    objek.bersuara()
harimau = Harimau()
serigala = Serigala()
cetak_suara(harimau) 
cetak_suara(serigala)