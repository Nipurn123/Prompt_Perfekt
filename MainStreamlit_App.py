import streamlit as st
import asyncio
from image_app.main import image_main
from vision_app.main import vision_main
from web_app.app import Chatbot_main
from prompt_app.main import prompt_main 
from chatbot_app.main import Bot 




class StreamlitApp:
    def __init__(self):
        self.option = None

    def select_script(self):
        st.sidebar.title("Select Script")
        self.option = st.sidebar.selectbox(
            'Choose Script:',
            ('Prompt Perfekt','Chat with Images', 'Web Assistant', 'Chat-Bot' ,'Image Generator', )  # Added 'Image_Edit' option
        )

    def display_selected_script(self):
        
        
        
        if self.option == 'Chat with Images':
            vision_main()

        elif self.option=="Prompt Perfekt":
            prompt_main()    

        elif self.option =="Web Assistant":
             bot = Chatbot_main()
             bot.stream_main()  

        elif self.option == 'Image Generator':
            image_main() 

        elif self.option =="Chat-Bot":
            bot=Bot()
            bot.run()      


        
            

        


    async def run_async(self, func):
        await func()

if __name__ == "__main__":
    app = StreamlitApp()
    app.select_script()
    app.display_selected_script()
