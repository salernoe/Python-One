import tkinter as tk
import tkinter.font as tkFont

class sesion(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Cargar Sesión ")
        #setting window size
        width=428
        height=228
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_370=tk.Label(self)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_370["font"] = ft
        GLabel_370["fg"] = "#333333"
        GLabel_370["justify"] = "center"
        GLabel_370["text"] = "Cargar Sesión "
        GLabel_370.place(x=80,y=10,width=252,height=30)

        GLabel_487=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_487["font"] = ft
        GLabel_487["fg"] = "#333333"
        GLabel_487["justify"] = "center"
        GLabel_487["text"] = "Fecha"
        GLabel_487.place(x=20,y=50,width=70,height=25)

        GLineEdit_522=tk.Entry(self)
        GLineEdit_522["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_522["font"] = ft
        GLineEdit_522["fg"] = "#333333"
        GLineEdit_522["justify"] = "center"
        GLineEdit_522["text"] = "Entry"
        GLineEdit_522.place(x=90,y=50,width=90,height=30)

        GLabel_258=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_258["font"] = ft
        GLabel_258["fg"] = "#333333"
        GLabel_258["justify"] = "center"
        GLabel_258["text"] = "ID Salas"
        GLabel_258.place(x=200,y=50,width=70,height=25)

        GListBox_491=tk.Listbox(self)
        GListBox_491["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_491["font"] = ft
        GListBox_491["fg"] = "#333333"
        GListBox_491["justify"] = "center"
        GListBox_491.place(x=280,y=50,width=90,height=30)

        GLabel_649=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_649["font"] = ft
        GLabel_649["fg"] = "#333333"
        GLabel_649["justify"] = "center"
        GLabel_649["text"] = "ID Pelicula"
        GLabel_649.place(x=130,y=100,width=70,height=25)

        GListBox_787=tk.Listbox(self)
        GListBox_787["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_787["font"] = ft
        GListBox_787["fg"] = "#333333"
        GListBox_787["justify"] = "center"
        GListBox_787.place(x=210,y=100,width=90,height=30)

        GButton_80=tk.Button(self)
        GButton_80["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_80["font"] = ft
        GButton_80["fg"] = "#000000"
        GButton_80["justify"] = "center"
        GButton_80["text"] = "Aceptar"
        GButton_80.place(x=160,y=160,width=70,height=25)
        GButton_80["command"] = self.GButton_80_command

        GButton_937=tk.Button(self)
        GButton_937["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_937["font"] = ft
        GButton_937["fg"] = "#000000"
        GButton_937["justify"] = "center"
        GButton_937["text"] = "Cancelar"
        GButton_937.place(x=260,y=160,width=70,height=25)
        GButton_937["command"] = self.GButton_937_command

    def GButton_80_command(self):
        print("command")


    def GButton_937_command(self):
        print("command")

