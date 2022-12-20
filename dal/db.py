import sqlite3
from datetime import date
import hashlib

#database = "super.db" 
database = "tablatpfinal"
class Db:
    @staticmethod
    def ejecutar(consulta, parametros = ()):
        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            cursor.execute(consulta, parametros)
            cnn.commit()            
    
    @staticmethod
    def consultar(consulta, pametros = (), fetchAll = True):
        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            cursor.execute(consulta, pametros)
            if fetchAll:
                result = cursor.fetchall()
            else:
                result = cursor.fetchone()
            return result
    
    @staticmethod
    def crear_tablas():
        sql_usuarios = '''CREATE TABLE IF NOT EXISTS "Usuarios" (
                                "UsuarioId"	INTEGER NOT NULL,
                                "Apellido"	VARCHAR(50),
                                "Nombre"	VARCHAR(30),
                                "FechaNacimiento"	VARCHAR(23),
                                "Dni"	INTEGER,
                                "CorreoElectronico"	VARCHAR(30),
                                "Usuario"	VARCHAR(15) UNIQUE,
                                "Contrasenia"	VARCHAR(100),
                                "RolId"	INTEGER,
                                "Activo"	INTEGER NOT NULL DEFAULT 1,
                                PRIMARY KEY("UsuarioId" AUTOINCREMENT)
                            );'''
        sql_roles = '''CREATE TABLE IF NOT EXISTS "Roles" (
                            "RolId"	INTEGER NOT NULL,
                            "Nombre"	VARCHAR(30) NOT NULL UNIQUE,
                            "Activo"	INTEGER NOT NULL DEFAULT 1,
                            PRIMARY KEY("RolId")
                        );'''
        sql_salas = '''CREATE TABLE "salas" (
	                        "idsalas"	INTEGER NOT NULL UNIQUE,
	                        "Numero_de_sala"	TEXT NOT NULL UNIQUE,
	                        "Pelicula"	TEXT NOT NULL,
	                        "butacas"	NUMERIC NOT NULL,
	                        "Horarios"	TEXT NOT NULL,
	                        "Formato"	TEXT NOT NULL,
                            "UsuarioId"	TEXT,
	                        FOREIGN KEY("UsuarioId") REFERENCES "Usuario"("UsuarioId"),
	                        PRIMARY KEY("idsalas" AUTOINCREMENT)
                        );'''
        sql_descuentos = '''CREATE TABLE "descuentos " (
	                        "id descuentod "	INTEGER NOT NULL,
	                        "Dia"	TEXT NOT NULL,
	                        "descuento"	REAL NOT NULL,
	                        "estado"	INTEGER NOT NULL,
	                        PRIMARY KEY("id descuentod " AUTOINCREMENT) 
                        );'''

        tablas = {"Usuarios": sql_usuarios, "Roles": sql_roles,"descuentos":sql_descuentos ,"salas": sql_salas} # de aca saque 
        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Creando tabla {tabla}")
                cursor.execute(sql)
                # TODO agregar commit
            
    @staticmethod
    def poblar_tablas():        
        sql_roles = '''INSERT INTO Roles (RolId, Nombre) 
                    VALUES 
                        (1, "Administrador"),
                        (2, "Supervisor"),
                        (3, "Operador"),
                        (4, "Cliente");'''

        sql_descuentos = '''INSERT INTO DESCUENTOS (Dia, descuento) 
                        VALUES 
                            ("LUNES", 0.2),
                            ("MARTES", 0.15),
                            ("MIERCOLES", 0.2),
                            ("JUEVES", 0.15),
                            ("VIERNES", 0.1),
                            ("SABADO", 0.1),
                            ("DOMINGO", 0.1);'''
        

        tablas = {"Roles": sql_roles, "descuentos":sql_descuentos } 
                

        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Poblando tabla {tabla}")
                cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
                count = int(cursor.fetchone()[0])
                if count == 0:
                    cursor.execute(sql)
    @staticmethod
    def formato_fecha_db(fecha):
        return date(int(fecha[6:]), int(fecha[3:5]), int(fecha[0:2]))
    
    @staticmethod
    def encriptar_contraseña(contrasenia):
        return hashlib.sha256(contrasenia.encode("utf-8")).hexdigest()