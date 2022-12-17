import tkinter as tk
import tkinter.font as tkFont

class clasificacion (tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("cargar clasificación")
        #setting window size
        width=566
        height=398
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_464=tk.Label(self)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_464["font"] = ft
        GLabel_464["fg"] = "#333333"
        GLabel_464["justify"] = "center"
        GLabel_464["text"] = "Cargar Clasificación "
        GLabel_464.place(x=90,y=10,width=237,height=30)

        GLabel_354=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_354["font"] = ft
        GLabel_354["fg"] = "#333333"
        GLabel_354["justify"] = "center"
        GLabel_354["text"] = "Identificación"
        GLabel_354.place(x=40,y=70,width=70,height=25)

        GLineEdit_867=tk.Entry(self)
        GLineEdit_867["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_867["font"] = ft
        GLineEdit_867["fg"] = "#333333"
        GLineEdit_867["justify"] = "center"
        GLineEdit_867["text"] = "Entry"
        GLineEdit_867.place(x=120,y=70,width=150,height=30)

        GLabel_548=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_548["font"] = ft
        GLabel_548["fg"] = "#333333"
        GLabel_548["justify"] = "center"
        GLabel_548["text"] = "Recomendación"
        GLabel_548.place(x=30,y=130,width=70,height=25)

        GLineEdit_458=tk.Entry(self)
        GLineEdit_458["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_458["font"] = ft
        GLineEdit_458["fg"] = "#333333"
        GLineEdit_458["justify"] = "center"
        GLineEdit_458["text"] = "Entry"
        GLineEdit_458.place(x=120,y=110,width=300,height=65)

        GLabel_612=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_612["font"] = ft
        GLabel_612["fg"] = "#333333"
        GLabel_612["justify"] = "center"
        GLabel_612["text"] = "Descripción"
        GLabel_612.place(x=30,y=240,width=70,height=25)

        GLineEdit_744=tk.Entry(self)
        GLineEdit_744["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_744["font"] = ft
        GLineEdit_744["fg"] = "#333333"
        GLineEdit_744["justify"] = "center"
        GLineEdit_744["text"] = "Entry"
        GLineEdit_744.place(x=120,y=200,width=300,height=109)

        GButton_336=tk.Button(self)
        GButton_336["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_336["font"] = ft
        GButton_336["fg"] = "#000000"
        GButton_336["justify"] = "center"
        GButton_336["text"] = "Aceptar"
        GButton_336.place(x=290,y=350,width=70,height=25)
        GButton_336["command"] = self.GButton_336_command

        GButton_464=tk.Button(self)
        GButton_464["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_464["font"] = ft
        GButton_464["fg"] = "#000000"
        GButton_464["justify"] = "center"
        GButton_464["text"] = "Cancelar"
        GButton_464.place(x=380,y=350,width=70,height=25)
        GButton_464["command"] = self.GButton_464_command

    def GButton_336_command(self):
        print("command")


    def GButton_464_command(self):
        print("command")


