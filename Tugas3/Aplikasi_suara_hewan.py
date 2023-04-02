from pygame import mixer 
mixer.init()
print ("Nama  : Rizky Resi Julian\nNIM   : 210511027\nKelas : R1(A)")
print ("APLIKASI SEDERHANA 10 SUARA HEWAN")
print ("1.  Kucing\n2.  Anjing\n3.  Babi\n4.  Harimau\n5.  Sapi\n6.  Ayam\n7.  Gajah\n8.  Kuda\n9.  Kambing\n10. Elang")
print ("Masukkan angka yang ada pada daftar untuk memilih suara!")
while True:
    x = input("Pilih Suara: ")
    if x == '1':
        mixer.music.load('kucing.mp3')
        mixer.music.play()
        print ("Suara Kucing!")
        stop = input()
        if True:
            stop == ("<Return>")
            mixer.music.stop()
        else :
            pass
    elif x == '2':
        mixer.music.load('anjing.mp3')
        mixer.music.play()
        print ("Suara Anjing!")
        stop = input()
        if True:
            stop == ("<Return>")
            mixer.music.stop()
        else :
            pass
    elif x == '3':
        mixer.music.load('babi.mp3')
        mixer.music.play()
        print ("Suara Babi!")
        stop = input()
        if True:
            stop == ("<Return>")
            mixer.music.stop()
        else :
            pass
    elif x == '4':
        mixer.music.load('harimau.mp3')
        mixer.music.play()
        print ("Suara Harimau!")
        stop = input()
        if True:
            stop == ("<Return>")
            mixer.music.stop()
        else :
            pass
    elif x == '5':
        mixer.music.load('sapi.mp3')
        mixer.music.play()
        print ("Suara Sapi!")
        stop = input()
        if True:
            stop == ("<Return>")
            mixer.music.stop()
        else :
            pass
    elif x == '6':
        mixer.music.load('ayam.mp3')
        mixer.music.play()
        print ("Suara Ayam!")
        stop = input()
        if True:
            stop == ("<Return>")
            mixer.music.stop()
        else :
            pass
    elif x == '7':
        mixer.music.load('gajah.mp3')
        mixer.music.play()
        print ("Suara Gajah!")
        stop = input()
        if True:
            stop == ("<Return>")
            mixer.music.stop()
        else :
            pass
    elif x == '8':
        mixer.music.load('kuda.mp3')
        mixer.music.play()
        print ("Suara Kuda!")
        stop = input()
        if True:
            stop == ("<Return>")
            mixer.music.stop()
        else :
            pass
    elif x == '9':
        mixer.music.load('kambing.mp3')
        mixer.music.play()
        print ("Suara Kambing!")
        stop = input()
        if True:
            stop == ("<Return>")
            mixer.music.stop()
        else :
            pass
    elif x == '10':
        mixer.music.load('elang.mp3')
        mixer.music.play()
        print ("Suara Elang!")
        stop = input()
        if True:
            stop == ("<Return>")
            mixer.music.stop()
        else :
            pass
    else :
        pass