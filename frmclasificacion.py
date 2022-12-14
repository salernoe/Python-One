import tkinter as tk
import tkinter.font as tkFont

class clasificacion(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Clasificacion ")
        #setting window size
        width=461
        height=237
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_476=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_476["font"] = ft
        GLabel_476["fg"] = "#333333"
        GLabel_476["justify"] = "center"
        GLabel_476["text"] = "Formato"
        GLabel_476.place(x=20,y=50,width=70,height=25)

        GListBox_667=tk.Listbox(self)
        GListBox_667["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_667["font"] = ft
        GListBox_667["fg"] = "#333333"
        GListBox_667["justify"] = "center"
        GListBox_667.place(x=90,y=50,width=110,height=30)

        GLabel_731=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_731["font"] = ft
        GLabel_731["fg"] = "#333333"
        GLabel_731["justify"] = "center"
        GLabel_731["text"] = "Idioma"
        GLabel_731.place(x=20,y=110,width=70,height=25)

        GLineEdit_371=tk.Entry(self)
        GLineEdit_371["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_371["font"] = ft
        GLineEdit_371["fg"] = "#333333"
        GLineEdit_371["justify"] = "center"
        GLineEdit_371["text"] = ""
        GLineEdit_371.place(x=90,y=110,width=300,height=30)

        GLabel_539=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_539["font"] = ft
        GLabel_539["fg"] = "#333333"
        GLabel_539["justify"] = "center"
        GLabel_539["text"] = "Subtítulos"
        GLabel_539.place(x=10,y=160,width=70,height=25)

        GListBox_643=tk.Listbox(self)
        GListBox_643["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_643["font"] = ft
        GListBox_643["fg"] = "#333333"
        GListBox_643["justify"] = "center"
        GListBox_643.place(x=90,y=160,width=110,height=30)
