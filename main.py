import streamlit as st
import functions
from PIL import Image

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


