import tkinter as tk
import tkinter.font as tkFont

class butacas(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("butacas")
        width=472
        height=163
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_885=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_885["font"] = ft
        GLabel_885["fg"] = "#333333"
        GLabel_885["justify"] = "center"
        GLabel_885["text"] = "Fila"
        GLabel_885.place(x=10,y=40,width=70,height=25)

        GLineEdit_531=tk.Entry(self)
        GLineEdit_531["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_531["font"] = ft
        GLineEdit_531["fg"] = "#333333"
        GLineEdit_531["justify"] = "center"
        GLineEdit_531["text"] = ""
        GLineEdit_531.place(x=70,y=40,width=130,height=30)

        GLabel_51=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_51["font"] = ft
        GLabel_51["fg"] = "#333333"
        GLabel_51["justify"] = "center"
        GLabel_51["text"] = "Numero"
        GLabel_51.place(x=220,y=40,width=70,height=25)

        GLineEdit_570=tk.Entry(self)
        GLineEdit_570["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_570["font"] = ft
        GLineEdit_570["fg"] = "#333333"
        GLineEdit_570["justify"] = "center"
        GLineEdit_570["text"] = ""
        GLineEdit_570.place(x=290,y=40,width=130,height=30)

        GLabel_192=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_192["font"] = ft
        GLabel_192["fg"] = "#333333"
        GLabel_192["justify"] = "center"
        GLabel_192["text"] = "Disponible"
        GLabel_192.place(x=130,y=100,width=70,height=25)

        GLineEdit_564=tk.Entry(self)
        GLineEdit_564["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_564["font"] = ft
        GLineEdit_564["fg"] = "#333333"
        GLineEdit_564["justify"] = "center"
        GLineEdit_564["text"] = ""
        GLineEdit_564.place(x=210,y=100,width=130,height=30)
