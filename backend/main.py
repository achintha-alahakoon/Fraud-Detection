from database import create_connection

def main():
    conn = create_connection()
    if conn:
        print("Can now use the database connection.")
        conn.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()