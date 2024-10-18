import mysql.connector          #pip install mysql-connector-python
import fetchReg

def update_registration(id, name, email=None, phone=None, address=None):
    try:
        conn = mysql.connector.connect(host='localhost',username='root',password='',database='test')
        my_cursor = conn.cursor(dictionary=True)
        existing_data = fetchReg.fetch_registration_by_id(id)
        if not existing_data:
            return "No registration found with this ID."
        
        # Use existing data if no new value is provided
        name = name if name else existing_data['Name']
        email = email if email else existing_data['Email']
        phone = phone if phone else existing_data['PhoneNumber']
        address = address if address else existing_data['Address']
        
        query = """UPDATE Registration SET Name = %s, Email = %s, PhoneNumber = %s, Address = %s
                   WHERE ID = %s"""
        values = (name, email, phone, address, id)
        my_cursor.execute(query, values)
        conn.commit()
        return f"Registration ID {id} updated successfully."

    except mysql.connector.Error as error:
        return f"Error: {error}"
    finally:
        if conn.is_connected():
            my_cursor.close()
            conn.close()

if __name__ == "__main__" :
    update_registration(1, name="John Updated", email="john.new@example.com", phone="1234567890", address="New Address")
