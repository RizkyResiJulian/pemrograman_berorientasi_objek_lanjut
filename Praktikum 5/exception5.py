list_angka = [1, 4, 6]
try:
    value = list_angka[3]
except IndexError:
    print("Index yang diminta melebihi jumlah elemen dalam list!")