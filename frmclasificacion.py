import tkinter as tk
import tkinter.font as tkFont

class clasificacion (tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Clasificacion")
        
        width=537
        height=212
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_656=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_656["font"] = ft
        GLabel_656["fg"] = "#333333"
        GLabel_656["justify"] = "center"
        GLabel_656["text"] = "Identificador"
        GLabel_656.place(x=20,y=30,width=70,height=25)

        GLineEdit_487=tk.Entry(self)
        GLineEdit_487["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_487["font"] = ft
        GLineEdit_487["fg"] = "#333333"
        GLineEdit_487["justify"] = "center"
        GLineEdit_487["text"] = ""
        GLineEdit_487.place(x=110,y=30,width=110,height=30)

        GLabel_736=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_736["font"] = ft
        GLabel_736["fg"] = "#333333"
        GLabel_736["justify"] = "center"
        GLabel_736["text"] = "Recomendación"
        GLabel_736.place(x=250,y=30,width=70,height=25)

        GLineEdit_160=tk.Entry(self)
        GLineEdit_160["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_160["font"] = ft
        GLineEdit_160["fg"] = "#333333"
        GLineEdit_160["justify"] = "center"
        GLineEdit_160["text"] = ""
        GLineEdit_160.place(x=340,y=30,width=110,height=30)

        GLabel_9=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_9["font"] = ft
        GLabel_9["fg"] = "#333333"
        GLabel_9["justify"] = "center"
        GLabel_9["text"] = "Descripción"
        GLabel_9.place(x=20,y=100,width=70,height=25)

        GLineEdit_400=tk.Entry(self)
        GLineEdit_400["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_400["font"] = ft
        GLineEdit_400["fg"] = "#333333"
        GLineEdit_400["justify"] = "center"
        GLineEdit_400["text"] = ""
        GLineEdit_400.place(x=110,y=80,width=340,height=60)

