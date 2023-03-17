class Mahasiswa:
    def __init__(self, nama, nim, kelas):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        
    def info(self):
        print(f"Nama  : {self.nama}\nNIM   : {self.nim}\nKelas : {self.kelas}\n")
        
mahasiswaB = Mahasiswa("Rizky Resi Julian", "210511027", "R1 (A)")
mahasiswaB.info()

class Fahrenhait:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit
        
    def celcius(self):
        return 5/9 * (self.fahrenheit-32)
    
    def reamur(self):
        return 4/9 * (self.fahrenheit-32)
    
    def kelvin(self):
        return 5/9 *(self.fahrenheit-32)+273
    
    def info(self):
        print ("Konversi suhu dari fahrenheit ke celcius, reamur, dan kelvin")
        print ("konversi ke celcius dari",self.fahrenheit,"derajat fahrenheit adalah",fahrenheitA.celcius(), "derajat celcius")
        print ("konversi ke reamur dari",self.fahrenheit,"derajat fahrenheit adalah",fahrenheitA.reamur(), "derajat reamur")
        print ("konversi ke kelvin dari",self.fahrenheit,"derajat fahrenheit adalah",fahrenheitA.kelvin(), "derajat kelvin\n")

fahrenheitA = Fahrenhait(90)
fahrenheitA.info()

class Reamur:
    def __init__(self, reamur):
        self.reamur = reamur
        
    def celcius(self):
        return 5/4 * self.reamur
    
    def fahrenheit(self):
        return (4/9 * self.reamur) + 32
    
    def kelvin(self):
        return 5/4 * self.reamur +273
    
    def info(self):
        print ("Konversi suhu dari reamur ke celcius, fahrenheit, dan kelvin")
        print ("konversi ke celcius dari",self.reamur,"derajat reamur adalah",reamurA.celcius(), "derajat celcius")
        print ("konversi ke fahrenheit dari",self.reamur,"derajat reamur adalah",reamurA.fahrenheit(), "derajat fahrenheit")
        print ("konversi ke kelvin dari",self.reamur,"derajat reamur adalah",reamurA.kelvin(), "derajat kelvin\n")
    
reamurA = Reamur(60)
reamurA.info()

class Kelvin:
    def __init__(self, kelvin):
        self.kelvin = kelvin
        
    def celcius(self):
        return self.kelvin - 273
    
    def reamur(self):
        return 4/5 * (self.kelvin-273)
    
    def fahrenheit(self):
        return 9/5 *(self.kelvin-273)+32
    
    def info(self):
        print ("Konversi suhu dari kelvin ke celcius, reamur, dan fahrenheit")
        print ("konversi ke celcius dari",self.kelvin,"derajat kelvin adalah",kelvinA.celcius(), "derajat celcius")
        print ("konversi ke reamur dari",self.kelvin,"derajat kelvin adalah",kelvinA.reamur(), "derajat reamur")
        print ("konversi ke kelvin dari",self.kelvin,"derajat kelvin adalah",kelvinA.fahrenheit(), "derajat fahrenheit")
        
kelvinA = Kelvin(300)
kelvinA.info()
