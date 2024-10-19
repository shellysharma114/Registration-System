import mysql.connector          #pip install mysql-connector-python
import createConn

def fetch_registration_by_id(id):
    try:
        conn , my_cursor = createConn.create_connection()
        query = "SELECT * FROM Registration WHERE ID = %s"
        my_cursor.execute(query, (id,))
        record = my_cursor.fetchone()
        return record
    except mysql.connector.Error as e:
        return f"Error: {e}"
    finally:
        if conn.is_connected():
            my_cursor.close()
            conn.close()