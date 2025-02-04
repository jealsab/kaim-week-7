import psycopg2
from psycopg2 import sql

def setup_database():
    # Database connection parameters
    db_params = {
        'dbname': 'data_warehouse',
        'user': 'postgres',
        'password': '123456789',
        'host': 'localhost',
        'port': 5432
    }
    
    # Connect to PostgreSQL server
    conn = psycopg2.connect(**db_params)
    conn.autocommit = True
    cur = conn.cursor()

    # Create database and table if they don't exist
    cur.execute(sql.SQL("CREATE DATABASE IF NOT EXISTS data_warehouse"))
    cur.execute("""
        CREATE TABLE IF NOT EXISTS medical_messages (
            message_id TEXT PRIMARY KEY,
            sender_id TEXT,
            message_text TEXT,
            channel TEXT
        )
    """)
    
    # Close the connection
    cur.close()
    conn.close()
    print("Database setup completed.")

if __name__ == '__main__':
    setup_database()