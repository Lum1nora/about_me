import streamlit as st
import csv
from PIL import Image
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    img = Image.open("images/photo.png")
    st.image(img)

with col2:
    st.header("About Me")
    content = """Celina Tarn, Beginner Python developer, Lorem ipsum dolor sit amet,
     consectetur adipiscing elit. Morbi 
    rhoncus lacus id mattis malesuada. Duis leo arcu, vehicula vel lacus eget, 
    laoreet dictum dui. Cras ultricies molestie enim, vel pulvinar ante vestibulum 
    ac. Praesent ac tincidunt enim. Cras sagittis libero sit amet nibh tristique 
    pulvinar. Sed tempus et erat sit amet tristique. Mauris eleifend ligula sed du
    rhoncus lacus id mattis malesuada. Duis leo arcu, vehicula vel lacus eget, 
    laoreet dictum dui. Cras ultricies molestie enim, vel pulvinar ante vestibulum 
    ac. Praesent ac tincidunt enim. Cras sagittis libero sit amet nibh tristique 
    pulvinar. Sed tempus et erat sit amet tristique. Mauris eleifend ligula sed du
    """
    st.info(content)

with st.empty():
    st.markdown(f"<h4 style='background-color:#99b0cc'> Below you can find some of the apps I have built in Python. "
                 "Feel free to contact me!</h4>", unsafe_allow_html=True)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")


with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.text(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.text(row['description'])
        st.image("images/" + row['image'])