import google.generativeai as genai

class ModelInterface:
    def __init__(self, api_key, model_name):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate_content(self, inputs):
        response_prompt_image = self.model.generate_content(inputs, stream=True)
        response_prompt_image.resolve()
        hello= response_prompt_image.parts[0].text
        
        if response_prompt_image is not None and response_prompt_image.parts:
            return hello
        else:
            return "Sorry, the response could not be generated."
