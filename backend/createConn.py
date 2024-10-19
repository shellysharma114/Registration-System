import mysql.connector          #pip install mysql-connector-python
def create_connection():
    try:
        conn = mysql.connector.connect(host='localhost',username='root',password='',database='test')
        my_cursor = conn.cursor()
        if conn.is_connected():
            return conn, my_cursor
    except mysql.connector.Error as error:
        print(f"Error: {error}")