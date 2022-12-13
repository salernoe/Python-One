import tkinter as tk
import tkinter.font as tkFont

class descuentos(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Descuento")
        width=533
        height=133
        screenwidth = self.winfo_screenwidth()
        screenheight =self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_479=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_479["font"] = ft
        GLabel_479["fg"] = "#333333"
        GLabel_479["justify"] = "center"
        GLabel_479["text"] = "Día"
        GLabel_479.place(x=20,y=40,width=70,height=25)

        GListBox_523=tk.Listbox(self)
        GListBox_523["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_523["font"] = ft
        GListBox_523["fg"] = "#333333"
        GListBox_523["justify"] = "center"
        GListBox_523.place(x=80,y=40,width=110,height=30)

        GLabel_312=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_312["font"] = ft
        GLabel_312["fg"] = "#333333"
        GLabel_312["justify"] = "center"
        GLabel_312["text"] = "Porcentaje"
        GLabel_312.place(x=220,y=40,width=70,height=25)

        GListBox_198=tk.Listbox(self)
        GListBox_198["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_198["font"] = ft
        GListBox_198["fg"] = "#333333"
        GListBox_198["justify"] = "center"
        GListBox_198.place(x=300,y=40,width=110,height=30)

