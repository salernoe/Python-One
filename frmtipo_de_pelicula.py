import tkinter as tk
import tkinter.font as tkFont

class tipo_de_pelicula(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Cargar Tipo de Película")
        #setting window size
        width=417
        height=275
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_867=tk.Label(self)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_867["font"] = ft
        GLabel_867["fg"] = "#333333"
        GLabel_867["justify"] = "center"
        GLabel_867["text"] = "Cargar Tipo de Película"
        GLabel_867.place(x=100,y=10,width=209,height=30)

        GLabel_697=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_697["font"] = ft
        GLabel_697["fg"] = "#333333"
        GLabel_697["justify"] = "center"
        GLabel_697["text"] = "Formato"
        GLabel_697.place(x=20,y=60,width=70,height=25)

        GLineEdit_88=tk.Entry(self)
        GLineEdit_88["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_88["font"] = ft
        GLineEdit_88["fg"] = "#333333"
        GLineEdit_88["justify"] = "center"
        GLineEdit_88["text"] = "Entry"
        GLineEdit_88.place(x=100,y=60,width=70,height=30)

        GLabel_560=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_560["font"] = ft
        GLabel_560["fg"] = "#333333"
        GLabel_560["justify"] = "center"
        GLabel_560["text"] = "Idioma"
        GLabel_560.place(x=20,y=110,width=70,height=25)

        GLineEdit_584=tk.Entry(self)
        GLineEdit_584["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_584["font"] = ft
        GLineEdit_584["fg"] = "#333333"
        GLineEdit_584["justify"] = "center"
        GLineEdit_584["text"] = "Entry"
        GLineEdit_584.place(x=100,y=110,width=100,height=30)

        GLabel_761=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_761["font"] = ft
        GLabel_761["fg"] = "#333333"
        GLabel_761["justify"] = "center"
        GLabel_761["text"] = "Subtitulos"
        GLabel_761.place(x=20,y=160,width=70,height=25)

        GLineEdit_626=tk.Entry(self)
        GLineEdit_626["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_626["font"] = ft
        GLineEdit_626["fg"] = "#333333"
        GLineEdit_626["justify"] = "center"
        GLineEdit_626["text"] = "Entry"
        GLineEdit_626.place(x=100,y=160,width=100,height=30)

        GButton_740=tk.Button(self)
        GButton_740["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_740["font"] = ft
        GButton_740["fg"] = "#000000"
        GButton_740["justify"] = "center"
        GButton_740["text"] = "Aceptar"
        GButton_740.place(x=220,y=210,width=70,height=25)
        GButton_740["command"] = self.GButton_740_command

        GButton_132=tk.Button(self)
        GButton_132["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_132["font"] = ft
        GButton_132["fg"] = "#000000"
        GButton_132["justify"] = "center"
        GButton_132["text"] = "Cancelar"
        GButton_132.place(x=300,y=210,width=70,height=25)
        GButton_132["command"] = self.GButton_132_command

    def GButton_740_command(self):
        print("command")


    def GButton_132_command(self):
        print("command")


