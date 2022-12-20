from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont # para generar grillas
import tkinter.messagebox as tkMsgBox
import bll.salas as salas1 #ver si sigue este parametro
import bll.usuarios as usuar

class Sala1(Toplevel):
    def __init__(self, master=usuar, idsalas = False, UsuarioId = None):        
        super().__init__(master)
        self.master = master
        self.UsuarioId = UsuarioId      
        self.title("Registro de salas")        
        width=443
        height=423
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        
        GLabel_336=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_336["font"] = ft
        GLabel_336["fg"] = "#333333"
        GLabel_336["justify"] = "center"
        GLabel_336["text"] = "Numero de sala"
        GLabel_336.place(x=10,y=70,width=110,height=25)
        
         
       
        GLabel_259=tk.Label(self)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_259["font"] = ft
        GLabel_259["fg"] = "#333333"
        GLabel_259["justify"] = "center"
        GLabel_259["text"] = "Salas"
        GLabel_259.place(x=230,y=20,width=70,height=25)

        
        GLineEdit_528=tk.Entry(self)
        GLineEdit_528["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_528["font"] = ft
        GLineEdit_528["fg"] = "#333333"
        GLineEdit_528["justify"] = "center"
        GLineEdit_528["text"] = "Entry"
        GLineEdit_528.place(x=120,y=70,width=100,height=30)

        GLabel_162=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_162["font"] = ft
        GLabel_162["fg"] = "#333333"
        GLabel_162["justify"] = "center"
        GLabel_162["text"] = "Pelicula"
        GLabel_162.place(x=40,y=120,width=70,height=25)

        GLineEdit_97=tk.Entry(self)
        GLineEdit_97["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_97["font"] = ft
        GLineEdit_97["fg"] = "#333333"
        GLineEdit_97["justify"] = "center"
        GLineEdit_97["text"] = "Entry"
        GLineEdit_97.place(x=120,y=120,width=250,height=30)

        GLabel_201=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_201["font"] = ft
        GLabel_201["fg"] = "#333333"
        GLabel_201["justify"] = "center"
        GLabel_201["text"] = "Butaca"
        GLabel_201.place(x=40,y=170,width=70,height=25)

        GLineEdit_331=tk.Entry(self)
        GLineEdit_331["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_331["font"] = ft
        GLineEdit_331["fg"] = "#333333"
        GLineEdit_331["justify"] = "center"
        GLineEdit_331["text"] = "Entry"
        GLineEdit_331.place(x=120,y=170,width=100,height=30)

        GLabel_524=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_524["font"] = ft
        GLabel_524["fg"] = "#333333"
        GLabel_524["justify"] = "center"
        GLabel_524["text"] = "Horario"
        GLabel_524.place(x=30,y=220,width=70,height=25)

        GLineEdit_444=tk.Entry(self)
        GLineEdit_444["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_444["font"] = ft
        GLineEdit_444["fg"] = "#333333"
        GLineEdit_444["justify"] = "center"
        GLineEdit_444["text"] = "Entry"
        GLineEdit_444.place(x=120,y=220,width=100,height=30)

        GLabel_173=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_173["font"] = ft
        GLabel_173["fg"] = "#333333"
        GLabel_173["justify"] = "center"
        GLabel_173["text"] = "Formato"
        GLabel_173.place(x=30,y=270,width=70,height=25)

        GLineEdit_292=tk.Entry(self)
        GLineEdit_292["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_292["font"] = ft
        GLineEdit_292["fg"] = "#333333"
        GLineEdit_292["justify"] = "center"
        GLineEdit_292["text"] = "Entry"
        GLineEdit_292.place(x=120,y=270,width=100,height=30)
        
        roles = dict(rol.listar())# haca hay problea con el rol ver en la tabla roles bll
        if idsalas:
            cb_roles = ttk.Combobox(self, state="readonly", values=list(roles.values()), name="cbRoles")
        else:
            cb_roles = ttk.Combobox(self, state="disabled", values=list(roles.values()), name="cbRoles")
            cb_roles.set(roles[4])
        cb_roles.place(x=140,y=330,width=283,height=30)

        GButton_825 = Button(self)
        GButton_825["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_825["font"] = ft
        GButton_825["fg"] = "#000000"
        GButton_825["justify"] = "center"
        GButton_825["text"] = "Aceptar"
        GButton_825.place(x=270,y=370,width=70,height=25)
        GButton_825["command"] = self.aceptar
        
        GButton_341 = Button(self)
        GButton_341["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_341["font"] = ft
        GButton_341["fg"] = "#000000"
        GButton_341["justify"] = "center"
        GButton_341["text"] = "Cancelar"
        GButton_341.place(x=350,y=370,width=70,height=25)
        GButton_341["command"] = self.GButton_341_command

        if idsalas is not None:
            usuario = user.obtener_id(idsalas)
            if usuario is None:
               tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos del usuario, reintente nuevamente")
               #esto es caja de cometarios 
               self.destroy()
            else:
                # TODO bloquear el campo usuario
                GLineEdit_97.insert(0, usuario[1])
                GLineEdit_292.insert(0, usuario[2])
                GLineEdit_331.insert(0, usuario[3]) # TODO corregir formato de fecha
                GLineEdit_528.insert(0, usuario[4])
                GLineEdit_444.insert(0, usuario[5])
                GLineEdit_292.insert(0, usuario[6])                
                cb_roles.set(usuario[8])

    def get_value(self, name):
        return self.nametowidget(name).get()

    def get_index(self, name):
        return self.nametowidget(name).current() + 1

    def GButton_341_command(self):
        self.destroy()

    def aceptar(self):
        try:            
            apellido = self.get_value("txtApellido")
            nombre = self.get_value("txtNombre")            
            fecha_nac = self.get_value("txtFechaNac")            
            dni = self.get_value("txtDni")
            email = self.get_value("txtEmail")            
            usuario = self.get_value("txtUsuario")

            contrasenia = self.get_value("txtContrasenia")            
            confirmacion = self.get_value("txtConfirmacion")
            rol_id = self.get_index("cbRoles")

            # TODO validar los datos antes de ingresar
            if self.user_id is None:
                print("Alta de usuario")
                if not user.existe(usuario):
                    user.agregar(apellido, nombre, fecha_nac, dni, email, usuario, contrasenia, rol_id)
                    tkMsgBox.showinfo(self.master.title(), "Registro agregado!!!!!!")                
                    try:
                        self.master.refrescar()
                    except Exception as ex:
                        print(ex)
                    self.destroy()                
                else:
                    tkMsgBox.showwarning(self.master.title(), "Usuario existente en nuestros registros")
            else:
                print("Actualizacion de usuario")
                user.actualizar(self.user_id, apellido, nombre, fecha_nac, dni, email, contrasenia, rol_id)  # TODO ver el tema de la contraseña
                tkMsgBox.showinfo(self.master.title(), "Registro modificado!!!!!!")                
                self.master.refrescar()
                self.destroy()  

        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))