import streamlit as st          #pip install streamlit  
import sys
import os

# Add the backend directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))
import createReg

def run():
    st.subheader("Create a New Registration")
    name = st.text_input("Name")
    email = st.text_input("Email")
    dob = st.date_input("Date of Birth")
    phone = st.text_input("Phone Number")
    address = st.text_input("Address")

    if st.button("Submit Registration"):
        result = createReg.create_registration(name, email, dob, phone, address)
        st.write(result)