from image_app.components.user_interface import StreamlitUI
from image_app.components.dependency_injection import inject_dependencies

def image_main():
    ui = StreamlitUI()
    ui.show_title()
    user_input = ui.get_user_input()

    # Create an empty element for displaying the image
    image_container = ui.create_image_container()

    if user_input:
        image_url = ui.generator.generate_image(user_input)
        if image_url:
            # Display the image in the container
            ui.display_image(image_url, image_container)
        else:
            ui.display_error("Unable to generate image. Please check your API key.")
    else:
        ui.display_info("Please provide a detailed description to generate images.")

if __name__ == "__main__":
    inject_dependencies()
    image_main()
