from database import get_db_connection

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
