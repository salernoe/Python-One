import tkinter as tk
import tkinter.font as tkFont

class reservas(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Reservas")
        #setting window size
        width=440
        height=312
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_404=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_404["font"] = ft
        GLabel_404["fg"] = "#333333"
        GLabel_404["justify"] = "center"
        GLabel_404["text"] = "Hola!!!, por favor Carga tu reserva  no te olvides  llenar todos los campos "
        GLabel_404.place(x=10,y=10,width=404,height=39)

        GLabel_275=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_275["font"] = ft
        GLabel_275["fg"] = "#333333"
        GLabel_275["justify"] = "center"
        GLabel_275["text"] = "Usuarios"
        GLabel_275.place(x=20,y=80,width=70,height=25)

        GLineEdit_306=tk.Entry(self)
        GLineEdit_306["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_306["font"] = ft
        GLineEdit_306["fg"] = "#333333"
        GLineEdit_306["justify"] = "center"
        GLineEdit_306["text"] = "Entry"
        GLineEdit_306.place(x=90,y=80,width=90,height=30)

        GLabel_258=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_258["font"] = ft
        GLabel_258["fg"] = "#333333"
        GLabel_258["justify"] = "center"
        GLabel_258["text"] = "Fecha"
        GLabel_258.place(x=190,y=80,width=70,height=25)

        GLineEdit_362=tk.Entry(self)
        GLineEdit_362["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_362["font"] = ft
        GLineEdit_362["fg"] = "#333333"
        GLineEdit_362["justify"] = "center"
        GLineEdit_362["text"] = "Entry"
        GLineEdit_362.place(x=260,y=80,width=90,height=30)

        GLabel_961=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_961["font"] = ft
        GLabel_961["fg"] = "#333333"
        GLabel_961["justify"] = "center"
        GLabel_961["text"] = "Butaca"
        GLabel_961.place(x=20,y=140,width=70,height=25)

        GListBox_8=tk.Listbox(self)
        GListBox_8["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_8["font"] = ft
        GListBox_8["fg"] = "#333333"
        GListBox_8["justify"] = "center"
        GListBox_8.place(x=90,y=140,width=90,height=30)

        GLabel_332=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_332["font"] = ft
        GLabel_332["fg"] = "#333333"
        GLabel_332["justify"] = "center"
        GLabel_332["text"] = "Descuento"
        GLabel_332.place(x=190,y=140,width=70,height=25)

        GLineEdit_228=tk.Entry(self)
        GLineEdit_228["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_228["font"] = ft
        GLineEdit_228["fg"] = "#333333"
        GLineEdit_228["justify"] = "center"
        GLineEdit_228["text"] = "Entry"
        GLineEdit_228.place(x=260,y=140,width=90,height=30)

        GLabel_433=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_433["font"] = ft
        GLabel_433["fg"] = "#333333"
        GLabel_433["justify"] = "center"
        GLabel_433["text"] = "Tarjeta"
        GLabel_433.place(x=120,y=190,width=70,height=25)

        GLineEdit_666=tk.Entry(self)
        GLineEdit_666["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_666["font"] = ft
        GLineEdit_666["fg"] = "#333333"
        GLineEdit_666["justify"] = "center"
        GLineEdit_666["text"] = "Entry"
        GLineEdit_666.place(x=190,y=190,width=90,height=30)

        GButton_517=tk.Button(self)
        GButton_517["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_517["font"] = ft
        GButton_517["fg"] = "#000000"
        GButton_517["justify"] = "center"
        GButton_517["text"] = "Aceptar"
        GButton_517.place(x=190,y=260,width=70,height=25)
        GButton_517["command"] = self.GButton_517_command

        GButton_779=tk.Button(self)
        GButton_779["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_779["font"] = ft
        GButton_779["fg"] = "#000000"
        GButton_779["justify"] = "center"
        GButton_779["text"] = "Cancelar"
        GButton_779.place(x=280,y=260,width=70,height=25)
        GButton_779["command"] = self.GButton_779_command

    def GButton_517_command(self):
        print("command")


    def GButton_779_command(self):
        print("command")


