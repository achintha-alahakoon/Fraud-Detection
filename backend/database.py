import psycopg2

DB_HOST = "localhost"
DB_NAME = "fraud"
DB_USER = "postgres"
DB_PASSWORD = "22929"
DB_PORT = "5432"

def create_connection():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        print("Database connection successful")
        return connection
    except Exception as e:
        print("Error connecting to the database:", e)
        return None
