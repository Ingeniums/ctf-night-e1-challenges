import base64

def image_to_text(image_path, text_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
    with open(text_path, "w") as text_file:
        text_file.write(encoded_string)
    print(f"Image successfully converted to text and saved to {text_path}")

def text_to_image(text_path, output_image_path):
    with open(text_path, "r") as text_file:
        encoded_string = text_file.read()
    with open(output_image_path, "wb") as img_file:
        img_file.write(base64.b64decode(encoded_string))
    print(f"Text successfully converted back to image and saved to {output_image_path}")

# Example usage
image_to_text("flag.png", "output.txt")
text_to_image("output.txt", "restored.png")


