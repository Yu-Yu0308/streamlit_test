import streamlit as st
from PIL import Image

st.title('Streamlit App Example')
st.caption('This is a caption')

image = Image.open('./data/image.jpg')
st.image(image, width=300)
