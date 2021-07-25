import streamlit as st
#import openpyxl as pxl
def textFm():
    st.subheader("Login Section")
    userName = st.sidebar.text_input("User Name")
    password = st.sidebar.text_input("password",type='password')
    '''
    submissionButton = st.form_submit_button(label="Login")
    if submissionButton == True:

        for i in range(2, sheet.max_row):
            if((sheet.cell(row=i, column=2).value == userName)):
                if((sheet.cell(row=i, column=3).value == password)):
                        y = sheet.cell(row=i, column=4).value
                        st.success('Successfully Login')
                        type(y)

                else:
                        st.error(
                            "either username or password is incorrect")
                            '''


    if st.sidebar.checkbox('Login'):
              st.success("Logged In as {}".format(userName))
              task = st.selectbox("Role",["Role","Waste Giver","Waste Taker"])
              if task =="Role":
                  st.subheader("Add your Role")
              elif task == "Waste Giver":
                    st.subheader("Waste Giver")
                   #user_name = st.write("Enter your name")
                    Name_ = st.text_input("Enter your Name")
                    email_id = st.text_input("Enter your email_id")
                    contact_no = st.text_input("Enter your contact no")
                    address = st.text_input("Enter your address")
                    #type = st.text_input("Enter type of Waste")
                    type= st.selectbox("Type",["type","Municipal solid waste","Hazardous waste","Biodegreadable waste","E-waste","Household hazardous waste"])




              elif task == "Waste Taker":
                    st.subheader("Waste Taker")
                    compony_Name = st.text_input("Enter your Compony/Industry Name")
                    email_id = st.text_input("Enter your email_id")
                    contact_no = st.text_input("Enter your contact no")
                    address = st.text_input("Enter your address")
                    type= st.selectbox("Type of waste you want for recycle",["type","Municipal solid waste","Hazardous waste","Biodegreadable waste","E-waste","Household hazardous waste"])  
