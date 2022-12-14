import tkinter as tk
import tkinter.font as tkFont

class sesion(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("sesión")
        
        width=319
        height=221
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_763=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_763["font"] = ft
        GLabel_763["fg"] = "#333333"
        GLabel_763["justify"] = "center"
        GLabel_763["text"] = "Fecha"
        GLabel_763.place(x=10,y=50,width=70,height=25)

        GLineEdit_172=tk.Entry(self)
        GLineEdit_172["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_172["font"] = ft
        GLineEdit_172["fg"] = "#333333"
        GLineEdit_172["justify"] = "center"
        GLineEdit_172["text"] = ""
        GLineEdit_172.place(x=70,y=50,width=110,height=30)

        GLabel_115=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_115["font"] = ft
        GLabel_115["fg"] = "#333333"
        GLabel_115["justify"] = "center"
        GLabel_115["text"] = "Sala"
        GLabel_115.place(x=10,y=100,width=70,height=25)

        GListBox_777=tk.Listbox(self)
        GListBox_777["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_777["font"] = ft
        GListBox_777["fg"] = "#333333"
        GListBox_777["justify"] = "center"
        GListBox_777.place(x=70,y=100,width=110,height=30)

        GLabel_232=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_232["font"] = ft
        GLabel_232["fg"] = "#333333"
        GLabel_232["justify"] = "center"
        GLabel_232["text"] = "Pelicula"
        GLabel_232.place(x=0,y=150,width=70,height=25)

        GListBox_138=tk.Listbox(self)
        GListBox_138["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_138["font"] = ft
        GListBox_138["fg"] = "#333333"
        GListBox_138["justify"] = "center"
        GListBox_138.place(x=70,y=150,width=110,height=30)
