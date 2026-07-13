from database import get_db_connection

def create_table():
    with get_db_connection() as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS courses(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         department TEXT NOT NULL,
         description TEXT NOT NULL,
         is_online BOOLEAN DEFAULT FALSE,
         credit_hours INTEGER NOT NULL ) ''')
