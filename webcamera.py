import streamlit as st
from PIL import Image

uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
#start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    #create a pillow image instance
    img = Image.open(uploaded_image)

    #Convert the pillow image to grayscale
    gray_img = img.convert("L")
    #Render the grayscale image on the webpage
    st.image(gray_img)