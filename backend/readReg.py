import mysql.connector          #pip install mysql-connector-python
def read_registration(id=None):
    try:
        conn = mysql.connector.connect(host='localhost',username='root',password='',database='test')
        my_cursor = conn.cursor()
        query = "SELECT * FROM Registration WHERE ID = %s" if id else "SELECT * FROM Registration"
        my_cursor.execute(query, (id,) if id else None)
        records = my_cursor.fetchall()
        return records
    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        if conn.is_connected():
            my_cursor.close()
            conn.close()

if __name__ == "__main__" :
    read_registration(1)  # Read a specific registration by ID
    read_registration()   # Read all registrations
