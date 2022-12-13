import tkinter as tk
import tkinter.font as tkFont

class pelicula(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Peliculas")
        width=600
        height=500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_269=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_269["font"] = ft
        GLabel_269["fg"] = "#333333"
        GLabel_269["justify"] = "center"
        GLabel_269["text"] = "Nombre"
        GLabel_269.place(x=20,y=40,width=70,height=25)

        GLineEdit_813=tk.Entry(self)
        GLineEdit_813["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_813["font"] = ft
        GLineEdit_813["fg"] = "#333333"
        GLineEdit_813["justify"] = "center"
        GLineEdit_813["text"] = ""
        GLineEdit_813.place(x=80,y=40,width=460,height=30)

        GLabel_460=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_460["font"] = ft
        GLabel_460["fg"] = "#333333"
        GLabel_460["justify"] = "center"
        GLabel_460["text"] = "Sinopsis"
        GLabel_460.place(x=20,y=100,width=70,height=25)

        GLineEdit_467=tk.Entry(self)
        GLineEdit_467["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_467["font"] = ft
        GLineEdit_467["fg"] = "#333333"
        GLineEdit_467["justify"] = "center"
        GLineEdit_467["text"] = ""
        GLineEdit_467.place(x=80,y=90,width=460,height=50)

        GLabel_795=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_795["font"] = ft
        GLabel_795["fg"] = "#333333"
        GLabel_795["justify"] = "center"
        GLabel_795["text"] = "Descripcion"
        GLabel_795.place(x=10,y=170,width=70,height=25)

        GLineEdit_233=tk.Entry(self)
        GLineEdit_233["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_233["font"] = ft
        GLineEdit_233["fg"] = "#333333"
        GLineEdit_233["justify"] = "center"
        GLineEdit_233["text"] = ""
        GLineEdit_233.place(x=80,y=160,width=460,height=50)

        GLabel_874=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_874["font"] = ft
        GLabel_874["fg"] = "#333333"
        GLabel_874["justify"] = "center"
        GLabel_874["text"] = "Duracion"
        GLabel_874.place(x=20,y=230,width=70,height=25)

        GLineEdit_232=tk.Entry(self)
        GLineEdit_232["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_232["font"] = ft
        GLineEdit_232["fg"] = "#333333"
        GLineEdit_232["justify"] = "center"
        GLineEdit_232["text"] = ""
        GLineEdit_232.place(x=80,y=230,width=110,height=25)

