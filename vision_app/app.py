from vision_app.components.image_uploader import ImageUploader
from vision_app.components.chat_interface import ChatInterface
from vision_app.components.model_interface import ModelInterface
from vision_app.components.message_history import MessageHistory
from vision_app.components.response_handler import ResponseHandler

import streamlit as st
from PIL import Image

class VisionApp:
    def __init__(self, api_key, model_name):
        self.api_key = api_key
        self.model_name = model_name
        self.image_uploader = ImageUploader()
        self.chat_interface = ChatInterface()
        self.model_interface = ModelInterface(api_key=self.api_key, model_name=self.model_name)
        self.max_messages = 20

    def run(self):
        st.title("Chat with images")
        uploaded_image = self.image_uploader.upload_image()
        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            self.process_image(image)

    def process_image(self, image):
        st.image(image, caption='Uploaded Image', use_column_width=True)

        if "messages" not in st.session_state:
            st.session_state.messages = []

        self.display_chat_history()
        self.handle_user_input(image)

    def display_chat_history(self):
        for message in st.session_state.messages[-self.max_messages:]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def handle_user_input(self, image):
        user_input = self.chat_interface.get_user_input()
        if user_input:
            st.chat_message("user").write(user_input)
            st.session_state.messages.append({"role": "user", "content": user_input})
            self.generate_and_display_response(user_input, image)

    def generate_and_display_response(self, prompt, image):
        prompt_with_history = ResponseHandler.generate_prompt_with_history(prompt, st.session_state.messages, self.max_messages)
        response_prompt_image = self.model_interface.generate_content([prompt_with_history, image])
        with st.chat_message("assistant"):
            st.markdown(response_prompt_image)
        st.session_state.messages.append({"role": "assistant", "content": response_prompt_image})

    