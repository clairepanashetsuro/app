import sqlite3
from contextlib import contextmanager
sqlite_file_name = "school.db"

@contextmanager
def get_db_connection():
    connection = sqlite3.connect(sqlite_file_name)
    connection.row_factory= sqlite3.Row
    try:
        yield connection
    finally:
        connection.close()

def create_table():
    with get_db_connection() as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS students(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         age INTEGER NOT NULL,
         email TEXT NOT NULL,
         country TEXT NOT NULL,
         id_number INTEGER NOT NULL ) ''')

        connection.execute('''CREATE TABLE IF NOT EXISTS teachers(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         age INTEGER NOT NULL,
         email TEXT NOT NULL,
         country TEXT NOT NULL,
         id_number INTEGER NOT NULL ) ''')
        
        connection.execute('''CREATE TABLE IF NOT EXISTS courses(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         department TEXT NOT NULL,
         description TEXT NOT NULL,
         is_online BOOLEAN DEFAULT FALSE,
         credit_hours INTEGER NOT NULL ) ''')

def add_student(name,age,email,country,id_number):
    with get_db_connection() as connection:
        connection.execute(
            'INSERT INTO students (name, age,email,country,id_number) VALUES (?,?,?,?,?)',
            (name,age,email,country,id_number),
        )
        connection.commit()

def get_students():
    with get_db_connection() as connection:
        return connection.execute('SELECT * FROM students').fetchall()

def update_student(id_number, name, age, email, country):
    with get_db_connection() as connection:
        connection.execute(
            'UPDATE students SET name = ?, age = ?, email = ?, country = ? WHERE id_number = ?',
            (name, age, email, country, id_number)
        )
        connection.commit()

def delete_student(id_number):
    with get_db_connection() as connection:
        connection.execute('DELETE FROM students WHERE id_number = ?', (id_number,))
        connection.commit()

def add_teacher(name,age,email,country,id_number):
    with get_db_connection() as connection:
        connection.execute(
            'INSERT INTO teachers (name, age,email,country,id_number) VALUES (?,?,?,?,?)',
            (name,age,email,country,id_number),
        )
        connection.commit()

def get_teachers():
    with get_db_connection() as connection:
        return connection.execute('SELECT * FROM teachers').fetchall()

def update_teacher(id_number, name, age, email, country):
    with get_db_connection() as connection:
        connection.execute(
            'UPDATE teachers SET name = ?, age = ?, email = ?, country = ? WHERE id_number = ?',
            (name, age, email, country, id_number)
        )
        connection.commit()

def delete_teacher(id_number):
    with get_db_connection() as connection:
        connection.execute('DELETE FROM teachers WHERE id_number = ?', (id_number,))
        connection.commit()

def add_course(name,department,description,is_online,credit_hours):
    with get_db_connection() as connection:
        connection.execute(
            'INSERT INTO courses (name, department,description,is_online,credit_hours) VALUES (?,?,?,?,?)',
            (name,department,description,is_online,credit_hours),
        )
        connection.commit()

def get_courses():
    with get_db_connection() as connection:
        return connection.execute('SELECT * FROM courses').fetchall()

def update_course(name, department, description, is_online, credit_hours):
    with get_db_connection() as connection:
        connection.execute(
            'UPDATE courses SET department = ?, description = ?, is_online = ?, credit_hours = ? WHERE name = ?',
            (department, description, is_online, credit_hours, name)
        )
        connection.commit()

def delete_course(name):
    with get_db_connection() as connection:
        connection.execute('DELETE FROM courses WHERE name = ?', (name,))
        connection.commit()
