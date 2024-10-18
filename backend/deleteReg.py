import mysql.connector          #pip install mysql-connector-python
import fetchReg

def delete_registration(id):
    try:
        conn = mysql.connector.connect(host='localhost',username='root',password='',database='test')
        my_cursor = conn.cursor(dictionary=True)
        existing_data = fetchReg.fetch_registration_by_id(id)
        if not existing_data:
            return "No registration found with this ID."
        else:
            query = "DELETE FROM Registration WHERE ID = %s"
            my_cursor.execute(query, (id,))
            conn.commit()
            return f"Registration ID {id} deleted successfully."
    except mysql.connector.Error as error:
        return f"Error: {error}"
    finally:
        if conn.is_connected():
            my_cursor.close()
            conn.close()

if __name__ == "__main__" :
    delete_registration(1)
