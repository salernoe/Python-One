import tkinter as tk
import tkinter.font as tkFont


class pelicula(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title(" Cargar Películas")
        #setting window size
        width=477
        height=410
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_956=tk.Label(self)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_956["font"] = ft
        GLabel_956["fg"] = "#333333"
        GLabel_956["justify"] = "center"
        GLabel_956["text"] = " Cargar Peliculas"
        GLabel_956.place(x=150,y=10,width=152,height=30)

        GLabel_737=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_737["font"] = ft
        GLabel_737["fg"] = "#333333"
        GLabel_737["justify"] = "center"
        GLabel_737["text"] = "ID Peliculas"
        GLabel_737.place(x=10,y=60,width=70,height=25)

        GLabel_740=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_740["font"] = ft
        GLabel_740["fg"] = "#333333"
        GLabel_740["justify"] = "center"
        GLabel_740["text"] = "Nombre"
        GLabel_740.place(x=10,y=100,width=70,height=25)

        GLineEdit_301=tk.Entry(self)
        GLineEdit_301["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_301["font"] = ft
        GLineEdit_301["fg"] = "#333333"
        GLineEdit_301["justify"] = "center"
        GLineEdit_301["text"] = "Entry"
        GLineEdit_301.place(x=90,y=60,width=40,height=30)

        GLineEdit_402=tk.Entry(self)
        GLineEdit_402["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_402["font"] = ft
        GLineEdit_402["fg"] = "#333333"
        GLineEdit_402["justify"] = "center"
        GLineEdit_402["text"] = "Entry"
        GLineEdit_402.place(x=90,y=100,width=350,height=30)

        GLabel_404=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_404["font"] = ft
        GLabel_404["fg"] = "#333333"
        GLabel_404["justify"] = "center"
        GLabel_404["text"] = "Sinopsis"
        GLabel_404.place(x=10,y=170,width=70,height=25)

        GLineEdit_132=tk.Entry(self)
        GLineEdit_132["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_132["font"] = ft
        GLineEdit_132["fg"] = "#333333"
        GLineEdit_132["justify"] = "center"
        GLineEdit_132["text"] = "Entry"
        GLineEdit_132.place(x=90,y=150,width=350,height=75)

        GLabel_204=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_204["font"] = ft
        GLabel_204["fg"] = "#333333"
        GLabel_204["justify"] = "center"
        GLabel_204["text"] = "Descrpcion"
        GLabel_204.place(x=10,y=260,width=70,height=25)

        GLineEdit_746=tk.Entry(self)
        GLineEdit_746["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_746["font"] = ft
        GLineEdit_746["fg"] = "#333333"
        GLineEdit_746["justify"] = "center"
        GLineEdit_746["text"] = "Entry"
        GLineEdit_746.place(x=90,y=240,width=350,height=75)

        GButton_130=tk.Button(self)
        GButton_130["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_130["font"] = ft
        GButton_130["fg"] = "#000000"
        GButton_130["justify"] = "center"
        GButton_130["text"] = "Aceptar"
        GButton_130.place(x=270,y=360,width=70,height=25)
        GButton_130["command"] = self.GButton_130_command

        GButton_411=tk.Button(self)
        GButton_411["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_411["font"] = ft
        GButton_411["fg"] = "#000000"
        GButton_411["justify"] = "center"
        GButton_411["text"] = "Cancelas"
        GButton_411.place(x=350,y=360,width=70,height=25)
        GButton_411["command"] = self.GButton_411_command

    def GButton_130_command(self):
        print("command")


    def GButton_411_command(self):
        print("command")

