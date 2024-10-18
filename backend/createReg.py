import mysql.connector          #pip install mysql-connector-python
def create_registration(name, email, dob, phone=None, address=None):
    try:
        conn = mysql.connector.connect(host='localhost',username='root',password='',database='test')
        my_cursor = conn.cursor()
        query = """INSERT INTO Registration (Name, Email, DateOfBirth, PhoneNumber, Address)
                    VALUES (%s, %s, %s, %s, %s)"""
        values = (name, email, dob, phone, address)
        my_cursor.execute(query, values)
        conn.commit()
        return f"Registration for {name} created successfully."
    except mysql.connector.Error as error:
        return f"Error: {error}"
    finally:
        if conn.is_connected():
            my_cursor.close()
            conn.close()

if __name__ == "__main__" :
    create_registration("John", "johndoe11@example.com", "1995-05-15", "9876543210", "123 Street, City")
