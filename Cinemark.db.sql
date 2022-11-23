BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Salas" (
	"idsala"	INTEGER NOT NULL,
	"pelicula"	TEXT NOT NULL,
	"butaca"	INTEGER NOT NULL,
	"fila"	TEXT NOT NULL,
	"horario"	TEXT NOT NULL,
	"fecha"	TEXT NOT NULL,
	PRIMARY KEY("idsala" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Reserva" (
	"idreserva"	INTEGER NOT NULL,
	"sala"	INTEGER NOT NULL,
	"pelicula"	BLOB NOT NULL,
	"2d"	BLOB,
	"3d"	BLOB,
	"fecha"	TEXT NOT NULL,
	"hora"	TEXT NOT NULL,
	"cantidad"	INTEGER NOT NULL,
	"sucursal"	TEXT NOT NULL,
	"socio"	TEXT NOT NULL,
	PRIMARY KEY("idreserva" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Cliente" (
	"id"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL,
	"apellido"	TEXT NOT NULL,
	"edad"	INTEGER NOT NULL,
	"email"	TEXT,
	"telefono"	TEXT NOT NULL,
	"historial de peliculas"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Tarjeta" (
	"idtarjeta"	INTEGER NOT NULL,
	"tipo_de_tarjeta"	TEXT NOT NULL,
	"nombre"	TEXT NOT NULL,
	"codigo_de_cliente"	TEXT NOT NULL,
	PRIMARY KEY("idtarjeta" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Descuento" (
	"iddescuento"	INTEGER NOT NULL,
	"dia"	TEXT NOT NULL,
	"porcentaje"	REAL NOT NULL,
	"precio"	REAL NOT NULL,
	PRIMARY KEY("iddescuento" AUTOINCREMENT)
);
COMMIT;
