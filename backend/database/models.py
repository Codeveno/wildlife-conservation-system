from backend.database.db_config import get_db_connection

# ========================TABLE CREATION FUNCTION======================== #
def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Animal Tracking Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS AnimalTracking (
            id INT AUTO_INCREMENT PRIMARY KEY,
            animal_name VARCHAR(255) NOT NULL,
            location VARCHAR(255) NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Users Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            verified INT DEFAULT 0,
            verification_code VARCHAR(6)
        )
    ''')

    conn.commit()
    conn.close()
