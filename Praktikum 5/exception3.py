try:
    with open("alberteinstain.txt") as file:
        data = file.read()
except FileNotFoundError:
    print("File tidak ditemukan!, pastikan menuliskan nama file yang benar!")
