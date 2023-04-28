import streamlit as st
import pandas as pd

df = pd.read_csv("data/data.csv",sep=";", header=0)
st.set_page_config(layout="wide")

#st is the module, columns is the method. We are creating two columns here
col1, col2 = st.columns(2)

with col1:
    st.image("images/JimMcKeown.jpg")

with col2:
    st.title("Jim McKeown")
    content = """
    Hi, I'm Qhawe. Working to help children in South Africa. 
    My core belief is that children are amazing and we owe it to each of them to give them the opportunities to grow, develop, and reach their potential in life. 
    Hoping these Python skills can help me make a bigger difference in this beautiful world of ours :).
    """
    st.write(content)

st.write("Below, you can find some of the apps I have built in Python")

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write("[Source Code](https://pythonhow.com)")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write("[Source Code](https://pythonhow.com)")
