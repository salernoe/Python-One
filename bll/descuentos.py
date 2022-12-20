from dal.db import Db



def agregar(dia, descuento):    
    sql = "INSERT INTO descuentos(Dia, descuento) VALUES(?, ?);"
    parametros = (dia, descuento)
    Db.ejecutar(sql, parametros)

def actualizar(dia, descuento, id):    
    sql = "UPDATE descuentos SET Dia = ?, descuento = ? WHERE id descuentod = ? AND ESTADO = 1;"
    parametros = (dia, descuento, id)
    Db.ejecutar(sql, parametros)    

def eliminar(id, logical = True):    
    if logical:
        sql = "UPDATE descuentos SET ESTADO = 0 WHERE id descuentod = ? AND estado = 1;"
    else:
        sql = "DELETE FROM descuentos WHERE ID = ?;"
    parametros = (id,)
    Db.ejecutar(sql, parametros)

def listar():
    sql = '''SELECT id descuentod, Dia, descuentos, estado
            FROM descuentos;'''
    result = Db.consultar(sql)
    return result

def obtener_id(id):
    sql = '''SELECT id descuentod, Dia, descuento, estado
            FROM decuentos           
            WHERE id descuentod = ? AND estado = 1;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result

