import requests
from image_app.utils.api_keys import get_api_key

class ImageGenerator:
    def generate_image(self, prompt):
        api_key = get_api_key()
        authorization_header = {"Authorization": f"Bearer {api_key}"}
        
        # Define the endpoint URL
        url = "https://api.openai.com/v1/images/generations"

        # Define the request headers
        headers = {
            "Content-Type": "application/json",
        }

        # Add the API key to the headers
        headers.update(authorization_header)

        # Define the request payload
        data = {
            "prompt": prompt,
            "n": 1,
            "size": "1024x1024"
        }

        # Send the POST request to the API
        response = requests.post(url, headers=headers, json=data)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the URL of the generated image from the response JSON
            image_url = response.json()["data"][0]["url"]
            return image_url
        else:
            return None
