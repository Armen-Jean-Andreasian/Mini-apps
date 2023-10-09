import streamlit as st
from PIL import Image

st.title("Color to grayscale converter")
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Camera"):
    camera_image = st.camera_input("Camera")
    if camera_image:
        img = Image.open(camera_image)
        gray = img.convert("L")
        st.image(gray)
if uploaded_image:
    img = Image.open(uploaded_image)
    gray = img.convert("L")
    st.image(gray)
