class Hitunglah:
    def add(self, a, b):
        return a + b
    def add(self, a, b, c=0):
        return a + b + c
mat = Hitunglah()
B = mat.add(10, 2, 9)
print(B)
mut = Hitunglah()
C = mut.add(2, 3)
print(C)