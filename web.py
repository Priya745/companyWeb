import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("The Best Company")
content = ("""
           Premier IT Consulting is a leading provider of strategic IT consulting services, dedicated to helping organizations harness the power of technology 
           to achieve their business objectives. With over 15 years of experience, our consultants offer expert advice and hands-on assistance in areas such as cloud computing,
            cybersecurity, and digital transformation. We work closely with our clients to understand their challenges and deliver tailored solutions that maximize efficiency and drive innovation.
            """)
st.write(content)

st.header("Our team")

col1, gap1, col2, gap2,  col3 = st.columns([1, 0.5, 1, 0.5, 1])

df = pd.read_csv("data.csv")
# df.columns = df.columns.str.strip()

with col1:
    for index, row in df[:4].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image("images/" + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image("images/" + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image("images/" + row['image'])
