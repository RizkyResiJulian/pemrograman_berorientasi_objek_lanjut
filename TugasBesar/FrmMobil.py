import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Mobil import *
class FrmMobil:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("420x445")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='PLAT:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='MERK:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JENIS:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='WARNA:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='HARGASEWA:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtPlat = Entry(mainFrame) 
        self.txtPlat.grid(row=0, column=1, padx=5, pady=5)
        self.txtPlat.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtMerk = Entry(mainFrame) 
        self.txtMerk.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtJenis = Entry(mainFrame) 
        self.txtJenis.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtWarna = Entry(mainFrame) 
        self.txtWarna.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtHargasewa = Entry(mainFrame) 
        self.txtHargasewa.grid(row=4, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id','plat','merk','jenis','warna','hargasewa')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('plat', text='PLAT')
        self.tree.column('plat', width="70")
        self.tree.heading('merk', text='MERK')
        self.tree.column('merk', width="70")
        self.tree.heading('jenis', text='JENIS')
        self.tree.column('jenis', width="70")
        self.tree.heading('warna', text='WARNA')
        self.tree.column('warna', width="70")
        self.tree.heading('hargasewa', text='HARGASEWA')
        self.tree.column('hargasewa', width="90")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtPlat.delete(0,END)
        self.txtPlat.insert(END,"")
        self.txtMerk.delete(0,END)
        self.txtMerk.insert(END,"")
        self.txtJenis.delete(0,END)
        self.txtJenis.insert(END,"")
        self.txtWarna.delete(0,END)
        self.txtWarna.insert(END,"")
        self.txtHargasewa.delete(0,END)
        self.txtHargasewa.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mobil
        obj = Mobil()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"],d["plat"],d["merk"],d["jenis"],d["warna"],d["hargasewa"]))
    def onCari(self, event=None):
        plat = self.txtPlat.get()
        obj = Mobil()
        a = obj.get_by_plat(plat)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        plat = self.txtPlat.get()
        obj = Mobil()
        res = obj.get_by_plat(plat)
        self.txtPlat.delete(0,END)
        self.txtPlat.insert(END,obj.plat)
        self.txtMerk.delete(0,END)
        self.txtMerk.insert(END,obj.merk)
        self.txtJenis.delete(0,END)
        self.txtJenis.insert(END,obj.jenis)
        self.txtWarna.delete(0,END)
        self.txtWarna.insert(END,obj.warna)
        self.txtHargasewa.delete(0,END)
        self.txtHargasewa.insert(END,obj.hargasewa)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        plat = self.txtPlat.get()
        merk = self.txtMerk.get()
        jenis = self.txtJenis.get()
        warna = self.txtWarna.get()
        hargasewa = self.txtHargasewa.get()
        # create new Object
        obj = Mobil()
        obj.plat = plat
        obj.merk = merk
        obj.jenis = jenis
        obj.warna = warna
        obj.hargasewa = hargasewa
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_plat(plat)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        plat = self.txtPlat.get()
        obj = Mobil()
        obj.plat = plat
        if(self.ditemukan==True):
            res = obj.delete_by_plat(plat)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmMobil(root2, "Aplikasi Data Mobil")
    root2.mainloop()
