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
    def __init__(self, celcius):
        self.celcius = celcius
        
    def konversi(self):
        return 9/5 * self.celcius + 32
    
    def info(self):
        print ("konversi",self.celcius,"derajat celcius adalah",celciusA.konversi(), "derajat fahrenhait")
        
celciusA = Fahrenhait(75)
celciusA.info()

class Reamur:
    def __init__(self, celcius):
        self.celcius = celcius
        
    def konversi(self):
        return 4/5 * self.celcius
    
    def info(self):
        print ("konversi",self.celcius,"derajat celcius adalah",celciusA.konversi(), "derajat fahrenhait")
        
celciusA = Reamur(60)
celciusA.info()

class Kelvin:
    def __init__(self, celcius):
        self.celcius = celcius
        
    def konversi(self):
        return  self.celcius + 273
    
    def info(self):
        print ("konversi",self.celcius,"derajat celcius adalah",celciusA.konversi(), "derajat fahrenhait")
        
celciusA = Kelvin(90)
celciusA.info()
