import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',       # Replace with your MySQL username
            password='Lewis@2024'    # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Use CREATE DATABASE IF NOT EXISTS to avoid failure if DB exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Close connection properly
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Uncomment the line below if you want a closing confirmation
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
