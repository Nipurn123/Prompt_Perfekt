from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

class GoogleModel:
    def __init__(self, google_api_key):
        self.model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=google_api_key, convert_system_message_to_human=True)

    # Add any additional methods or customization you need here



class OpenaiModel:
    def __init__(self, api_key):
        self.model = ChatOpenAI( openai_api_key=api_key)

    # Add any additional methods or customization you need here
