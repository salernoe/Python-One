from dal.db import Db

def agregar(Numero_de_sala, Pelicula, butacas, Horarios, Formato, UsuarioId):    
    sql = "INSERT INTO Usuarios(Numero_de_sala, Pelicula,butacas, Horarios, Formato, Usuario,UsuarioId) VALUES(?, ?, ?, ?, ?, ?, ?, ?);"
    parametros = (Numero_de_sala, Pelicula,butacas, Horarios, Formato,UsuarioId)
    Db.ejecutar(sql, parametros)

def actualizar(id, Numero_de_sala, Pelicula, butacas, Horarios, Formato, UsuarioId, rol_Id):    
    sql = "UPDATE salas SET Numero_de_sala = ?, Pelicula = ?, butacas = ?,Horarios = ?, Formato = ?, UsuarioId = ? WHERE UsuarioId = ? AND Activo = 1;"
    parametros = (Numero_de_sala, Pelicula, butacas, Horarios, Formato, UsuarioId, id)
    Db.ejecutar(sql, parametros)    

def eliminar(id, logical = True):    
    if logical:
        sql = "UPDATE salas SET Activo = 0 WHERE UsuarioId = ? AND Activo = 1;"
    else:
        sql = "DELETE FROM salas WHERE UsuarioId = ?;"
    parametros = (id,)
    Db.ejecutar(sql, parametros)

def listar():
    sql = '''SELECT u.UsuarioId, u.Numero_de_sala, u.Pelicula, u.butacas, u.Horarios, u.Formato, u.UsuarioId, r.Nombre usuario
            FROM Usuarios u
            INNER JOIN Roles r ON u.UsuarioId = r.UsuarioId
            WHERE u.Activo = 1;'''
    result = Db.consultar(sql)
    return result

def filtrar(salas):    
    sql = '''SELECT u.UsuarioId, u.Numero_de_sala, u.Pelicula, u.butacas, u.Horarios, u.Formato, u.Usuario, u.UsuarioId, r.Nombre usuario
            FROM Usuarios u
            INNER JOIN Roles r ON u.UsuarioId = r.UsuarioId
            WHERE u.Usuario LIKE ? AND u.Activo = 1;'''    
    parametros = ('%{}%'.format(salas),)    
    result = Db.consultar(sql, parametros)
    return result

"""def validar(usuario, contrasenia):     #comente esto por que no se de donde saale 
    sql = "SELECT Usuario FROM Usuarios WHERE Usuario = ? AND Contrasenia = ? AND Activo = 1;"
    parametros = (usuario, Db.encriptar_contraseña(contrasenia))
    result = Db.consultar(sql, parametros, False)
    return result != None"""

def existe(sala):# cambie usuario por sala
    sql = "SELECT COUNT(*) FROM Usuarios WHERE Usuario = ? AND Activo = 1;"
    parametros = (sala,)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1

def obtener_id(id):
    sql = '''SELECT u.UsuarioId, u.Numero_de_sala, u.Pelicula, u.butacas, u.Horarios, u.Formato, u.Usuario, u.UsuarioId, r.Nombre usuario
            FROM Usuarios u
            INNER JOIN Roles r ON u.UsuarioId = r.UsuarioId
            WHERE u.UsuarioId = ? AND u.Activo = 1;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result