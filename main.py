import ctypes
import requests
import random
import sys
import os
from notify import notification

url = "https://source.unsplash.com/random/1920x1080/?"
tag_list = []

if len(sys.argv) < 2:
    print("Please provide at least one tag.")
    tag_list.append("Wallpaper")
else:
    for tag in sys.argv[1:]:
        tag_list.append(tag)

tag = random.choice(tag_list)
url += "," + tag
print(url)




def download_image(image_source, filename):
    """Downloads an image from the specified source and saves it with the given filename.

    Args:
        image_source (str): The URL of the image to download.
        filename (str): The desired filename for the downloaded image.

    Returns:
        bool: True if the download was successful, False otherwise.
    """

    try:
        response = requests.get(image_source, stream=True)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"Image downloaded successfully: {filename}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        return False

# Example usage (replace with the actual image source obtained from previous steps)
filename = "downloaded_image.jpg"

if download_image(url, filename):
    print("You can now access the downloaded image:", filename)


print(os.getcwd() + "\\downloaded_image.jpg")
ctypes.windll.user32.SystemParametersInfoW(20, 0, os.getcwd() + "\\downloaded_image.jpg" , 0)
notification.send("Your walpaper has been changed. It is photo of " + tag + ". Enjoy!")