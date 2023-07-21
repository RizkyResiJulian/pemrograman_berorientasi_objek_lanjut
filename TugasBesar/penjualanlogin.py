# Tambahkan fungsi menu Admin, menu Manager, dan menu Operator
# Update script onLogin
# Tambahkan fungsi onLogout
import tkinter as tk
from tkinter import *
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox, Menu
from login import *
from FrmSewa import *
from FrmPelanggan import *
from FrmMobil import *

class Dashboard:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("400x300")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.my_w_child = None
        self.aturKomponen()

    def new_window( self, number, _class):
        new = tk.Toplevel()
        new.transient()
        new.grab_set()
        _class(new, number)
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        mainmenu = Menu(self.parent)
        self.parent.config(menu=mainmenu)
        file_menu_awal = Menu(mainmenu)
        file_menu_awal
        
        # Menu Awal
        file_menu_awal.add_command(
            label='Login', command=self.show_login
        )
        file_menu_awal.add_command(
            label='Exit', command=root.destroy
        )
        
        # Tampilkan menu ke layar
        mainmenu.add_cascade(
            label="Menu", menu=file_menu_awal
        )    
        
        
    def menuAdmin(self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
       
        # create a menu
        file_menu = Menu(menubar)
        admin_menu = Menu(menubar)

        # Menu File
       
        file_menu.add_command(
            label='Logout', command=self.onLogout
        )
        file_menu.add_command(
            label='Exit', command=root.destroy
        )

      
        # Menu Admin
        admin_menu.add_command(
            label='Pelanggan', command= lambda: self.new_window("Pelanggan", FrmPelanggan)
        )
        admin_menu.add_command(
            label='Mobil', command= lambda: self.new_window("Mobil", FrmMobil)
        )
        admin_menu.add_command(
            label='Sewa', command= lambda: self.new_window("Sewa", FrmSewa)
        )

        # Tampilkan menu ke layar
        menubar.add_cascade(
            label="File", menu=file_menu
        )
        
        menubar.add_cascade(
            label="Menu Admin", menu=admin_menu
        )
       

    def menuPelanggan(self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
       
        # create a menu
        file_menu = Menu(menubar)
        pelanggan_menu = Menu(menubar)
        
        # Menu File
        file_menu.add_command(
            label='Logout', command=self.onLogout
        )
        file_menu.add_command(
            label='Exit', command=root.destroy
        )

      

        # Menu kaperpus
        pelanggan_menu.add_command(
            label='Mobil', command= lambda: self.new_window("Mobil", FrmMobil)
        )

        
        # Tampilkan menu ke layar
        menubar.add_cascade(
            label="File", menu=file_menu
        )    
        menubar.add_cascade(
            label="Menu Pelanggan", menu=pelanggan_menu
        )
             
    def show_login(self):
        self.my_w_child=tk.Toplevel(root)
        self.my_w_child.geometry("250x200") 
        # pasang Label
        Label(self.my_w_child, text='Username:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)

        Label(self.my_w_child, text="Password:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtUsername = Entry(self.my_w_child) 
        self.txtUsername.grid(row=0, column=1, padx=5, pady=5)

        self.txtPassword = Entry(self.my_w_child) 
        self.txtPassword.grid(row=1, column=1, padx=5, pady=5)  
        self.txtPassword.config(show='*')
                
        # Pasang Button
        self.btnLogin = tk.Button(self.my_w_child, text='Login',
            command=self.onLogin)
        self.btnLogin.grid(row=2, column=1, padx=5, pady=5) 
        
    def onLogin(self, event=None):
        u = self.txtUsername.get()
        p = self.txtPassword.get()
        A = penjualan()
        B =[]
        A.username = u
        A.password = p
        B = A.Login()
        
        if(B[0]=='True'):           
            if(B[1]=='admin'):
                self.my_w_child.destroy()
                self.menuAdmin()
                messagebox.showinfo("showinfo", "Login diterima, Anda login sebagai " + B[1])
            elif(B[1]=='pelanggan'): 
                self.my_w_child.destroy() 
                self.menuPelanggan()
                messagebox.showinfo("showinfo", "Login diterima, Anda login sebagai " + B[1])
            else: 
                messagebox.showinfo("showinfo", "Maaf, User tidak dikenal")    
            
        else:
            messagebox.showinfo("showinfo", "Login Not Valid")   
    def onLogout(self):
        self.aturKomponen()
        
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = Dashboard(root, "Rental Mobil")
    root.geometry("500x400")
    root.mainloop() 