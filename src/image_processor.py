import cv2
import numpy as np
import requests
import json

# Function to convert an image to an array and send it as JSON
def send_image_as_json(image_path, url):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Could not read the image at {image_path}")
        return

    # Convert the image to a 3D array (H x W x C)
    image_array = image.tolist()  # Convert to list for JSON serialization

    # Create the JSON payload
    payload = {
        "image_array": image_array
    }

    # Send the POST request with the image array
    response = requests.post(url, json=payload)

    # Check the response
    if response.status_code == 200:
        print("Image sent successfully. Response:", response.json())
    else:
        print("Failed to send image. Status code:", response.status_code)

# Example usage
if __name__ == "__main__":
    image_path = "assets/test_image.jpg"
    url = "http://127.0.0.1:8050/process_image"
    send_image_as_json(image_path, url)
