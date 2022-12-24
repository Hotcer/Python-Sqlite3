import sqlite3 as sql
"""""
conn = sql.connect('Alumnos.db', isolation_level=None)
c = conn.cursor()
c.execute('CREATE TABLE alumnos (nombre text, apellido text, id integer)')
conn.close() """""


def insertarFilas(alumnosList):
    conn = sql.connect('Alumnos.db', isolation_level=None)
    c = conn.cursor()
    instruccion = f"INSERT INTO alumnos values (?, ?, ?)"
    c.executemany(instruccion, alumnosList)
    conn.close()


if __name__ == '__main__':
    alumnos = [
        ('David', 'Gonzalez', 15.52548),
        ('David', 'Gonzalez', 15.52548),
        ('David', 'Gonzalez', 15.52548),
        ('David', 'Gonzalez', 15.52548),
        ('David', 'Gonzalez', 15.52548),
        ('David', 'Gonzalez', 15.52548),
        ('David', 'Gonzalez', 15.52548),
        ('David', 'Gonzalez', 15.52548)
    ]
insertarFilas(alumnos)