import tkinter as tk
import tkinter.font as tkFont

class butacas(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Cargar butacas")
        #setting window size
        width=384
        height=225
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_42=tk.Label(self)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_42["font"] = ft
        GLabel_42["fg"] = "#333333"
        GLabel_42["justify"] = "center"
        GLabel_42["text"] = "Cargar butacas"
        GLabel_42.place(x=50,y=10,width=217,height=30)

        GLabel_416=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_416["font"] = ft
        GLabel_416["fg"] = "#333333"
        GLabel_416["justify"] = "center"
        GLabel_416["text"] = "Id butacas"
        GLabel_416.place(x=10,y=50,width=70,height=25)

        GLineEdit_416=tk.Entry(self)
        GLineEdit_416["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_416["font"] = ft
        GLineEdit_416["fg"] = "#333333"
        GLineEdit_416["justify"] = "center"
        GLineEdit_416["text"] = "Entry"
        GLineEdit_416.place(x=90,y=50,width=70,height=30)

        GLabel_386=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_386["font"] = ft
        GLabel_386["fg"] = "#333333"
        GLabel_386["justify"] = "center"
        GLabel_386["text"] = "Fila"
        GLabel_386.place(x=180,y=50,width=70,height=25)

        GLineEdit_470=tk.Entry(self)
        GLineEdit_470["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_470["font"] = ft
        GLineEdit_470["fg"] = "#333333"
        GLineEdit_470["justify"] = "center"
        GLineEdit_470["text"] = "Entry"
        GLineEdit_470.place(x=250,y=50,width=80,height=30)

        GLabel_643=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_643["font"] = ft
        GLabel_643["fg"] = "#333333"
        GLabel_643["justify"] = "center"
        GLabel_643["text"] = "Numero de  Butaca"
        GLabel_643.place(x=10,y=100,width=70,height=25)

        GLineEdit_930=tk.Entry(self)
        GLineEdit_930["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_930["font"] = ft
        GLineEdit_930["fg"] = "#333333"
        GLineEdit_930["justify"] = "center"
        GLineEdit_930["text"] = "Entry"
        GLineEdit_930.place(x=90,y=100,width=70,height=30)

        GLabel_666=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_666["font"] = ft
        GLabel_666["fg"] = "#333333"
        GLabel_666["justify"] = "center"
        GLabel_666["text"] = "Id de sala"
        GLabel_666.place(x=180,y=100,width=70,height=25)

        GListBox_195=tk.Listbox(self)
        GListBox_195["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_195["font"] = ft
        GListBox_195["fg"] = "#333333"
        GListBox_195["justify"] = "center"
        GListBox_195.place(x=250,y=100,width=80,height=30)

        GButton_563=tk.Button(self)
        GButton_563["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_563["font"] = ft
        GButton_563["fg"] = "#000000"
        GButton_563["justify"] = "center"
        GButton_563["text"] = "Aceptar"
        GButton_563.place(x=140,y=170,width=70,height=25)
        GButton_563["command"] = self.GButton_563_command

        GButton_515=tk.Button(self)
        GButton_515["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_515["font"] = ft
        GButton_515["fg"] = "#000000"
        GButton_515["justify"] = "center"
        GButton_515["text"] = "Cancelar"
        GButton_515.place(x=230,y=170,width=70,height=25)
        GButton_515["command"] = self.GButton_515_command

    def GButton_563_command(self):
        print("command")


    def GButton_515_command(self):
        print("command")


