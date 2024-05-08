import streamlit as st
from PIL import Image

class ImageUploader:
    @staticmethod
    def upload_image():
        return st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'], key="image_uploader")
