# Generative AI Image Generator

This project is a Streamlit application that generates images using the Stable Diffusion model from the `diffusers` library. The application allows users to input prompts and configure various parameters to generate images.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run AI_EDA/.streamlit/app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Configure the image generation settings in the sidebar:
    - **Prompt**: The main prompt for image generation.
    - **Negative Prompt**: The negative prompt to avoid certain features in the generated images.
    - **Número de Imagens**: The number of images to generate.
    - **Número de Passos de Inferência**: The number of inference steps.
    - **Altura da Imagem**: The height of the generated images.
    - **Largura da Imagem**: The width of the generated images.
    - **Seed**: The seed for random number generation.
    - **Escala de Orientação**: The guidance scale for image generation.

4. Click the "Gerar Imagem" button to generate images based on the configured settings.

## Code Overview

- `generate_images`: This function generates images using the Stable Diffusion model. It takes several parameters such as `prompt`, `negative_prompt`, `num_images_per_prompt`, `num_inference_steps`, `height`, `width`, `seed`, and `guidance_scale`.

- Streamlit UI:
    - The sidebar contains input fields for configuring the image generation settings.
    - The main area displays the generated images with captions.

## Dependencies

- [streamlit](https://streamlit.io/)
- [diffusers](https://github.com/huggingface/diffusers)
- [torch](https://pytorch.org/)

## License

This project is licensed under the MIT License. Generative AI Image Generator
