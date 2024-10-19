# Registration-System
This project implements a simple registration system using a MySQL database, Python, and Streamlit for the frontend. The system supports CRUD operations (Create, Read, Update, and Delete) for managing user registration data.

## Project Structure

```plaintext
Registration-System/
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
* Python 3.x
* MySQL Server

##Setup Steps
Follow these steps to set up the project on your local machine:

<p>1. Clone the repository</p>
```
git clone repo_url
```
<p>2. Install the required Python dependencies:</p>
```
pip install streamlit mysql-connector-python pandas
```
<p>3. Navigate to the backend directory:</p>
```
cd backend
```
<p>4. Set up a connection with your MySQL database. Make sure MySQL is installed and running on your local machine.</p>
<p>5. Update the MySQL connection details in registration-system/backend/createConn.py. You need to provide your MySQL username, password, host, and database name:</p>
```
# Example content for createConn.py
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",      # Update with your host
        user="your_username",  # Update with your MySQL username
        password="your_password",  # Update with your MySQL password
        database="your_database"   # Update with your MySQL database name
    )

```
