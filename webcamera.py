import streamlit as st
from PIL import Image

uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    #start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # create a pillow image instance
    img=Image.open(camera_image)
    # convert image to grayscale
    gray_img = img.convert("L")
    # render the image on website
    st.image(gray_img)

if uploaded_image:
    
    img_up = Image.open(uploaded_image)

    gray = img_up.convert("L")

    st.image(gray)

