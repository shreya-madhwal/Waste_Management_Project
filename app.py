import streamlit as st
'''import openpyxl as pxl
import pandas as pd
projDemo = pd.read_excel('login (1).xlsx')
exp = pxl.load_workbook('login (1).xlsx')
sheet = exp.active
maxrow = sheet.max_row+1
sheet = exp['Sheet1']'''


from streamlit.proto.Button_pb2 import Button 
from src import login ,home ,signup

def main():
      st.title("Login Page")
      menu = ["Home","Login","Signup"]
      choice = st.sidebar.selectbox("Menu",menu)
      
      if choice == "Home":
          home.textFm()


      elif choice == "Login":
          login.textFm()


      elif choice == "Signup":
          signup.textFm()


if __name__ == '__main__':
    main()      
