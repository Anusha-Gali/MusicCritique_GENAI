# import requests

# API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
# headers = {"Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}


# def generate_image(query: str, api_key: str):
#     """Generate image from a text prompt.

#     Args:
#     query (str): The input query/prompt.
#             api_key (str): The Hugging Face API key.

#     Returns:
#     image_bytes (bytes): Content of the response, in bytes.
#     """
#     headers = {"Authorization": f"Bearer {api_key}"}
#     payload = {"inputs": query}
#     response = requests.post(API_URL, headers=headers, json=payload)
#     image_bytes = response.content
#     return image_bytes
