from fastapi import FastAPI
import streamlit as st
import time
import psycopg2
from psycopg2.extras import RealDictCursor
import pandas as pd

while True:

    try:
        connection = psycopg2.connect(host="localhost",database="sample",user="postgres",password="rohanpatil",
        cursor_factory=RealDictCursor)
        
        cursor = connection.cursor()
        print("Connected Successfully!")
        break
    
    except Exception as error:
        print("Unsuccesful")
        time.sleep(3)



app = FastAPI()
def getData():
    cursor.execute(""" select * from salaries """)
    data = cursor.fetchall()
    return data

st.write("hello world !")



if st.button("Get Data"):
    data = getData()
    data = pd.DataFrame(data)
    st.write(data)















