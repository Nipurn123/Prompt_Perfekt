import streamlit as st
from image_app.components.image_generator import ImageGenerator

class StreamlitUI:
    def __init__(self):
        self.generator = ImageGenerator()

    def show_title(self):
        st.title("Image Generator")

    def get_user_input(self):
        return st.text_input("Describe in a very detailed manner what kind of image you would like to have:")

    def create_image_container(self):
        return st.empty()

    def display_image(self, image_url, container):
        container.image(image_url, caption='Generated Image', use_column_width=True)

    def display_error(self, message):
        st.error(message)

    def display_info(self, message):
        st.info(message)
