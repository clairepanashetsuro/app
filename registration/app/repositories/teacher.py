from database import get_db_connection


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
