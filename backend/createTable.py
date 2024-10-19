import mysql.connector          #pip install mysql-connector-python 
import createConn
try:
    conn , my_cursor = createConn.create_connection()
    query = """CREATE TABLE Registration (
                ID INT AUTO_INCREMENT PRIMARY KEY,         -- Primary Key for the table, auto-increments
                Name VARCHAR(255) NOT NULL,                -- User's name, cannot be null
                Email VARCHAR(255) NOT NULL UNIQUE,        -- Email, must be unique
                DateOfBirth DATE,                          -- Date of birth in the format YYYY-MM-DD
                PhoneNumber VARCHAR(15),                   -- Optional phone number field
                Address VARCHAR(255),                      -- Optional address field
                RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Stores the date and time of registration
);
    """
    my_cursor.execute(query)
    conn.commit()
    print("Table is successfully created.")
except mysql.connector.Error as error:
    print(f"Error: {error}")
finally:
    if conn.is_connected():
        my_cursor.close()
        conn.close()
