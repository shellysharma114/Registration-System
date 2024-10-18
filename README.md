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
