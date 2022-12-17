import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Salas")
        #setting window size
        width=495
        height=370
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_336=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_336["font"] = ft
        GLabel_336["fg"] = "#333333"
        GLabel_336["justify"] = "center"
        GLabel_336["text"] = "Numero de sala"
        GLabel_336.place(x=10,y=70,width=110,height=25)

        GLabel_259=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_259["font"] = ft
        GLabel_259["fg"] = "#333333"
        GLabel_259["justify"] = "center"
        GLabel_259["text"] = "Salas"
        GLabel_259.place(x=230,y=20,width=70,height=25)

        GLineEdit_528=tk.Entry(root)
        GLineEdit_528["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_528["font"] = ft
        GLineEdit_528["fg"] = "#333333"
        GLineEdit_528["justify"] = "center"
        GLineEdit_528["text"] = "Entry"
        GLineEdit_528.place(x=120,y=70,width=100,height=30)

        GLabel_162=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_162["font"] = ft
        GLabel_162["fg"] = "#333333"
        GLabel_162["justify"] = "center"
        GLabel_162["text"] = "Pelicula"
        GLabel_162.place(x=40,y=120,width=70,height=25)

        GLineEdit_97=tk.Entry(root)
        GLineEdit_97["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_97["font"] = ft
        GLineEdit_97["fg"] = "#333333"
        GLineEdit_97["justify"] = "center"
        GLineEdit_97["text"] = "Entry"
        GLineEdit_97.place(x=120,y=120,width=250,height=30)

        GLabel_201=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_201["font"] = ft
        GLabel_201["fg"] = "#333333"
        GLabel_201["justify"] = "center"
        GLabel_201["text"] = "Butaca"
        GLabel_201.place(x=40,y=170,width=70,height=25)

        GLineEdit_331=tk.Entry(root)
        GLineEdit_331["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_331["font"] = ft
        GLineEdit_331["fg"] = "#333333"
        GLineEdit_331["justify"] = "center"
        GLineEdit_331["text"] = "Entry"
        GLineEdit_331.place(x=120,y=170,width=100,height=30)

        GLabel_524=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_524["font"] = ft
        GLabel_524["fg"] = "#333333"
        GLabel_524["justify"] = "center"
        GLabel_524["text"] = "Horario"
        GLabel_524.place(x=30,y=220,width=70,height=25)

        GLineEdit_444=tk.Entry(root)
        GLineEdit_444["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_444["font"] = ft
        GLineEdit_444["fg"] = "#333333"
        GLineEdit_444["justify"] = "center"
        GLineEdit_444["text"] = "Entry"
        GLineEdit_444.place(x=120,y=220,width=100,height=30)

        GLabel_173=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_173["font"] = ft
        GLabel_173["fg"] = "#333333"
        GLabel_173["justify"] = "center"
        GLabel_173["text"] = "Formato"
        GLabel_173.place(x=30,y=270,width=70,height=25)

        GLineEdit_292=tk.Entry(root)
        GLineEdit_292["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_292["font"] = ft
        GLineEdit_292["fg"] = "#333333"
        GLineEdit_292["justify"] = "center"
        GLineEdit_292["text"] = "Entry"
        GLineEdit_292.place(x=120,y=270,width=100,height=30)

        GButton_852=tk.Button(root)
        GButton_852["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_852["font"] = ft
        GButton_852["fg"] = "#000000"
        GButton_852["justify"] = "center"
        GButton_852["text"] = "Aceptar"
        GButton_852.place(x=300,y=320,width=70,height=25)
        GButton_852["command"] = self.GButton_852_command

        GButton_275=tk.Button(root)
        GButton_275["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_275["font"] = ft
        GButton_275["fg"] = "#000000"
        GButton_275["justify"] = "center"
        GButton_275["text"] = "Cancelar"
        GButton_275.place(x=400,y=320,width=70,height=25)
        GButton_275["command"] = self.GButton_275_command

    def GButton_852_command(self):
        print("command")


    def GButton_275_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
