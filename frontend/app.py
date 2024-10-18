import streamlit as st          #pip install streamlit        

import create, read, update, delete

st.title("Registration CRUD App")

st.sidebar.title("CRUD Operations")
choice = st.sidebar.radio("Select an Operation", ("Create Registration", "Read Registration", "Update Registration", "Delete Registration"))

# Create a new registration
if choice == "Create Registration":
    create.run()
    

# Read and display registrations
elif choice == "Read Registration":
    read.run()

# Update a registration
elif choice == "Update Registration":
    update.run()

# Delete a registration
elif choice == "Delete Registration":
    delete.run()