# Registration-System
This project implements a simple registration system using a MySQL database, Python, and Streamlit for the frontend. The system supports CRUD operations (Create, Read, Update, and Delete) for managing user registration data.

## Project Structure

```plaintext
project/
│
├── frontend/           # Frontend code (Streamlit)
│    ├── app.py         # Streamlit app to interact with the backend
│    ├── create.py         # Streamlit app to interact with the backend
│    ├── update.py         # Streamlit app to interact with the backend
│    ├── read.py         # Streamlit app to interact with the backend
│    ├── delete.py         # Streamlit app to interact with the backend
│
└── backend/            # Backend code (MySQL connection, CRUD operations)
     ├── createReg.py      # Create operation
     ├── updateReg.py      # Update operation
     ├── deleteReg.py      # Delete operation
     ├── readReg.py        # Read operation
     ├── createConn.py  # MySQL connection setup
     └── createTable.py # Table creation script
```
##Prerequisites
Ensure you have the following installed on your machine:

Python 3.x
MySQL Server

##Setup Steps
Follow these steps to set up the project on your local machine:

###Clone the repository to your local machine:

bash
Copy code
git clone "this repo"
Install the required Python dependencies:

bash
Copy code
pip install streamlit mysql-connector-python pandas
Navigate to the backend directory:

bash
Copy code
cd backend
Set up a connection with your MySQL database. Make sure MySQL is installed and running on your local machine.

Update the MySQL connection details in registration-system/backend/createConn.py. You need to provide your MySQL username, password, host, and database name:

python
Copy code
# Example content for createConn.py
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",      # Update with your host
        user="your_username",  # Update with your MySQL username
        password="your_password",  # Update with your MySQL password
        database="your_database"   # Update with your MySQL database name
    )
Create the MySQL table by running the createTable.py script:

bash
Copy code
python createTable.py
This will create the necessary Registration table in your MySQL database.

Running the Project
Once the setup is complete, you can start the Streamlit app by running:

bash
Copy code
streamlit run frontend/app.py
This will launch the registration system in your browser, allowing you to interact with the backend through the web interface.
