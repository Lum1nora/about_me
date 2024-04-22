import streamlit as st
import functions
from PIL import Image


col1, col2 = st.columns(2)

with col1:
    img = Image.open("sheep.png")
    st.image(img)

with col2:
    st.header("About Me")
    st.write("""Celina Tarn, Beginner Python developer, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi 
    rhoncus lacus id mattis malesuada. Duis leo arcu, vehicula vel lacus eget, 
    laoreet dictum dui. Cras ultricies molestie enim, vel pulvinar ante vestibulum 
    ac. Praesent ac tincidunt enim. Cras sagittis libero sit amet nibh tristique 
    pulvinar. Sed tempus et erat sit amet tristique. Mauris eleifend ligula sed du
    """)