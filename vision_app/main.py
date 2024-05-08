from vision_app.app import VisionApp

def vision_main():
    GOOGLE_API_KEY = 'AIzaSyADEdfxRrcyqB-Kp-5u5CYjDrKNnxokWXQ'
    MODEL_NAME = 'gemini-pro-vision'
    app = VisionApp(api_key=GOOGLE_API_KEY, model_name=MODEL_NAME)
    app.run()

if __name__ == "__main__":
    vision_main()
