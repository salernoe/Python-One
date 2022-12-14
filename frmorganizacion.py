import tkinter as tk
import tkinter.font as tkFont
from frmpeliculas import pelicula
from frmtipo_de_pelicula import tipo_de_pelicula
from frmbutacas import butacas
from frmsesion import sesion

class organizacion(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Organización ")
        width=476
        height=145
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GButton_888=tk.Button(self)
        GButton_888["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_888["font"] = ft
        GButton_888["fg"] = "#000000"
        GButton_888["justify"] = "center"
        GButton_888["text"] = "Peliculas"
        GButton_888.place(x=40,y=40,width=110,height=25)
        GButton_888["command"] = self.abrir_peliculas

        GButton_148=tk.Button(self)
        GButton_148["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_148["font"] = ft
        GButton_148["fg"] = "#000000"
        GButton_148["justify"] = "center"
        GButton_148["text"] = "Clasificacion"
        GButton_148.place(x=180,y=40,width=110,height=25)
        GButton_148["command"] = self.abrir_clasificacion

        GButton_773=tk.Button(self)
        GButton_773["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_773["font"] = ft
        GButton_773["fg"] = "#000000"
        GButton_773["justify"] = "center"
        GButton_773["text"] = "Tipo de películas"
        GButton_773.place(x=310,y=40,width=110,height=25)
        GButton_773["command"] = self.GButton_773_command

        GButton_305=tk.Button(self)
        GButton_305["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_305["font"] = ft
        GButton_305["fg"] = "#000000"
        GButton_305["justify"] = "center"
        GButton_305["text"] = "Butacas"
        GButton_305.place(x=40,y=80,width=110,height=25)
        GButton_305["command"] = self.abrir_butacas

        GButton_345=tk.Button(self)
        GButton_345["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_345["font"] = ft
        GButton_345["fg"] = "#000000"
        GButton_345["justify"] = "center"
        GButton_345["text"] = "sesion"
        GButton_345.place(x=180,y=80,width=110,height=25)
        GButton_345["command"] = self.abrir_sesion

    def abrir_peliculas(self):
        pelicula(self)


    def abrir_clasificacion(self):
         print("command")


    def GButton_773_command(self):
        tipo_de_pelicula(self)


    def abrir_butacas(self):
       butacas(self)


    def abrir_sesion(self):
        sesion(self)

