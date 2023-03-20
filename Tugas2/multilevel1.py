class Orang:
    def __init__(self, name):
        self.name = name
    def kenalan(self):
        print("Hallo nama saya adalah",self.name)
class Cukur(Orang):
    def __init__(self, name, potong):
        super().__init__(name)
        self.potong = potong
    def potongan(self):
        print("Potongan",self.potong)
class Model(Cukur):
    def __init__(self, name, potong, model):
        super().__init__(name, potong)
        self.model = model
    def info(self):
        print(self.name, "Ingin Memotong rambut dengan potongan",self.potong,"dengan nama model potongan",self.model)
modelA = Model("Rizky","samping","cepmek")
modelA.kenalan()
modelA.potongan()
modelA.info()
