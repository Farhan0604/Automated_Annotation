import base64
import os

def image_to_base64(image_path: str) -> str:
    """Convert image to base64 string."""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def save_json(json_data: str, output_path: str):
    """Save JSON string to a file."""
    with open(output_path, "w") as f:
        f.write(json_data)

def save_binary_file(content: bytes, output_path: str):
    """Save binary content to a file."""
    with open(output_path, "wb") as f:
        f.write(content)
