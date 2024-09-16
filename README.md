# Image_Gen

---
![flux1](https://github.com/user-attachments/assets/15770058-7cf8-4870-a1fa-f876dc9ee2aa)
![flux2](https://github.com/user-attachments/assets/f283cfab-7105-4707-b586-474b7b155555)

# AI Image Generator with FLUX.1-dev

This project is a **Streamlit-based web application** that uses the Hugging Face FLUX.1-dev model to generate images from text prompts. You can enter creative prompts like "Moonwalker on Mars," customize the image size, and download the generated images.

## Features
- 📝 Enter any text prompt to generate an image.
- 📏 Customize the width and height of the generated image with sliders.
- 💾 Download the generated image in PNG format.
- 🎨 Clean and responsive UI with tooltips and status notifications.

## Getting Started

### 1. Clone the repository:

```bash
git clone https://github.com/RkanGen/Image_Gen.git
cd Image_Gen
```

### 2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Set up your Hugging Face API Key:
Create a `.env` file in the project root and add your Hugging Face API key:

```env
HF_API_TOken=your_huggingface_api_key
```

### 4. Run the application:

```bash
streamlit run image.py
```

## Usage
1. Enter a prompt (e.g., "A futuristic city at night").
2. Adjust the image size using the sliders on the sidebar.
3. Click **Generate Image** to see the result.
4. Download the image using the **Download Image** button.

## Example Prompts
- "A cat playing guitar"
- "Sunset over the mountains"
- "A robot exploring a neon city"

## Dependencies
- `streamlit`
- `requests`
- `Pillow`
- `python-dotenv`



