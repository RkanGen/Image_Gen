import streamlit as st
import requests
from PIL import Image
import io
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
HF_API_KEY = os.getenv("HF_API_TOKEN")

# Set the API URL and authorization header
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

# Function to send query to the model
def query_model(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content  # Return image bytes
    else:
        st.error(f"Error {response.status_code}: {response.text}")
        return None

# Streamlit UI
st.title("🖼️ AI Image Generator  FLUX.1-dev")
st.write("Generate stunning images from your creative text prompts using the Hugging Face FLUX.1-dev model!")

# Create a sidebar for user options
st.sidebar.header("🔧 Options")
image_width = st.sidebar.slider("Select Image Width", 256, 1024, 512)
image_height = st.sidebar.slider("Select Image Height", 256, 1024, 512)


# Text input for the prompt
prompt = st.text_input("Enter your prompt (e.g., 'Dance Moonwalker on Mars'):")

# Generate and display image in two columns layout
col1, col2 = st.columns(2)

with col1:
    if st.button("🎨 Generate Image"):
        if prompt:
            with st.spinner("Generating image..."):
                image_bytes = query_model(prompt)
                if image_bytes:
                    # Display the generated image
                    image = Image.open(io.BytesIO(image_bytes))
                    image = image.resize((image_width, image_height))  # Resize based on user selection
                    st.image(image, caption=f"Generated Image for: '{prompt}'", use_column_width=True)
                    
                    # Save image for download
                    buf = io.BytesIO()
                    image.save(buf, format="PNG")
                    byte_im = buf.getvalue()

                    # Display download button for the image
                    st.download_button(
                        label="💾 Download Image",
                        data=byte_im,
                        file_name=f"generated_image_{prompt.replace(' ', '_')}.png",
                        mime="image/png",
                    )
                else:
                    st.error("Failed to generate image. Please try again.")
        else:
            st.warning("Please enter a prompt.")




# Footer
st.markdown("""
    ---



    **Made by**      "Rkan "        .**
    **Explore** more advanced prompts and adjust image size for the best results!
""")
