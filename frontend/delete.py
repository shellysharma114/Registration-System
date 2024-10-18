import streamlit as st          #pip install streamlit  
import sys
import os

# Add the backend directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))
import deleteReg

def run():
    st.subheader("Delete Registration")
    id = st.number_input("Enter Registration ID to delete", min_value=1)

    if st.button("Delete"):
        result = deleteReg.delete_registration(id)
        st.write(result)