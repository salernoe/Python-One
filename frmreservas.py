import tkinter as tk
import tkinter.font as tkFont

class reservas(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Reservas")
        width=483
        height=163
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_669=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_669["font"] = ft
        GLabel_669["fg"] = "#333333"
        GLabel_669["justify"] = "center"
        GLabel_669["text"] = "Precio"
        GLabel_669.place(x=20,y=20,width=70,height=25)

        GLineEdit_909=tk.Entry(self)
        GLineEdit_909["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_909["font"] = ft
        GLineEdit_909["fg"] = "#333333"
        GLineEdit_909["justify"] = "center"
        GLineEdit_909["text"] = "Entry"
        GLineEdit_909.place(x=80,y=20,width=110,height=30)

        GLabel_364=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_364["font"] = ft
        GLabel_364["fg"] = "#333333"
        GLabel_364["justify"] = "center"
        GLabel_364["text"] = "Fecha"
        GLabel_364.place(x=210,y=20,width=70,height=25)

        GListBox_165=tk.Listbox(self)
        GListBox_165["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_165["font"] = ft
        GListBox_165["fg"] = "#333333"
        GListBox_165["justify"] = "center"
        GListBox_165.place(x=290,y=20,width=110,height=30)

        GLabel_348=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_348["font"] = ft
        GLabel_348["fg"] = "#333333"
        GLabel_348["justify"] = "center"
        GLabel_348["text"] = "Butaca"
        GLabel_348.place(x=10,y=80,width=70,height=25)

        GListBox_661=tk.Listbox(self)
        GListBox_661["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_661["font"] = ft
        GListBox_661["fg"] = "#333333"
        GListBox_661["justify"] = "center"
        GListBox_661.place(x=80,y=80,width=110,height=30)

        GLabel_420=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_420["font"] = ft
        GLabel_420["fg"] = "#333333"
        GLabel_420["justify"] = "center"
        GLabel_420["text"] = "Descuento"
        GLabel_420.place(x=210,y=80,width=70,height=25)

        GListBox_764=tk.Listbox(self)
        GListBox_764["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_764["font"] = ft
        GListBox_764["fg"] = "#333333"
        GListBox_764["justify"] = "center"
        GListBox_764.place(x=290,y=80,width=110,height=30)

