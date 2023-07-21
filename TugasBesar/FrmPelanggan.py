import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Pelanggan import *
class FrmPelanggan:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("470x445")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='IDPELANGGAN:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JK:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ALAMAT:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TELP:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtIdpelanggan = Entry(mainFrame) 
        self.txtIdpelanggan.grid(row=0, column=1, padx=5, pady=5)
        self.txtIdpelanggan.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)
        # Combo Box
        self.txtJk = StringVar()
        Cbo_jk = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJk) 
        Cbo_jk.grid(row=2, column=1, padx=5, pady=5)
        # Adding jk combobox drop down list
        Cbo_jk['values'] = ('L','P')
        Cbo_jk.current()
        # Textbox
        self.txtAlamat = Entry(mainFrame) 
        self.txtAlamat.grid(row=3, column=1, padx=5, pady=5)
         # Textbox
        self.txtTelp = Entry(mainFrame) 
        self.txtTelp.grid(row=4, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('no','idpelanggan','nama','jk','alamat','telp')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('no', text='NO')
        self.tree.column('no', width="30")
        self.tree.heading('idpelanggan', text='IDPELANGGAN')
        self.tree.column('idpelanggan', width="100")
        self.tree.heading('nama', text='NAMA')
        self.tree.column('nama', width="100")
        self.tree.heading('jk', text='JK')
        self.tree.column('jk', width="30")
        self.tree.heading('alamat', text='ALAMAT')
        self.tree.column('alamat', width="100")
        self.tree.heading('telp', text='TELP')
        self.tree.column('telp', width="90")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtIdpelanggan.delete(0,END)
        self.txtIdpelanggan.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtJk.set("")
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,"")
        self.txtTelp.delete(0,END)
        self.txtTelp.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data pelanggan
        obj = Pelanggan()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["no"],d["idpelanggan"],d["nama"],d["jk"],d["alamat"],d["telp"]))
    def onCari(self, event=None):
        idpelanggan = self.txtIdpelanggan.get()
        obj = Pelanggan()
        a = obj.get_by_idpelanggan(idpelanggan)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        idpelanggan = self.txtIdpelanggan.get()
        obj = Pelanggan()
        res = obj.get_by_idpelanggan(idpelanggan)
        self.txtIdpelanggan.delete(0,END)
        self.txtIdpelanggan.insert(END,obj.idpelanggan)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obj.nama)
        self.txtJk.set(obj.jk)
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,obj.alamat)
        self.txtTelp.delete(0,END)
        self.txtTelp.insert(END,obj.telp)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        idpelanggan = self.txtIdpelanggan.get()
        nama = self.txtNama.get()
        jk = self.txtJk.get()
        alamat = self.txtAlamat.get()
        telp = self.txtTelp.get()
        # create new Object
        obj = Pelanggan()
        obj.idpelanggan = idpelanggan
        obj.nama = nama
        obj.jk = jk
        obj.alamat = alamat
        obj.telp = telp
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_idpelanggan(idpelanggan)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        idpelanggan = self.txtIdpelanggan.get()
        obj = Pelanggan()
        obj.idpelanggan = idpelanggan
        if(self.ditemukan==True):
            res = obj.delete_by_idpelanggan(idpelanggan)
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
    aplikasi = FrmPelanggan(root2, "Aplikasi Data Pelanggan")
    root2.mainloop()
