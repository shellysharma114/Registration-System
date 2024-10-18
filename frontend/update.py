import streamlit as st          #pip install streamlit  
import sys
import os

# Add the backend directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))
import updateReg

def run():
    st.subheader("Update Registration")
    id = st.number_input("Enter Registration ID to update", min_value=1)
    name = st.text_input("New Name")
    email = st.text_input("New Email")
    phone = st.text_input("New Phone Number")
    address = st.text_input("New Address")

    if st.button("Update"):
        result = updateReg.update_registration(id, name, email, phone, address)
        st.write(result)