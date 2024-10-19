import mysql.connector          #pip install mysql-connector-python
import fetchReg, createConn

def update_registration(id, name=None, email=None, phone=None, address=None):
    try:
        conn , my_cursor = createConn.create_connection()
        
        existing_data = fetchReg.fetch_registration_by_id(id)
        if not existing_data:
            return "No registration found with this ID."
        
        # Unpack existing data tuple into variables (adjust the order as per your database)
        existing_id, existing_name, existing_email, existing_dob, existing_phone, existing_address, registration_date = existing_data
        
        # Use existing data if no new value is provided
        name = name if name else existing_name
        email = email if email else existing_email
        phone = phone if phone else existing_phone
        address = address if address else existing_address
        
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
