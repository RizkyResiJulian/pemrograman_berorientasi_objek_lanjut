import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Sewa import *
class FrmSewa:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("650x445")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='IDSEWA:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='IDPELANGGAN:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PLAT:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TGLSEWA:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='WAKTU:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TGLKEMBALI:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='HARGASEWA:').grid(row=0, column=4,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TOTALBIAYA:').grid(row=1, column=4,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtIdsewa = Entry(mainFrame) 
        self.txtIdsewa.grid(row=0, column=1, padx=5, pady=5)
        self.txtIdsewa.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtIdpelanggan = Entry(mainFrame) 
        self.txtIdpelanggan.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtPlat = Entry(mainFrame) 
        self.txtPlat.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtTglsewa = Entry(mainFrame) 
        self.txtTglsewa.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtWaktu = Entry(mainFrame) 
        self.txtWaktu.grid(row=4, column=1, padx=5, pady=5)
        # Textbox
        self.txtTglkembali = Entry(mainFrame) 
        self.txtTglkembali.grid(row=5, column=1, padx=5, pady=5)
        # Textbox
        self.txtHargasewa = Entry(mainFrame) 
        self.txtHargasewa.grid(row=0, column=5, padx=5, pady=5)
        # Textbox
        self.txtTotalbiaya = Entry(mainFrame) 
        self.txtTotalbiaya.grid(row=1, column=5, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung, width=10)
        self.btnHitung.grid(row=3, column=4, padx=5, pady=5)
        # define columns
        columns = ('no','idsewa','idpelanggan','plat','tglsewa','waktu','tglkembali','hargasewa','totalbiaya')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('no', text='NO')
        self.tree.column('no', width="30")
        self.tree.heading('idsewa', text='IDSEWA')
        self.tree.column('idsewa', width="60")
        self.tree.heading('idpelanggan', text='IDPELANGGAN')
        self.tree.column('idpelanggan', width="100")
        self.tree.heading('plat', text='PLAT')
        self.tree.column('plat', width="65")
        self.tree.heading('tglsewa', text='TGLSEWA')
        self.tree.column('tglsewa', width="70")
        self.tree.heading('waktu', text='WAKTU')
        self.tree.column('waktu', width="50")
        self.tree.heading('tglkembali', text='TGLKEMBALI')
        self.tree.column('tglkembali', width="80")
        self.tree.heading('hargasewa', text='HARGASEWA')
        self.tree.column('hargasewa', width="90")
        self.tree.heading('totalbiaya', text='TOTALBIAYA')
        self.tree.column('totalbiaya', width="90")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtIdsewa.delete(0,END)
        self.txtIdsewa.insert(END,"")
        self.txtIdpelanggan.delete(0,END)
        self.txtIdpelanggan.insert(END,"")
        self.txtPlat.delete(0,END)
        self.txtPlat.insert(END,"")
        self.txtTglsewa.delete(0,END)
        self.txtTglsewa.insert(END,"")
        self.txtWaktu.delete(0,END)
        self.txtWaktu.insert(END,"")
        self.txtTglkembali.delete(0,END)
        self.txtTglkembali.insert(END,"")
        self.txtHargasewa.delete(0,END)
        self.txtHargasewa.insert(END,"")
        self.txtTotalbiaya.delete(0,END)
        self.txtTotalbiaya.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data sewa
        obj = Sewa()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["no"],d["idsewa"],d["idpelanggan"],d["plat"],d["tglsewa"],d["waktu"],d["tglkembali"],d["hargasewa"],d["totalbiaya"]))
    def onCari(self, event=None):
        idsewa = self.txtIdsewa.get()
        obj = Sewa()
        a = obj.get_by_idsewa(idsewa)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
            
    def onHitung(self, event=None):
        waktu = int(self.txtWaktu.get())
        hargasewa = int(self.txtHargasewa.get())
        totalbiaya = hargasewa * waktu
        self.txtTotalbiaya.delete(0,END)
        self.txtTotalbiaya.insert(END,str(totalbiaya))
        
    def TampilkanData(self, event=None):
        idsewa = self.txtIdsewa.get()
        obj = Sewa()
        res = obj.get_by_idsewa(idsewa)
        self.txtIdsewa.delete(0,END)
        self.txtIdsewa.insert(END,obj.idsewa)
        self.txtIdpelanggan.delete(0,END)
        self.txtIdpelanggan.insert(END,obj.idpelanggan)
        self.txtPlat.delete(0,END)
        self.txtPlat.insert(END,obj.plat)
        self.txtTglsewa.delete(0,END)
        self.txtTglsewa.insert(END,obj.tglsewa)
        self.txtWaktu.delete(0,END)
        self.txtWaktu.insert(END,obj.waktu)
        self.txtTglkembali.delete(0,END)
        self.txtTglkembali.insert(END,obj.tglkembali)
        self.txtHargasewa.delete(0,END)
        self.txtHargasewa.insert(END,obj.hargasewa)
        self.txtTotalbiaya.delete(0,END)
        self.txtTotalbiaya.insert(END,obj.totalbiaya)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        idsewa = self.txtIdsewa.get()
        idpelanggan = self.txtIdpelanggan.get()
        plat = self.txtPlat.get()
        tglsewa = self.txtTglsewa.get()
        waktu = self.txtWaktu.get()
        tglkembali = self.txtTglkembali.get()
        hargasewa = self.txtHargasewa.get()
        totalbiaya = self.txtTotalbiaya.get()
        # create new Object
        obj = Sewa()
        obj.idsewa = idsewa
        obj.idpelanggan = idpelanggan
        obj.plat = plat
        obj.tglsewa = tglsewa
        obj.waktu = waktu
        obj.tglkembali = tglkembali
        obj.hargasewa = hargasewa
        obj.totalbiaya = totalbiaya
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_idsewa(idsewa)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        idsewa = self.txtIdsewa.get()
        obj = Sewa()
        obj.idsewa = idsewa
        if(self.ditemukan==True):
            res = obj.delete_by_idsewa(idsewa)
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
    aplikasi = FrmSewa(root2, "Aplikasi Data Sewa")
    root2.mainloop()
