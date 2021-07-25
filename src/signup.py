import streamlit as st
def textFm():
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password",type='password')
          
          
    if st.button("signup"):
        st.success("You have successfully created an account")
        st.info("Goto Login Menu to Login")