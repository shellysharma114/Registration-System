import streamlit as st          #pip install streamlit  
import pandas as pd 
import sys
import os

# Add the backend directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))
import readReg

def run():
    st.subheader("View Registrations")
    records = readReg.read_registration()
    if records:
        # Ensure columns are ordered correctly and display names
        df = pd.DataFrame(records)

        # Adjust column names based on your table schema
        df.columns = ['ID', 'Name', 'Email', 'DateOfBirth', 'PhoneNumber', 'Address', 'RegistrationDate']

        # Display the table without the index
        st.dataframe(df)
    else:
        st.write("No registrations found.")