import mysql.connector          #pip install mysql-connector-python
import fetchReg, createConn

def delete_registration(id):
    try:
        conn , my_cursor = createConn.create_connection()
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
