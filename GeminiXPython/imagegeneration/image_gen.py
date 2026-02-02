import os
from google import genai
from google.genai import types
from PIL import Image

# --- Configuration ---
# Ensure your GOOGLE_API_KEY is set in your environment variables.
# If you haven't set it globally, uncomment the next line and paste your key:
# os.environ['GOOGLE_API_KEY'] = "YOUR_ACTUAL_API_KEY_HERE"

def generate_image_from_text(prompt_text, output_filename="generated_image.png"):
    """
    Generates an image using the Gemini API based on a text prompt.
    """
    print(f"Initializing Client...")
    client = genai.Client()

    print(f"Sending prompt to Gemini: '{prompt_text}'...")

    try:
        # We must use the specific image-generation model: 'gemini-2.5-flash-image'
        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=[prompt_text],
            # Crucial config: Tell Gemini we expect an IMAGE response, not text.
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
            )
        )

        image_saved = False

        # The response contains 'parts'. We need to find the part that has image data.
        for part in response.parts:
            # Check if the part contains inline binary data (the image)
            if part.inline_data:
                print("Image data received successfully.")
                # The SDK provides a helper method .as_image() to convert
                # raw data directly into a PIL Image object.
                img = part.as_image()
                
                # Save the image locally
                img.save(output_filename)
                print(f"Image saved successfully as '{output_filename}'")
                
                # Optional: Open the image automatically in your default viewer
                img.show() 
                image_saved = True
                break # Exit loop after finding the image

        if not image_saved:
            print("Error: The model responded, but no image data was found in the response.")

    except Exception as e:
        print(f"An error occurred during generation: {e}")

# --- Run the program ---
if __name__ == "__main__":
    # Define your text prompt here
    my_prompt = "A highly detailed photograph of a nepali guy with foreigner guys in the foothills of mountain in the middle of trekking"

    
    # Call the function
    generate_image_from_text(my_prompt, "trekker.jpeg")