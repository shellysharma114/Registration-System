import mysql.connector          #pip install mysql-connector-python

def fetch_registration_by_id(id):
    try:
        conn = mysql.connector.connect(host='localhost',username='root',password='',database='test')
        my_cursor = conn.cursor(dictionary=True)
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