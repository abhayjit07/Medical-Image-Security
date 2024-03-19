import streamlit as st
import pandas as pd
import os
import nbformat
from nbconvert import ScriptExporter

# Set page configuration
st.set_page_config(
    page_title="Medical Image Security",
    page_icon=":hospital:",
    layout="wide",  # Use wide layout for better UI
)

st.title("Medical Image Security App")

st.markdown("### Principal Component Analysis (PCA)")

st.write("---")

# Upload image
image = st.file_uploader("Upload Image", type=["png"])

st.write("---")

# Define a section to display the uploaded image
if image:
    st.subheader("Uploaded Image")
    col1, col2, col3 = st.columns(3)
    with col1:
          st.write(' ')
    with col2:         
           st.image(image, use_column_width=True)
    with col3:
          st.write(' ')

    # Save the image to a specified location
    save_path = "assets/input_image_pca.png"  # Specify your desired file path
    with open(save_path, "wb") as f:
        f.write(image.read())
else:
    st.subheader("Uploaded Image")
    st.warning("Please upload an image using the uploader above.")

st.write("---")
st.subheader("PCA")

if not image:
    st.warning("Please upload an image using the uploader above.")
else:
    with st.spinner("Performing PCA. Please wait..."):
        os.system("jupyter nbconvert --to script modules/pca.ipynb")
        os.system("python modules/pca.py")

    if os.path.exists("generated_assets/output_image_pca.png"):    
        
        col1, col2, col3 = st.columns(3)
        with col1:
          st.write(' ')
        with col2:     
            st.image("generated_assets/output_image_pca.png", use_column_width=True)
        with col3:
          st.write(' ')
    else:
         st.error("An error occurred while processing the image. Please try again.")







