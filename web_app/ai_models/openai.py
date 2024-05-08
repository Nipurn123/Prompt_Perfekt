from langchain_openai import ChatOpenAI

class OpenaiModel:
    def __init__(self, api_key):
        self.model = ChatOpenAI( openai_api_key=api_key)

    # Add any additional methods or customization you need here
