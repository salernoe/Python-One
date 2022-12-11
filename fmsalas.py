import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=519
        height=143
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_18=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_18["font"] = ft
        GLabel_18["fg"] = "#333333"
        GLabel_18["justify"] = "center"
        GLabel_18["text"] = "Fecha"
        GLabel_18.place(x=20,y=30,width=83,height=30)

        GLineEdit_854=tk.Entry(root)
        GLineEdit_854["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_854["font"] = ft
        GLineEdit_854["fg"] = "#333333"
        GLineEdit_854["justify"] = "center"
        GLineEdit_854["text"] = ""
        GLineEdit_854.place(x=90,y=30,width=138,height=33)

        GLabel_983=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_983["font"] = ft
        GLabel_983["fg"] = "#333333"
        GLabel_983["justify"] = "center"
        GLabel_983["text"] = "hora"
        GLabel_983.place(x=20,y=80,width=70,height=25)

        GLineEdit_526=tk.Entry(root)
        GLineEdit_526["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_526["font"] = ft
        GLineEdit_526["fg"] = "#333333"
        GLineEdit_526["justify"] = "center"
        GLineEdit_526["text"] = ""
        GLineEdit_526.place(x=90,y=80,width=139,height=30)

        GLabel_495=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_495["font"] = ft
        GLabel_495["fg"] = "#333333"
        GLabel_495["justify"] = "center"
        GLabel_495["text"] = "Pelicula"
        GLabel_495.place(x=280,y=30,width=70,height=25)

        GListBox_901=tk.Listbox(root)
        GListBox_901["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_901["font"] = ft
        GListBox_901["fg"] = "#333333"
        GListBox_901["justify"] = "center"
        GListBox_901.place(x=360,y=80,width=140,height=30)

        GLabel_534=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_534["font"] = ft
        GLabel_534["fg"] = "#333333"
        GLabel_534["justify"] = "center"
        GLabel_534["text"] = "salas"
        GLabel_534.place(x=280,y=80,width=70,height=25)

        GListBox_71=tk.Listbox(root)
        GListBox_71["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_71["font"] = ft
        GListBox_71["fg"] = "#333333"
        GListBox_71["justify"] = "center"
        GListBox_71.place(x=360,y=30,width=145,height=30)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
