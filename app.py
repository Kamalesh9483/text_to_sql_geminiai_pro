from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# configure API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini model and provide SQL query as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

# FUnction to retrieve query from SQL database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt=["""
        you are expert in converting english questions to SQL query.
        The SQL database has name EMPLOYEE and has collowing column - NAME, DEPARTMENT,
        SECTION, SALARY \n\n
        Example 1 - How many entries are there in db, the SQL command will be SELECT COUNT(*) FROM EMPLOYEE;\n
        Example 2 - Get me all employees belonging to Department Data Science, the SQL command will be SELECT * FROM EMPLOYEE WHERE DEPARTMENT='Data Science';
        
        also sql code should not have ''' in the beginning and end and sql word in output
        """]

st.set_page_config(page_title='Text to SQL Retrieval App')
st.header('App to retrieve SQL Data on user text input')

question=st.text_input("Input: ",key="input")
submit=st.button('Ask the question')

if submit:
    response=get_gemini_response(question=question,prompt=prompt)
    st.subheader('The SQL Query is: ')
    st.write(response)
    print(response)
    data=read_sql_query(response,"Employee.db")
    st.subheader('The response is')
    for row in data:
        print(row)
        st.header(row)